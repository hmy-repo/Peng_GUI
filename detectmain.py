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
        num = [1, 2, 3, 4, 5]
        con = [1, 10, 20, 30, 40]
        green = [79.48, 90.13, 102.62, 124.11, 146.29]
        blue = [74.04, 78.43, 90.29, 110.84, 132.29]
        red = [79.49, 90.13, 102.45, 125.30, 145.29]
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

        x = [1, 10, 20, 30, 40]
        y = [79.4798923817615, 90.1310552500655, 102.6154051172710, 124.1063063063060, 146.2869718309860]
        slope, intercept, r, p, std_err = stats.linregress(x, y)
        R2 = pow(r, 2)
        def myfunc(x):
            return slope*x+intercept
        mymodel = list(map(myfunc, x))

        text = "Y = {:.4f}*X+{:.2f}".format(slope, intercept)
#        print('text=', text)
#        print("y = {:.2f}*x+{:.2f}".format(slope, intercept))

        rgb_G = [75.74, 120.51, 139.03, 75.73, 126.45, 139.87]
        con = []
        for item_G in rgb_G:
            con_temp = (item_G - intercept)/slope
            con.append(con_temp)
        print('con: ', con)

#        plt.plot(x, y, 'k')
        plt.title('Linear Regression and ML-assisted HT-Detection', fontdict=font, fontsize=15)

        plt.text(4, 135, "Y = {:.4f} * X+{:.2f} ,  R$^2$ = {:.4f}".format(slope, intercept, R2),
                backgroundcolor='#81e68e', fontsize=16,
                fontstyle='italic', fontfamily='times new roman',
                color=(0, 0, 0, 1)) # #069AF3
        # plt.text(61, 143, r'$\cos(2 \pi t) \exp(-t)$', fontdict=font)
        plt.xlabel('Concentration of Hg$^{2+}$ (μM)', fontdict=font, fontsize=13)
        plt.ylabel('Green Value', fontdict=font, fontsize=13)



        plt.scatter(x,y, color='#07b553', linewidths=4, zorder=1) #  #0343DF #0db838
        plt.plot(x, mymodel, color='#81e68e', linewidth=3,linestyle='--', zorder=2) # #0db838 #069AF3
        plt.scatter(con, rgb_G, color='#ff7f0e', linewidths=4, zorder=3)




        plt.legend(('experimental data', 'linear regression', 'detection result'),
                   loc='lower right', shadow=True)

        marker_color = '#ff7f0e'
        marker_size = 10
        plt.text(con[0]+1, rgb_G[0], '({:.2f},{:.2f})'.format(con[0], rgb_G[0]),fontsize=marker_size,rotation=0,color=marker_color)
        plt.text(con[1]-1, rgb_G[1]-4, '({:.2f},{:.2f})'.format(con[1], rgb_G[1]),fontsize=marker_size,rotation=0,color=marker_color)
        plt.text(con[2]-7.5, rgb_G[2]-0.5, '({:.2f},{:.2f})'.format(con[2], rgb_G[2]),fontsize=marker_size,rotation=0,color=marker_color)
        plt.text(con[3]+1, rgb_G[3]-3, '({:.2f},{:.2f})'.format(con[3], rgb_G[3]),fontsize=marker_size,rotation=0,color=marker_color)
        plt.text(con[4]+1, rgb_G[4]-1, '({:.2f},{:.2f})'.format(con[4], rgb_G[4]),fontsize=marker_size,rotation=0,color=marker_color)
        plt.text(con[5]-5.5, rgb_G[5]+2.5, '({:.2f},{:.2f})'.format(con[5], rgb_G[5]),fontsize=marker_size,rotation=0,color=marker_color)


        # for x, y in zip(con[0:3], rgb_G[0:3]):
        #     plt.text(x+1, y, '({:.2f},{:.2f})'.format(x,y),fontsize=10,rotation=0,color='#ff7f0e') #f'(x: {x}, y: {y})')
        # for x, y in zip(con[3:6], rgb_G[3:6]):
        #     plt.text(x+1, y, '({:.2f},{:.2f})'.format(x,y),fontsize=10,rotation=0,color='#ff7f0e') #f'(x: {x}, y: {y})')
        plt.show()



        # tableview for the recognized img, the concentration and RGB are NOT known
        num = [1, 2, 3, 4, 5, 6]
        rgb_B = [65.13, 108.38, 125.03, 72.40, 112.34, 122.40]
        rgb_R = [77.99, 120.41, 138.03, 76.18, 125.52, 141.62]
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
