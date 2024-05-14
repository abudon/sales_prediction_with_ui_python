import sys
import os
import sqlite3
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from statsmodels.tsa.arima.model import ARIMA
from pmdarima.arima import auto_arima
# IMPORT PYSIDE6 MODULES
from PySide6 import QtGui, QtCore, QtWidgets
from PySide6.QtWidgets import *
# IMPORT PAGES
from welcome_page import Ui_Welcome_Page
from login_page import Ui_Log_In
from dashboard_2 import Ui_Dashboard_2

import matplotlib

matplotlib.use('Qt5Agg')

# GLOBAL VARIABLE
counter = 0


class DashBoard(QMainWindow):
    def __init__(self):
        super(DashBoard, self).__init__()
        # VARIABLE INITIALIZATION
        self.file_path_sales = None
        self.file_path_indicator = None
        self.file_dialog = None
        self.start_prediction = None
        self.end_prediction = None
        # ASSIGING THE UI CLASS
        self.ui = Ui_Dashboard_2()
        self.ui.setupUi(self)

        # Adding Signals to NAVIGATION BUTTONS
        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.btn_settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.btn_save_inventory.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.btn_sales_analytics.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.btn_create_account.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))

        # ADDING SIGNAL TO BUTTON ON THE SETTING PAGE
        self.ui.btn_save_setting.clicked.connect(lambda: self.assign_date)
        # Adding Signals to BUTTONS ON INVENTORY PAGE
        self.ui.btn_path_indicator.clicked.connect(lambda: self.show_file_dialog("indicators"))
        # THIS IS FOR SALES BUTTON
        self.ui.btn_path_indicator_2.clicked.connect(lambda: self.show_file_dialog("sales"))
        self.ui.btn_upload.clicked.connect(self.upload_to_database)
        # Adding Signals to sale visualization buttons
        self.ui.btn_actual_sale.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))
        self.ui.btn_prediction_sale.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(1))
        self.ui.btn_display_score.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(2))

        # Add a widget to the sale analytics page to display the plot
        self.plot_layout_actual_sale = QVBoxLayout(self.ui.page_actual_sale)
        self.plot_layout_predict_sale = QVBoxLayout(self.ui.page_predict_sale)
        # self.canvas = FigureCanvas(Figure(figsize=(10, 6)))
        # self.plot_layout_actual_sale.addWidget(self.canvas)
        # self.plot_layout_predict_sale.addWidget(self.canvas)

        # ASSIGN DATE FUNCTION

    def assign_date(self):
        self.start_prediction = self.ui.start_year_input.text()
        self.end_prediction = self.ui.end_year_input.text()

    # SHOW FILE UPLOAD DIALOG BOX FUNCTION
    def show_file_dialog(self, file_type):
        self.file_dialog = QFileDialog()
        self.file_dialog.setNameFilter("CSV Files (*.csv)")
        self.file_dialog.setFileMode(QFileDialog.ExistingFile)

        if self.file_dialog.exec_():
            select_files = self.file_dialog.selectedFiles()
            if select_files:
                selected_file = select_files[0]

                if file_type == "indicators":
                    self.ui.path_edit_indicator.setText(f"Selected file:   {selected_file}")
                    print(f"Selected File: {selected_file}")
                    self.file_path_indicator = selected_file
                elif file_type == "sales":
                    self.ui.path_edit_indicator_2.setText(f"Selected file:   {selected_file}")
                    print(f"Selected File: {selected_file}")
                    self.file_path_sales = selected_file
            else:
                print("No file selected")
        else:
            print("Dialog canceled")

        # SEND DATA TO DATABASE FUNCTION

    def upload_to_database(self, ):
        if hasattr(self, 'file_path_sales'):
            # GET THE CSV FILES
            indicators = pd.read_csv(self.file_path_indicator)
            sales = pd.read_csv(self.file_path_sales)
            sales = sales.drop(["store"], axis=1)
            self.assign_date()
            start_prediction = self.start_prediction
            end_prediction = self.end_prediction
            print(start_prediction, end_prediction)

            # CONVERTING DATE FROM OBJECT DATATYPE TO PANDAS DATETIME DATATYPE
            sales["date"] = pd.to_datetime(sales['date'])
            indicators['year'] = pd.to_datetime(indicators['year'], format='%Y')

            # CONVERTING DATE IN SALES TO YEAR PERIOD AND SUM THE NUMBER OF ITEM IN EACH YEAR
            sales['year'] = sales['date'].dt.to_period('Y')
            sales = sales.drop(['date'], axis=1)

            # CONVERT THE YEAR GENERATED TO TIMESTAMP OF YEAR IN THE PANDAS SERIES
            sales['year'] = sales['year'].dt.to_timestamp()
            yearly_sales = sales.groupby(['year', 'item']).sum().reset_index()

            # MERGE THE BOTH FILES IN TERMS OF YEAR
            merge_data = pd.merge(yearly_sales, indicators, on='year')

            # FEATURE ENGINEERING
            merge_data['month'] = pd.to_datetime(merge_data['year'], format='%Y').dt.month
            merge_data['quarter'] = pd.to_datetime(merge_data['year'], format='%Y').dt.quarter
            merge_data['day_of_week'] = merge_data['year'].dt.dayofweek
            merge_data['rolling_mean_sales'] = merge_data.groupby(['item'])['sales'].transform('mean')
            merge_data['lagged_sales_1'] = merge_data.groupby('item')['sales'].shift(1)
            merge_data['lagged_sales_2'] = merge_data.groupby('item')['sales'].shift(2)
            merge_data['year'] = pd.to_datetime(merge_data['year'], format='%Y').dt.to_period('Y')
            merge_data['rolling_mean_sales'] = \
                merge_data.groupby('item')['sales'].rolling(window=3).mean().reset_index()['sales']
            merge_data['rolling_std_sales'] = merge_data.groupby('item')['sales'].rolling(window=3).std().reset_index()[
                'sales']
            merge_data['sales_times_weather'] = merge_data['sales'] * merge_data['Precipitation']
            merge_data['sales_divided_by_economic'] = merge_data['sales'] / merge_data['GDP']

            # SORTING MISSING VALUES
            missing_column_data = ['rolling_mean_sales', 'lagged_sales_1', 'lagged_sales_2', 'rolling_std_sales']
            # Fill missing values
            for col in missing_column_data:
                merge_data[col].fillna(merge_data[col].mean(), inplace=True)

            # CREATE A CLEAN DATA
            merge_data.to_csv('clean_data.csv', index=False)

            # SPLITTING INTO TRAINING AND TESTING SETS
            x_train = merge_data[merge_data['year'] < pd.Period(start_prediction)].drop('sales', axis=1)
            x_train['year'] = x_train['year'].dt.year
            y_train = merge_data[merge_data['year'] < pd.Period(start_prediction)]['sales']
            x_test = merge_data[merge_data['year'] >= pd.Period(start_prediction)].drop('sales', axis=1)
            x_test['year'] = x_test['year'].dt.year

            # TO CREATE THE LINEAR  REGRESSION MODEL, AND PREDICTED OUTPUT
            linear_model = LinearRegression()
            linear_model.fit(x_train, y_train)
            predict_sales = linear_model.predict(x_test)

            # Create a DataFrame with future years
            x_future = pd.DataFrame({'year': range(int(start_prediction), int(end_prediction))})
            num_items = len(x_train['item'].unique())
            x_future = pd.concat([x_future] * num_items, ignore_index=True)
            x_future['item'] = np.tile(x_train['item'].unique(), len(x_future) // num_items)[:len(x_future)]
            missing_columns = [col for col in x_train.columns if col not in x_future.columns]
            for col in missing_columns:
                x_future[col] = np.nan  # or assign default values if available
            x_future = x_future[x_train.columns]

            # Predict sales using ARIMA model
            predicted_values = []
            for item in merge_data['item'].unique():
                item_data = merge_data[merge_data['item'] == item]
                item_data.set_index('year', inplace=True)

                try:
                    model = auto_arima(item_data['sales'], seasonal=False, trace=False)
                    # model_fit = model.fit()
                    end = len(item_data) + len(x_future[x_future['item'] == item]) - 1
                    predictions = model.predict(n_periods=end - len(item_data) + 1)
                    # predictions = model.predict(start=len(item_data), end=end)
                    predicted_values.extend(predictions)
                except:
                    print(f"Error occurred while fitting ARIMA model for item '{item}'")
                    continue

            # Flatten predicted values
            predicted_values_flat = np.array(predicted_values).flatten()
            actual_values = merge_data.set_index('year')['sales']
            min_len = min(len(predicted_values_flat), len(actual_values))
            predicted_values_flat = predicted_values_flat[:min_len]
            actual_values = actual_values[:min_len]

            # Calculate metrics

            predicted_values_series = pd.Series(predicted_values_flat, index=actual_values.index)

            # Check the number of unique indices
            unique_indices_actual = actual_values.index.unique()
            unique_indices_predicted = predicted_values_series.index.unique()

            # Print or assert the unique indices
            print("Unique indices in actual_values:", unique_indices_actual)
            print("Unique indices in predicted_values_series:", unique_indices_predicted)

            # Assert that the unique indices match
            assert np.array_equal(unique_indices_actual, unique_indices_predicted), "Indices mismatch"

            # Continue with calculating metrics
            mse = mean_squared_error(actual_values, predicted_values_series)
            mae = mean_absolute_error(actual_values, predicted_values_series)
            r2 = r2_score(actual_values, predicted_values_series)
            # Print the metrics
            print("Mean Squared Error:", mse)
            print("Mean Absolute Error:", mae)
            print("R-squared Score:", r2)

            # DISPLAY METRICS ON LABELS
            self.ui.label_mse.setText(str(mse))
            self.ui.label_mae.setText(str(mae))
            self.ui.label_r2.setText(str(r2))

            actual_sales = merge_data.pivot(index='year', columns='item', values='sales')

            # Reshape predicted values to match the expected shape
            num_items = len(x_train['item'].unique())
            predicted_values_reshaped = np.array(predicted_values).reshape(-1, num_items)

            # Create a DataFrame with predicted sales
            predicted_sales = pd.DataFrame(predicted_values_reshaped, columns=x_train['item'].unique())
            predicted_sales['year'] = range(int(start_prediction), int(end_prediction))
            predicted_sales = predicted_sales.set_index('year')

            # CONNECT TO DATABASE
            connection = sqlite3.connect('sale_forecast.db')

            # SEND DATA TO THE DATABASE
            merge_data['year'] = merge_data['year'].astype(str)
            merge_data.to_sql('all_dataset', connection, if_exists='replace', index=False)
            connection.close()


            print("Data uploaded to the database successfully!")
            self.plot_predictions(actual_sales, predicted_sales)

        else:
            print("Please select a CSV file first.")

    def plot_predictions(self, actual_sales, predicted_sales):
        fig_actual = plt.Figure(figsize=(20, 15))
        ax_actual = fig_actual.add_subplot(111)
        actual_sales.plot(ax=ax_actual, marker='o', linestyle='-', legend=True)
        ax_actual.set_xlabel('Year')
        ax_actual.set_ylabel('Actual Sales')
        ax_actual.set_title('Actual Sales of Individual Items Over Time')

        # Create a canvas for actual sales
        canvas_actual = FigureCanvasQTAgg(fig_actual)
        self.plot_layout_actual_sale.addWidget(canvas_actual)

        # Create a figure for predicted sales
        fig_predicted = plt.Figure(figsize=(20, 15))
        ax_predicted = fig_predicted.add_subplot(111)
        predicted_sales.plot(ax=ax_predicted, marker='o', linestyle='-', legend=True)
        ax_predicted.set_xlabel('Year')
        ax_predicted.set_ylabel('Predicted Sales')
        ax_predicted.set_title('Predicted Sales of Individual Items Over Time')

        # Create a canvas for predicted sales
        canvas_predicted = FigureCanvasQTAgg(fig_predicted)
        self.plot_layout_predict_sale.addWidget(canvas_predicted)




# LOGIN CLASS
class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.dashboard = None
        self.ui = Ui_Log_In()
        self.ui.setupUi(self)

        # LOGIN LABEL IMAGE

        pixmap = QtGui.QPixmap("Images/sales-forecast.jpg")
        self.ui.label.setPixmap(pixmap)
        self.ui.label.setScaledContents(True)
        self.ui.label.setSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        self.ui.label.setStyleSheet(u"border-top-left-radius: 60px;")

        # GET LOGIN BUTTON
        self.ui.loginBtn.clicked.connect(self.authenticate)
        # SQLITE CONNECTION
        self.connection = sqlite3.connect('sale_forecast.db')
        self.cursor = self.connection.cursor()

    def authenticate(self):
        username = self.ui.username.text()
        password = self.ui.password.text()

        if self.check_credentials(username, password):
            print("Authentication successful")
            self.close()
            self.open_dashboard()
        else:
            print("Authentication Failed")

    def check_credentials(self, username, password):
        query = "select * from users where username=? and password=?"
        self.cursor.execute(query, (username, password))
        user = self.cursor.fetchone()

        return user is not None

    def close_event(self, event):
        self.connection.close()

    def open_dashboard(self):
        self.dashboard = DashBoard()
        self.dashboard.show()


class Sales_Predictions(QMainWindow):
    def __init__(self):
        super(Sales_Predictions, self).__init__()
        self.ui = Ui_Welcome_Page()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET APP LOGO
        pixmap = QtGui.QPixmap('clipart1477074.png')
        self.ui.logo_image.setPixmap(pixmap)
        self.ui.logo_image.setScaledContents(True)
        self.ui.logo_image.setSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)

        # HIDE BACKGROUND
        self.ui.background.setMaximumHeight(0)

        # SET INITIAL STATUS
        self.ui.status.setText("Loading..")

        # INITIALIZE ANIMATION
        self.logo_animation()
        self.description_animation()
        self.start_animation()

        # QTIMER
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECOND
        self.timer.start(35)

        # CHANGE STATUS
        QtCore.QTimer.singleShot(2500, lambda: self.ui.status.setText("Loading data..."))
        QtCore.QTimer.singleShot(4500, lambda: self.ui.status.setText("Loading App..."))
        QtCore.QTimer.singleShot(6500, lambda: self.ui.status.setText("Starting App..."))

        # ANIMATE APP  LOGO

    # lOGO  ANIMATION /////////////////////////////////////////////////////
    def logo_animation(self):
        opacity_effect = QGraphicsOpacityEffect(self.ui.logo_image)
        self.ui.logo_image.setGraphicsEffect(opacity_effect)
        # OPACITY ANIMATION /////////////////////////////////////////////////////
        self.logo_opacity_animation = QtCore.QPropertyAnimation(
            opacity_effect, b'opacity', duration=1500, startValue=0, endValue=1
        )
        self.logo_opacity_animation.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        self.logo_opacity_animation.start()

    # ANIMATE APP DESCRIPTION
    def description_animation(self):
        opacity_effect = QtWidgets.QGraphicsOpacityEffect(self.ui.background)
        self.ui.background.setGraphicsEffect(opacity_effect)
        # HIEGHT ANIMATION /////////////////////////////////////////////////////
        geometry_animation = QtCore.QPropertyAnimation(
            self.ui.background,
            b'maximumHeight',
            duration=1000,
            startValue=0,
            endValue=220
        )
        geometry_animation.setEasingCurve(QtCore.QEasingCurve.InOutCubic)

        # OPACITY ANIMATION /////////////////////////////////////////////////////
        opacity_animation = QtCore.QPropertyAnimation(
            opacity_effect, b'opacity', duration=500, startValue=0, endValue=1
        )
        self.description_animation = QtCore.QParallelAnimationGroup(self.ui.background)
        self.description_animation.addAnimation(geometry_animation)
        self.description_animation.addAnimation(opacity_animation)
        self.description_animation.start()

    # START ANIMATION
    # /////////////////////////////////////////////////////////////////////
    def start_animation(self):
        self.anim_group = QtCore.QSequentialAnimationGroup(self)
        self.anim_group.addAnimation(self.logo_opacity_animation)
        self.anim_group.addAnimation(self.description_animation)
        self.anim_group.start()

    # PROGRESS FUNCTION
    # /////////////////////////////////////////////////////////////////////
    def progress(self):
        global counter

        # set value to progress bar
        self.ui.progressBar.setValue(counter)
        self.ui.precentage.setText(f'{int(counter)}%')

        # CLOSE WELCOME SCREEN AND OPEN APP
        if counter > 100:
            # Stop Timer
            self.timer.stop()
            # SHOW LOGIN WINDOW
            self.login = Login()
            self.login.show()

            # CLOSE WELCOME PAGE
            self.close()

        # INCREASE COUNTER
        counter += 0.5


if __name__ == '__main__':
    app = QApplication([])
    window = Sales_Predictions()
    window.show()
    sys.exit(app.exec_())
