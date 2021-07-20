import mysql.connector
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from qt_material import apply_stylesheet
from items import Ui_Items
from qrmaker import Ui_QRWindow




class Ui_AdminProzor(object):
    def openWindowItemsInput(self):

            self.appItems = QtWidgets.QApplication(sys.argv)
            apply_stylesheet(self.appItems, theme='dark_teal.xml',invert_secondary=True)
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Items()
            self.ui.setupUi(self.window)
            self.window.show()
            

    def openWindowQRInput(self):

            self.appQRWindow = QtWidgets.QApplication(sys.argv)
            apply_stylesheet(self.appQRWindow, theme='dark_teal.xml',invert_secondary=False)
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_QRWindow()
            self.ui.setupUi(self.window)
            self.window.show()
           
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("admin board")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 40, 601, 141))
        self.label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 280, 261, 201))
        self.pushButton_2.setStyleSheet("background-color:rgb(125, 192, 255);\n""")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 280, 261, 201))
        self.pushButton_3.setStyleSheet("background-color:rgb(125, 192, 255);\n""")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "WELCOMING"))
        self.pushButton_2.setText(_translate("MainWindow", "DODAVANJE ROBE"))
        self.pushButton_2.clicked.connect(self.openWindowItemsInput)
        self.pushButton_3.setText(_translate("MainWindow", "DODAVANJE KONOBARA"))
        self.pushButton_3.clicked.connect(self.openWindowQRInput)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_red.xml',invert_secondary=True)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AdminProzor()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    def update_label():
            new_text = ("welcome  please select what option you want")#inserting into a label refresh rate 1 sec 
            ui.label.setText(new_text)

    timer = QtCore.QTimer()
    timer.timeout.connect(update_label)
    timer.start(1000)  
    sys.exit(app.exec_())
