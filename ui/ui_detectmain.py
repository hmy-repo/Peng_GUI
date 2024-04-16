# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detectmain.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGridLayout,
    QGroupBox, QHBoxLayout, QLCDNumber, QLabel,
    QListView, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1261, 802)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.detectmainWidget = QWidget(Form)
        self.detectmainWidget.setObjectName(u"detectmainWidget")
        self.verticalLayout_13 = QVBoxLayout(self.detectmainWidget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cameraMainGroupBox = QGroupBox(self.detectmainWidget)
        self.cameraMainGroupBox.setObjectName(u"cameraMainGroupBox")
        self.horizontalLayout_9 = QHBoxLayout(self.cameraMainGroupBox)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.cameraMainlVLayout = QVBoxLayout()
        self.cameraMainlVLayout.setObjectName(u"cameraMainlVLayout")

        self.horizontalLayout_9.addLayout(self.cameraMainlVLayout)


        self.gridLayout_3.addWidget(self.cameraMainGroupBox, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.detectmainWidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tabWidget_2 = QTabWidget(self.groupBox_4)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.scrollArea = QScrollArea(self.tab_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Panel)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 692, 317))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_5.addWidget(self.scrollArea)

        self.tabWidget_2.addTab(self.tab_4, "")

        self.horizontalLayout_6.addWidget(self.tabWidget_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)

        self.verticalLayout_8.addWidget(self.label_2)

        self.listView = QListView(self.groupBox_4)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_8.addWidget(self.listView)


        self.horizontalLayout_6.addLayout(self.verticalLayout_8)

        self.horizontalLayout_6.setStretch(0, 5)
        self.horizontalLayout_6.setStretch(1, 1)

        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)


        self.gridLayout_3.addWidget(self.groupBox_4, 0, 1, 1, 1)

        self.groupBox_6 = QGroupBox(self.detectmainWidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget = QWidget(self.groupBox_6)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_12.addWidget(self.widget)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_3 = QPushButton(self.groupBox_6)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.groupBox_6)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox_6)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.groupBox_6)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 0, 3, 1, 1)

        self.pushButton_4 = QPushButton(self.groupBox_6)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.groupBox_6)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 1, 1, 1, 1)

        self.pushButton = QPushButton(self.groupBox_6)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.groupBox_6)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 1, 3, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout)

        self.verticalLayout_12.setStretch(0, 5)

        self.horizontalLayout_10.addLayout(self.verticalLayout_12)


        self.gridLayout_3.addWidget(self.groupBox_6, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.detectmainWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.tabWidget = QTabWidget(self.groupBox_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setFrameShape(QFrame.Panel)
        self.graphicsView.setLineWidth(1)

        self.horizontalLayout_3.addWidget(self.graphicsView)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_10.addWidget(self.tabWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_5.setFont(font1)
        self.label_5.setFrameShape(QFrame.NoFrame)
        self.label_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.progressBar = QProgressBar(self.groupBox_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(50)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.BottomToTop)

        self.horizontalLayout_2.addWidget(self.progressBar)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setFrameShape(QFrame.NoFrame)
        self.label_9.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.label_9)

        self.lcdNumber = QLCDNumber(self.groupBox_3)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setAcceptDrops(False)
        self.lcdNumber.setFrameShape(QFrame.Panel)

        self.horizontalLayout_2.addWidget(self.lcdNumber)


        self.verticalLayout_10.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_10)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_9.addWidget(self.label_4)

        self.Res01_Num08_Ser1jpg = QListView(self.groupBox_3)
        self.Res01_Num08_Ser1jpg.setObjectName(u"Res01_Num08_Ser1jpg")
        self.Res01_Num08_Ser1jpg.setFrameShape(QFrame.Panel)
        self.Res01_Num08_Ser1jpg.setSelectionRectVisible(False)

        self.verticalLayout_9.addWidget(self.Res01_Num08_Ser1jpg)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)

        self.horizontalLayout_4.setStretch(0, 5)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_11.addLayout(self.horizontalLayout_4)


        self.gridLayout_3.addWidget(self.groupBox_3, 1, 1, 1, 1)


        self.verticalLayout_13.addLayout(self.gridLayout_3)

        self.label_3 = QLabel(self.detectmainWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_13.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.detectmainWidget)


        self.retranslateUi(Form)

        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.cameraMainGroupBox.setTitle("")
        self.groupBox_4.setTitle("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("Form", u"Original Image", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Import from file:", None))
        self.groupBox_6.setTitle("")
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Import Data", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Load Original Img", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Single Detect", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"Export PDF", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Plot Figure", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"Load Original Imgs", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Batch Detect", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"Save Results", None))
        self.groupBox_3.setTitle("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Recgnition Results:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Progress:", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Period:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Recgnised Images\uff1a", None))
        self.label_3.setText("")
    # retranslateUi

