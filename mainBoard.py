import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
from qt_material import apply_stylesheet


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
        "background-color:rgb(186,85,211);")
                self.KindLabel.setAlignment(QtCore.Qt.AlignCenter)
                self.KindLabel.setObjectName("KindLabel")
                self.horizontalLayout.addWidget(self.KindLabel)
                self.KindLabelUpdate = QtWidgets.QLabel(self.horizontalLayoutWidget)
                self.KindLabelUpdate.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
        "border: solid black;\n"
        "border-width : 1px 0px 1px 0px;\n"
        "background-color:rgb(221,160,221);")
                self.KindLabelUpdate.setAlignment(QtCore.Qt.AlignCenter)
                self.KindLabelUpdate.setObjectName("KindLabelUpdate")
                self.horizontalLayout.addWidget(self.KindLabelUpdate)
                self.QuantityLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
                self.QuantityLabel.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
        "border: solid black;\n"
        "border-width : 1px 0px 1px 1px;\n"
        "background-color:rgb(186,85,211);")
                self.QuantityLabel.setAlignment(QtCore.Qt.AlignCenter)
                self.QuantityLabel.setObjectName("QuantityLabel")
                self.horizontalLayout.addWidget(self.QuantityLabel)
                self.QuantityLabelUpdate = QtWidgets.QLabel(self.horizontalLayoutWidget)
                self.QuantityLabelUpdate.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
        "border: solid black;\n"
        "border-width : 1px 0px 1px 0px;\n"
        "background-color:rgb(221,160,221);")
                self.QuantityLabelUpdate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.QuantityLabelUpdate.setObjectName("QuantityLabelUpdate")
                self.horizontalLayout.addWidget(self.QuantityLabelUpdate)
                self.TotalLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
                self.TotalLabel.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
        "border: solid black;\n"
        "border-width : 1px 0px 1px 1px;\n"
        "background-color:rgb(186,85,211);")
                self.TotalLabel.setAlignment(QtCore.Qt.AlignCenter)
                self.TotalLabel.setObjectName("TotalLabel")
                self.horizontalLayout.addWidget(self.TotalLabel)
                self.TotallabelUpdate = QtWidgets.QLabel(self.horizontalLayoutWidget)
                self.TotallabelUpdate.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
        "border: solid black;\n"
        "border-width : 1px 1px 1px 0px;\n"
        "background-color:rgb(221,160,221);")
                self.TotallabelUpdate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.TotallabelUpdate.setObjectName("label")
                self.horizontalLayout.addWidget(self.TotallabelUpdate)
                self.kafaButton = QtWidgets.QPushButton(self.centralwidget)
                self.kafaButton.setGeometry(QtCore.QRect(20, 140, 181, 91))
                self.kafaButton.setObjectName("kafaButton")
                self.kafaButton.clicked.connect(self.kafa)
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
                self.label_7 = QtWidgets.QLabel(self.centralwidget)
                self.label_7.setGeometry(QtCore.QRect(1010, 380, 201, 81))
                self.label_7.setStyleSheet("background-color:grey;\n"
        "font: 16pt \"MS Shell Dlg 2\";\n"
        "border: solid black;\n"
        "border-width : 1px 1px 1px 1px;\n"
        "background-color:rgb(221,160,221);\n"
        "border-radius:10px;")
                self.label_7.setAlignment(QtCore.Qt.AlignCenter)
                self.label_7.setObjectName("label_7")
                self.EnterButton = QtWidgets.QPushButton(self.centralwidget)
                self.EnterButton.setGeometry(QtCore.QRect(1000, 490, 221, 241))

                self.EnterButton.setObjectName("EnterButton")
                self.label_8 = QtWidgets.QLabel(self.centralwidget)
                self.label_8.setGeometry(QtCore.QRect(1014, 150, 191, 201))
                self.label_8.setStyleSheet("background-color:grey;\n"
        "border: solid black;\n"
        "border-width : 1px 1px 1px 1px;\n"
        "background-color:rgb(221,160,221);\n"
        "border-radius:10px;")
                self.label_8.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
                self.label_8.setObjectName("label_8")
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
                self.KindLabel.setText(_translate("MainWindow", "kind"))
                self.KindLabelUpdate.setText(_translate("MainWindow", ""))
                self.QuantityLabel.setText(_translate("MainWindow", "quantity"))
                self.QuantityLabelUpdate.setText(_translate("MainWindow", ""))
                self.TotalLabel.setText(_translate("MainWindow", "total"))
                self.TotallabelUpdate.setText(_translate("MainWindow", "TextLabel"))
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
                self.label_7.setText(_translate("MainWindow", "waiter"))
                self.EnterButton.setText(_translate("MainWindow", "Enter"))

                self.EnterButton.clicked.connect(self.Enter)
                self.label_8.setText(_translate("MainWindow", "TextLabel"))


        global mydb
        mydb = mysql.connector.connect(user='root', password='wildfactor', host='127.0.0.1',port=3306,database='items',
        auth_plugin='mysql_native_password')
        global mycursor
        mycursor = mydb.cursor()
        """
        kahva = 1
        

        
        def test(self,MainWindow):
                global kahva
                print("radi")
                kahva +=1
                cijena = kahva *1.5
                new_text = (f"kafa{kahva},{cijena}KM")#inserting into a label refresh rate 1 sec 
                ui.label_8.setText(new_text)
                return
        
        timer = QtCore.QTimer()        
        timer.start(100)  
        timer.timeout.connect(test)
        """
        def kafa(self,MainWindow):

                
                sql = ("SELECT kolicina FROM kafa ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))

                        a = int(c)


                total = a -1  
                
                sql = ("DELETE  FROM kafa WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO kafa (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM kafa ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return
        def caj(self,MainWindow):

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

                sql = ("SELECT kolicina FROM Pizza(): ")
                mycursor.execute(sql)
                kol = mycursor.fetchall()
                
                mydb.commit
                for i in kol:
                        global a 
                        c = "".join(map(str,i))
                        a = int(c)
                total = a + 1  
                
                sql = ("DELETE  FROM Pizza(): WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO Pizza(): (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM Pizza(): ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                mydb.commit()
                return

        def Doner(self,MainWindow):
                
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
                app.exit()
if __name__ == "__main__":
        import sys
        extra = {
                
                # Button colors
                'danger': '#dc3545', 
                'warning': '#ffc107',
                'success': '#17a2b8',

                # Font
                'font-family': 'Viaoda Libre',
        }           
        app = QtWidgets.QApplication(sys.argv)
        apply_stylesheet(app, theme='dark_blue.xml',invert_secondary=False,extra=extra)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        app.exec_()
