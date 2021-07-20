import qrcode
from PIL import Image
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from qt_material import apply_stylesheet
import time
import mysql.connector
global mydb
mydb = mysql.connector.connect(user='root', password='wildfactor', host='127.0.0.1',port=3306,database='items',
auth_plugin='mysql_native_password')
global mycursor
mycursor = mydb.cursor()
class Ui_QRWindow(object):
    def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(559, 661)
            MainWindow.setStyleSheet("background-color: ")
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
            self.lineEdit.setGeometry(QtCore.QRect(170, 160, 201, 41))
            self.lineEdit.setStyleSheet("background-color:rgb(255, 255, 255);")
            self.lineEdit.setStyleSheet("border: 2px solid blue;")
            self.lineEdit.setObjectName("lineEdit")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(170, 100, 201, 41))
            self.label.setStyleSheet("background-color:rgb(255, 255, 255);")
            self.label.setStyleSheet("border: 2px solid blue;")
            self.label.setObjectName("label")
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setGeometry(QtCore.QRect(170, 220, 201, 41))
            self.label_2.setStyleSheet("background-color:rgb(255, 255, 255);")
            self.label_2.setStyleSheet("border: 2px solid blue;")
            self.label_2.setObjectName("label_2")
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)

            self.label_3 = QtWidgets.QLabel(self.centralwidget)
            self.label_3.setGeometry(QtCore.QRect(170, 340, 201, 41))
            self.label_3.setStyleSheet("background-color:rgb(255, 255, 255);")
            self.label_3.setStyleSheet("border: 2px solid blue;")
            self.label_3.setObjectName("label_3")
            self.label_3.setAlignment(QtCore.Qt.AlignCenter)
            self.label_4 = QtWidgets.QLabel(self.centralwidget)
            self.label_4.setGeometry(QtCore.QRect(70, 40, 411, 20))
            self.label_4.setStyleSheet("background-color:rgb(255, 255, 255);")
            self.label_4.setStyleSheet("border: 2px solid blue;")
            self.label_4.setObjectName("label_4")
            self.label_4.setAlignment(QtCore.Qt.AlignCenter)
            self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
            self.lineEdit_2.setGeometry(QtCore.QRect(170, 280, 201, 41))
            self.lineEdit_2.setStyleSheet("background-color:rgb(255, 255, 255);")
            self.lineEdit_2.setStyleSheet("border: 2px solid blue;")
            self.lineEdit_2.setObjectName("lineEdit_2")
            self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
            self.lineEdit_3.setGeometry(QtCore.QRect(170, 400, 201, 41))
            self.lineEdit_3.setStyleSheet("background-color:rgb(255, 255, 255);")
            self.lineEdit_3.setStyleSheet("border: 2px solid blue;")
            self.lineEdit_3.setObjectName("lineEdit_3")
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setGeometry(QtCore.QRect(210, 500, 98, 81))
            self.pushButton.setStyleSheet("background-color:rgb(255, 255, 255);")
            self.pushButton.setStyleSheet("border: 2px solid blue;")
            self.pushButton.setObjectName("Admin")
            self.pushButton.clicked.connect(self.printanje)

            self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_2.setGeometry(QtCore.QRect(210,550,98,81))
            self.pushButton_2.setStyleSheet("background-color:rgb(255, 255, 255);")
            self.pushButton_2.setStyleSheet("border: 2px solid blue;")
            self.pushButton_2.setObjectName("Konobar")

            self.pushButton_2.clicked.connect(self.printanje2)
            MainWindow.setCentralWidget(self.centralwidget)


            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.label.setText(_translate("MainWindow", "First name"))
            self.label_2.setText(_translate("MainWindow", "Last name "))
            self.label_3.setText(_translate("MainWindow", "QR code will be saved as ?"))
            self.label_4.setText(_translate("MainWindow", "Please fill out required informations"))
            self.pushButton.setText(_translate("MainWindow", "Admin"))
            self.pushButton_2.setText(_translate("MainWindow", "konobar"))

    def printanje(self, MainWindow):
            ime = self.lineEdit.text()
            prezime = self.lineEdit_2.text()
            imeSlike = self.lineEdit_3.text()
            print(ime,prezime,imeSlike)
            img = qrcode.make(f'{ime,prezime}')

            qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10,
                    border=4,
            )

            qr.add_data(f"{ime,prezime}")
            try:
                blank = " "
                sql = ("INSERT INTO admin (ime_prezime) VALUE (%s %s %s)")
                val = (ime,blank,prezime)
                mycursor.execute(sql,val)
                mydb.commit()
                
            except:
                pass


            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

            img.save(f"{imeSlike}.png")
            sys.exit(0)(app.exec_())
    def printanje2(self, MainWindow):
            ime = self.lineEdit.text()
            prezime = self.lineEdit_2.text()
            imeSlike = self.lineEdit_3.text()
            print(ime,prezime,imeSlike)
            img = qrcode.make(f'{ime,prezime}')

            qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10,
                    border=4,
            )

            qr.add_data(f"{ime,prezime}")
            try :
                blank = " "
                sql = ("INSERT INTO konobari (ime_prezime) VALUE  (%s %s %s)")
                val = (ime,blank,prezime)
                mycursor.execute(sql,val)
                mydb.commit()
            except:
                print("nije proslo")
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

            img.save(f"{imeSlike}.png")
            sys.exit(0)(app.exec_())
            
if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        apply_stylesheet(app, theme='dark_teal.xml',invert_secondary=False)
        MainWindow = QtWidgets.QMainWindow()
        qrWindow = Ui_QRWindow()
        qrWindow.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
