import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
from qt_material import apply_stylesheet
from pyzbar import pyzbar
import cv2
from adminPanel import Ui_AdminProzor
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

                        global konobar
                        for konobar in outputKonobar:
                                konobar = ','.join(str(o) for o in konobar)
                                konobar = konobar.replace("(","")
                                konobar = konobar.replace(")","")
                                konobar = konobar.replace(",","")
                                konobar = konobar.replace("'","")
                                konobar = konobar.replace("[","")
                                konobar = konobar.replace("]","")
                                if konobar == barcode_info:
                                        sql = ("INSERT INTO privermena (konobar) VALUES (%s)")
                                        val = (konobar,)
                                        mycursor.execute(sql,val)
                                        mydb.commit()
                                        print("radi konobar")
                                        import sys
                                        appMainBoard = QtWidgets.QApplication(sys.argv)
                                        apply_stylesheet(appMainBoard,theme ="dark_blue.xml",invert_secondary=False)
                                        window = QtWidgets.QMainWindow()
                                        ui = Ui_MainWindow()
                                        ui.setupUi(window)
                                        global update_label        
                                        def update_label():
                                                sql = ("SELECT kind FROM vrsta")
                                                mycursor.execute(sql)
                                                kind = mycursor.fetchall()
                                                for vrsta in kind:
                                                        vrsta = ','.join(str(o) for o in vrsta)
                                                        vrsta = vrsta.replace("(","")
                                                        vrsta = vrsta.replace(")","")
                                                        vrsta = vrsta.replace(",","")
                                                        vrsta = vrsta.replace("'","")
                                                        vrsta = vrsta.replace("[","")
                                                        vrsta = vrsta.replace("]","")
                                                        kind = vrsta
                                                KindLabelText = (f"{kind} ")

                                                sql = ("SELECT Receipt FROM printanje")
                                                mycursor.execute(sql)

                                                rec  = mycursor.fetchall()
                                                lista = []
                                                for priv in rec:
                                                        priv = ','.join(str(o) for o in priv)
                                                        priv = priv.replace("(","")
                                                        priv = priv.replace(")","")
                                                        priv = priv.replace(",","")
                                                        priv = priv.replace("'","")
                                                        priv = priv.replace("[","")
                                                        priv = priv.replace("]","")
                                                        lista.append(priv)
                                                lista = ','.join(str(i) for i in lista)
                                                lista =        lista.replace("(","")
                                                lista =        lista.replace(")","")
                                                lista =        lista.replace(","," \n")
                                                lista =        lista.replace("'","")
                                                lista =        lista.replace("[","")
                                                lista =        lista.replace("]","")
                                                ReceiptLabelText = (f"Receipt\n{lista}\n")
                                                sql = ("SELECT konobar FROM privermena")
                                                mycursor.execute(sql)
                                                privremeni = mycursor.fetchall()
                                                for priv in privremeni:
                                                        priv = ','.join(str(o) for o in priv)
                                                        priv = priv.replace("(","")
                                                        priv = priv.replace(")","")
                                                        priv = priv.replace(",","")
                                                        priv = priv.replace("'","")
                                                        priv = priv.replace("[","")
                                                        priv = priv.replace("]","")
                                                        konobar  = priv
                                                WaiterLabelText = (f"{konobar}")
                                                sqlQuantity = ("SELECT Quantity FROM kolicina")
                                                mycursor.execute(sqlQuantity)
                                                kolicina = mycursor.fetchall()
                                                quantity = 0
                                                zbir = 0
                                                for kol in kolicina:
                                                        kol = ','.join(str(o) for o in kol)
                                                        kol = kol.replace("(","")
                                                        kol = kol.replace(")","")
                                                        kol = kol.replace(",","")
                                                        kol = kol.replace("'","")
                                                        kol = kol.replace("[","")
                                                        kol = kol.replace("]","")
                                                        quantity += 1
                                                        if kol == "kafa":
                                                            zbir +=1.5
                                                        elif kol == "caj":
                                                            zbir +=1
                                                        elif kol == "CocaCola":
                                                            zbir += 2.5
                                                        elif kol == "Cockta":
                                                            zbir += 3
                                                        elif kol == "Senzacija":
                                                            zbir +=1.5
                                                        elif kol == "Kapucino":
                                                            zbir += 2


                                                    
                                                        
                                                
                                                QuantityLabelText = (f"{quantity}")
                                                TotalLabelText = (f"{zbir}")
                                                ui.ReceiptLabel.setText(ReceiptLabelText)
                                                ui.KindLabelUpdate.setText(KindLabelText)
                                                ui.QuantityLabelUpdate.setText(QuantityLabelText)
                                                ui.TotalLabelUpdate.setText(TotalLabelText)
                                                ui.WaiterLabel.setText(WaiterLabelText)
                                                return update_label
                                        window.show()
                                        timer = QtCore.QTimer()
                                        timer.timeout.connect(update_label)
                                        timer.start(100)                
                                        sys.exit(appMainBoard.exec_())
                                
                        
                




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
                
class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                
                MainWindow.setObjectName("MainWindow")
                MainWindow.setWindowModality(QtCore.Qt.NonModal)
                MainWindow.resize(1230, 800)
                MainWindow.setMinimumSize(QtCore.QSize(1230, 800))
                MainWindow.setSizeIncrement(QtCore.QSize(1230, 800))
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setAutoFillBackground(False)
                self.centralwidget.setObjectName("centralwidget")
                self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
                self.horizontalLayoutWidget.setGeometry(QtCore.QRect(19, 19, 1191, 81))
                self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
                self.horizontalLayout.setSpacing(0)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.KindLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
                self.KindLabel.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
        "border: solid black;\n" 
        "border-width : 1px 0px 1px 1px;\n"
        "background-color:rgb(68,138,255);")
                self.KindLabel.setAlignment(QtCore.Qt.AlignCenter)
                self.KindLabel.setObjectName("KindLabel")
                self.horizontalLayout.addWidget(self.KindLabel)
                self.KindLabelUpdate = QtWidgets.QLabel(self.horizontalLayoutWidget)
                self.KindLabelUpdate.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
        "border: solid black;\n"
        "border-width : 1px 0px 1px 0px;\n"
        "background-color:rgb(68,138,255);")
                self.KindLabelUpdate.setAlignment(QtCore.Qt.AlignCenter)
                self.KindLabelUpdate.setObjectName("KindLabelUpdate")
                self.horizontalLayout.addWidget(self.KindLabelUpdate)
                self.QuantityLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
                self.QuantityLabel.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
        "border: solid black;\n"
        "border-width : 1px 0px 1px 1px;\n"
        "background-color:rgb(68,138,255);")
                self.QuantityLabel.setAlignment(QtCore.Qt.AlignCenter)
                self.QuantityLabel.setObjectName("QuantityLabel")
                self.horizontalLayout.addWidget(self.QuantityLabel)
                self.QuantityLabelUpdate = QtWidgets.QLabel(self.horizontalLayoutWidget)
                self.QuantityLabelUpdate.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
        "border: solid black;\n"
        "border-width : 1px 0px 1px 0px;\n"
        "background-color:rgb(68,138,255);")
                self.QuantityLabelUpdate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.QuantityLabelUpdate.setObjectName("QuantityLabelUpdate")
                self.horizontalLayout.addWidget(self.QuantityLabelUpdate)
                self.TotalLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
                self.TotalLabel.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
        "border: solid black;\n"
        "border-width : 1px 0px 1px 1px;\n"
        "background-color:rgb(68,138,255);")
                self.TotalLabel.setAlignment(QtCore.Qt.AlignCenter)
                self.TotalLabel.setObjectName("TotalLabel")
                self.horizontalLayout.addWidget(self.TotalLabel)
                self.TotalLabelUpdate = QtWidgets.QLabel(self.horizontalLayoutWidget)
                self.TotalLabelUpdate.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
        "border: solid black;\n"
        "border-width : 1px 1px 1px 0px;\n"
        "background-color:rgb(68,138,255);")
                self.TotalLabelUpdate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.TotalLabelUpdate.setObjectName("label")
                self.horizontalLayout.addWidget(self.TotalLabelUpdate)
                self.kafaButton = QtWidgets.QPushButton(self.centralwidget)
                self.kafaButton.setGeometry(QtCore.QRect(20, 140, 181, 91))
                self.kafaButton.setObjectName("kafaButton")
                self.kapucinaButton = QtWidgets.QPushButton(self.centralwidget)
                self.kapucinaButton.setGeometry(QtCore.QRect(20, 440, 181, 91))
                
                self.kapucinaButton.setObjectName("kapucinaButton")
                self.cajButton = QtWidgets.QPushButton(self.centralwidget)
                self.cajButton.setGeometry(QtCore.QRect(20, 240, 181, 91))
                self.cajButton.setObjectName("cajButton")
                self.CocaColaButton = QtWidgets.QPushButton(self.centralwidget)
                self.CocaColaButton.setGeometry(QtCore.QRect(20, 540, 181, 91))
                
                self.CocaColaButton.setObjectName("CocaColaButton")
                self.senzacijaButton = QtWidgets.QPushButton(self.centralwidget)
                self.senzacijaButton.setGeometry(QtCore.QRect(20, 340, 181, 91))
                
                self.senzacijaButton.setObjectName("senzacijaButton")
                self.CocktaButton = QtWidgets.QPushButton(self.centralwidget)
                self.CocktaButton.setGeometry(QtCore.QRect(20, 640, 181, 91))

                self.CocktaButton.setObjectName("CocktaButton")
                self.JagodButton = QtWidgets.QPushButton(self.centralwidget)
                self.JagodButton.setGeometry(QtCore.QRect(220, 340, 181, 91))

                self.JagodButton.setObjectName("JagodButton")
                self.LemonadeButton = QtWidgets.QPushButton(self.centralwidget)
                self.LemonadeButton.setGeometry(QtCore.QRect(220, 640, 181, 91))
                
                self.LemonadeButton.setObjectName("LemonadeButton")
                self.NarandzaButton = QtWidgets.QPushButton(self.centralwidget)
                self.NarandzaButton.setGeometry(QtCore.QRect(220, 440, 181, 91))
                
                self.NarandzaButton.setObjectName("NarandzaButton")
                self.BreskvaButton = QtWidgets.QPushButton(self.centralwidget)
                self.BreskvaButton.setGeometry(QtCore.QRect(220, 140, 181, 91))
        
                self.BreskvaButton.setObjectName("BreskvaButton")
                self.MarelicaButton = QtWidgets.QPushButton(self.centralwidget)
                self.MarelicaButton.setGeometry(QtCore.QRect(220, 540, 181, 91))
                
                self.MarelicaButton.setObjectName("MarelicaButton")
                self.JabukaButton = QtWidgets.QPushButton(self.centralwidget)
                self.JabukaButton.setGeometry(QtCore.QRect(220, 240, 181, 91))

                self.JabukaButton.setObjectName("JabukaButton")
                self.KarlovackoButton = QtWidgets.QPushButton(self.centralwidget)
                self.KarlovackoButton.setGeometry(QtCore.QRect(420, 340, 181, 91))
                
                self.KarlovackoButton.setObjectName("KarlovackoButton")
                self.PaulanerButton = QtWidgets.QPushButton(self.centralwidget)
                self.PaulanerButton.setGeometry(QtCore.QRect(420, 640, 181, 91))
                
                self.PaulanerButton.setObjectName("PaulanerButton")
                self.BavariaButton = QtWidgets.QPushButton(self.centralwidget)
                self.BavariaButton.setGeometry(QtCore.QRect(420, 440, 181, 91))
        
                self.BavariaButton.setObjectName("BavariaButton")
                self.SomersbyButton = QtWidgets.QPushButton(self.centralwidget)
                self.SomersbyButton.setGeometry(QtCore.QRect(420, 140, 181, 91))
                
                self.SomersbyButton.setObjectName("SomersbyButton")
                self.TuborgButton = QtWidgets.QPushButton(self.centralwidget)
                self.TuborgButton.setGeometry(QtCore.QRect(420, 540, 181, 91))

                self.TuborgButton.setObjectName("TuborgButton")
                self.RadlerButton = QtWidgets.QPushButton(self.centralwidget)
                self.RadlerButton.setGeometry(QtCore.QRect(420, 240, 181, 91))

                self.RadlerButton.setObjectName("RadlerButton")
                self.JanaNarandzaButton = QtWidgets.QPushButton(self.centralwidget)
                self.JanaNarandzaButton.setGeometry(QtCore.QRect(610, 340, 181, 91))
                self
                self.JanaNarandzaButton.setObjectName("JanaNarandzaButton")
                self.RedBullButton = QtWidgets.QPushButton(self.centralwidget)
                self.RedBullButton.setGeometry(QtCore.QRect(610, 640, 181, 91))
        
                self.RedBullButton.setObjectName("RedBullButton")
                self.JanaLimunButton = QtWidgets.QPushButton(self.centralwidget)
                self.JanaLimunButton.setGeometry(QtCore.QRect(610, 440, 181, 91))
                
                self.JanaLimunButton.setObjectName("JanaLimunButton")
                self.VinoButton = QtWidgets.QPushButton(self.centralwidget)
                self.VinoButton.setGeometry(QtCore.QRect(610, 140, 181, 91))
                self.VinoButton.setObjectName("VinoButton")
                self.JanaIceTeaButton = QtWidgets.QPushButton(self.centralwidget)
                self.JanaIceTeaButton.setGeometry(QtCore.QRect(610, 540, 181, 91))
                
                self.JanaIceTeaButton.setObjectName("JanaIceTeaButton")
                self.CedevitaButton = QtWidgets.QPushButton(self.centralwidget)
                self.CedevitaButton.setGeometry(QtCore.QRect(610, 240, 181, 91))
                
                self.CedevitaButton.setObjectName("CedevitaButton")
                self.HamburgerButton = QtWidgets.QPushButton(self.centralwidget)
                self.HamburgerButton.setGeometry(QtCore.QRect(800, 340, 181, 91))
        
                self.HamburgerButton.setObjectName("HamburgerButton")
                self.SalataButton = QtWidgets.QPushButton(self.centralwidget)
                self.SalataButton.setGeometry(QtCore.QRect(800, 640, 181, 91))

                self.SalataButton.setObjectName("SalataButton")
                self.DonerButton = QtWidgets.QPushButton(self.centralwidget)
                self.DonerButton.setGeometry(QtCore.QRect(800, 440, 181, 91))

                self.DonerButton.setObjectName("DonerButton")
                self.PizzaButton = QtWidgets.QPushButton(self.centralwidget)
                self.PizzaButton.setGeometry(QtCore.QRect(800, 140, 181, 91))

                self.PizzaButton.setObjectName("PizzaButton")
                self.PastaButton = QtWidgets.QPushButton(self.centralwidget)
                self.PastaButton.setGeometry(QtCore.QRect(800, 540, 181, 91))

                self.PastaButton.setObjectName("PastaButton")
                self.PalacinciButton = QtWidgets.QPushButton(self.centralwidget)
                self.PalacinciButton.setGeometry(QtCore.QRect(800, 240, 181, 91))
                
                self.PalacinciButton.setObjectName("PalacinciButton")
                self.WaiterLabel = QtWidgets.QLabel(self.centralwidget)
                self.WaiterLabel.setGeometry(QtCore.QRect(1010, 380, 201, 81))
                self.WaiterLabel.setStyleSheet("background-color:grey;\n"
        "font: 16pt \"MS Shell Dlg 2\";\n"
        "border: solid black;\n"
        "border-width : 1px 1px 1px 1px;\n"
        "background-color:rgb(68,138,255);\n"
        "border-radius:10px;")
                self.WaiterLabel.setAlignment(QtCore.Qt.AlignCenter)
                self.WaiterLabel.setObjectName("WaiterLabel")
                self.EnterButton = QtWidgets.QPushButton(self.centralwidget)
                self.EnterButton.setGeometry(QtCore.QRect(1000, 490, 221, 241))

                self.EnterButton.setObjectName("EnterButton")
                self.ReceiptLabel = QtWidgets.QLabel(self.centralwidget)
                self.ReceiptLabel.setGeometry(QtCore.QRect(1014, 150, 191, 201))
                self.ReceiptLabel.setStyleSheet("background-color:grey;\n"
        "border: solid black;\n"
        "border-width : 1px 1px 1px 1px;\n"
        "background-color:rgb(68,138,255);\n"
        "border-radius:10px;")
                self.ReceiptLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignCenter)
                self.ReceiptLabel.setIndent(20)
                self.ReceiptLabel.setObjectName("ReceiptLabel")
                self.ReceiptLabel.setWordWrap(True)
                self.line = QtWidgets.QFrame(self.centralwidget)
                self.line.setGeometry(QtCore.QRect(400, 120, 20, 601))
                self.line.setFrameShape(QtWidgets.QFrame.VLine)
                self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line.setObjectName("line")
                self.line_2 = QtWidgets.QFrame(self.centralwidget)
                self.line_2.setGeometry(QtCore.QRect(0, 120, 1231, 20))
                self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
                self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_2.setObjectName("line_2")
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 1230, 26))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Emir"))
                self.KindLabel.setText(_translate("MainWindow", "kind:"))
                self.KindLabelUpdate.setText(_translate("MainWindow", ""))
                self.QuantityLabel.setText(_translate("MainWindow", "Quantity:"))
                self.QuantityLabelUpdate.setText(_translate("MainWindow", ""))
                self.TotalLabel.setText(_translate("MainWindow", "Total:"))
                self.TotalLabelUpdate.setText(_translate("MainWindow", ""))
                self.kafaButton.setText(_translate("MainWindow", "kafa"))
                self.kafaButton.clicked.connect(self.kafa)
                self.kapucinaButton.setText(_translate("MainWindow", "kapucino"))
                self.kapucinaButton.clicked.connect(self.kapucino)
                self.cajButton.setText(_translate("MainWindow", "caj"))
                self.cajButton.clicked.connect(self.caj)
                self.CocaColaButton.setText(_translate("MainWindow", "Coca Cola"))
                self.CocaColaButton.clicked.connect(self.CocaCola)
                self.senzacijaButton.setText(_translate("MainWindow", "senzacija"))
                self.senzacijaButton.clicked.connect(self.Senzacija)
                self.CocktaButton.setText(_translate("MainWindow", "Cockta"))
                self.CocktaButton.clicked.connect(self.cockta)
                self.JagodButton.setText(_translate("MainWindow", "Cappy Jagoda"))
                self.JagodButton.clicked.connect(self.CappyJagoda)
                self.LemonadeButton.setText(_translate("MainWindow", "Cappy Lemonade"))
                self.LemonadeButton.clicked.connect(self.Lemonade)
                self.NarandzaButton.setText(_translate("MainWindow", "Cappy Narandža"))
                self.NarandzaButton.clicked.connect(self.CappyNarandza)
                self.BreskvaButton.setText(_translate("MainWindow", "Cappy Breskva"))
                self.BreskvaButton.clicked.connect(self.CappyBreskva)
                self.MarelicaButton.setText(_translate("MainWindow", "Cappy Marelica"))
                self.MarelicaButton.clicked.connect(self.CappyMarelica)
                self.JabukaButton.setText(_translate("MainWindow", "Cappy Jabuka"))
                self.JabukaButton.clicked.connect(self.CappyJabuka)
                self.KarlovackoButton.setText(_translate("MainWindow", "Karlovacko"))
                self.KarlovackoButton.clicked.connect(self.karlovacko)
                self.PaulanerButton.setText(_translate("MainWindow", "Paulaner"))
                self.PaulanerButton.clicked.connect(self.paulaner)
                self.BavariaButton.setText(_translate("MainWindow", "Bavaria"))
                self.BavariaButton.clicked.connect(self.bavaria)
                self.SomersbyButton.setText(_translate("MainWindow", "Somersby"))
                self.SomersbyButton.clicked.connect(self.Somersby)
                self.TuborgButton.setText(_translate("MainWindow", "Tuborg"))
                self.TuborgButton.clicked.connect(self.tuborg)
                self.RadlerButton.setText(_translate("MainWindow", "Radler"))
                self.RadlerButton.clicked.connect(self.radler)
                self.JanaNarandzaButton.setText(_translate("MainWindow", "Jana Narandža"))
                self.JanaNarandzaButton.clicked.connect(self.JanaNarandza)
                self.RedBullButton.setText(_translate("MainWindow", "Red Bull"))
                self.RedBullButton.clicked.connect(self.RedBull)
                self.JanaLimunButton.setText(_translate("MainWindow", "Jana Limun"))
                self.JanaLimunButton.clicked.connect(self.JanaLimun)
                self.VinoButton.setText(_translate("MainWindow", "Vino"))
                self.VinoButton.clicked.connect(self.vino)
                self.JanaIceTeaButton.setText(_translate("MainWindow", "Jana Ice Tea"))
                self.JanaIceTeaButton.clicked.connect(self.JanaIceTea)
                self.CedevitaButton.setText(_translate("MainWindow", "Cedevita"))
                self.CedevitaButton.clicked.connect(self.cedevita)
                self.HamburgerButton.setText(_translate("MainWindow", "Hamburger"))
                self.HamburgerButton.clicked.connect(self.Hamburger)
                self.SalataButton.setText(_translate("MainWindow", "Salata"))
                self.SalataButton.clicked.connect(self.Salata)
                self.DonerButton.setText(_translate("MainWindow", "Doner"))
                self.DonerButton.clicked.connect(self.Doner)
                self.PizzaButton.setText(_translate("MainWindow", "Pizza"))
                self.PizzaButton.clicked.connect(self.Pizza)
                self.PastaButton.setText(_translate("MainWindow", "Pasta"))
                self.PastaButton.clicked.connect(self.Pasta)
                self.PalacinciButton.setText(_translate("MainWindow", "Palacinci"))
                self.PalacinciButton.clicked.connect(self.Palacinci)
                self.WaiterLabel.setText(_translate("MainWindow", "Waiter:"))
                self.EnterButton.setText(_translate("MainWindow", "Enter"))

                self.EnterButton.clicked.connect(self.Enter)
                self.ReceiptLabel.setText(_translate("MainWindow", "Receipt:"))


        global mydb
        mydb = mysql.connector.connect(user='root', password='wildfactor', host='127.0.0.1',port=3306,database='items',
        auth_plugin='mysql_native_password')
        global mycursor
        mycursor = mydb.cursor()

        def kafa(self,MainWindow):
                
                kind = "kafa"
                
                sql1 = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                sql4 = ("TRUNCATE TABLE vrsta")
                sql3 = ("INSERT INTO vrsta(kind) VALUES (%s)")
                mycursor.execute(sql3,val)
                mycursor.execute(sql1,val)
                mycursor.execute(sql2,val)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "kafa":

                                quantity += 1
                                
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)




                update_label()

                sql = ("SELECT kolicina FROM kafa ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                

                for i in kol:
                        global a 
                        c = "".join(map(str,i))

                        a = int(c)
                
                print(a)

                
                total = a - 1
                sql = ("DELETE  FROM kafa WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)

                sql = ("INSERT INTO kafa (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                
                sql = ("SELECT kolicina FROM kafa ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return
                

        def caj(self,MainWindow):
                
                global kind
                kind = "caj"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)

                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "caj":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()

                sql = ("SELECT kolicina FROM caj ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))

                        a = int(c)


                total = a -1  
                
                sql = ("DELETE  FROM caj WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO caj (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM caj ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return

        def kapucino(self,MainWindow):
                
                global kind 
                kind = "kapucino"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "kapucino":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
   
                sql = ("SELECT kolicina FROM kapucino ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))

                        a = int(c)


                total = a -1  
                
                sql = ("DELETE  FROM kapucino WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO kapucino (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM kapucino ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return

        def CocaCola(self,MainWindow):
                global kind 
                kind = "CocaCola"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "CocaCola":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

      
      
                update_label()

                sql = ("SELECT kolicina FROM CocaCola ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))

                        a = int(c)


                total = a -1  
                
                sql = ("DELETE  FROM CocaCola WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO CocaCola (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM CocaCola ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return

        def CappyJagoda(self,MainWindow):
                global kind 
                kind = "Cappy Jagoda"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Cappy Jagoda":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                sql = ("SELECT kolicina FROM CappyJagoda ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))

                        a = int(c)


                total = a -1  
                
                sql = ("DELETE  FROM CappyJagoda WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO CappyJagoda (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM CappyJagoda ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return

        def CappyNarandza(self,MainWindow):
                global kind 
                kind = "Cappy Narandza"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Cappy Narandza":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                sql = ("SELECT kolicina FROM CappyNarandza ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))

                        a = int(c)


                total = a -1  
                
                sql = ("DELETE  FROM CappyNarandza WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO CappyNarandza (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM CappyNarandza ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return
        def CappyJabuka(self,MainWindow):
                global kind 
                kind = "Cappy Jabuka"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Cappy Jabuka":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                sql = ("SELECT kolicina FROM CappyJabuka ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))

                        a = int(c)


                total = a -1  
                
                sql = ("DELETE  FROM CappyJabuka WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO CappyJabuka (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM CappyJabuka ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return
                
        def Senzacija(self,MainWindow):
                global kind 
                kind = "Senzacija"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Senzacija":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)

                

                update_label()
                sql = ("SELECT kolicina FROM Senzacija ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))

                        a = int(c)


                total = a - 1
                
                sql = ("DELETE  FROM Senzacija WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO Senzacija (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM Senzacija ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return

        def cockta(self,MainWindow):
                global kind 
                kind = "Cockta"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Cockta":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                sql = ("SELECT kolicina FROM cockta ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))

                        a = int(c)


                total = a -1  
                
                sql = ("DELETE  FROM cockta WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO cockta (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM cockta ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return

        def Lemonade(self,MainWindow):
                global kind 
                kind = "Lemonade"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Lemonade":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                sql = ("SELECT kolicina FROM Lemonade ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))

                        a = int(c)


                total = a -1  
                
                sql = ("DELETE  FROM Lemonade WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO Lemonade (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM Lemonade ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return

        def CappyBreskva(self,MainWindow):
                global kind 
                kind = "Cappy Breskva"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Cappy Breskva":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                sql = ("SELECT kolicina FROM CappyBreskva ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))

                        a = int(c)


                total = a -1  
                
                sql = ("DELETE  FROM CappyBreskva WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO CappyBreskva (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM CappyBreskva ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return


                
        def CappyMarelica(self,MainWindow):
                global kind 
                kind = "Cappy Marelica"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Cappy Marelica":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                sql = ("SELECT kolicina FROM CappyMarelica ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))
                        a = int(c)
                total = a -1  
                
                sql = ("DELETE  FROM CappyMarelica WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO CappyMarelica (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM CappyMarelica ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return
                
        def JanaIceTea(self,MainWindow):
                global kind 
                kind = "Janna Ice Tea"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Jana Ice Tea":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                sql = ("SELECT kolicina FROM JanaIceTea ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))

                        a = int(c)
                total = a -1  
                
                sql = ("DELETE  FROM JanaIceTea WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO JanaIceTea (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM JanaIceTea ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return
                
        def JanaNarandza(self,MainWindow):
                global kind 
                kind = "Jana Narandza"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Jana Narandza":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                sql = ("SELECT kolicina FROM JanaNarandza ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
        
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))
                        a = int(c)
                total = a -1  
                
                sql = ("DELETE  FROM JanaNarandza WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO JanaNarandza (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM JanaNarandza ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return

        def JanaLimun(self,MainWindow):
                global kind 
                kind = "Jana Limun"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Jana Limun":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                sql = ("SELECT kolicina FROM JanaLimun ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))
                        a = int(c)
                total = a -1  
                
                sql = ("DELETE  FROM JanaLimun WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO JanaLimun (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM JanaLimun ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return

        def RedBull(self,MainWindow):
                global kind 
                kind = "Red Bull"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Red Bull":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                sql = ("SELECT kolicina FROM RedBull ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))
                        a = int(c)
                total = a -1  
                
                sql = ("DELETE  FROM RedBull WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO RedBull (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM RedBull ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return





        def Somersby(self,MainWindow):
                global kind 
                kind = "Somersby"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Somersby":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                sql = ("SELECT kolicina FROM Somersby ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))
                        a = int(c)
                total = a -1  
                
                sql = ("DELETE  FROM Somersby WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO Somersby (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM Somersby ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return


        def Pizza(self,MainWindow):
                global kind 
                kind = "pizza"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Pizza":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                sql = ("SELECT kolicina FROM pizza")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))
                        a = int(c)
                total = a + 1  
                
                sql = ("DELETE  FROM pizza WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO pizza (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM pizza ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return

        def Doner(self,MainWindow):
                global kind 
                kind = "Doner"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Doner":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                sql = ("SELECT kolicina FROM Doner ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))
                        a = int(c)
                total = a + 1  
                
                sql = ("DELETE  FROM Doner WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO Doner (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM Doner ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return
                

                
        def karlovacko(self,MainWindow):
                global kind 
                kind = "Karlovacko"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Karlovacko":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                sql = ("SELECT kolicina FROM karlovacko ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))
                        a = int(c)
                total = a -1  
                
                sql = ("DELETE  FROM karlovacko WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO karlovacko (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM karlovacko ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return
                
        def Palacinci(self,MainWindow):
                global kind 
                kind = "Palacinci"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Palacinci":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                
                sql = ("SELECT kolicina FROM Palacinci ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))
                        a = int(c)
                total = a + 1  
                
                sql = ("DELETE  FROM Palacinci WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO Palacinci (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM Palacinci ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return
                

        def radler(self,MainWindow):
                global kind 
                kind = "Radler"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Radler":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                sql = ("SELECT kolicina FROM radler ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))
                        a = int(c)
                total = a -1  
                
                sql = ("DELETE  FROM radler WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO radler (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM radler ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return
                

                
        
        def bavaria(self,MainWindow):
                global kind 
                kind = "Bavaria"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Bavaria":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                sql = ("SELECT kolicina FROM bavaria ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))
                        a = int(c)
                total = a -1  
                
                sql = ("DELETE  FROM bavaria WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO bavaria (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM bavaria ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return
                
        def paulaner(self,MainWindow):
                global kind 
                kind = "Paulaner"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Paulaner":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                sql = ("SELECT kolicina FROM paulaner ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))
                        a = int(c)
                total = a -1  
                
                sql = ("DELETE  FROM paulaner WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO paulaner (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM paulaner ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return
                
        def tuborg(self,MainWindow):
                global kind 
                kind = "Tuborg"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Tuborg":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                sql = ("SELECT kolicina FROM tuborg ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))
                        a = int(c)
                total = a -1  
                
                sql = ("DELETE  FROM tuborg WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO tuborg (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM tuborg ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return   
                
        def vino(self,MainWindow):
                global kind 
                kind = "Vino"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Vino":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                sql = ("SELECT kolicina FROM vino ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))
                        a = int(c)
                total = a -1  
                
                sql = ("DELETE  FROM vino WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO vino (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM vino ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return
                
        def cedevita(self,MainWindow):

                global kind 
                kind = "cedevita"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "cedevita":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                sql = ("SELECT kolicina FROM cedevita ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))

                        a = int(c)


                total = a -1  
                
                sql = ("DELETE  FROM cedevita WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO cedevita (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM cedevita ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return


        def Hamburger(self,MainWindow):
                global kind 
                kind = "Hamburger"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "hamburger":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()

                sql = ("SELECT kolicina FROM Hamburger ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))

                        a = int(c)


                total = a + 1  
                
                sql = ("DELETE  FROM Hamburger WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO Hamburger (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM Hamburger ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                
                return

        def Salata(self,MainWindow):
                global kind 
                kind = "Salata"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Salata":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()

                sql = ("SELECT kolicina FROM Salata ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))

                        a = int(c)


                total = a + 1  
                
                sql = ("DELETE  FROM Salata WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO Salata (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM Salata ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return

        def Pasta(self,MainWindow):
                global kind 
                kind = "Pasta"
                sql = ("INSERT INTO printanje (Receipt) VALUES (%s)")
                val = (kind,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql2 = ("INSERT INTO kolicina (Quantity) VALUES (%s)")
                val = (kind,)
                val2 = (kind,)
                
                mycursor.execute(sql,val)
                mycursor.execute(sql2,val2)
                sql = ("SELECT Quantity FROM kolicina ")
                mycursor.execute(sql)
                
                Quantity = mycursor.fetchall()

                global quantity
                quantity = 0 

                for i in Quantity:
                        print(i)
                        i = ','.join(str(o) for o in i)
                        i = i.replace("(","")
                        i = i.replace(")","")
                        i = i.replace(",","")
                        i = i.replace("'","")
                        i = i.replace("[","")
                        i = i.replace("]","")
                        if i == "Pasta":
                                quantity += 1
                                print(quantity)
                        else:
                                sql = ("TRUNCATE TABLE kolicina")
                                mycursor.execute(sql)


                

                update_label()
                sql = ("SELECT kolicina FROM Pasta ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))
                        a = int(c)
                total = a + 1  
                
                sql = ("DELETE  FROM Pasta WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO Pasta (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM Pasta ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return

        def Enter(self,MainWindow):
                sql1 = ("TRUNCATE TABLE printanje")
                sql2 = ("TRUNCATE TABLE kolicina")
                sql3 = ("TRUNCATE TABLE privermena")
                mycursor.execute(sql1)
                mycursor.execute(sql2)
                mycursor.execute(sql3)
                app.exit()
                return skener()

                
                
if __name__ == "__main__":
    skener()