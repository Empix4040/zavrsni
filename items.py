import mysql.connector
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from qt_material import apply_stylesheet

class Ui_Items(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1575, 400)
        MainWindow.setMinimumSize(QtCore.QSize(1230, 700))
        MainWindow.setSizeIncrement(QtCore.QSize(1230, 700))
        MainWindow.setStyleSheet("background+color:rgb(97, 134, 133);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.kafaButton = QtWidgets.QPushButton(self.centralwidget)
        self.kafaButton.setGeometry(QtCore.QRect(10, 80, 181, 91))
        self.kafaButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.kafaButton.setObjectName("kafaButton")
        self.kafaButton.clicked.connect(self.Kafa)
        self.kapucinaButton = QtWidgets.QPushButton(self.centralwidget)
        self.kapucinaButton.setGeometry(QtCore.QRect(10, 380, 181, 91))
        self.kapucinaButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.kapucinaButton.setObjectName("kapucinaButton")
        self.kapucinaButton.clicked.connect(self.Kapucino)
        self.cajButton = QtWidgets.QPushButton(self.centralwidget)
        self.cajButton.setGeometry(QtCore.QRect(10, 180, 181, 91))
        self.cajButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.cajButton.setObjectName("cajButton")
        self.cajButton.clicked.connect(self.Caj)
        self.CocaColaButton = QtWidgets.QPushButton(self.centralwidget)
        self.CocaColaButton.setGeometry(QtCore.QRect(10, 480, 181, 91))
        self.CocaColaButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.CocaColaButton.setObjectName("CocaColaButton")
        self.CocaColaButton.clicked.connect(self.CocaCola)
        self.senzacijaButton = QtWidgets.QPushButton(self.centralwidget)
        self.senzacijaButton.setGeometry(QtCore.QRect(10, 280, 181, 91))
        self.senzacijaButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.senzacijaButton.setObjectName("senzacijaButton")
        self.senzacijaButton.clicked.connect(self.Senzacija)
        self.CocktaButton = QtWidgets.QPushButton(self.centralwidget)
        self.CocktaButton.setGeometry(QtCore.QRect(10, 580, 181, 91))
        self.CocktaButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.CocktaButton.setObjectName("CocktaButton")
        self.CocktaButton.clicked.connect(self.Cockta)
        self.JagodaButton = QtWidgets.QPushButton(self.centralwidget)
        self.JagodaButton.setGeometry(QtCore.QRect(330, 280, 181, 91))
        self.JagodaButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.JagodaButton.setObjectName("JagodaButton")
        self.JagodaButton.clicked.connect(self.CappyJagoda)
        self.LemonadeButton = QtWidgets.QPushButton(self.centralwidget)
        self.LemonadeButton.setGeometry(QtCore.QRect(330, 580, 181, 91))
        self.LemonadeButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.LemonadeButton.setObjectName("LemonadeButton")
        self.LemonadeButton.clicked.connect(self.Lemonade)
        self.NarandzaButton = QtWidgets.QPushButton(self.centralwidget)
        self.NarandzaButton.setGeometry(QtCore.QRect(330, 380, 181, 91))
        self.NarandzaButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.NarandzaButton.setObjectName("NarandzaButton")
        self.NarandzaButton.clicked.connect(self.CappyNarandza)
        self.BreskvaButton = QtWidgets.QPushButton(self.centralwidget)
        self.BreskvaButton.setGeometry(QtCore.QRect(330, 80, 181, 91))
        self.BreskvaButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.BreskvaButton.setObjectName("BreskvaButton")
        self.BreskvaButton.clicked.connect(self.CappyBreskva)
        self.MarelicaButton = QtWidgets.QPushButton(self.centralwidget)
        self.MarelicaButton.setGeometry(QtCore.QRect(330, 480, 181, 91))
        self.MarelicaButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.MarelicaButton.setObjectName("MarelicaButton")
        self.MarelicaButton.clicked.connect(self.CappyMarelica)
        self.JabukaButton = QtWidgets.QPushButton(self.centralwidget)
        self.JabukaButton.setGeometry(QtCore.QRect(330, 180, 181, 91))
        self.JabukaButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.JabukaButton.setObjectName("JabukaButton")
        self.JabukaButton.clicked.connect(self.CappyJabuka)
        self.KarlovackoButton = QtWidgets.QPushButton(self.centralwidget)
        self.KarlovackoButton.setGeometry(QtCore.QRect(650, 280, 181, 91))
        self.KarlovackoButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.KarlovackoButton.setObjectName("KarlovackoButton")
        self.KarlovackoButton.clicked.connect(self.Karlovacko)
        self.PaulanerButton = QtWidgets.QPushButton(self.centralwidget)
        self.PaulanerButton.setGeometry(QtCore.QRect(650, 580, 181, 91))
        self.PaulanerButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.PaulanerButton.setObjectName("PaulanerButton")
        self.PaulanerButton.clicked.connect(self.Paulaner)
        self.BavariaButton = QtWidgets.QPushButton(self.centralwidget)
        self.BavariaButton.setGeometry(QtCore.QRect(650, 380, 181, 91))
        self.BavariaButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.BavariaButton.setObjectName("BavariaButton")
        self.BavariaButton.clicked.connect(self.Bavaria)
        self.SomersbyButton = QtWidgets.QPushButton(self.centralwidget)
        self.SomersbyButton.setGeometry(QtCore.QRect(650, 80, 181, 91))
        self.SomersbyButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.SomersbyButton.setObjectName("SomersbyButton")
        self.SomersbyButton.clicked.connect(self.Somersby)
        self.TuborgButton = QtWidgets.QPushButton(self.centralwidget)
        self.TuborgButton.setGeometry(QtCore.QRect(650, 480, 181, 91))
        self.TuborgButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.TuborgButton.setObjectName("TuborgButton")
        self.TuborgButton.clicked.connect(self.Tuborg)
        self.RadlerButton = QtWidgets.QPushButton(self.centralwidget)
        self.RadlerButton.setGeometry(QtCore.QRect(650, 180, 181, 91))
        self.RadlerButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.RadlerButton.setObjectName("RadlerButton")
        self.RadlerButton.clicked.connect(self.Radler)
        self.JanaNarandzaButton = QtWidgets.QPushButton(self.centralwidget)
        self.JanaNarandzaButton.setGeometry(QtCore.QRect(960, 280, 181, 91))
        self.JanaNarandzaButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.JanaNarandzaButton.setObjectName("JanaNarandzaButton")
        self.JanaNarandzaButton.clicked.connect(self.JanaNarandza)
        self.RedBullButton = QtWidgets.QPushButton(self.centralwidget)
        self.RedBullButton.setGeometry(QtCore.QRect(960, 580, 181, 91))
        self.RedBullButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.RedBullButton.setObjectName("RedBullButton")
        self.RedBullButton.clicked.connect(self.RedBull)
        self.JanaLimunButton = QtWidgets.QPushButton(self.centralwidget)
        self.JanaLimunButton.setGeometry(QtCore.QRect(960, 380, 181, 91))
        self.JanaLimunButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.JanaLimunButton.setObjectName("JanaLimunButton")
        self.JanaLimunButton.clicked.connect(self.JanaLimun)
        self.VinoButton = QtWidgets.QPushButton(self.centralwidget)
        self.VinoButton.setGeometry(QtCore.QRect(960, 80, 181, 91))
        self.VinoButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.VinoButton.setObjectName("VinoButton")
        self.VinoButton.clicked.connect(self.Vino)
        self.JanaIceTeaButton = QtWidgets.QPushButton(self.centralwidget)
        self.JanaIceTeaButton.setGeometry(QtCore.QRect(960, 480, 181, 91))
        self.JanaIceTeaButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.JanaIceTeaButton.setObjectName("JanaIceTeaButton")
        self.JanaIceTeaButton.clicked.connect(self.JanaIceTea)
        self.CedevitaButton = QtWidgets.QPushButton(self.centralwidget)
        self.CedevitaButton.setGeometry(QtCore.QRect(960, 180, 181, 91))
        self.CedevitaButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.CedevitaButton.setObjectName("CedevitaButton")
        self.CedevitaButton.clicked.connect(self.Cedevita)
        self.HamburgerButton = QtWidgets.QPushButton(self.centralwidget)
        self.HamburgerButton.setGeometry(QtCore.QRect(1260, 280, 181, 91))
        self.HamburgerButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.HamburgerButton.setObjectName("HamburgerButton")
        self.HamburgerButton.clicked.connect(self.Hamburger)
        self.SalataButton = QtWidgets.QPushButton(self.centralwidget)
        self.SalataButton.setGeometry(QtCore.QRect(1260, 580, 181, 91))
        self.SalataButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.SalataButton.setObjectName("SalataButton")
        self.SalataButton.clicked.connect(self.Salata)
        self.DonerButton = QtWidgets.QPushButton(self.centralwidget)
        self.DonerButton.setGeometry(QtCore.QRect(1260, 380, 181, 91))
        self.DonerButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.DonerButton.setObjectName("DonerButton")
        self.DonerButton.clicked.connect(self.Doner)
        self.PizzaButton = QtWidgets.QPushButton(self.centralwidget)
        self.PizzaButton.setGeometry(QtCore.QRect(1260, 80, 181,91))
        self.PizzaButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.PizzaButton.setObjectName("PizzaButton")
        self.PizzaButton.clicked.connect(self.Pizza)
        self.PastaButton = QtWidgets.QPushButton(self.centralwidget)
        self.PastaButton.setGeometry(QtCore.QRect(1260, 480, 181, 91))
        self.PastaButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.PastaButton.setObjectName("PastaButton")
        self.PastaButton.clicked.connect(self.Pasta)
        self.PalacinciButton = QtWidgets.QPushButton(self.centralwidget)
        self.PalacinciButton.setGeometry(QtCore.QRect(1260, 180, 181, 91))
        self.PalacinciButton.setStyleSheet("QPushButton{background+color:rgb(128, 206, 214);}\n"
"QPushButton{box+shadow: 5px 10px;}\n"
"QPushButton{border+radius:10px;}\n"
"QPushButton:hover:!pressed { background+color:rgb(170, 170, 255); }\n"
"")
        self.PalacinciButton.setObjectName("PalacinciButton")
        self.PalacinciButton.clicked.connect(self.Palacinci)
        self.CappyBreskvaSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.CappyBreskvaSpinBox.setGeometry(QtCore.QRect(520, 78, 101, 40))
        self.CappyBreskvaSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.CappyBreskvaSpinBox.setObjectName("spinBox")
        
        self.CappyJabukaSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.CappyJabukaSpinBox.setGeometry(QtCore.QRect(520, 178, 101,40))
        self.CappyJabukaSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.CappyJabukaSpinBox.setObjectName("CappyJAbukaSpinBox")
        
        self.CappyJagodaSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.CappyJagodaSpinBox.setGeometry(QtCore.QRect(520, 278, 101,40))
        self.CappyJagodaSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.CappyJagodaSpinBox.setObjectName("CappyJagoda")
        
        self.CappyMarelicaSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.CappyMarelicaSpinBox.setGeometry(QtCore.QRect(520, 478, 101,40))
        self.CappyMarelicaSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.CappyMarelicaSpinBox.setObjectName("CappyMarelica")
        
        self.CappyLemonadeSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.CappyLemonadeSpinBox.setGeometry(QtCore.QRect(520, 578, 101,40))
        self.CappyLemonadeSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.CappyLemonadeSpinBox.setObjectName("CappyLemonde")
        
        self.CappyNarandzaSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.CappyNarandzaSpinBox.setGeometry(QtCore.QRect(520, 378, 101,40))
        self.CappyNarandzaSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.CappyNarandzaSpinBox.setObjectName("CappyNarandza")
        
        self.CocktaSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.CocktaSpinBox.setGeometry(QtCore.QRect(200, 578, 101,40))
        self.CocktaSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.CocktaSpinBox.setObjectName("spinBox_7")
        
        self.CajSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.CajSpinBox.setGeometry(QtCore.QRect(200, 178, 101,40))
        self.CajSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.CajSpinBox.setObjectName("Caj")
        
        self.SenzacijaSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.SenzacijaSpinBox.setGeometry(QtCore.QRect(200, 278, 101,40))
        self.SenzacijaSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.SenzacijaSpinBox.setObjectName("Senzacija")
        
        self.CocaColaSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.CocaColaSpinBox.setGeometry(QtCore.QRect(200, 478, 101,40))
        self.CocaColaSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.CocaColaSpinBox.setObjectName("CocaCola")
        
        self.KapucinoSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.KapucinoSpinBox.setGeometry(QtCore.QRect(200, 378, 101,40))
        self.KapucinoSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.KapucinoSpinBox.setObjectName("KapucinoSpinBox")
        
        self.KafaSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.KafaSpinBox.setGeometry(QtCore.QRect(200, 78, 101,40))
        self.KafaSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.KafaSpinBox.setObjectName("KafaSpinBox")
        
        self.PaulanerSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.PaulanerSpinBox.setGeometry(QtCore.QRect(840, 578, 101,40))
        self.PaulanerSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.PaulanerSpinBox.setObjectName("PaulanerSpinBox")
        
        self.RadlerSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.RadlerSpinBox.setGeometry(QtCore.QRect(840, 178, 101,40))
        self.RadlerSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.RadlerSpinBox.setObjectName("RadlerSpinBox")
        
        self.KarlovackoSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.KarlovackoSpinBox.setGeometry(QtCore.QRect(840, 278, 101,40))
        self.KarlovackoSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.KarlovackoSpinBox.setObjectName("KarlovackoSpinBox")
        
        self.TuborgSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.TuborgSpinBox.setGeometry(QtCore.QRect(840, 478, 101,40))
        self.TuborgSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.TuborgSpinBox.setObjectName("TuborgSpinBox")
        
        self.BavariaSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.BavariaSpinBox.setGeometry(QtCore.QRect(840, 378, 101,40))
        self.BavariaSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.BavariaSpinBox.setObjectName("BavariaSpinBox")
        
        self.SomersbySpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.SomersbySpinBox.setGeometry(QtCore.QRect(840, 78, 101,40))
        self.SomersbySpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.SomersbySpinBox.setObjectName("SomersbySpinBox")
        
        self.RedBullSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.RedBullSpinBox.setGeometry(QtCore.QRect(1150, 578, 101,40))
        self.RedBullSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.RedBullSpinBox.setObjectName("RedBullSpinBox")
        
        self.CedevitaSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.CedevitaSpinBox.setGeometry(QtCore.QRect(1150, 178, 101,40))
        self.CedevitaSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.CedevitaSpinBox.setObjectName("CedevitaSpinBox")
        
        self.JanaNarandzaSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.JanaNarandzaSpinBox.setGeometry(QtCore.QRect(1150, 278, 101,40))
        self.JanaNarandzaSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.JanaNarandzaSpinBox.setObjectName("JanaNarandzaSpinBox")
        
        self.JanaIceTeaSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.JanaIceTeaSpinBox.setGeometry(QtCore.QRect(1150, 478, 101,40))
        self.JanaIceTeaSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.JanaIceTeaSpinBox.setObjectName("JanaIceTeaSpinBox")
        
        self.JanaLimunSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.JanaLimunSpinBox.setGeometry(QtCore.QRect(1150, 378, 101,40))
        self.JanaLimunSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.JanaLimunSpinBox.setObjectName("JanaLimunSpinBox")
        
        self.VinoSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.VinoSpinBox.setGeometry(QtCore.QRect(1150, 78, 101,40))
        self.VinoSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.VinoSpinBox.setObjectName("VinoSpinBox")

        self.SalataSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.SalataSpinBox.setGeometry(QtCore.QRect(1450, 578, 101,40))
        self.SalataSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.SalataSpinBox.setObjectName("SalataSpinBox")
    
        self.PalacinciSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.PalacinciSpinBox.setGeometry(QtCore.QRect(1450, 178, 101,40))
        self.PalacinciSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.PalacinciSpinBox.setObjectName("PalacinciSpinBox")
        
        self.HamburgerSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.HamburgerSpinBox.setGeometry(QtCore.QRect(1450, 278, 101,40))
        self.HamburgerSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.HamburgerSpinBox.setObjectName("HamburgerSpinBox")
        
        self.PastaSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.PastaSpinBox.setGeometry(QtCore.QRect(1450, 478, 101,40))
        self.PastaSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.PastaSpinBox.setObjectName("PastaSpinBox")
        
        self.DonerSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.DonerSpinBox.setGeometry(QtCore.QRect(1450, 378, 101,40))
        self.DonerSpinBox.setStyleSheet("background+color:rgb(255, 255, 255);")
        self.DonerSpinBox.setObjectName("DonerSpinBox")
        
        self.PizzaSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.PizzaSpinBox.setGeometry(QtCore.QRect(1450, 78, 101,40))
        self.PizzaSpinBox.setObjectName("PizzaSpinBox")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1575, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Emir"))
        self.kafaButton.setText(_translate("MainWindow", "kafa"))
        self.kapucinaButton.setText(_translate("MainWindow", "kapucino"))
        self.cajButton.setText(_translate("MainWindow", "caj"))
        self.CocaColaButton.setText(_translate("MainWindow", "Coca Cola"))
        self.senzacijaButton.setText(_translate("MainWindow", "senzacija"))
        self.CocktaButton.setText(_translate("MainWindow", "Cockta"))
        self.JagodaButton.setText(_translate("MainWindow", "Cappy Jagoda"))
        self.LemonadeButton.setText(_translate("MainWindow", "Cappy Lemonade"))
        self.NarandzaButton.setText(_translate("MainWindow", "Cappy Narandža"))
        self.BreskvaButton.setText(_translate("MainWindow", "Cappy Breskva"))
        self.MarelicaButton.setText(_translate("MainWindow", "Cappy Marelica"))
        self.JabukaButton.setText(_translate("MainWindow", "Cappy Jabuka"))
        self.KarlovackoButton.setText(_translate("MainWindow", "Karlovacko"))
        self.PaulanerButton.setText(_translate("MainWindow", "Paulaner"))
        self.BavariaButton.setText(_translate("MainWindow", "Bavaria"))
        self.SomersbyButton.setText(_translate("MainWindow", "Somersby"))
        self.TuborgButton.setText(_translate("MainWindow", "Tuborg"))
        self.RadlerButton.setText(_translate("MainWindow", "Radler"))
        self.JanaNarandzaButton.setText(_translate("MainWindow", "Jana Narandža"))
        self.RedBullButton.setText(_translate("MainWindow", "Red Bull"))
        self.JanaLimunButton.setText(_translate("MainWindow", "Jana Limun"))
        self.VinoButton.setText(_translate("MainWindow", "Vino"))
        self.JanaIceTeaButton.setText(_translate("MainWindow", "Jana Ice Tea"))
        self.CedevitaButton.setText(_translate("MainWindow", "Cedevita"))
        self.HamburgerButton.setText(_translate("MainWindow", "Hamburger"))
        self.SalataButton.setText(_translate("MainWindow", "Salata"))
        self.DonerButton.setText(_translate("MainWindow", "Doner"))
        self.PizzaButton.setText(_translate("MainWindow", "Pizza"))
        self.PastaButton.setText(_translate("MainWindow", "Pasta"))
        self.PalacinciButton.setText(_translate("MainWindow", "Palacinci"))

    global mydb
    mydb = mysql.connector.connect(user='root', password='wildfactor', host='127.0.0.1',port=3306,database='items',
    auth_plugin='mysql_native_password')
    global mycursor
    mycursor = mydb.cursor()
    def test(self,MainWindow):
        print("radi")
    def Kafa(self,MainWindow):
     
            sql = ("SELECT kolicina FROM kafa ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.KafaSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE kafa SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM kafa ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
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
                print(output)
                mydb.commit()
                return
            
    def Caj(self,MainWindow):

            sql = ("SELECT kolicina FROM caj ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.CajSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE caj SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM caj ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
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
                print(output)
                mydb.commit()
                return

    def Kapucino(self,MainWindow):
            
            sql = ("SELECT kolicina FROM kapucino ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.KapucinoSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE kapucino SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM kapucino ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
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
                print(output)
                mydb.commit()
                return

    def CocaCola(self,MainWindow):

            sql = ("SELECT kolicina FROM cocacola ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.CocaColaSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE cocacola SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM cocacola ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
                sql = ("DELETE  FROM cocacola WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO cocacola (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM cocacola ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return

    def CappyJagoda(self,MainWindow):

            sql = ("SELECT kolicina FROM cappyjagoda ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.CappyJagodaSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE cappyjagoda SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM cappyjagoda ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
                sql = ("DELETE  FROM cappyjagoda WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO cappyjagoda (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM cappyjagoda ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
    def CappyLemonde(self,MainWindow):

            sql = ("SELECT kolicina FROM cappylemonade ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.CappyLemonadeSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE cappylemonade SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM cappylemonade ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
                sql = ("DELETE  FROM cappylemonade WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO cappylemonade (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM cappylemonade ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return



    def CappyNarandza(self,MainWindow):
            
            sql = ("SELECT kolicina FROM cappynarandza ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.CappyNarandzaSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE cappynarandza SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM cappynarandza ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
                sql = ("DELETE  FROM cappynarandza WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO cappynarandza (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM cappynarandza ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return

    def CappyJabuka(self,MainWindow):

            sql = ("SELECT kolicina FROM cappyjabuka ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.CappyJabukaSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE cappyjabuka SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM cappyjabuka ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
                sql = ("DELETE  FROM cappyjabuka WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO cappyjabuka (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM cappyjabuka ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            
    def Senzacija(self,MainWindow):
            
            sql = ("SELECT kolicina FROM senzacija ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.SenzacijaSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE senzacija SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM senzacija ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
                sql = ("DELETE  FROM senzacija WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO senzacija (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM senzacija ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return

    def Cockta(self,MainWindow):
            
            sql = ("SELECT kolicina FROM cockta ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.CocktaSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE cockta SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM cockta ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
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
                print(output)
                mydb.commit()
                return
    def Lemonade(self,MainWindow):
            
            sql = ("SELECT kolicina FROM lemonade ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.CappyLemonadeSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE lemonade SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM lemonade ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
                sql = ("DELETE  FROM lemonade WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO lemonade (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM lemonade ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return

    def CappyBreskva(self,MainWindow):
            
            sql = ("SELECT kolicina FROM cappybreskva ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.CappyBreskvaSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE cappybreskva SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM cappybreskva ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
                sql = ("DELETE  FROM cappybreskva WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO cappybreskva (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM cappybreskva ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            
    def CappyMarelica(self,MainWindow):
            
            sql = ("SELECT kolicina FROM cappymarelica ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.CappyMarelicaSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE cappymarelica SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM cappymarelica ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
                sql = ("DELETE  FROM cappymarelica WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO cappymarelica (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM cappymarelica ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            
    def JanaIceTea(self,MainWindow):
            
            sql = ("SELECT kolicina FROM janaicetea ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.JanaIceTeaSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE janaicetea SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM janaicetea ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
                sql = ("DELETE  FROM janaicetea WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO janaicetea (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM janaicetea ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            
    def JanaNarandza(self,MainWindow):
            
            sql = ("SELECT kolicina FROM jananarandza ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.JanaNarandzaSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE jananarandza SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM jananarandza ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
                sql = ("DELETE  FROM jananarandza WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO jananarandza (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM jananarandza ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return

    def JanaLimun(self,MainWindow):
            
            sql = ("SELECT kolicina FROM janalimun ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.JanaLimunSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE janalimun SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM janalimun ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
                sql = ("DELETE  FROM janalimun WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO janalimun (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM janalimun ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return

    def RedBull(self,MainWindow):
            
            sql = ("SELECT kolicina FROM redbull ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.RedBullSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE redbull SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM redbull ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
                sql = ("DELETE  FROM redbull WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO redbull (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM redbull ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return





    def Somersby(self,MainWindow):
            
            sql = ("SELECT kolicina FROM somersby ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.SomersbySpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE somersby SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM somersby ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
                sql = ("DELETE  FROM somersby WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO somersby (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM somersby ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return


    def Pizza(self,MainWindow):

            sql = ("SELECT kolicina FROM pizza ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.PizzaSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE pizza SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM pizza ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
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
                print(output)
                mydb.commit()
                return

    def Doner(self,MainWindow):
            
            sql = ("SELECT kolicina FROM doner ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.DonerSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE doner SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM doner ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
                sql = ("DELETE  FROM doner WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO doner (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM doner ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            

            
    def Karlovacko(self,MainWindow):

            sql = ("SELECT kolicina FROM karlovacko ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.KarlovackoSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE karlovacko SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM karlovacko ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
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
                print(output)
                mydb.commit()
                return
            
    def Palacinci(self,MainWindow):
            
            sql = ("SELECT kolicina FROM palacinci ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.PalacinciSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE palacinci SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM palacinci ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
                sql = ("DELETE  FROM palacinci WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO palacinci (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM palacinci ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            
    def Hamburger(self,MainWindow):
            
            sql = ("SELECT kolicina FROM hamburger ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.HamburgerSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE hamburger SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM hamburger ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
                sql = ("DELETE  FROM hamburger WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO hamburger (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM hamburger ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return

    def Salata(self,MainWindow):
            
            sql = ("SELECT kolicina FROM salata ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.SalataSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE salata SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM salata ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
                sql = ("DELETE  FROM salata WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO salata (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM salata ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return

    def Pasta(self,MainWindow):
            
            sql = ("SELECT kolicina FROM pasta ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.PastaSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE pasta SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM pasta ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
                sql = ("DELETE  FROM pasta WHERE kolicina = %s")
                val = (a,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("INSERT INTO pasta (kolicina) VALUES (%s)")
                val = (total,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM pasta ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
    def Radler(self,MainWindow):

            sql = ("SELECT kolicina FROM radler ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.RadlerSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE radler SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM radler ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
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
                print(output)
                mydb.commit()
                return
            

            

    def Bavaria(self,MainWindow):

            sql = ("SELECT kolicina FROM bavaria ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.BavariaSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE bavaria SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM bavaria ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
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
                print(output)
                mydb.commit()
                return
            
    def Paulaner(self,MainWindow):
            
            sql = ("SELECT kolicina FROM paulaner ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.PaulanerSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE paulaner SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM paulaner ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
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
                print(output)
                mydb.commit()
                return
            
    def Tuborg(self,MainWindow):
            
            sql = ("SELECT kolicina FROM tuborg ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.TuborgSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE tuborg SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM tuborg ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
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
                print(output)
                mydb.commit()
                return
            
    def Vino(self,MainWindow):
            
            sql = ("SELECT kolicina FROM vino ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.VinoSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE vino SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM vino ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
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
                print(output)
                mydb.commit()
                return
    
    def Cedevita(self,MainWindow):
            
            sql = ("SELECT kolicina FROM cedevita ")
            mycursor.execute(sql)
            kol = mycursor.fetchall()
            
            mydb.commit
            for i in kol:
                    c = "".join(map(str,i))

                    a = int(c)

            unos = self.CedevitaSpinBox.value()
            if unos >0:
                print(unos)
                unos = a + unos
                sql = ("UPDATE cedevita SET kolicina = %s WHERE kolicina > 0")
                
                val = (unos,)
                mycursor.execute(sql,val)
                mydb.commit()
                sql = ("SELECT kolicina FROM cedevita ")
                mycursor.execute(sql)

                output = mycursor.fetchall()
                print(output)
                mydb.commit()
                return
            else:
            
                total = a +1
                
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
                print(output)
                mydb.commit()
                return



 
        
if __name__ == "__main__":
        
    import sys
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml',invert_secondary=True)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Items()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

