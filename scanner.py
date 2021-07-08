import mysql.connector
import sys
import time
import cv2
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from pyzbar import pyzbar
from adminPanel import *
from qt_material import  apply_stylesheet


def openAdminPanel():
        import sys
        aplikacija = QtWidgets.QApplication(sys.argv)
        apply_stylesheet( aplikacija , theme='dark_red.xml',invert_secondary=True)
        window = QtWidgets.QMainWindow()
        ui = Ui_AdminProzor()
        ui.setupUi(window)
        window.show()
        def update_label():
            new_text = (f"welcome {ime} please select what option you want")#inserting into a label refresh rate 1 sec 
            ui.label.setText(new_text)
        timer = QtCore.QTimer()
        timer.timeout.connect(update_label)
        timer.start(100)
        sys.exit(aplikacija.exec_())
        return skener()
              

def skener():
        def read_barcodes(frame):
                global mydb
                mydb = mysql.connector.connect(user='root', password='wildfactor', host='127.0.0.1',port=3306,database='items',
                auth_plugin='mysql_native_password')
                global mycursor
                mycursor = mydb.cursor()
                
                barcodes = pyzbar.decode(frame)
                for barcode in barcodes:
                        x, y , w, h = barcode.rect
                        global barcode_info
                        barcode_info = barcode.data.decode('utf-8')
                
                        barcode_info = barcode_info.replace("(","")
                        barcode_info = barcode_info.replace(")","")
                        barcode_info = barcode_info.replace(",","")
                        barcode_info = barcode_info.replace("'","")
                        barcode_info = barcode_info.replace("[","")
                        barcode_info = barcode_info.replace("]","")
                        
                        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
                        
                        
                        sql1 = ("SELECT * FROM konobari")
                        mycursor.execute(sql1,)
                        outputKonobar = mycursor.fetchall()
                        
                        sql = ("SELECT * FROM admin")
                        mycursor.execute(sql,)
                        outputAdmin = mycursor.fetchall()
                        
                        for admin in outputAdmin:
                                admin = ','.join(str(o) for o in admin)
                                admin = admin.replace("(","")
                                admin = admin.replace(")","")
                                admin = admin.replace(",","")
                                admin = admin.replace("'","")
                                admin = admin.replace("[","")
                                admin = admin.replace("]","")
                                if admin == barcode_info:
                                        global ime
                                        ime = admin
                                        print("radi")
                                        openAdminPanel()
                                else:
                                        pass

                        
                        for konobar in outputKonobar:
                                konobar = ','.join(str(o) for o in konobar)
                                konobar = konobar.replace("(","")
                                konobar = konobar.replace(")","")
                                konobar = konobar.replace(",","")
                                konobar = konobar.replace("'","")
                                konobar = konobar.replace("[","")
                                konobar = konobar.replace("]","")
                                if konobar == barcode_info:
                                        print("radi konobar")
                                
                        
                




                        font = cv2.FONT_HERSHEY_DUPLEX
                        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
                
                                        
                        
                return frame
                                    
        def main():
                global frame
                camera = cv2.VideoCapture(0) 
                ret, frame = camera.read()
                
                while ret:
                        ret, frame = camera.read()
                        frame = read_barcodes(frame)
                        cv2.imshow('Barcode/QR code reader', frame)
                        if cv2.waitKey(1) & 0xFF == 27:
                                break
                camera.release()
                cv2.destroyWindows()

        if __name__ == '__main__':
                main()
skener()