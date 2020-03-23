from MainWindow1 import *
import sys
import os
from PyQt5 import QtWidgets
sys.path.insert(0,'..')
sys.path.insert(0,'../lib')

def file_open(ui):
		name = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File')
		if(len(name[0]) == 0):
			return
		code_file = open(name[0],'r')
		with code_file:
			text = code_file.read()
			ui.codeEditor.clear()
			ui.codeEditor.appendPlainText(text)

def file_save(ui):
	file = open("../lib/Files/assemblyCode.asm",'w+')
	text = ui.codeEditor.toPlainText()
	file.write(text)
	file.close()


def onTabChange(ui,i):
	if(i == 1):
		ui.file_save()
		mydir = os.getcwd()
		mydir_tmp = "../lib/"
		mydir_new = os.chdir(mydir_tmp)
		exec(open("controller.py").read())
		mydir = os.chdir(mydir)
		ui.showProcessedCode()
		
		
def showProcessedCode(self):
	ori = open("../lib/Files/assemblyCodeFinal.asm")
	mac = open("../lib/Files/machine_code.mc")
	
	ori = ori.readlines()
	mac = mac.readlines()
	self.codeTable.setRowCount(len(ori)+1)
	
	for ind in range(len(ori)):
		print(ind)
		item = self.codeTable.verticalHeaderItem(ind)
		item = QtWidgets.QTableWidgetItem()
		self.codeTable.setItem(ind, 0, item)
		item = QtWidgets.QTableWidgetItem()
		self.codeTable.setItem(ind, 1, item)
		item = QtWidgets.QTableWidgetItem()
		self.codeTable.setItem(ind, 2, item)
		item.setText(self.translate("MainWindow", "New Row"))
		item = self.codeTable.item(ind, 0)
		item.setText(self.translate("MainWindow", mac[ind]))
		item = self.codeTable.item(ind, 1)
		item.setText(self.translate("MainWindow", ori[ind]))
		item = self.codeTable.item(ind, 2)
		item.setText(self.translate("MainWindow", ori[ind]))


if __name__=='__main__':
	import sys
	app = QtWidgets.QApplication([])
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
