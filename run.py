from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication , QWidget
import re
import sys
from func import Ui_Form

class main(QWidget,Ui_Form):
	def __init__(self):
		QWidget.__init__(self)
		self.setupUi(self)
		self.btn2.clicked.connect(self.revers)
		self.btn1.clicked.connect(self.normal)
	def revers(self):
		new = re.sub(pattern = rf"{self.tb2.text()}",repl = "",string = self.tb1.text())
		if new :
			self.tx.setText(str(new))
		else :
			self.tx.setText("Something Error ! Please Check Your Pattern")

	def normal(self):
		matchs = ""
		new = re.findall(rf"{self.tb2.text()}", self.tb1.text())
		if new :
			for alph in new :  
		  		matchs +=alph
			self.tx.setText(str(matchs))	
		else : 
			self.tx.setText("Something Error ! Please Check Your Pattern")
app = QApplication(sys.argv)
window = main()
window.show()
app.exec_()