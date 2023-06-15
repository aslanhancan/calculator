from PyQt5 import QtWidgets, QtGui
import sys
from hesap_makinesi_main import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)




        self.ui.bir.clicked.connect(self.bir)
        self.ui.iki.clicked.connect(self.iki)
        self.ui.uc.clicked.connect(self.uc)
        self.ui.dort.clicked.connect(self.dort)
        self.ui.bes.clicked.connect(self.bes)
        self.ui.alti.clicked.connect(self.alti)
        self.ui.yedi.clicked.connect(self.yedi)
        self.ui.sekiz.clicked.connect(self.sekiz)
        self.ui.dokuz.clicked.connect(self.dokuz)
        self.ui.sifir.clicked.connect(self.sifir)

        self.ui.toplama.clicked.connect(lambda: self.islem("+"))
        self.ui.cikarma.clicked.connect(lambda: self.islem("-"))
        self.ui.carpma.clicked.connect(lambda: self.islem("*"))
        self.ui.bolme.clicked.connect(lambda: self.islem("/"))
        self.ui.hesapla.clicked.connect(lambda: self.hesapla())
        self.ui.ac.clicked.connect(lambda: self.temizle())
        self.ui.nokta.clicked.connect(lambda: self.islem("."))



    def bir(self):
        num = self.ui.lineEdit.text() +"1"
        self.ui.lineEdit.setText(num)

    def iki(self):
        num = self.ui.lineEdit.text() +"2"
        self.ui.lineEdit.setText(num)

    def uc(self):
        num = self.ui.lineEdit.text() +"3"
        self.ui.lineEdit.setText(num)

    def dort(self):
        num = self.ui.lineEdit.text() +"4"
        self.ui.lineEdit.setText(num)

    def bes(self):
        num = self.ui.lineEdit.text() +"5"
        self.ui.lineEdit.setText(num)

    def alti(self):
        num = self.ui.lineEdit.text() +"6"
        self.ui.lineEdit.setText(num)

    def yedi(self):
        num = self.ui.lineEdit.text() +"7"
        self.ui.lineEdit.setText(num)

    def sekiz(self):
        num = self.ui.lineEdit.text() +"8"
        self.ui.lineEdit.setText(num)

    def dokuz(self):
        num = self.ui.lineEdit.text() +"9"
        self.ui.lineEdit.setText(num)

    def sifir(self):
        num = self.ui.lineEdit.text() +"0"
        self.ui.lineEdit.setText(num)

    def islem(self,isle):
        if isle == "+":
            self.ui.lineEdit.setText(self.ui.lineEdit.text()+"+")
        elif isle == "-":
            self.ui.lineEdit.setText(self.ui.lineEdit.text()+"-")
        elif isle == "*":
            self.ui.lineEdit.setText(self.ui.lineEdit.text()+"*")
        elif isle == "/":
            self.ui.lineEdit.setText(self.ui.lineEdit.text()+"/")
        elif isle == ".":
            self.ui.lineEdit.setText(self.ui.lineEdit.text()+".")

    def hesapla(self):
        sonuc = eval(self.ui.lineEdit.text())
        self.ui.lineEdit.setText(str(sonuc))
    def temizle(self):
        self.ui.lineEdit.setText("")





def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()