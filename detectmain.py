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

        self.origImg ='./imgs/origImg.jpg'
        self.recgImg ='./imgs/recgImg.jpg'

        self.ui.labelOrigImg.setPixmap(QPixmap(self.origImg).scaled(self.ui.labelOrigImg.width(), self.ui.labelOrigImg.height(), Qt.KeepAspectRatio))
        self.ui.labelRecgImg.setPixmap(QPixmap(self.recgImg).scaled(self.ui.labelRecgImg.width(), self.ui.labelRecgImg.height(), Qt.KeepAspectRatio))


        # tableview for the original img, the concentration and RGB are known, to get the chart
        x = [1, 10, 30, 50, 80, 100, 120]
        y = [156, 144, 126, 103, 73, 53, 29]
        con_rgb_list = []
        for i in range(len(x)):
            con_rgb_list.append(str(x[i]))
            con_rgb_list.append(str(y[i]))
        model = QStandardItemModel()
        model.setColumnCount(2)
        for row in range(len(x)):
            for col in range(2):
                index = row*2+col
                item = QStandardItem(con_rgb_list[index])
                model.setItem(row, col, item)

        model.setHeaderData(0, Qt.Horizontal, "Con")
        model.setHeaderData(1, Qt.Horizontal, "Blue")

        self.ui.tabviewOrig.setModel(model)
        self.ui.tabviewOrig.verticalHeader().hide()
#        self.ui.tabviewOrig.setHorizontalHeader(QHeaderView())
        self.ui.tabviewOrig.setColumnWidth(0, self.ui.tabviewOrig.width()/2+16)
        self.ui.tabviewOrig.setColumnWidth(1, self.ui.tabviewOrig.width()/2+16)



        # plot the Chart
        font = {'family': 'serif',
                'color':  'black',
                'weight': 'normal',
                'size': 13,
                }

        x = [1, 10, 30, 50, 80, 100, 120]
        y = [156, 144, 126, 103, 73, 53, 29]
        slope, intercept, r, p, std_err = stats.linregress(x, y)
        def myfunc(x):
            return slope*x+intercept
        mymodel = list(map(myfunc, x))

        text = "y = {:.2f}*x+{:.2f}".format(slope, intercept)
        print('text=', text)
#        print("y = {:.2f}*x+{:.2f}".format(slope, intercept))

        rgb_B = [145, 111, 93, 50, 143, 114, 92, 48]
        con = []
        for item_B in rgb_B:
            con_temp = (item_B - intercept)/slope
            con.append(con_temp)

#        plt.plot(x, y, 'k')
        plt.title('Linear Regression and ML-based Fast Prediction', fontdict=font)

        plt.text(71, 143, "y = {:.2f} * x+{:.2f}".format(slope, intercept),
                backgroundcolor='#069AF3', fontsize=13,
                fontstyle='italic', fontfamily='times new roman',
                color=(1, 1, 1, 1))
#        plt.text(61, 143, r'$\cos(2 \pi t) \exp(-t)$', fontdict=font)
        plt.xlabel('Concentration %', fontdict=font)
        plt.ylabel('Blue Value', fontdict=font)



        plt.scatter(x,y, color='#0343DF')
        plt.plot(x, mymodel, color='#069AF3')
        plt.scatter(con, rgb_B, color='#ff7f0e')
        plt.legend(('experiment data', 'linear regression', 'prediction'),
                   loc='lower left', shadow=True)
        for x, y in zip(con, rgb_B):
            plt.text(x, y, '({:.1f},{:.1f})'.format(x,y),fontsize=7,rotation=30,color='#ff7f0e') #f'(x: {x}, y: {y})')
        plt.show()



        # tableview for the recognized img, the concentration and RGB are NOT known
        rgb_con_list = []
        for i in range(len(rgb_B)):
            rgb_con_list.append(str(round(rgb_B[i],1)))
            rgb_con_list.append(str(round(con[i],1)))
        model = QStandardItemModel()
        model.setColumnCount(2)
        for row in range(len(rgb_B)):
            for col in range(2):
                index = row*2+col
                item = QStandardItem(rgb_con_list[index])
                model.setItem(row, col, item)

        model.setHeaderData(0, Qt.Horizontal, "Blue")
        model.setHeaderData(1, Qt.Horizontal, "Con")

        self.ui.tabviewRecg.setModel(model)
        self.ui.tabviewRecg.verticalHeader().hide()
#        self.ui.tabviewRecg.setHorizontalHeader(QHeaderView())
        self.ui.tabviewRecg.setColumnWidth(0, self.ui.tabviewRecg.width()/2+16)
        self.ui.tabviewRecg.setColumnWidth(1, self.ui.tabviewRecg.width()/2+16)






#class Camera(QMainWindow):
#class ImageSettings(QDialog):
