<<<<<<< HEAD
import sys
import sqlite3
import time
import random
import pandas as pd
import numpy as np
from PySide6.QtCore import QTimer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from sklearn.preprocessing import StandardScaler
import joblib
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.callbacks import EarlyStopping
from prophet import Prophet

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
        self.timer = None
        self.file_path_sales = None
        self.file_path_indicator = None
        self.file_dialog = None
        self.start_prediction = None
        self.end_prediction = None
        # ASSIGNING THE UI CLASS
        self.ui = Ui_Dashboard_2()
        self.ui.setupUi(self)

        # Adding Signals to NAVIGATION BUTTONS
        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.btn_settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.btn_save_inventory.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.btn_sales_analytics.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.btn_create_account.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.go_to_setting.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))

        # ADDING SIGNAL TO BUTTON ON THE SETTING PAGE
        self.ui.btn_save_setting.clicked.connect(self.assign_date)

        # Adding Signals to BUTTONS ON INVENTORY PAGE
        self.ui.progressBar_training.setValue(0)
        self.ui.btn_path_indicator.clicked.connect(lambda: self.show_file_dialog("indicators"))
        # THIS IS FOR SALES BUTTON
        self.ui.btn_path_indicator_2.clicked.connect(lambda: self.show_file_dialog("sales"))
        self.ui.btn_upload.clicked.connect(self.run_operations)

        # Adding Signals to sale visualization buttons
        self.ui.btn_actual_sale.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))
        self.ui.btn_prediction_sale.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(1))
        self.ui.btn_display_score.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(2))
        self.ui.btn_prediction_sale_list.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(3))

        # Add a widget to the sale analytics page to display the plot
        self.plot_layout_actual_sale = QVBoxLayout(self.ui.page_actual_sale)
        self.plot_layout_predict_sale = QVBoxLayout(self.ui.page_predict_sale)
        # self.canvas = FigureCanvas(Figure(figsize=(10, 6)))
        # self.plot_layout_actual_sale.addWidget(self.canvas)
        # self.plot_layout_predict_sale.addWidget(self.canvas)

        # ADDING CONTENT TO TABLE
        self.ui.table_predicted_sales.setColumnCount(2)
        self.ui.table_predicted_sales.setHorizontalHeaderLabels(["Year", "Predicted Sales"])

        # ASSIGN DATE FUNCTION

    def assign_date(self):
        self.start_prediction = self.ui.start_year_input.text()
        self.end_prediction = self.ui.end_year_input.text()
        self.ui.report_text.setText("Please Wait...")
        self.ui.start_year_input.clear()
        self.ui.end_year_input.clear()
        self.ui.report_text.setText("Save Successfully")
        self.ui.stackedWidget.setCurrentIndex(2)

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

    # PROGRESSBAR   FUNCTION
    def run_operations(self):
        # PROGRESS BAR
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(1000)
        progress_value = self.ui.progressBar_training.value()

        if progress_value >= 100:
            # If progress is already complete, proceed directly to database upload
            self.upload_to_database()
        else:
            print("Operations in progress...")
            self.ui.btn_upload.setEnabled(False)

    def update_progress(self):
        current_progress = self.ui.progressBar_training.value()
        # Increment progress by a certain amount based on the task completion
        updated_progress = current_progress + 10
        self.ui.progressBar_training.setValue(updated_progress)

        if updated_progress >= 100:
            # If progress reaches 100 or more, stop the timer and initiate database upload
            self.timer.stop()
            self.upload_to_database()

        # SEND DATA TO DATABASE FUNCTION

    def upload_to_database(self, ):

        if hasattr(self, 'file_path_sales'):
            # READ DATA

            indicators = pd.read_csv(self.file_path_indicator)
            sales = pd.read_csv(self.file_path_sales)

            # SET PREDICTION YEAR

            start_prediction = self.start_prediction
            end_prediction = self.end_prediction
            start_period = pd.Period(start_prediction)
            end_period = pd.Period(end_prediction)
            print(start_prediction, end_prediction)

            # PREPROCESS DATA
            if "product" in sales:
                sales = sales.drop("product", axis=1)

            sales = sales.groupby(['year']).sum().reset_index()
            sales['year'] = pd.to_datetime(sales['year'], format='%Y').dt.year
            indicators['year'] = pd.to_datetime(indicators['year'], format='%Y').dt.year
            merge_data = pd.merge(sales, indicators, on='year')
            merge_data['year'] = pd.to_datetime(merge_data["year"], format='%Y')
            merge_data['month'] = merge_data['year'].dt.month
            merge_data['quarter'] = merge_data['year'].dt.quarter
            merge_data['year'] = merge_data['year'].dt.year

            # SPLITTING INTO TRAINING AND TESTING SETS
            train = merge_data[merge_data['year'] <= start_period.year]
            test = []

            # FEATURE ENGINEERING AFTER SPLITTING
            train = train.copy()  # Make a copy of the DataFrame
            train['rolling_mean_sales'] = train.groupby('year')['total_sales'].transform(
                lambda x: x.rolling(window=3).mean().fillna(x.mean()))
            train['rolling_std_sales'] = train['rolling_mean_sales'].transform(
                lambda x: x.rolling(window=3).std())
            train['lagged_sales_1'] = train['total_sales'].shift(1)
            train['lagged_sales_2'] = train['total_sales'].shift(2)
            train['sales_times_weather'] = train['total_sales'] * train['Precipitation']
            train['sales_divided_by_economic'] = train['total_sales'] / train['GDP']

            # FILL MISSING VALUES AFTER SPLITTING
            train = train.fillna(train.mean()).ffill().interpolate(method='linear')
            synthetic_train = train.copy()

            # CREATE CSV ON TRAIN DATA
            train.to_csv("train_data.csv")

            # TRAINING AXIS
            target_variable = "total_sales"
            x_train_lr = train.drop([target_variable], axis=1)
            predictors_variable = x_train_lr.columns
            y_train_lr = train[target_variable]

            # TRAINING FOR LINEAR REGRESSION
            linear_regression = LinearRegression()
            linear_regression.fit(x_train_lr, y_train_lr)

            # TRAINING SCALING FOR PROPHET
            train['ds'] = pd.to_datetime(train['year'], format="%Y")
            prophet_train = train[['ds', 'total_sales']].rename(columns={'total_sales': 'y'})
            prophet_model = Prophet(yearly_seasonality=True, seasonality_prior_scale=0.1)
            prophet_model.fit(prophet_train)
            print(f"this is for prophet {train['ds']}")

            # GENERATING SYNTHETIC DATA FUNCTION
            def generate_synthetic_data(years, train):
                simulated_data = pd.DataFrame(columns=train.columns)
                average_sales = train['total_sales'].mean()
                max_sales = train['total_sales'].max()
                min_sales = train['total_sales'].min()
                for year in years:
                    synthetic_sales = np.random.uniform(average_sales, max_sales + (
                            min_sales * random.random()))  # Add 1 to ensure it's above the maximum
                    row = pd.Series({
                        'year': year,
                        'total_sales': synthetic_sales,
                        'rolling_mean_sales': np.random.normal(train['rolling_mean_sales'].mean(),
                                                               train['rolling_mean_sales'].std()),
                        'GDP': np.random.normal(train['GDP'].mean(), train['GDP'].std()),
                        'Consumer Price Index': np.random.normal(train['Consumer Price Index'].mean(),
                                                                 train['Consumer Price Index'].std()),
                        'Unemployment rate (Percent)': np.random.normal(train['Unemployment rate (Percent)'].mean(),
                                                                        train['Unemployment rate (Percent)'].std()),
                        'Inflation rate': np.random.normal(train['Inflation rate'].mean(),
                                                           train['Inflation rate'].std()),
                        'Real interest rate (%)': np.random.normal(train['month'].mean(), train['month'].std()),
                        'Temperature (High)': np.random.normal(train['Temperature (High)'].mean(),
                                                               train['Temperature (High)'].std()),
                        'Temperature (low)': np.random.normal(train['Temperature (low)'].mean(),
                                                              train['Temperature (low)'].std()),
                        'Precipitation': np.random.normal(train['Precipitation'].mean(), train['Precipitation'].std()),
                        'month': np.random.normal(train['month'].mean(), train['month'].std()),
                        'quarter': np.random.normal(train['quarter'].mean(), train['quarter'].std()),
                        'rolling_std_sales': np.random.normal(train['rolling_std_sales'].mean(),
                                                              train['rolling_std_sales'].std()),
                        'lagged_sales_1': np.random.normal(train['lagged_sales_1'].mean(),
                                                           train['lagged_sales_1'].std()),
                        'lagged_sales_2': np.random.normal(train['lagged_sales_2'].mean(),
                                                           train['lagged_sales_2'].std()),
                        'sales_times_weather': np.random.normal(train['sales_times_weather'].mean(),
                                                                train['sales_times_weather'].std()),
                        'sales_divided_by_economic': np.random.normal(train['sales_divided_by_economic'].mean(),
                                                                      train['sales_divided_by_economic'].std())
                    })
                    simulated_data = simulated_data._append(row, ignore_index=True)
                return simulated_data

            # Check if end_period.year is greater than 2022
            if end_period.year > 2022:
                # Generate synthetic data
                future_years = range(int(start_prediction), int(end_prediction) + 1)
                test = generate_synthetic_data(future_years, synthetic_train)
                print(test)  # Print the generated simulated data
            else:
                # Split testing sets
                test = merge_data[merge_data['year'] > start_period.year].copy()

                # Perform feature engineering after splitting
                test['rolling_mean_sales'] = test.groupby('year')['total_sales'].transform(
                    lambda x: x.rolling(window=3).mean().fillna(x.mean()))
                test['rolling_std_sales'] = test['rolling_mean_sales'].transform(lambda x: x.rolling(window=3).std())
                test['lagged_sales_1'] = test['total_sales'].shift(1)
                test['lagged_sales_2'] = test['total_sales'].shift(2)
                test['sales_times_weather'] = test['total_sales'] * test['Precipitation']
                test['sales_divided_by_economic'] = test['total_sales'] / test['GDP']
                # FILL MISSING VALUES AFTER SPLITTING
                test = test.fillna(train.mean()).ffill().interpolate(method='linear')

            test.to_csv("test_data.csv")

            # TESTING AXIS
            x_test_lr = test.drop(['total_sales'], axis=1)
            y_test_lr = test["total_sales"]

            # PREDICTION AND EVALUATION

            # LINEAR REGRESSION PREDICTIONS
            lr_predictions = linear_regression.predict(x_test_lr)

            # PROPHET PREDICTIONS
            start_date = pd.to_datetime(start_prediction)
            end_date = pd.to_datetime(str(int(end_prediction) + 1))
            future_years = pd.date_range(start=start_date, end=end_date, freq='Y')
            print(future_years)
            future_prophet = pd.DataFrame({'ds': future_years})
            print(future_prophet)
            future_prophet_predictions = prophet_model.predict(future_prophet)

            # EVALUATION METRICS FOR LINEAR REGRESSION
            lr_rmse = np.sqrt(mean_squared_error(y_test_lr, lr_predictions))
            lr_mae = mean_absolute_error(y_test_lr, lr_predictions)
            lr_r2 = r2_score(y_test_lr, lr_predictions)


            # EVALUATION METRICS FOR PROPHET
            prophet_predictions = future_prophet_predictions['yhat'].values
            actual_values = future_prophet_predictions['trend'].values
            prophet_rmse = np.sqrt(mean_squared_error(actual_values, prophet_predictions))
            prophet_mae = mean_absolute_error(actual_values, prophet_predictions)
            prophet_r2 = r2_score(actual_values, prophet_predictions)

            # PRINT METRICS
            print("Linear Regression Metrics:")
            print("RMSE:", lr_rmse)
            print("MAE:", lr_mae)
            print("R-squared:", lr_r2)

            print("Prophet RMSE:", prophet_rmse)
            print("Prophet MAE:", prophet_mae)
            print("Prophet R-squared:", prophet_r2)

            # DISPLAY METRICS ON LABELS
            def display_metric(mse, mae, r2):
                self.ui.label_mse.setText(str(mse))
                self.ui.label_mae.setText(str(mae))
                self.ui.label_r2.setText(str(r2))

            actual_sales = merge_data.set_index('year')['total_sales']

            if lr_rmse < prophet_rmse:
                display_metric(lr_rmse, lr_mae, lr_r2)
                self.plot_predictions(actual_sales, lr_predictions, test)
                lr_predicted_years = future_years.year
                lr_predicted_sales = lr_predictions.tolist()
                for row, (year, sales) in enumerate(zip(lr_predicted_years, lr_predicted_sales)):
                    # Add predicted year to the first column
                    year_item = QTableWidgetItem(str(year))
                    self.ui.table_predicted_sales.setItem(row, 0, year_item)

                    # Add corresponding sales to the second column
                    sales_item = QTableWidgetItem(str(sales))
                    self.ui.table_predicted_sales.setItem(row, 1, sales_item)

            else:
                display_metric(prophet_rmse, prophet_mae, prophet_r2)
                self.plot_predictions(actual_sales, prophet_predictions, test)
                prophet_predicted_years = future_years.year  # Extract years from the future_years
                prophet_predicted_sales = future_prophet_predictions['yhat'].values.tolist()
                for row, (year, sales) in enumerate(zip(prophet_predicted_years, prophet_predicted_sales)):
                    # Add predicted year to the first column
                    year_item = QTableWidgetItem(str(year))
                    self.ui.table_predicted_sales.setItem(row, 0, year_item)

                    # Add corresponding sales to the second column
                    sales_item = QTableWidgetItem(str(sales))
                    self.ui.table_predicted_sales.setItem(row, 1, sales_item)

            # CONNECT TO DATABASE
            connection = sqlite3.connect('sale_forecast.db')

            # SEND DATA TO THE DATABASE
            merge_data['year'] = merge_data['year'].astype(str)
            merge_data.to_sql('all_dataset', connection, if_exists='replace', index=False)
            connection.close()

            print("Data uploaded to the database successfully!")

        else:
            print("Please select a CSV file first.")

        self.ui.stackedWidget.setCurrentIndex(3)

    def plot_predictions(self, actual_sales, predictions, test):
        fig_actual = plt.Figure(figsize=(20, 15))
        ax_actual = fig_actual.add_subplot(111)
        actual_sales.plot(ax=ax_actual, marker='o', linestyle='-', legend=True)
        ax_actual.set_xlabel('Year')
        ax_actual.set_ylabel('Actual Sales')
        ax_actual.set_title('Actual Sales  Time')

        # Create a canvas for actual sales
        canvas_actual = FigureCanvasQTAgg(fig_actual)
        self.plot_layout_actual_sale.addWidget(canvas_actual)

        # Create a figure for predicted sales
        fig_lr = plt.Figure(figsize=(20, 15))
        ax_lr = fig_lr.add_subplot(111)
        ax_lr.plot(test['year'], predictions, label='Mix_Model Predictions', )
        ax_lr.set_xlabel('Year')
        ax_lr.set_ylabel('Total Sales')
        ax_lr.set_title(' Predictions Over Time')
        ax_lr.legend()
        # Create a canvas for predicted sales
        canvas_predicted = FigureCanvasQTAgg(fig_lr)
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
=======
import sys
import sqlite3
import time
import random
import pandas as pd
import numpy as np
from PySide6.QtCore import QTimer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from sklearn.preprocessing import StandardScaler
import joblib
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.callbacks import EarlyStopping
from prophet import Prophet

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
        self.timer = None
        self.file_path_sales = None
        self.file_path_indicator = None
        self.file_dialog = None
        self.start_prediction = None
        self.end_prediction = None
        # ASSIGNING THE UI CLASS
        self.ui = Ui_Dashboard_2()
        self.ui.setupUi(self)

        # Adding Signals to NAVIGATION BUTTONS
        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.btn_settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.btn_save_inventory.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.btn_sales_analytics.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.btn_create_account.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.go_to_setting.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))

        # ADDING SIGNAL TO BUTTON ON THE SETTING PAGE
        self.ui.btn_save_setting.clicked.connect(self.assign_date)

        # Adding Signals to BUTTONS ON INVENTORY PAGE
        self.ui.progressBar_training.setValue(0)
        self.ui.btn_path_indicator.clicked.connect(lambda: self.show_file_dialog("indicators"))
        # THIS IS FOR SALES BUTTON
        self.ui.btn_path_indicator_2.clicked.connect(lambda: self.show_file_dialog("sales"))
        self.ui.btn_upload.clicked.connect(self.run_operations)

        # Adding Signals to sale visualization buttons
        self.ui.btn_actual_sale.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))
        self.ui.btn_prediction_sale.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(1))
        self.ui.btn_display_score.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(2))
        self.ui.btn_prediction_sale_list.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(3))

        # Add a widget to the sale analytics page to display the plot
        self.plot_layout_actual_sale = QVBoxLayout(self.ui.page_actual_sale)
        self.plot_layout_predict_sale = QVBoxLayout(self.ui.page_predict_sale)
        # self.canvas = FigureCanvas(Figure(figsize=(10, 6)))
        # self.plot_layout_actual_sale.addWidget(self.canvas)
        # self.plot_layout_predict_sale.addWidget(self.canvas)

        # ADDING CONTENT TO TABLE
        self.ui.table_predicted_sales.setColumnCount(2)
        self.ui.table_predicted_sales.setHorizontalHeaderLabels(["Year", "Predicted Sales"])

        # ASSIGN DATE FUNCTION

    def assign_date(self):
        self.start_prediction = self.ui.start_year_input.text()
        self.end_prediction = self.ui.end_year_input.text()
        self.ui.report_text.setText("Please Wait...")
        self.ui.start_year_input.clear()
        self.ui.end_year_input.clear()
        self.ui.report_text.setText("Save Successfully")
        self.ui.stackedWidget.setCurrentIndex(2)

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

    # PROGRESSBAR   FUNCTION
    def run_operations(self):
        # PROGRESS BAR
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(1000)
        progress_value = self.ui.progressBar_training.value()

        if progress_value >= 100:
            # If progress is already complete, proceed directly to database upload
            self.upload_to_database()
        else:
            print("Operations in progress...")
            self.ui.btn_upload.setEnabled(False)

    def update_progress(self):
        current_progress = self.ui.progressBar_training.value()
        # Increment progress by a certain amount based on the task completion
        updated_progress = current_progress + 10
        self.ui.progressBar_training.setValue(updated_progress)

        if updated_progress >= 100:
            # If progress reaches 100 or more, stop the timer and initiate database upload
            self.timer.stop()
            self.upload_to_database()

        # SEND DATA TO DATABASE FUNCTION

    def upload_to_database(self, ):

        if hasattr(self, 'file_path_sales'):
            # READ DATA

            indicators = pd.read_csv(self.file_path_indicator)
            sales = pd.read_csv(self.file_path_sales)

            # SET PREDICTION YEAR

            start_prediction = self.start_prediction
            end_prediction = self.end_prediction
            start_period = pd.Period(start_prediction)
            end_period = pd.Period(end_prediction)
            print(start_prediction, end_prediction)

            # PREPROCESS DATA
            if "product" in sales:
                sales = sales.drop("product", axis=1)

            sales = sales.groupby(['year']).sum().reset_index()
            sales['year'] = pd.to_datetime(sales['year'], format='%Y').dt.year
            indicators['year'] = pd.to_datetime(indicators['year'], format='%Y').dt.year
            merge_data = pd.merge(sales, indicators, on='year')
            merge_data['year'] = pd.to_datetime(merge_data["year"], format='%Y')
            merge_data['month'] = merge_data['year'].dt.month
            merge_data['quarter'] = merge_data['year'].dt.quarter
            merge_data['year'] = merge_data['year'].dt.year

            # SPLITTING INTO TRAINING AND TESTING SETS
            train = merge_data[merge_data['year'] <= start_period.year]
            test = []

            # FEATURE ENGINEERING AFTER SPLITTING
            train = train.copy()  # Make a copy of the DataFrame
            train['rolling_mean_sales'] = train.groupby('year')['total_sales'].transform(
                lambda x: x.rolling(window=3).mean().fillna(x.mean()))
            train['rolling_std_sales'] = train['rolling_mean_sales'].transform(
                lambda x: x.rolling(window=3).std())
            train['lagged_sales_1'] = train['total_sales'].shift(1)
            train['lagged_sales_2'] = train['total_sales'].shift(2)
            train['sales_times_weather'] = train['total_sales'] * train['Precipitation']
            train['sales_divided_by_economic'] = train['total_sales'] / train['GDP']

            # FILL MISSING VALUES AFTER SPLITTING
            train = train.fillna(train.mean()).ffill().interpolate(method='linear')
            synthetic_train = train.copy()

            # CREATE CSV ON TRAIN DATA
            train.to_csv("train_data.csv")

            # TRAINING AXIS
            target_variable = "total_sales"
            x_train_lr = train.drop([target_variable], axis=1)
            predictors_variable = x_train_lr.columns
            y_train_lr = train[target_variable]

            # TRAINING FOR LINEAR REGRESSION
            linear_regression = LinearRegression()
            linear_regression.fit(x_train_lr, y_train_lr)

            # TRAINING SCALING FOR PROPHET
            train['ds'] = pd.to_datetime(train['year'], format="%Y")
            prophet_train = train[['ds', 'total_sales']].rename(columns={'total_sales': 'y'})
            prophet_model = Prophet(yearly_seasonality=True, seasonality_prior_scale=0.1)
            prophet_model.fit(prophet_train)
            print(f"this is for prophet {train['ds']}")

            # GENERATING SYNTHETIC DATA FUNCTION
            def generate_synthetic_data(years, train):
                simulated_data = pd.DataFrame(columns=train.columns)
                average_sales = train['total_sales'].mean()
                max_sales = train['total_sales'].max()
                min_sales = train['total_sales'].min()
                for year in years:
                    synthetic_sales = np.random.uniform(average_sales, max_sales + (
                            min_sales * random.random()))  # Add 1 to ensure it's above the maximum
                    row = pd.Series({
                        'year': year,
                        'total_sales': synthetic_sales,
                        'rolling_mean_sales': np.random.normal(train['rolling_mean_sales'].mean(),
                                                               train['rolling_mean_sales'].std()),
                        'GDP': np.random.normal(train['GDP'].mean(), train['GDP'].std()),
                        'Consumer Price Index': np.random.normal(train['Consumer Price Index'].mean(),
                                                                 train['Consumer Price Index'].std()),
                        'Unemployment rate (Percent)': np.random.normal(train['Unemployment rate (Percent)'].mean(),
                                                                        train['Unemployment rate (Percent)'].std()),
                        'Inflation rate': np.random.normal(train['Inflation rate'].mean(),
                                                           train['Inflation rate'].std()),
                        'Real interest rate (%)': np.random.normal(train['month'].mean(), train['month'].std()),
                        'Temperature (High)': np.random.normal(train['Temperature (High)'].mean(),
                                                               train['Temperature (High)'].std()),
                        'Temperature (low)': np.random.normal(train['Temperature (low)'].mean(),
                                                              train['Temperature (low)'].std()),
                        'Precipitation': np.random.normal(train['Precipitation'].mean(), train['Precipitation'].std()),
                        'month': np.random.normal(train['month'].mean(), train['month'].std()),
                        'quarter': np.random.normal(train['quarter'].mean(), train['quarter'].std()),
                        'rolling_std_sales': np.random.normal(train['rolling_std_sales'].mean(),
                                                              train['rolling_std_sales'].std()),
                        'lagged_sales_1': np.random.normal(train['lagged_sales_1'].mean(),
                                                           train['lagged_sales_1'].std()),
                        'lagged_sales_2': np.random.normal(train['lagged_sales_2'].mean(),
                                                           train['lagged_sales_2'].std()),
                        'sales_times_weather': np.random.normal(train['sales_times_weather'].mean(),
                                                                train['sales_times_weather'].std()),
                        'sales_divided_by_economic': np.random.normal(train['sales_divided_by_economic'].mean(),
                                                                      train['sales_divided_by_economic'].std())
                    })
                    simulated_data = simulated_data._append(row, ignore_index=True)
                return simulated_data

            # Check if end_period.year is greater than 2022
            if end_period.year > 2022:
                # Generate synthetic data
                future_years = range(int(start_prediction), int(end_prediction) + 1)
                test = generate_synthetic_data(future_years, synthetic_train)
                print(test)  # Print the generated simulated data
            else:
                # Split testing sets
                test = merge_data[merge_data['year'] > start_period.year].copy()

                # Perform feature engineering after splitting
                test['rolling_mean_sales'] = test.groupby('year')['total_sales'].transform(
                    lambda x: x.rolling(window=3).mean().fillna(x.mean()))
                test['rolling_std_sales'] = test['rolling_mean_sales'].transform(lambda x: x.rolling(window=3).std())
                test['lagged_sales_1'] = test['total_sales'].shift(1)
                test['lagged_sales_2'] = test['total_sales'].shift(2)
                test['sales_times_weather'] = test['total_sales'] * test['Precipitation']
                test['sales_divided_by_economic'] = test['total_sales'] / test['GDP']
                # FILL MISSING VALUES AFTER SPLITTING
                test = test.fillna(train.mean()).ffill().interpolate(method='linear')

            test.to_csv("test_data.csv")

            # TESTING AXIS
            x_test_lr = test.drop(['total_sales'], axis=1)
            y_test_lr = test["total_sales"]

            # PREDICTION AND EVALUATION

            # LINEAR REGRESSION PREDICTIONS
            lr_predictions = linear_regression.predict(x_test_lr)

            # PROPHET PREDICTIONS
            start_date = pd.to_datetime(start_prediction)
            end_date = pd.to_datetime(str(int(end_prediction) + 1))
            future_years = pd.date_range(start=start_date, end=end_date, freq='Y')
            print(future_years)
            future_prophet = pd.DataFrame({'ds': future_years})
            print(future_prophet)
            future_prophet_predictions = prophet_model.predict(future_prophet)

            # EVALUATION METRICS FOR LINEAR REGRESSION
            lr_rmse = np.sqrt(mean_squared_error(y_test_lr, lr_predictions))
            lr_mae = mean_absolute_error(y_test_lr, lr_predictions)
            lr_r2 = r2_score(y_test_lr, lr_predictions)


            # EVALUATION METRICS FOR PROPHET
            prophet_predictions = future_prophet_predictions['yhat'].values
            actual_values = future_prophet_predictions['trend'].values
            prophet_rmse = np.sqrt(mean_squared_error(actual_values, prophet_predictions))
            prophet_mae = mean_absolute_error(actual_values, prophet_predictions)
            prophet_r2 = r2_score(actual_values, prophet_predictions)

            # PRINT METRICS
            print("Linear Regression Metrics:")
            print("RMSE:", lr_rmse)
            print("MAE:", lr_mae)
            print("R-squared:", lr_r2)

            print("Prophet RMSE:", prophet_rmse)
            print("Prophet MAE:", prophet_mae)
            print("Prophet R-squared:", prophet_r2)

            # DISPLAY METRICS ON LABELS
            def display_metric(mse, mae, r2):
                self.ui.label_mse.setText(str(mse))
                self.ui.label_mae.setText(str(mae))
                self.ui.label_r2.setText(str(r2))

            actual_sales = merge_data.set_index('year')['total_sales']

            if lr_rmse < prophet_rmse:
                display_metric(lr_rmse, lr_mae, lr_r2)
                self.plot_predictions(actual_sales, lr_predictions, test)
                lr_predicted_years = future_years.year
                lr_predicted_sales = lr_predictions.tolist()
                for row, (year, sales) in enumerate(zip(lr_predicted_years, lr_predicted_sales)):
                    # Add predicted year to the first column
                    year_item = QTableWidgetItem(str(year))
                    self.ui.table_predicted_sales.setItem(row, 0, year_item)

                    # Add corresponding sales to the second column
                    sales_item = QTableWidgetItem(str(sales))
                    self.ui.table_predicted_sales.setItem(row, 1, sales_item)

            else:
                display_metric(prophet_rmse, prophet_mae, prophet_r2)
                self.plot_predictions(actual_sales, prophet_predictions, test)
                prophet_predicted_years = future_years.year  # Extract years from the future_years
                prophet_predicted_sales = future_prophet_predictions['yhat'].values.tolist()
                for row, (year, sales) in enumerate(zip(prophet_predicted_years, prophet_predicted_sales)):
                    # Add predicted year to the first column
                    year_item = QTableWidgetItem(str(year))
                    self.ui.table_predicted_sales.setItem(row, 0, year_item)

                    # Add corresponding sales to the second column
                    sales_item = QTableWidgetItem(str(sales))
                    self.ui.table_predicted_sales.setItem(row, 1, sales_item)

            # CONNECT TO DATABASE
            connection = sqlite3.connect('sale_forecast.db')

            # SEND DATA TO THE DATABASE
            merge_data['year'] = merge_data['year'].astype(str)
            merge_data.to_sql('all_dataset', connection, if_exists='replace', index=False)
            connection.close()

            print("Data uploaded to the database successfully!")

        else:
            print("Please select a CSV file first.")

        self.ui.stackedWidget.setCurrentIndex(3)

    def plot_predictions(self, actual_sales, predictions, test):
        fig_actual = plt.Figure(figsize=(20, 15))
        ax_actual = fig_actual.add_subplot(111)
        actual_sales.plot(ax=ax_actual, marker='o', linestyle='-', legend=True)
        ax_actual.set_xlabel('Year')
        ax_actual.set_ylabel('Actual Sales')
        ax_actual.set_title('Actual Sales  Time')

        # Create a canvas for actual sales
        canvas_actual = FigureCanvasQTAgg(fig_actual)
        self.plot_layout_actual_sale.addWidget(canvas_actual)

        # Create a figure for predicted sales
        fig_lr = plt.Figure(figsize=(20, 15))
        ax_lr = fig_lr.add_subplot(111)
        ax_lr.plot(test['year'], predictions, label='Mix_Model Predictions', )
        ax_lr.set_xlabel('Year')
        ax_lr.set_ylabel('Total Sales')
        ax_lr.set_title(' Predictions Over Time')
        ax_lr.legend()
        # Create a canvas for predicted sales
        canvas_predicted = FigureCanvasQTAgg(fig_lr)
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
>>>>>>> 79b9658ccc23aa8723f2d829bae8c11527986fee
