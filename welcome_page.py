<<<<<<< HEAD
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome_page.ui'
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
                               QMainWindow, QProgressBar, QSizePolicy, QVBoxLayout,
                               QWidget)


class Ui_Welcome_Page(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(612, 467)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
                                         "color: #fff;\n"
                                         "}\n"
                                         "QWidget{\n"
                                         "background-color:rgb(92, 163, 230);\n"
                                         "border-radius: 12px;\n"
                                         "}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.app_logo = QFrame(self.centralwidget)
        self.app_logo.setObjectName(u"app_logo")
        self.app_logo.setMinimumSize(QSize(0, 200))
        self.app_logo.setFrameShape(QFrame.StyledPanel)
        self.app_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.app_logo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo_image = QLabel(self.app_logo)
        self.logo_image.setObjectName(u"logo_image")
        self.logo_image.setMinimumSize(QSize(100, 100))
        self.logo_image.setMaximumSize(QSize(100, 100))
        self.logo_image.setStyleSheet(u"QLabel{\n"
                                      "	background: #fff;\n"
                                      "	border-radius: 50%;\n"
                                      "}")
        self.logo_image.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.logo_image)

        self.verticalLayout.addWidget(self.app_logo)

        self.background = QFrame(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.background)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.app_name = QLabel(self.background)
        self.app_name.setObjectName(u"app_name")
        font = QFont()
        font.setFamilies([u"Futura XBlk BT"])
        font.setPointSize(32)
        self.app_name.setFont(font)
        self.app_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.app_name)

        self.app_descrition = QLabel(self.background)
        self.app_descrition.setObjectName(u"app_descrition")
        font1 = QFont()
        font1.setFamilies([u"Poppins ExtraBold"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.app_descrition.setFont(font1)
        self.app_descrition.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.app_descrition)

        self.progres = QFrame(self.background)
        self.progres.setObjectName(u"progres")
        self.progres.setFrameShape(QFrame.StyledPanel)
        self.progres.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.progres)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, -1, 30, -1)
        self.precentage = QLabel(self.progres)
        self.precentage.setObjectName(u"precentage")
        font2 = QFont()
        font2.setFamilies([u"Poppins SemiBold"])
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        self.precentage.setFont(font2)
        self.precentage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.precentage)

        self.progressBar = QProgressBar(self.progres)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 10))
        self.progressBar.setMaximumSize(QSize(16777215, 10))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
                                       "background: rgba(255, 255, 255, 180);\n"
                                       "border-style: none;\n"
                                       "border-radius: 5px;\n"
                                       "color: rgba(200, 200, 200, 0);\n"
                                       "text-align: center;\n"
                                       "}\n"
                                       "QProgressBar::chunk{\n"
                                       "border-radius: 5px;\n"
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 85, 255, 255), stop:1 rgba(0, 85, 127, 255))\n"
                                       "}")
        self.progressBar.setValue(24)

        self.verticalLayout_3.addWidget(self.progressBar)

        self.verticalLayout_2.addWidget(self.progres)

        self.footer = QFrame(self.background)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.status = QLabel(self.footer)
        self.status.setObjectName(u"status")
        font3 = QFont()
        font3.setFamilies([u"Poppins SemiBold"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.status.setFont(font3)
        self.status.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.status)

        self.author = QLabel(self.footer)
        self.author.setObjectName(u"author")
        self.author.setFont(font3)
        self.author.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.author)

        self.verticalLayout_2.addWidget(self.footer)

        self.verticalLayout.addWidget(self.background)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_image.setText(QCoreApplication.translate("MainWindow", u"logo", None))
        self.app_name.setText(QCoreApplication.translate("MainWindow", u"SalesSense ", None))
        self.app_descrition.setText(QCoreApplication.translate("MainWindow", u"Smart Sales Projections With Economic "
                                                                             u"and Weather Stats", None))
        self.precentage.setText(QCoreApplication.translate("MainWindow", u"24%", None))
        self.status.setText(QCoreApplication.translate("MainWindow", u"status:", None))
        self.author.setText(QCoreApplication.translate("MainWindow", u"Author:AbdulAzzez", None))
    # retranslateUi
=======
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome_page.ui'
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
                               QMainWindow, QProgressBar, QSizePolicy, QVBoxLayout,
                               QWidget)


class Ui_Welcome_Page(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(612, 467)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
                                         "color: #fff;\n"
                                         "}\n"
                                         "QWidget{\n"
                                         "background-color:rgb(92, 163, 230);\n"
                                         "border-radius: 12px;\n"
                                         "}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.app_logo = QFrame(self.centralwidget)
        self.app_logo.setObjectName(u"app_logo")
        self.app_logo.setMinimumSize(QSize(0, 200))
        self.app_logo.setFrameShape(QFrame.StyledPanel)
        self.app_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.app_logo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo_image = QLabel(self.app_logo)
        self.logo_image.setObjectName(u"logo_image")
        self.logo_image.setMinimumSize(QSize(100, 100))
        self.logo_image.setMaximumSize(QSize(100, 100))
        self.logo_image.setStyleSheet(u"QLabel{\n"
                                      "	background: #fff;\n"
                                      "	border-radius: 50%;\n"
                                      "}")
        self.logo_image.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.logo_image)

        self.verticalLayout.addWidget(self.app_logo)

        self.background = QFrame(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.background)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.app_name = QLabel(self.background)
        self.app_name.setObjectName(u"app_name")
        font = QFont()
        font.setFamilies([u"Futura XBlk BT"])
        font.setPointSize(32)
        self.app_name.setFont(font)
        self.app_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.app_name)

        self.app_descrition = QLabel(self.background)
        self.app_descrition.setObjectName(u"app_descrition")
        font1 = QFont()
        font1.setFamilies([u"Poppins ExtraBold"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.app_descrition.setFont(font1)
        self.app_descrition.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.app_descrition)

        self.progres = QFrame(self.background)
        self.progres.setObjectName(u"progres")
        self.progres.setFrameShape(QFrame.StyledPanel)
        self.progres.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.progres)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, -1, 30, -1)
        self.precentage = QLabel(self.progres)
        self.precentage.setObjectName(u"precentage")
        font2 = QFont()
        font2.setFamilies([u"Poppins SemiBold"])
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        self.precentage.setFont(font2)
        self.precentage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.precentage)

        self.progressBar = QProgressBar(self.progres)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 10))
        self.progressBar.setMaximumSize(QSize(16777215, 10))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
                                       "background: rgba(255, 255, 255, 180);\n"
                                       "border-style: none;\n"
                                       "border-radius: 5px;\n"
                                       "color: rgba(200, 200, 200, 0);\n"
                                       "text-align: center;\n"
                                       "}\n"
                                       "QProgressBar::chunk{\n"
                                       "border-radius: 5px;\n"
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 85, 255, 255), stop:1 rgba(0, 85, 127, 255))\n"
                                       "}")
        self.progressBar.setValue(24)

        self.verticalLayout_3.addWidget(self.progressBar)

        self.verticalLayout_2.addWidget(self.progres)

        self.footer = QFrame(self.background)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.status = QLabel(self.footer)
        self.status.setObjectName(u"status")
        font3 = QFont()
        font3.setFamilies([u"Poppins SemiBold"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.status.setFont(font3)
        self.status.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.status)

        self.author = QLabel(self.footer)
        self.author.setObjectName(u"author")
        self.author.setFont(font3)
        self.author.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.author)

        self.verticalLayout_2.addWidget(self.footer)

        self.verticalLayout.addWidget(self.background)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_image.setText(QCoreApplication.translate("MainWindow", u"logo", None))
        self.app_name.setText(QCoreApplication.translate("MainWindow", u"SalesSense ", None))
        self.app_descrition.setText(QCoreApplication.translate("MainWindow", u"Smart Sales Projections With Economic "
                                                                             u"and Weather Stats", None))
        self.precentage.setText(QCoreApplication.translate("MainWindow", u"24%", None))
        self.status.setText(QCoreApplication.translate("MainWindow", u"status:", None))
        self.author.setText(QCoreApplication.translate("MainWindow", u"Author:AbdulAzzez", None))
    # retranslateUi
>>>>>>> 79b9658ccc23aa8723f2d829bae8c11527986fee
