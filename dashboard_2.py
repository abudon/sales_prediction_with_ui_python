# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard_2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSlider, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import files_rc

class Ui_Dashboard_2(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 720)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 60))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: #f5f5f5;")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(92,163,230);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 30))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(92, 163, 230, .5);")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(8, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamilies([u"Futura XBlkCnIt BT"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"margin-left: 5px;\n"
"color: #fff;")
        self.label_title_bar_top.setAlignment(Qt.AlignCenter)
        self.label_title_bar_top.setWordWrap(True)

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setStyleSheet(u"background-color: rgb(92, 163, 230);\n"
"")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color:#000;")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setBold(True)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: #000;")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy1)
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)
        self.btn_save_inventory = QPushButton(self.frame_menus)
        self.btn_save_inventory.setObjectName(u"btn_save_inventory")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_save_inventory.sizePolicy().hasHeightForWidth())
        self.btn_save_inventory.setSizePolicy(sizePolicy2)
        self.btn_save_inventory.setMinimumSize(QSize(0, 60))
        self.btn_save_inventory.setFont(font2)
        self.btn_save_inventory.setLayoutDirection(Qt.LeftToRight)
        self.btn_save_inventory.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/16x16/icons/16x16/cil-folder-open.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid rgb(27, 29, 35);\n"
"	border-right: 5px solid rgb(44, 49, 60);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.layout_menus.addWidget(self.btn_save_inventory)

        self.btn_home = QPushButton(self.frame_menus)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy2.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy2)
        self.btn_home.setMinimumSize(QSize(0, 60))
        self.btn_home.setFont(font2)
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/16x16/icons/16x16/cil-save.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.layout_menus.addWidget(self.btn_home)

        self.btn_sales_analytics = QPushButton(self.frame_menus)
        self.btn_sales_analytics.setObjectName(u"btn_sales_analytics")
        sizePolicy2.setHeightForWidth(self.btn_sales_analytics.sizePolicy().hasHeightForWidth())
        self.btn_sales_analytics.setSizePolicy(sizePolicy2)
        self.btn_sales_analytics.setMinimumSize(QSize(0, 60))
        self.btn_sales_analytics.setFont(font2)
        self.btn_sales_analytics.setLayoutDirection(Qt.LeftToRight)
        self.btn_sales_analytics.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/16x16/icons/16x16/cil-file.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.layout_menus.addWidget(self.btn_sales_analytics)

        self.btn_create_account = QPushButton(self.frame_menus)
        self.btn_create_account.setObjectName(u"btn_create_account")
        sizePolicy2.setHeightForWidth(self.btn_create_account.sizePolicy().hasHeightForWidth())
        self.btn_create_account.setSizePolicy(sizePolicy2)
        self.btn_create_account.setMinimumSize(QSize(0, 60))
        self.btn_create_account.setFont(font2)
        self.btn_create_account.setLayoutDirection(Qt.LeftToRight)
        self.btn_create_account.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/16x16/icons/16x16/cil-user-follow.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.layout_menus.addWidget(self.btn_create_account)


        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy1.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy1)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy3)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)

        self.btn_settings = QPushButton(self.frame_extra_menus)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy2.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy2)
        self.btn_settings.setMinimumSize(QSize(0, 60))
        self.btn_settings.setFont(font2)
        self.btn_settings.setLayoutDirection(Qt.LeftToRight)
        self.btn_settings.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/20x20/icons/20x20/cil-settings.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 26px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 26px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 26px solid rgb(85, 170, 255);\n"
"}")

        self.layout_menu_bottom.addWidget(self.btn_settings)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.page_home)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(40)
        font5.setBold(True)
        font5.setItalic(True)
        self.label_6.setFont(font5)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label_6)

        self.frame_2 = QFrame(self.page_home)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.widget_9 = QWidget(self.frame_2)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(600, 0))
        self.widget_9.setStyleSheet(u"QWidget{\n"
"width: 70%\n"
"}")
        self.verticalLayout_22 = QVBoxLayout(self.widget_9)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(-1, -1, 10, -1)
        self.label_2 = QLabel(self.widget_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(500, 0))
        self.label_2.setMaximumSize(QSize(500, 16777215))
        self.label_2.setStyleSheet(u"QLabel{\n"
"background-color:#f5f5f5 ;\n"
"color: rgb(92,163,230);\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"padding: 0 30px;\n"
"border: 3px solid #f5f5f5;\n"
"border-radius: 25px\n"
"}")
        self.label_2.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.label_2)


        self.horizontalLayout_19.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.frame_2)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92,163,230);\n"
"border: 3px solid rgb(92,163,230);\n"
"border-radius: 25px\n"
"}")
        self.verticalLayout_23 = QVBoxLayout(self.widget_10)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_7 = QLabel(self.widget_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setStyleSheet(u"QLabel{\n"
"padding-left: 20px;\n"
"color: white;\n"
"font-size: 18px;\n"
"font-weight: bold;\n"
"font-style: italic\n"
"}")
        self.label_7.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.label_7)

        self.label_16 = QLabel(self.widget_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"QLabel{\n"
"font-weight: bold;\n"
"color: white\n"
"}")
        self.label_16.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.label_16)

        self.go_to_setting = QPushButton(self.widget_10)
        self.go_to_setting.setObjectName(u"go_to_setting")
        self.go_to_setting.setMinimumSize(QSize(150, 30))
        self.go_to_setting.setMaximumSize(QSize(150, 30))
        self.go_to_setting.setStyleSheet(u"QPushButton{ \n"
"border: 1px solid #000000; /* Border color and width */\n"
"	border-radius: 5px;\n"
"	color: rgb(92,163,230);\n"
"	font-size: 14px;\n"
"background-color:#fff;\n"
"font-weight: bold\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: #000\n"
"}")

        self.verticalLayout_23.addWidget(self.go_to_setting, 0, Qt.AlignHCenter)


        self.horizontalLayout_19.addWidget(self.widget_10)


        self.verticalLayout_10.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_home)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.horizontalLayout_9 = QHBoxLayout(self.page_settings)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.container = QWidget(self.page_settings)
        self.container.setObjectName(u"container")
        self.verticalLayout_7 = QVBoxLayout(self.container)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(100, -1, 100, -1)
        self.label = QLabel(self.container)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(16777215, 120))
        font6 = QFont()
        font6.setPointSize(48)
        font6.setBold(True)
        font6.setItalic(True)
        self.label.setFont(font6)

        self.verticalLayout_7.addWidget(self.label)

        self.widget = QWidget(self.container)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_11 = QVBoxLayout(self.widget_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.prediction_setting = QFrame(self.widget_2)
        self.prediction_setting.setObjectName(u"prediction_setting")
        self.prediction_setting.setFrameShape(QFrame.StyledPanel)
        self.prediction_setting.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.prediction_setting)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_13 = QLabel(self.prediction_setting)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"QLabel{\n"
"font-size: 36px;\n"
"font-weight: bold;\n"
"font-style: italic;\n"
"}")
        self.label_13.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_13)

        self.frame_5 = QFrame(self.prediction_setting)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.widget_7 = QWidget(self.frame_5)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_20 = QVBoxLayout(self.widget_7)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_15 = QLabel(self.widget_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"QLabel{\n"
"font-size: 24px;\n"
"font-weight: bold;\n"
"font-style: italic;\n"
"}")
        self.label_15.setWordWrap(True)

        self.verticalLayout_20.addWidget(self.label_15)

        self.start_year_input = QLineEdit(self.widget_7)
        self.start_year_input.setObjectName(u"start_year_input")
        self.start_year_input.setMinimumSize(QSize(0, 0))
        font7 = QFont()
        font7.setPointSize(10)
        font7.setBold(True)
        self.start_year_input.setFont(font7)
        self.start_year_input.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    selection-background-color: lightblue;\n"
"	color: #000000\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(92,163,230);\n"
"}")

        self.verticalLayout_20.addWidget(self.start_year_input)


        self.horizontalLayout_16.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.frame_5)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_19 = QVBoxLayout(self.widget_6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_14 = QLabel(self.widget_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"QLabel{\n"
"font-size: 24px;\n"
"font-weight: bold;\n"
"font-style: italic;\n"
"}")

        self.verticalLayout_19.addWidget(self.label_14)

        self.end_year_input = QLineEdit(self.widget_6)
        self.end_year_input.setObjectName(u"end_year_input")
        self.end_year_input.setMinimumSize(QSize(0, 0))
        font8 = QFont()
        font8.setBold(True)
        self.end_year_input.setFont(font8)
        self.end_year_input.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    selection-background-color: lightblue;\n"
"	color: #000000\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(92,163,230);\n"
"}")

        self.verticalLayout_19.addWidget(self.end_year_input)


        self.horizontalLayout_16.addWidget(self.widget_6)


        self.verticalLayout_18.addWidget(self.frame_5)


        self.verticalLayout_11.addWidget(self.prediction_setting)

        self.frame_3 = QFrame(self.widget_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel{\n"
"font-size: 36px;\n"
"font-weight: bold;\n"
"font-style: italic;\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.horizontalSlider = QSlider(self.frame_3)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height: 10px;\n"
"    background: #ddd;\n"
"    border: 1px solid #bbb;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #4CAF50;\n"
"    border: 1px solid #4CAF50;\n"
"    width: 18px;\n"
"    margin: -8px 0;\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #4CAF50;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #ddd;\n"
"}")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.horizontalSlider, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_3)

        self.frame = QFrame(self.widget_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.email = QLabel(self.frame)
        self.email.setObjectName(u"email")
        self.email.setStyleSheet(u"QLabel{\n"
"font-size: 36px;\n"
"font-weight: bold;\n"
"font-style: italic;\n"
"}")

        self.verticalLayout_12.addWidget(self.email)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    selection-background-color: lightblue;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4CAF50;\n"
"}")

        self.verticalLayout_12.addWidget(self.lineEdit)

        self.report_text = QLabel(self.frame)
        self.report_text.setObjectName(u"report_text")
        font9 = QFont()
        font9.setPointSize(16)
        font9.setBold(True)
        font9.setItalic(True)
        self.report_text.setFont(font9)
        self.report_text.setStyleSheet(u"")
        self.report_text.setWordWrap(True)
        self.report_text.setMargin(2)

        self.verticalLayout_12.addWidget(self.report_text)

        self.btn_save_setting = QPushButton(self.frame)
        self.btn_save_setting.setObjectName(u"btn_save_setting")
        self.btn_save_setting.setMinimumSize(QSize(200, 40))
        self.btn_save_setting.setMaximumSize(QSize(16777215, 16777215))
        font10 = QFont()
        font10.setPointSize(10)
        font10.setBold(True)
        font10.setItalic(True)
        self.btn_save_setting.setFont(font10)
        self.btn_save_setting.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(92,163,230);\n"
"color: #000;\n"
"border: 1px solid #000000;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #fff;\n"
"color: rgb(92,163,230);\n"
"border: 1px solid #000000;\n"
"border-radius: 15px;\n"
"}")

        self.verticalLayout_12.addWidget(self.btn_save_setting, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame)


        self.verticalLayout_8.addWidget(self.widget_2)


        self.verticalLayout_7.addWidget(self.widget)


        self.horizontalLayout_9.addWidget(self.container)

        self.stackedWidget.addWidget(self.page_settings)
        self.page_save_inventory = QWidget()
        self.page_save_inventory.setObjectName(u"page_save_inventory")
        self.horizontalLayout = QHBoxLayout(self.page_save_inventory)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.container_2 = QWidget(self.page_save_inventory)
        self.container_2.setObjectName(u"container_2")
        self.verticalLayout_14 = QVBoxLayout(self.container_2)
        self.verticalLayout_14.setSpacing(15)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(100, 20, 100, 20)
        self.title = QWidget(self.container_2)
        self.title.setObjectName(u"title")
        self.horizontalLayout_11 = QHBoxLayout(self.title)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.title_text = QLabel(self.title)
        self.title_text.setObjectName(u"title_text")
        font11 = QFont()
        font11.setPointSize(36)
        font11.setBold(True)
        font11.setItalic(True)
        self.title_text.setFont(font11)
        self.title_text.setScaledContents(True)
        self.title_text.setWordWrap(True)

        self.horizontalLayout_11.addWidget(self.title_text, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout_14.addWidget(self.title)

        self.indicator_container = QWidget(self.container_2)
        self.indicator_container.setObjectName(u"indicator_container")
        self.indicator_container.setStyleSheet(u"QWidget {\n"
"    background-color: #f0f0f0; /* Background color */\n"
"    border: 1px solid #ccc; /* Border color and width */\n"
"    border-radius: 10px; /* Border radius for rounded corners */\n"
"    padding: 10px; /* Padding inside the widget */\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.indicator_container)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.select_msg = QLabel(self.indicator_container)
        self.select_msg.setObjectName(u"select_msg")
        self.select_msg.setStyleSheet(u"QLabel{\n"
"border: none;\n"
"color: rgb(92,163,230);\n"
"font-size: 14px;\n"
"font-weight: bold\n"
"}")

        self.verticalLayout_15.addWidget(self.select_msg)

        self.widget_4 = QWidget(self.indicator_container)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"border: none;\n"
"")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.path_edit_indicator = QLabel(self.widget_4)
        self.path_edit_indicator.setObjectName(u"path_edit_indicator")
        self.path_edit_indicator.setMinimumSize(QSize(0, 0))
        self.path_edit_indicator.setFont(font8)
        self.path_edit_indicator.setStyleSheet(u"QLabel {\n"
"    border: 1px solid #000000; /* Border color and width */\n"
"    padding: 5px; /* Padding inside the label */\n"
"	border-radius: 5px;\n"
"	color: #000;\n"
"	font-size: 14px\n"
"}")

        self.horizontalLayout_12.addWidget(self.path_edit_indicator, 0, Qt.AlignVCenter)

        self.btn_path_indicator = QPushButton(self.widget_4)
        self.btn_path_indicator.setObjectName(u"btn_path_indicator")
        self.btn_path_indicator.setMinimumSize(QSize(150, 30))
        self.btn_path_indicator.setMaximumSize(QSize(150, 30))
        font12 = QFont()
        font12.setBold(True)
        font12.setItalic(True)
        self.btn_path_indicator.setFont(font12)
        self.btn_path_indicator.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(92,163,230);\n"
"color: #000;\n"
"border: 1px solid #000000;\n"
"border-radius: 5px;\n"
"font-size: 13px;\n"
"font-weight: bold\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #fff;\n"
"color: rgb(92,163,230);\n"
"border: 1px solid #000000;\n"
"border-radius: 5px;\n"
"}")
        icon = QIcon(QIcon.fromTheme(u"drive-harddisk"))
        self.btn_path_indicator.setIcon(icon)

        self.horizontalLayout_12.addWidget(self.btn_path_indicator, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_15.addWidget(self.widget_4)


        self.verticalLayout_14.addWidget(self.indicator_container)

        self.sales_container = QWidget(self.container_2)
        self.sales_container.setObjectName(u"sales_container")
        self.sales_container.setStyleSheet(u"QWidget {\n"
"    background-color: #f0f0f0; /* Background color */\n"
"    border: 1px solid #ccc; /* Border color and width */\n"
"    border-radius: 10px; /* Border radius for rounded corners */\n"
"    padding: 10px; /* Padding inside the widget */\n"
"}")
        self.verticalLayout_16 = QVBoxLayout(self.sales_container)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.select_msg_2 = QLabel(self.sales_container)
        self.select_msg_2.setObjectName(u"select_msg_2")
        self.select_msg_2.setStyleSheet(u"QLabel{\n"
"border: none;\n"
"color: rgb(92,163,230);\n"
"font-size: 14px;\n"
"font-weight: bold\n"
"}")

        self.verticalLayout_16.addWidget(self.select_msg_2)

        self.widget_5 = QWidget(self.sales_container)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"border: none;\n"
"")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.path_edit_indicator_2 = QLabel(self.widget_5)
        self.path_edit_indicator_2.setObjectName(u"path_edit_indicator_2")
        self.path_edit_indicator_2.setMinimumSize(QSize(0, 0))
        self.path_edit_indicator_2.setFont(font8)
        self.path_edit_indicator_2.setStyleSheet(u"QLabel {\n"
"        border: 1px solid #000000; /* Border color and width */\n"
"    padding: 5px; /* Padding inside the label */\n"
"	border-radius: 5px;\n"
"	color: #000;\n"
"	font-size: 14px\n"
"}")

        self.horizontalLayout_13.addWidget(self.path_edit_indicator_2, 0, Qt.AlignVCenter)

        self.btn_path_indicator_2 = QPushButton(self.widget_5)
        self.btn_path_indicator_2.setObjectName(u"btn_path_indicator_2")
        self.btn_path_indicator_2.setMinimumSize(QSize(150, 30))
        self.btn_path_indicator_2.setMaximumSize(QSize(200, 30))
        self.btn_path_indicator_2.setFont(font12)
        self.btn_path_indicator_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(92,163,230);\n"
"color: #000;\n"
"border: 1px solid #000000;\n"
"border-radius: 5px;\n"
"font-size: 13px;\n"
"font-weight: bold\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #fff;\n"
"color: rgb(92,163,230);\n"
"border: 1px solid #000000;\n"
"border-radius: 5px;\n"
"}")
        self.btn_path_indicator_2.setIcon(icon)

        self.horizontalLayout_13.addWidget(self.btn_path_indicator_2, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_16.addWidget(self.widget_5)


        self.verticalLayout_14.addWidget(self.sales_container)

        self.btn_upload = QPushButton(self.container_2)
        self.btn_upload.setObjectName(u"btn_upload")
        self.btn_upload.setMinimumSize(QSize(150, 30))
        self.btn_upload.setMaximumSize(QSize(200, 30))
        self.btn_upload.setFont(font12)
        self.btn_upload.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(92,163,230);\n"
"color: #000;\n"
"border: 1px solid #000000;\n"
"border-radius: 5px;\n"
"font-size: 14px;\n"
"font-weight: bold\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #fff;\n"
"color: rgb(92,163,230);\n"
"border: 1px solid #000000;\n"
"border-radius: 15px;\n"
"}")

        self.verticalLayout_14.addWidget(self.btn_upload, 0, Qt.AlignRight|Qt.AlignTop)

        self.progressBar_training = QProgressBar(self.container_2)
        self.progressBar_training.setObjectName(u"progressBar_training")
        self.progressBar_training.setMinimumSize(QSize(0, 10))
        self.progressBar_training.setMaximumSize(QSize(16777215, 10))
        self.progressBar_training.setStyleSheet(u"QProgressBar{\n"
"background: rgba(255,255,255,180);\n"
"border-style: none;\n"
"border-radius: 5px;\n"
"color: rgba(200, 200, 200, 0);\n"
"text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"border-radius: 5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 85, 255, 255), stop:1 rgba(0, 85, 127, 255))\n"
"}")
        self.progressBar_training.setValue(24)

        self.verticalLayout_14.addWidget(self.progressBar_training)

        self.save_btn_container = QWidget(self.container_2)
        self.save_btn_container.setObjectName(u"save_btn_container")
        self.verticalLayout_17 = QVBoxLayout(self.save_btn_container)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, 0, -1, 9)
        self.notification_text = QLabel(self.save_btn_container)
        self.notification_text.setObjectName(u"notification_text")
        self.notification_text.setMinimumSize(QSize(250, 200))
        self.notification_text.setMaximumSize(QSize(250, 200))
        self.notification_text.setFont(font10)
        self.notification_text.setStyleSheet(u"QLabel{\n"
"background-color: rgb(92,163,230);\n"
"color: #fff;\n"
"border: 1px solid rgb(92,163,230);\n"
"border-radius: 15px;\n"
"padding: 0 15px \n"
"}")
        self.notification_text.setAlignment(Qt.AlignCenter)
        self.notification_text.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.notification_text)


        self.verticalLayout_14.addWidget(self.save_btn_container)


        self.horizontalLayout.addWidget(self.container_2)

        self.stackedWidget.addWidget(self.page_save_inventory)
        self.page_sale_analytics = QWidget()
        self.page_sale_analytics.setObjectName(u"page_sale_analytics")
        self.horizontalLayout_15 = QHBoxLayout(self.page_sale_analytics)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_4 = QFrame(self.page_sale_analytics)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_4)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.stackedWidget_2 = QStackedWidget(self.frame_4)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_actual_sale = QWidget()
        self.page_actual_sale.setObjectName(u"page_actual_sale")
        self.stackedWidget_2.addWidget(self.page_actual_sale)
        self.page_predict_sale = QWidget()
        self.page_predict_sale.setObjectName(u"page_predict_sale")
        self.stackedWidget_2.addWidget(self.page_predict_sale)
        self.page_display_error_score = QWidget()
        self.page_display_error_score.setObjectName(u"page_display_error_score")
        self.horizontalLayout_18 = QHBoxLayout(self.page_display_error_score)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.widget_8 = QWidget(self.page_display_error_score)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_13 = QVBoxLayout(self.widget_8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.mse_3 = QLabel(self.widget_8)
        self.mse_3.setObjectName(u"mse_3")
        self.mse_3.setMinimumSize(QSize(350, 20))
        font13 = QFont()
        font13.setPointSize(14)
        font13.setBold(True)
        font13.setItalic(True)
        self.mse_3.setFont(font13)
        self.mse_3.setTextFormat(Qt.AutoText)

        self.verticalLayout_13.addWidget(self.mse_3)

        self.label_mse = QLabel(self.widget_8)
        self.label_mse.setObjectName(u"label_mse")
        self.label_mse.setMinimumSize(QSize(0, 20))
        self.label_mse.setMaximumSize(QSize(16777215, 40))
        self.label_mse.setFont(font7)
        self.label_mse.setStyleSheet(u"QLabel {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    selection-background-color: lightblue;\n"
"	color: #000000\n"
"}")
        self.label_mse.setTextFormat(Qt.AutoText)

        self.verticalLayout_13.addWidget(self.label_mse)

        self.mae = QLabel(self.widget_8)
        self.mae.setObjectName(u"mae")
        self.mae.setMinimumSize(QSize(350, 20))
        self.mae.setFont(font13)
        self.mae.setTextFormat(Qt.AutoText)

        self.verticalLayout_13.addWidget(self.mae)

        self.label_mae = QLabel(self.widget_8)
        self.label_mae.setObjectName(u"label_mae")
        self.label_mae.setMinimumSize(QSize(0, 20))
        self.label_mae.setMaximumSize(QSize(16777215, 40))
        self.label_mae.setFont(font7)
        self.label_mae.setStyleSheet(u"QLabel {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    selection-background-color: lightblue;\n"
"	color: #000000\n"
"}")
        self.label_mae.setTextFormat(Qt.AutoText)

        self.verticalLayout_13.addWidget(self.label_mae)

        self.r2 = QLabel(self.widget_8)
        self.r2.setObjectName(u"r2")
        self.r2.setMinimumSize(QSize(350, 20))
        self.r2.setFont(font13)
        self.r2.setTextFormat(Qt.AutoText)

        self.verticalLayout_13.addWidget(self.r2)

        self.label_r2 = QLabel(self.widget_8)
        self.label_r2.setObjectName(u"label_r2")
        self.label_r2.setMinimumSize(QSize(0, 20))
        self.label_r2.setMaximumSize(QSize(16777215, 40))
        self.label_r2.setFont(font7)
        self.label_r2.setStyleSheet(u"QLabel {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    selection-background-color: lightblue;\n"
"	color: #000000\n"
"}")
        self.label_r2.setTextFormat(Qt.AutoText)

        self.verticalLayout_13.addWidget(self.label_r2)

        self.label_17 = QLabel(self.widget_8)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font13)

        self.verticalLayout_13.addWidget(self.label_17)

        self.label_accuracy = QLabel(self.widget_8)
        self.label_accuracy.setObjectName(u"label_accuracy")
        self.label_accuracy.setStyleSheet(u"QLabel {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    selection-background-color: lightblue;\n"
"	color: #000000\n"
"}")

        self.verticalLayout_13.addWidget(self.label_accuracy)

        self.label_19 = QLabel(self.widget_8)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font13)

        self.verticalLayout_13.addWidget(self.label_19)

        self.label_precision = QLabel(self.widget_8)
        self.label_precision.setObjectName(u"label_precision")
        self.label_precision.setStyleSheet(u"QLabel {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    selection-background-color: lightblue;\n"
"	color: #000000\n"
"}")

        self.verticalLayout_13.addWidget(self.label_precision)

        self.label_21 = QLabel(self.widget_8)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font13)

        self.verticalLayout_13.addWidget(self.label_21)

        self.label_recall = QLabel(self.widget_8)
        self.label_recall.setObjectName(u"label_recall")
        self.label_recall.setStyleSheet(u"QLabel {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    selection-background-color: lightblue;\n"
"	color: #000000\n"
"}")

        self.verticalLayout_13.addWidget(self.label_recall)

        self.label_23 = QLabel(self.widget_8)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font13)

        self.verticalLayout_13.addWidget(self.label_23)

        self.label_conf_matrix = QLabel(self.widget_8)
        self.label_conf_matrix.setObjectName(u"label_conf_matrix")
        self.label_conf_matrix.setStyleSheet(u"QLabel {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    selection-background-color: lightblue;\n"
"	color: #000000\n"
"}")

        self.verticalLayout_13.addWidget(self.label_conf_matrix)


        self.horizontalLayout_18.addWidget(self.widget_8, 0, Qt.AlignHCenter)

        self.stackedWidget_2.addWidget(self.page_display_error_score)
        self.page_predict_sales_list = QWidget()
        self.page_predict_sales_list.setObjectName(u"page_predict_sales_list")
        self.horizontalLayout_20 = QHBoxLayout(self.page_predict_sales_list)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.table_predicted_sales = QTableWidget(self.page_predict_sales_list)
        self.table_predicted_sales.setObjectName(u"table_predicted_sales")
        self.table_predicted_sales.setMinimumSize(QSize(0, 0))
        self.table_predicted_sales.setMaximumSize(QSize(300, 16777215))
        self.table_predicted_sales.setBaseSize(QSize(0, 0))
        font14 = QFont()
        font14.setPointSize(18)
        font14.setBold(True)
        font14.setItalic(True)
        self.table_predicted_sales.setFont(font14)
        self.table_predicted_sales.setColumnCount(0)

        self.horizontalLayout_20.addWidget(self.table_predicted_sales, 0, Qt.AlignVCenter)

        self.stackedWidget_2.addWidget(self.page_predict_sales_list)

        self.verticalLayout_21.addWidget(self.stackedWidget_2)

        self.switch_btn_container = QFrame(self.frame_4)
        self.switch_btn_container.setObjectName(u"switch_btn_container")
        self.switch_btn_container.setFrameShape(QFrame.StyledPanel)
        self.switch_btn_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.switch_btn_container)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.btn_actual_sale = QPushButton(self.switch_btn_container)
        self.btn_actual_sale.setObjectName(u"btn_actual_sale")
        self.btn_actual_sale.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(92,163,230);\n"
"color: #fff;\n"
"border: 1px solid #000000;\n"
"border-radius: 15px;\n"
"font-weight: bold\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #fff;\n"
"color: rgb(92,163,230);\n"
"border: 1px solid #000000;\n"
"border-radius: 15px;\n"
"}")

        self.horizontalLayout_17.addWidget(self.btn_actual_sale)

        self.btn_display_score = QPushButton(self.switch_btn_container)
        self.btn_display_score.setObjectName(u"btn_display_score")
        self.btn_display_score.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(92,163,230);\n"
"color: #fff;\n"
"border: 1px solid #000000;\n"
"border-radius: 15px;\n"
"font-weight: bold\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #fff;\n"
"color: rgb(92,163,230);\n"
"border: 1px solid #000000;\n"
"border-radius: 15px;\n"
"}")

        self.horizontalLayout_17.addWidget(self.btn_display_score)

        self.btn_prediction_sale = QPushButton(self.switch_btn_container)
        self.btn_prediction_sale.setObjectName(u"btn_prediction_sale")
        self.btn_prediction_sale.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(92,163,230);\n"
"color: #fff;\n"
"border: 1px solid #000000;\n"
"border-radius: 15px;\n"
"font-weight: bold\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #fff;\n"
"color: rgb(92,163,230);\n"
"border: 1px solid #000000;\n"
"border-radius: 15px;\n"
"}")

        self.horizontalLayout_17.addWidget(self.btn_prediction_sale)

        self.btn_prediction_sale_list = QPushButton(self.switch_btn_container)
        self.btn_prediction_sale_list.setObjectName(u"btn_prediction_sale_list")
        self.btn_prediction_sale_list.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(92,163,230);\n"
"color: #fff;\n"
"border: 1px solid #000000;\n"
"border-radius: 15px;\n"
"font-weight: bold\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #fff;\n"
"color: rgb(92,163,230);\n"
"border: 1px solid #000000;\n"
"border-radius: 15px;\n"
"}")

        self.horizontalLayout_17.addWidget(self.btn_prediction_sale_list)


        self.verticalLayout_21.addWidget(self.switch_btn_container)


        self.horizontalLayout_15.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_sale_analytics)
        self.page_create_account = QWidget()
        self.page_create_account.setObjectName(u"page_create_account")
        self.horizontalLayout_14 = QHBoxLayout(self.page_create_account)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.widget_3 = QWidget(self.page_create_account)
        self.widget_3.setObjectName(u"widget_3")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 0, 1091, 881))
        self.label_4.setStyleSheet(u"background-image:url(:/newPrefix/C:/Users/akxsh/Desktop/2c933fdd5a3b0a5f8a51a0f44eb0f619.jpg)")
        self.label_4.setPixmap(QPixmap(u":/newPrefix/C:/Users/akxsh/Desktop/2c933fdd5a3b0a5f8a51a0f44eb0f619.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(True)
        self.username = QLineEdit(self.widget_3)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(466, 345, 261, 31))
        self.username.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.password = QLineEdit(self.widget_3)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(466, 405, 261, 31))
        self.password.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.password.setEchoMode(QLineEdit.Password)
        self.Signup = QPushButton(self.widget_3)
        self.Signup.setObjectName(u"Signup")
        self.Signup.setGeometry(QRect(760, 550, 121, 51))
        self.Signup.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(92,163,230);\n"
"color: #000;\n"
"border: 1px solid #000000;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #fff;\n"
"color: rgb(92,163,230);\n"
"border: 1px solid #000000;\n"
"border-radius: 15px;\n"
"}")
        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(216, 405, 121, 31))
        self.label_8.setFont(font9)
        self.label_8.setStyleSheet(u"")
        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(216, 465, 221, 31))
        self.label_9.setFont(font9)
        self.label_9.setStyleSheet(u"")
        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 60, 241, 71))
        font15 = QFont()
        font15.setFamilies([u"Segoe UI"])
        font15.setPointSize(36)
        font15.setBold(True)
        font15.setItalic(True)
        self.label_5.setFont(font15)
        self.label_5.setStyleSheet(u"")
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(216, 345, 121, 31))
        self.label_10.setFont(font9)
        self.label_10.setStyleSheet(u"")
        self.phnum = QLineEdit(self.widget_3)
        self.phnum.setObjectName(u"phnum")
        self.phnum.setGeometry(QRect(466, 285, 261, 31))
        self.phnum.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.phnum.setEchoMode(QLineEdit.Normal)
        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(216, 285, 121, 31))
        self.label_11.setFont(font9)
        self.label_11.setStyleSheet(u"")
        self.confirmPassword = QLineEdit(self.widget_3)
        self.confirmPassword.setObjectName(u"confirmPassword")
        self.confirmPassword.setGeometry(QRect(466, 465, 261, 31))
        self.confirmPassword.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.confirmPassword.setEchoMode(QLineEdit.Password)
        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(216, 225, 121, 31))
        self.label_12.setFont(font9)
        self.label_12.setStyleSheet(u"")
        self.name = QLineEdit(self.widget_3)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(466, 225, 261, 31))
        self.name.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.error = QLabel(self.widget_3)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(360, 530, 371, 21))
        self.error.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"color:rgb(255, 0, 0)")
        self.error.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.widget_3)

        self.stackedWidget.addWidget(self.page_create_account)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.verticalLayout_6.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Sales Forecast With Economic and Weather Indicators", None))
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"C:\\Program Files\\Blender Foundation\\Blender 2.82", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.btn_save_inventory.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_sales_analytics.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_create_account.setText(QCoreApplication.translate("MainWindow", u"New User", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"AD", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Welcome to Our Sales Predictions Dashboard", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Discover the power of data with our Sales\" Predictions Dashboard. Gain valuable insights into your sales performance by exploring the correlation between weather conditions, economic indicators, and your business trends.", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"How To Operate ", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Set Test Dates</span>: Click the button below or the setting gear icon to define your test dates or prediction date range.</li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Save Settings</span>: After configuring the test dates, click the save button to proceed to the data upload page.</li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Start Analysis</span>: Click &quot;analyze&quot; to initiate the training process. Once training completes, you'll be directed to a graphical representation of the prediction data"
                        ".</li></ol></body></html>", None))
        self.go_to_setting.setText(QCoreApplication.translate("MainWindow", u"Start Here", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Sales Prediction Range", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Start Prediction Year", None))
        self.start_year_input.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"End Prediction Year", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Email Notifications", None))
        self.email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.report_text.setText("")
        self.btn_save_setting.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.title_text.setText(QCoreApplication.translate("MainWindow", u"INVENTORY", None))
        self.select_msg.setText(QCoreApplication.translate("MainWindow", u"Please Upload Your Indicators CSV File", None))
        self.path_edit_indicator.setText(QCoreApplication.translate("MainWindow", u"Select File:", None))
        self.btn_path_indicator.setText(QCoreApplication.translate("MainWindow", u"Browse Files", None))
        self.select_msg_2.setText(QCoreApplication.translate("MainWindow", u"Please Upload Your Sales History CSV File", None))
        self.path_edit_indicator_2.setText(QCoreApplication.translate("MainWindow", u"Select File:", None))
        self.btn_path_indicator_2.setText(QCoreApplication.translate("MainWindow", u"Browse Files", None))
        self.btn_upload.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
        self.notification_text.setText(QCoreApplication.translate("MainWindow", u"This page allows the user to upload a single CSV file containing sales records as well as economic and weather indicators. It uses the data to train the model up to the specified prediction date and then tests the model's performance using data from the prediction date onwards.", None))
        self.mse_3.setText(QCoreApplication.translate("MainWindow", u"Mean Squared Error", None))
        self.label_mse.setText("")
        self.mae.setText(QCoreApplication.translate("MainWindow", u"Mean Absolute Error", None))
        self.label_mae.setText("")
        self.r2.setText(QCoreApplication.translate("MainWindow", u"R-Squared Score", None))
        self.label_r2.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Accuracy Score", None))
        self.label_accuracy.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Precision Score", None))
        self.label_precision.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Recall Score", None))
        self.label_recall.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Confusion Matrix", None))
        self.label_conf_matrix.setText("")
        self.btn_actual_sale.setText(QCoreApplication.translate("MainWindow", u"Actual Sales Graph", None))
        self.btn_display_score.setText(QCoreApplication.translate("MainWindow", u"View Metrics", None))
        self.btn_prediction_sale.setText(QCoreApplication.translate("MainWindow", u"Predict Sales Graph", None))
        self.btn_prediction_sale_list.setText(QCoreApplication.translate("MainWindow", u"Predicted Sales", None))
        self.label_4.setText("")
        self.Signup.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PROFILE", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Username: ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Ph No:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.error.setText("")
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Registered by: AbdulAzzez", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

