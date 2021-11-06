# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'x.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(368, 533)
        Form.setMinimumSize(QtCore.QSize(368, 533))
        Form.setMaximumSize(QtCore.QSize(368, 533))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("\n"
"QWidget {\n"
"    \n"
"    background-color: rgb(34, 34, 34);\n"
"}\n"
"QTextEdit {\n"
"    background-color:rgb(42, 42, 42);\n"
"    \n"
"    color: rgb(47, 102, 205);\n"
"}\n"
"QPushButton{\n"
"border-color: transparent;\n"
"background-color: #444;\n"
"color: #fff;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 6px;\n"
"font-size: 12px;\n"
"padding: 2px;\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"    border-bottom-color: rgb(115, 115, 115);\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(107, 107, 107, 255), stop:1 rgba(157, 157, 157, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(62, 62, 62, 255), stop:1 rgba(22, 22, 22, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-bottom-color: rgb(58, 58, 58);\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-bottom-color: rgb(58, 58, 58);\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: rgb(0, 0, 0);\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(57, 57, 57, 255), stop:1 rgba(77, 77, 77, 255));\n"
"}\n"
"QLineEdit {\n"
"    border-width: 1px; border-radius: 4px;\n"
"    \n"
"    border-color: rgb(136, 138, 133);\n"
"    border-style: inset;\n"
"    padding: 0 8px;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(42, 42, 42);\n"
"    selection-background-color: rgb(187, 187, 187);\n"
"    selection-color: rgb(60, 63, 65);\n"
"}\n"
"QLabel {\n"
"    \n"
"    color: rgb(238, 238, 236);\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color:rgb(77,77,77);\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));\n"
"    border-radius: 5px;\n"
"}\n"
"QMenuBar {\n"
"    background:rgb(82, 82, 82);\n"
"}\n"
"QMenuBar::item {\n"
"    color:rgb(223,219,210);\n"
"    spacing: 3px;\n"
"    padding: 1px 4px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background:rgb(115, 115, 115);\n"
"}\n"
"QMenu::item:selected {\n"
"    color:rgb(255,255,255);\n"
"    border-width:2px;\n"
"    border-style:solid;\n"
"    padding-left:18px;\n"
"    padding-right:8px;\n"
"    padding-top:2px;\n"
"    padding-bottom:3px;\n"
"    background:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-bottom-color: rgb(58, 58, 58);\n"
"    border-bottom-width: 1px;\n"
"}\n"
"QMenu::item {\n"
"    color:rgb(223,219,210);\n"
"    background-color:rgb(78,78,78);\n"
"    padding-left:20px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:10px;\n"
"}\n"
"QMenu{\n"
"    background-color:rgb(78,78,78);\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:rgb(247,246,246);\n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(77,77,77);\n"
"        background-color:rgb(101,101,101);\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"    padding:2px;\n"
"    color:rgb(250,250,250);\n"
"      background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"      border-top-right-radius:4px;\n"
"   border-top-left-radius:4px;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));\n"
"    border-bottom-color: rgb(101,101,101);\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      background-color:rgb(101,101,101);\n"
"      margin-left: 0px;\n"
"      margin-right: 1px;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"        margin-top: 1px;\n"
"        margin-right: 1px;\n"
"}\n"
"QCheckBox {\n"
"    color:rgb(223,219,210);\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: rgb(87, 97, 106);\n"
"    background-color:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 150), stop:1 rgba(93, 103, 113, 150));\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    border-width:1px;\n"
"    border-color: rgb(180,180,180);\n"
"      background-color:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    border-width:1px;\n"
"    border-color: rgb(87, 97, 106);\n"
"      background-color:rgb(255,255,255);\n"
"}\n"
"QStatusBar {\n"
"    color:rgb(240,240,240);\n"
"}\n"
"")
        self.btn1 = QtWidgets.QPushButton(Form)
        self.btn1.setGeometry(QtCore.QRect(20, 231, 151, 31))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(1)
        self.btn1.setFont(font)
        self.btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/normal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn1.setIcon(icon1)
        self.btn1.setIconSize(QtCore.QSize(30, 30))
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(Form)
        self.btn2.setGeometry(QtCore.QRect(200, 231, 151, 31))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(1)
        self.btn2.setFont(font)
        self.btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/revers.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn2.setIcon(icon2)
        self.btn2.setIconSize(QtCore.QSize(15, 15))
        self.btn2.setObjectName("btn2")
        self.tx = QtWidgets.QTextEdit(Form)
        self.tx.setGeometry(QtCore.QRect(10, 280, 351, 191))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        self.tx.setFont(font)
        self.tx.setObjectName("tx")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 10, 291, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/baner.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lb3 = QtWidgets.QLabel(Form)
        self.lb3.setGeometry(QtCore.QRect(10, 470, 341, 71))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(8)
        self.lb3.setFont(font)
        self.lb3.setAutoFillBackground(False)
        self.lb3.setScaledContents(False)
        self.lb3.setAlignment(QtCore.Qt.AlignCenter)
        self.lb3.setWordWrap(True)
        self.lb3.setObjectName("lb3")
        self.tb2 = QtWidgets.QLineEdit(Form)
        self.tb2.setGeometry(QtCore.QRect(70, 181, 281, 31))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(10)
        self.tb2.setFont(font)
        self.tb2.setObjectName("tb2")
        self.lb2 = QtWidgets.QLabel(Form)
        self.lb2.setGeometry(QtCore.QRect(10, 189, 48, 17))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(10)
        self.lb2.setFont(font)
        self.lb2.setObjectName("lb2")
        self.lb1 = QtWidgets.QLabel(Form)
        self.lb1.setGeometry(QtCore.QRect(10, 149, 39, 17))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(10)
        self.lb1.setFont(font)
        self.lb1.setObjectName("lb1")
        self.tb1 = QtWidgets.QLineEdit(Form)
        self.tb1.setGeometry(QtCore.QRect(70, 141, 281, 31))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(10)
        self.tb1.setFont(font)
        self.tb1.setObjectName("tb1")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Regex Reverser"))
        self.btn1.setText(_translate("Form", "Normal Mode"))
        self.btn2.setText(_translate("Form", "Reverse Mode"))
        self.tx.setPlaceholderText(_translate("Form", "Results"))
        self.lb3.setText(_translate("Form", "This tool helps you to reverse any regex and gives you the opposite/allowed Letters,numerics and symbols.          By [ Kadnass-Dz ]   Idea: [ab2pentest]"))
        self.tb2.setPlaceholderText(_translate("Form", "[0-9a-zA-Z/_.]+"))
        self.lb2.setText(_translate("Form", "Pattern"))
        self.lb1.setText(_translate("Form", "String"))
        self.tb1.setText(_translate("Form", "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!\"#$%&\'()*+,-./:;<=>?@[\\\\]^_{|}~ `"))

