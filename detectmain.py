# This Python file uses the following encoding: utf-8

import sys
from PySide6.QtWidgets import (QMainWindow, QFileDialog,QColorDialog, QComboBox,
                                QDialog, QFontComboBox,QTextEdit, QInputDialog,
                                QLineEdit, QMenu, QMessageBox,QProgressBar, QToolBar,
                                QVBoxLayout, QWidget, QTreeView, QFileSystemModel)
from PySide6.QtGui import QAction, QGuiApplication, QIcon, QKeySequence
from PySide6.QtCore import QUrl, Qt, Slot, Signal, QDir

from PySide6.QtPrintSupport import (QAbstractPrintDialog, QPrinter,
                                    QPrintDialog, QPrintPreviewDialog)
from PySide6.QtGui import QIcon
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






#class Camera(QMainWindow):
#class ImageSettings(QDialog):
