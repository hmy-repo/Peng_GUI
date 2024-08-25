# This Python file uses the following encoding: utf-8

import sys
from PySide6.QtWidgets import (QMainWindow, QFileDialog,QColorDialog, QComboBox,
                                QDialog, QFontComboBox,QTextEdit, QInputDialog,
                                QLineEdit, QMenu, QMessageBox,QProgressBar, QToolBar,
                                QVBoxLayout, QWidget, QTreeView, QTableView, QFileSystemModel,
                                QHeaderView)
from PySide6.QtGui import (QAction, QGuiApplication, QIcon, QKeySequence, QStandardItemModel,
                            QStandardItem, QImage, QPixmap)
from PySide6.QtCore import (QUrl, Qt, Slot, Signal, QDir)

from PySide6.QtPrintSupport import (QAbstractPrintDialog, QPrinter,
                                    QPrintDialog, QPrintPreviewDialog)
from PySide6.QtSql import QSqlTableModel
from PySide6.QtGui import QIcon
#from tr import tr
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from scipy import stats

from ui import ui_detectmain
from camera import Camera


class DetectMain(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = ui_detectmain.Ui_Form()
        self.ui.setupUi(self)

#        #put the cameraWidget in cameraMainlVLayout
        self.mainCamera = Camera()
#        self.ui.cameraMainGroupBox.setWidget(self.mainCamera._ui.cameraWidget)
        self.ui.cameraMainlVLayout.addWidget(self.mainCamera._ui.cameraWidget)
        self.ui.cameraMainlVLayout.setContentsMargins(0,0,0,0)


        #
        self.layout = QVBoxLayout()
        self.ui.widgetChart.setLayout(self.layout)

        # canvas
#        self.figure = plt.figure()
        self.figure, self.ax = plt.subplots(figsize=(15,15), dpi=100)#nrows=1, ncols=1,figsize=(15,10))#figsize=(20,15))
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.layout.addWidget(self.canvas)
#        self.layout.addWidget(self.toolbar)




        # tableview for the linear img, the concentration and RGB are known, to get the chart
        num = [1, 2, 3, 4, 5, 6]
        con = [1, 5, 10, 20, 30, 40]
        green = [80.45, 75.42, 90.34, 102.69, 124.07, 146.41]
        blue = [75.08, 70.14, 78.66, 90.30, 110.80, 132.41]
        red = [80.62, 75.20, 90.34, 102.50, 125.26, 145.41]
        cols = 5
        con_rgb_list = []
        for i in range(len(con)):
            con_rgb_list.append(str(num[i]))
            con_rgb_list.append(str(con[i]))
            con_rgb_list.append(str(green[i]))
            con_rgb_list.append(str(blue[i]))
            con_rgb_list.append(str(red[i]))
        model = QStandardItemModel()
        model.setColumnCount(cols)
        for row in range(len(con)):
            for col in range(cols):
                index = row*cols+col
                item = QStandardItem(con_rgb_list[index])
                model.setItem(row, col, item)

        model.setHeaderData(0, Qt.Horizontal, "No.")
        model.setHeaderData(1, Qt.Horizontal, "Con.")
        model.setHeaderData(2, Qt.Horizontal, "Green")
        model.setHeaderData(3, Qt.Horizontal, "Blue")
        model.setHeaderData(4, Qt.Horizontal, "Red")

        self.ui.tabviewOrig.setModel(model)
        self.ui.tabviewOrig.verticalHeader().hide()
#        self.ui.tabviewOrig.setHorizontalHeader(QHeaderView())
        self.ui.tabviewOrig.setColumnWidth(0, self.ui.tabviewOrig.width()/2)#+16)
        self.ui.tabviewOrig.setColumnWidth(1, self.ui.tabviewOrig.width()/2)#+16)
        self.ui.tabviewOrig.setColumnWidth(2, self.ui.tabviewOrig.width()/2)#+16)
        self.ui.tabviewOrig.setColumnWidth(3, self.ui.tabviewOrig.width()/2)#+16)
        self.ui.tabviewOrig.setColumnWidth(4, self.ui.tabviewOrig.width()/2)#+16)



        # plot the Chart
        font = {'family': 'serif',
                'color':  'black',
                'weight': 'normal',
                'size': 13,
                }

        x = [1, 5, 10, 20, 30, 40]
        y = [80.4523809523809, 75.4212250712251, 90.3362637362637, 102.6918881118880, 124.0684624017960, 146.4058149058150]
        slope, intercept, r, p, std_err = stats.linregress(x, y)
        R2 = pow(r, 2)
        def myfunc(x):
            return slope*x+intercept
        mymodel = list(map(myfunc, x))

        text = "y = {:.4f}*x+{:.2f}".format(slope, intercept)
#        print('text=', text)
#        print("y = {:.2f}*x+{:.2f}".format(slope, intercept))

        rgb_G = [74.01, 117.48, 136.03, 73.70, 123.45, 136.86]
        con = []
        for item_G in rgb_G:
            con_temp = (item_G - intercept)/slope
            con.append(con_temp)
        print('con: ', con)

#        plt.plot(x, y, 'k')
        plt.title('Linear Regression and ML-assisted HT-Detection', fontdict=font)

        plt.text(5, 140, "y = {:.4f} * x+{:.2f}  R2 = {:.4f}".format(slope, intercept, R2),
                backgroundcolor='#81e68e', fontsize=13,
                fontstyle='italic', fontfamily='times new roman',
                color=(0, 0, 0, 1)) # #069AF3
        # plt.text(61, 143, r'$\cos(2 \pi t) \exp(-t)$', fontdict=font)
        plt.xlabel('Concentration of Hg2+ (μM)', fontdict=font)
        plt.ylabel('Green Value', fontdict=font)



        plt.scatter(x,y, color='#07b553') #  #0343DF #0db838
        plt.plot(x, mymodel, color='#81e68e') # #0db838 #069AF3
        plt.scatter(con, rgb_G, color='#ff7f0e')
        plt.legend(('experimental data', 'linear regression', 'detection result'),
                   loc='lower right', shadow=True)
        for x, y in zip(con, rgb_G):
            plt.text(x, y, '({:.1f},{:.1f})'.format(x,y),fontsize=7,rotation=0,color='#ff7f0e') #f'(x: {x}, y: {y})')
        plt.show()



        # tableview for the recognized img, the concentration and RGB are NOT known
        num = [1, 2, 3, 4, 5, 6]
        rgb_B = [63.50, 105.36, 122.03, 70.38, 109.34, 119.40]
        rgb_R = [76.29, 117.37, 135.03, 74.15, 122.52, 138.62]
        rgb_con_list = []
        cols = 5
        for i in range(len(rgb_G)):
            rgb_con_list.append(str(num[i]))
            rgb_con_list.append(str(round(con[i],2)))
            rgb_con_list.append(str(round(rgb_G[i],2)))
            rgb_con_list.append(str(rgb_B[i]))
            rgb_con_list.append(str(rgb_R[i]))
        model = QStandardItemModel()
        model.setColumnCount(cols)
        for row in range(len(rgb_G)):
            for col in range(cols):
                index = row*cols+col
                item = QStandardItem(rgb_con_list[index])
                model.setItem(row, col, item)

        model.setHeaderData(0, Qt.Horizontal, "No.")
        model.setHeaderData(1, Qt.Horizontal, "Con.")
        model.setHeaderData(2, Qt.Horizontal, "Green")
        model.setHeaderData(3, Qt.Horizontal, "Blue")
        model.setHeaderData(4, Qt.Horizontal, "Red")


        self.ui.tabviewRecg.setModel(model)
        self.ui.tabviewRecg.verticalHeader().hide()
#        self.ui.tabviewRecg.setHorizontalHeader(QHeaderView())
        self.ui.tabviewRecg.setColumnWidth(0, self.ui.tabviewRecg.width()/2)#+16)
        self.ui.tabviewRecg.setColumnWidth(1, self.ui.tabviewRecg.width()/2)#+16)
        self.ui.tabviewRecg.setColumnWidth(2, self.ui.tabviewRecg.width()/2)#+16)
        self.ui.tabviewRecg.setColumnWidth(3, self.ui.tabviewRecg.width()/2)#+16)
        self.ui.tabviewRecg.setColumnWidth(4, self.ui.tabviewRecg.width()/2)#+16)


        self.origImg ='./imgs/linearRegressionImg.jpg'
        self.recgImg ='./imgs/detectionImg.jpg'

        self.ui.labelOrigImg.setPixmap(QPixmap(self.origImg).scaled(self.ui.labelRecgImg.width(), self.ui.labelRecgImg.height(), Qt.KeepAspectRatio))
        self.ui.labelRecgImg.setPixmap(QPixmap(self.recgImg).scaled(self.ui.labelRecgImg.width(), self.ui.labelRecgImg.height(), Qt.KeepAspectRatio))


# self.ui.labelOrigImg.width(),

#class Camera(QMainWindow):
#class ImageSettings(QDialog):
