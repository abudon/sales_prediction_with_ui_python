<<<<<<< HEAD
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_page.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QLineEdit, QMainWindow, QPushButton, QSizePolicy,
                               QVBoxLayout, QWidget)



class Ui_Log_In(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(611, 501)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"\n"
                                         "QWidget{\n"
                                         "background-color:rgb(92, 163, 230);\n"
                                         "\n"
                                         "}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.BgImage = QWidget(self.widget)
        self.BgImage.setObjectName(u"BgImage")
        self.BgImage.setStyleSheet(u"background-image:url(:/img/Images/sales-forecast.jpg);\n"
                                   "background-repeat: no-repeat;\n"
                                   "background-size: cover;\n"
                                   "background-position: center center;\n"
                                   "border-top-left-radius: 60px;\n"
                                   "")
        self.hboxLayout = QHBoxLayout(self.BgImage)
        self.hboxLayout.setSpacing(0)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.BgImage)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(151, 181))
        self.label.setStyleSheet(u"background-image:url(:/img/Images/sales-forecast.jpg);")
        self.label.setAlignment(Qt.AlignCenter)

        self.hboxLayout.addWidget(self.label)

        self.horizontalLayout.addWidget(self.BgImage)

        self.loginBg = QWidget(self.widget)
        self.loginBg.setObjectName(u"loginBg")
        self.loginBg.setMinimumSize(QSize(200, 0))
        self.loginBg.setMaximumSize(QSize(16777215, 16777215))
        self.loginBg.setStyleSheet(u"background-color:rgba(255, 255, 255, 255);\n"
                                   "border-bottom-right-radius: 60px;")
        self.verticalLayout_2 = QVBoxLayout(self.loginBg)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.loginContainer = QFrame(self.loginBg)
        self.loginContainer.setObjectName(u"loginContainer")
        self.loginContainer.setFrameShape(QFrame.StyledPanel)
        self.loginContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.loginContainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.loginTxt = QLabel(self.loginContainer)
        self.loginTxt.setObjectName(u"loginTxt")
        font = QFont()
        font.setFamilies([u"Futura XBlkCnIt BT"])
        font.setPointSize(24)
        self.loginTxt.setFont(font)
        self.loginTxt.setStyleSheet(u"color: rgb(92, 163, 230);\n"
                                    "margin-top: 20px;")
        self.loginTxt.setAlignment(Qt.AlignCenter)
        self.loginTxt.setMargin(0)

        self.horizontalLayout_2.addWidget(self.loginTxt)

        self.verticalLayout_2.addWidget(self.loginContainer)

        self.inputContainer = QFrame(self.loginBg)
        self.inputContainer.setObjectName(u"inputContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputContainer.sizePolicy().hasHeightForWidth())
        self.inputContainer.setSizePolicy(sizePolicy)
        self.inputContainer.setMinimumSize(QSize(250, 0))
        self.inputContainer.setFrameShape(QFrame.StyledPanel)
        self.inputContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.inputContainer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.username = QLineEdit(self.inputContainer)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(0, 40))
        self.username.setMaximumSize(QSize(300, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Poppins SemiBold"])
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(True)
        self.username.setFont(font1)
        self.username.setStyleSheet(u"background-color: #f5f5f5;\n"
                                    "border:none;\n"
                                    "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                    "color:rgba(0, 0, 0, 240);\n"
                                    "padding-bottom:7px;")
        self.username.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.username)

        self.password = QLineEdit(self.inputContainer)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(0, 40))
        self.password.setMaximumSize(QSize(300, 16777215))
        self.password.setFont(font1)
        self.password.setStyleSheet(u"background-color: #f5f5f5;\n"
                                    "border:none;\n"
                                    "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                    "color:rgba(0, 0, 0, 240);\n"
                                    "padding-bottom:7px;")
        self.password.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.password)

        self.verticalLayout_2.addWidget(self.inputContainer, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.loginBg)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(250, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.loginBtn = QPushButton(self.frame_3)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setMinimumSize(QSize(0, 30))
        self.loginBtn.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamilies([u"Futura XBlkCnIt BT"])
        self.loginBtn.setFont(font2)
        self.loginBtn.setMouseTracking(True)
        self.loginBtn.setStyleSheet(u"QPushButton{\n"
                                    "background-color: rgb(92, 163, 230);\n"
                                    " border: none;\n"
                                    "border-radius: 10px;\n"
                                    "text-align: center;\n"
                                    "font-size: 16px;\n"
                                    "display: inline-block;\n"
                                    "color: #fff;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "cursor: pointer;\n"
                                    "background-color: #f5f5f5;\n"
                                    "color: rgb(92, 163, 230)\n"
                                    "}")
        self.loginBtn.setAutoDefault(False)

        self.verticalLayout_4.addWidget(self.loginBtn)

        self.forgetLink = QLabel(self.frame_3)
        self.forgetLink.setObjectName(u"forgetLink")
        self.forgetLink.setMinimumSize(QSize(200, 0))
        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(True)
        self.forgetLink.setFont(font3)
        self.forgetLink.setCursor(QCursor(Qt.PointingHandCursor))
        self.forgetLink.setMouseTracking(True)
        self.forgetLink.setStyleSheet(u"color: rgb(77, 0, 0)")
        self.forgetLink.setAlignment(Qt.AlignCenter)
        self.forgetLink.setWordWrap(True)
        self.forgetLink.setMargin(0)

        self.verticalLayout_4.addWidget(self.forgetLink, 0, Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignHCenter)

        self.horizontalLayout.addWidget(self.loginBg)

        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.loginBtn.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.loginTxt.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"LogIn", None))
        self.forgetLink.setText(QCoreApplication.translate("MainWindow", u"Forgot your Username or Password", None))
    # retranslateUi
=======
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_page.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QLineEdit, QMainWindow, QPushButton, QSizePolicy,
                               QVBoxLayout, QWidget)



class Ui_Log_In(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(611, 501)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"\n"
                                         "QWidget{\n"
                                         "background-color:rgb(92, 163, 230);\n"
                                         "\n"
                                         "}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.BgImage = QWidget(self.widget)
        self.BgImage.setObjectName(u"BgImage")
        self.BgImage.setStyleSheet(u"background-image:url(:/img/Images/sales-forecast.jpg);\n"
                                   "background-repeat: no-repeat;\n"
                                   "background-size: cover;\n"
                                   "background-position: center center;\n"
                                   "border-top-left-radius: 60px;\n"
                                   "")
        self.hboxLayout = QHBoxLayout(self.BgImage)
        self.hboxLayout.setSpacing(0)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.BgImage)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(151, 181))
        self.label.setStyleSheet(u"background-image:url(:/img/Images/sales-forecast.jpg);")
        self.label.setAlignment(Qt.AlignCenter)

        self.hboxLayout.addWidget(self.label)

        self.horizontalLayout.addWidget(self.BgImage)

        self.loginBg = QWidget(self.widget)
        self.loginBg.setObjectName(u"loginBg")
        self.loginBg.setMinimumSize(QSize(200, 0))
        self.loginBg.setMaximumSize(QSize(16777215, 16777215))
        self.loginBg.setStyleSheet(u"background-color:rgba(255, 255, 255, 255);\n"
                                   "border-bottom-right-radius: 60px;")
        self.verticalLayout_2 = QVBoxLayout(self.loginBg)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.loginContainer = QFrame(self.loginBg)
        self.loginContainer.setObjectName(u"loginContainer")
        self.loginContainer.setFrameShape(QFrame.StyledPanel)
        self.loginContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.loginContainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.loginTxt = QLabel(self.loginContainer)
        self.loginTxt.setObjectName(u"loginTxt")
        font = QFont()
        font.setFamilies([u"Futura XBlkCnIt BT"])
        font.setPointSize(24)
        self.loginTxt.setFont(font)
        self.loginTxt.setStyleSheet(u"color: rgb(92, 163, 230);\n"
                                    "margin-top: 20px;")
        self.loginTxt.setAlignment(Qt.AlignCenter)
        self.loginTxt.setMargin(0)

        self.horizontalLayout_2.addWidget(self.loginTxt)

        self.verticalLayout_2.addWidget(self.loginContainer)

        self.inputContainer = QFrame(self.loginBg)
        self.inputContainer.setObjectName(u"inputContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputContainer.sizePolicy().hasHeightForWidth())
        self.inputContainer.setSizePolicy(sizePolicy)
        self.inputContainer.setMinimumSize(QSize(250, 0))
        self.inputContainer.setFrameShape(QFrame.StyledPanel)
        self.inputContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.inputContainer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.username = QLineEdit(self.inputContainer)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(0, 40))
        self.username.setMaximumSize(QSize(300, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Poppins SemiBold"])
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(True)
        self.username.setFont(font1)
        self.username.setStyleSheet(u"background-color: #f5f5f5;\n"
                                    "border:none;\n"
                                    "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                    "color:rgba(0, 0, 0, 240);\n"
                                    "padding-bottom:7px;")
        self.username.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.username)

        self.password = QLineEdit(self.inputContainer)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(0, 40))
        self.password.setMaximumSize(QSize(300, 16777215))
        self.password.setFont(font1)
        self.password.setStyleSheet(u"background-color: #f5f5f5;\n"
                                    "border:none;\n"
                                    "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                    "color:rgba(0, 0, 0, 240);\n"
                                    "padding-bottom:7px;")
        self.password.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.password)

        self.verticalLayout_2.addWidget(self.inputContainer, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.loginBg)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(250, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.loginBtn = QPushButton(self.frame_3)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setMinimumSize(QSize(0, 30))
        self.loginBtn.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamilies([u"Futura XBlkCnIt BT"])
        self.loginBtn.setFont(font2)
        self.loginBtn.setMouseTracking(True)
        self.loginBtn.setStyleSheet(u"QPushButton{\n"
                                    "background-color: rgb(92, 163, 230);\n"
                                    " border: none;\n"
                                    "border-radius: 10px;\n"
                                    "text-align: center;\n"
                                    "font-size: 16px;\n"
                                    "display: inline-block;\n"
                                    "color: #fff;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "cursor: pointer;\n"
                                    "background-color: #f5f5f5;\n"
                                    "color: rgb(92, 163, 230)\n"
                                    "}")
        self.loginBtn.setAutoDefault(False)

        self.verticalLayout_4.addWidget(self.loginBtn)

        self.forgetLink = QLabel(self.frame_3)
        self.forgetLink.setObjectName(u"forgetLink")
        self.forgetLink.setMinimumSize(QSize(200, 0))
        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(True)
        self.forgetLink.setFont(font3)
        self.forgetLink.setCursor(QCursor(Qt.PointingHandCursor))
        self.forgetLink.setMouseTracking(True)
        self.forgetLink.setStyleSheet(u"color: rgb(77, 0, 0)")
        self.forgetLink.setAlignment(Qt.AlignCenter)
        self.forgetLink.setWordWrap(True)
        self.forgetLink.setMargin(0)

        self.verticalLayout_4.addWidget(self.forgetLink, 0, Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignHCenter)

        self.horizontalLayout.addWidget(self.loginBg)

        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.loginBtn.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.loginTxt.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"LogIn", None))
        self.forgetLink.setText(QCoreApplication.translate("MainWindow", u"Forgot your Username or Password", None))
    # retranslateUi
>>>>>>> 79b9658ccc23aa8723f2d829bae8c11527986fee
