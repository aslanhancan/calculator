# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hesapMakinesi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(220, 280)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../python/PYQT5/hsp/IMG-20180825-WA0003.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bir = QtWidgets.QPushButton(self.centralwidget)
        self.bir.setGeometry(QtCore.QRect(0, 50, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bir.setFont(font)
        self.bir.setObjectName("bir")
        self.iki = QtWidgets.QPushButton(self.centralwidget)
        self.iki.setGeometry(QtCore.QRect(60, 50, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.iki.setFont(font)
        self.iki.setObjectName("iki")
        self.uc = QtWidgets.QPushButton(self.centralwidget)
        self.uc.setGeometry(QtCore.QRect(120, 50, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.uc.setFont(font)
        self.uc.setObjectName("uc")
        self.bes = QtWidgets.QPushButton(self.centralwidget)
        self.bes.setGeometry(QtCore.QRect(60, 110, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bes.setFont(font)
        self.bes.setObjectName("bes")
        self.dort = QtWidgets.QPushButton(self.centralwidget)
        self.dort.setGeometry(QtCore.QRect(0, 110, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dort.setFont(font)
        self.dort.setObjectName("dort")
        self.alti = QtWidgets.QPushButton(self.centralwidget)
        self.alti.setGeometry(QtCore.QRect(120, 110, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.alti.setFont(font)
        self.alti.setObjectName("alti")
        self.yedi = QtWidgets.QPushButton(self.centralwidget)
        self.yedi.setGeometry(QtCore.QRect(0, 170, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.yedi.setFont(font)
        self.yedi.setObjectName("yedi")
        self.sekiz = QtWidgets.QPushButton(self.centralwidget)
        self.sekiz.setGeometry(QtCore.QRect(60, 170, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sekiz.setFont(font)
        self.sekiz.setObjectName("sekiz")
        self.dokuz = QtWidgets.QPushButton(self.centralwidget)
        self.dokuz.setGeometry(QtCore.QRect(120, 170, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dokuz.setFont(font)
        self.dokuz.setObjectName("dokuz")
        self.sifir = QtWidgets.QPushButton(self.centralwidget)
        self.sifir.setGeometry(QtCore.QRect(60, 230, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sifir.setFont(font)
        self.sifir.setObjectName("sifir")
        self.toplama = QtWidgets.QPushButton(self.centralwidget)
        self.toplama.setGeometry(QtCore.QRect(180, 170, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.toplama.setFont(font)
        self.toplama.setObjectName("toplama")
        self.cikarma = QtWidgets.QPushButton(self.centralwidget)
        self.cikarma.setGeometry(QtCore.QRect(180, 130, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cikarma.setFont(font)
        self.cikarma.setObjectName("cikarma")
        self.carpma = QtWidgets.QPushButton(self.centralwidget)
        self.carpma.setGeometry(QtCore.QRect(180, 90, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.carpma.setFont(font)
        self.carpma.setObjectName("carpma")
        self.bolme = QtWidgets.QPushButton(self.centralwidget)
        self.bolme.setGeometry(QtCore.QRect(180, 50, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.bolme.setFont(font)
        self.bolme.setObjectName("bolme")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 220, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(36)
        self.lineEdit.setFont(font)
        self.lineEdit.setMouseTracking(True)
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.hesapla = QtWidgets.QPushButton(self.centralwidget)
        self.hesapla.setGeometry(QtCore.QRect(180, 210, 41, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.hesapla.setFont(font)
        self.hesapla.setIconSize(QtCore.QSize(16, 16))
        self.hesapla.setAutoRepeat(False)
        self.hesapla.setAutoDefault(False)
        self.hesapla.setDefault(False)
        self.hesapla.setObjectName("hesapla")
        self.ac = QtWidgets.QPushButton(self.centralwidget)
        self.ac.setGeometry(QtCore.QRect(0, 230, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ac.setFont(font)
        self.ac.setObjectName("ac")
        self.nokta = QtWidgets.QPushButton(self.centralwidget)
        self.nokta.setGeometry(QtCore.QRect(120, 230, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.nokta.setFont(font)
        self.nokta.setObjectName("nokta")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bir.setText(_translate("MainWindow", "1"))
        self.iki.setText(_translate("MainWindow", "2"))
        self.uc.setText(_translate("MainWindow", "3"))
        self.bes.setText(_translate("MainWindow", "5"))
        self.dort.setText(_translate("MainWindow", "4"))
        self.alti.setText(_translate("MainWindow", "6"))
        self.yedi.setText(_translate("MainWindow", "7"))
        self.sekiz.setText(_translate("MainWindow", "8"))
        self.dokuz.setText(_translate("MainWindow", "9"))
        self.sifir.setText(_translate("MainWindow", "0"))
        self.toplama.setText(_translate("MainWindow", "+"))
        self.cikarma.setText(_translate("MainWindow", "-"))
        self.carpma.setText(_translate("MainWindow", "*"))
        self.bolme.setText(_translate("MainWindow", "/"))
        self.hesapla.setText(_translate("MainWindow", "="))
        self.ac.setText(_translate("MainWindow", "AC"))
        self.nokta.setText(_translate("MainWindow", "."))
