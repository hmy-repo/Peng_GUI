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
        num = [1, 2, 3, 4, 5, 6, 7]
        con = [1, 10, 30, 50, 80, 100, 120]
        blue = [156, 146, 126, 99, 71, 55, 34]
        green = [107, 102, 89, 68, 47, 34, 17]
        red = [75, 71, 61, 46, 30, 22, 12]
        cols = 5
        con_rgb_list = []
        for i in range(len(con)):
            con_rgb_list.append(str(num[i]))
            con_rgb_list.append(str(con[i]))
            con_rgb_list.append(str(blue[i]))
            con_rgb_list.append(str(green[i]))
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
        model.setHeaderData(2, Qt.Horizontal, "Blue")
        model.setHeaderData(3, Qt.Horizontal, "Green")
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

        x = [1, 10, 30, 50, 80, 100, 120]
        y = [156, 146, 126, 99, 71, 55, 34]
        slope, intercept, r, p, std_err = stats.linregress(x, y)
        def myfunc(x):
            return slope*x+intercept
        mymodel = list(map(myfunc, x))

        text = "y = {:.4f}*x+{:.2f}".format(slope, intercept)
        print('text=', text)
#        print("y = {:.2f}*x+{:.2f}".format(slope, intercept))

        rgb_B = [144, 109, 94, 49, 143, 111, 93, 50]
        con = []
        for item_B in rgb_B:
            con_temp = (item_B - intercept)/slope
            con.append(con_temp)

#        plt.plot(x, y, 'k')
        plt.title('Linear Regression and DL-based HT-Detection', fontdict=font)

        plt.text(71, 143, "y = {:.4f} * x+{:.2f}".format(slope, intercept),
                backgroundcolor='#069AF3', fontsize=13,
                fontstyle='italic', fontfamily='times new roman',
                color=(1, 1, 1, 1))
#        plt.text(61, 143, r'$\cos(2 \pi t) \exp(-t)$', fontdict=font)
        plt.xlabel('Concentration', fontdict=font)
        plt.ylabel('Blue Value', fontdict=font)



        plt.scatter(x,y, color='#0343DF')
        plt.plot(x, mymodel, color='#069AF3')
        plt.scatter(con, rgb_B, color='#ff7f0e')
        plt.legend(('experimental data', 'linear regression', 'detection result'),
                   loc='lower left', shadow=True)
        for x, y in zip(con, rgb_B):
            plt.text(x, y, '({:.1f},{:.1f})'.format(x,y),fontsize=7,rotation=30,color='#ff7f0e') #f'(x: {x}, y: {y})')
        plt.show()



        # tableview for the recognized img, the concentration and RGB are NOT known
        num = [1, 2, 3, 4, 5, 6, 7, 8]
        rgb_G = [94, 71, 61, 28, 96, 73, 61, 27]
        rgb_R = [68, 49, 43, 19, 69, 52, 43, 19]
        rgb_con_list = []
        cols = 5
        for i in range(len(rgb_B)):
            rgb_con_list.append(str(num[i]))
            rgb_con_list.append(str(round(con[i],1)))
            rgb_con_list.append(str(round(rgb_B[i],0)))
            rgb_con_list.append(str(rgb_G[i]))
            rgb_con_list.append(str(rgb_R[i]))
        model = QStandardItemModel()
        model.setColumnCount(cols)
        for row in range(len(rgb_B)):
            for col in range(cols):
                index = row*cols+col
                item = QStandardItem(rgb_con_list[index])
                model.setItem(row, col, item)

        model.setHeaderData(0, Qt.Horizontal, "No.")
        model.setHeaderData(1, Qt.Horizontal, "Con.")
        model.setHeaderData(2, Qt.Horizontal, "Blue")
        model.setHeaderData(3, Qt.Horizontal, "Green")
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
