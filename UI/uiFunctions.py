#from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.insert(0,'..')
sys.path.insert(0,'../lib')

from separate import text_data_seperator
from file_preprocess import initParser


base = "../lib/"
data_file = base + "data_file.txt"
text_file = base + "text_file.txt"
code_file = base + "code_file.txt"
lib = base


def file_open(self):
	name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
	file = open(name,'r')

	self.editor()

	with file:
		text = file.read()
		self.textEdit.setText(text)


def file_save(self):
	#name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
	file = open(code_file,'w+')
	text = self.textEdit.toPlainText()
	file.write(text)
	file.close()

def file_process(self):
	text_data_seperator(code_file,data_file,text_file)

	text_parser = initParser(text_file)
	text_list_with_labels = text_parser.preprocess_file()
	text_parser.write_to_file(text_file,text_list_with_labels)
	label_dict,text_without_label_list = text_parser.generate_labels_and_list(text_file)
	text_parser.write_to_file(text_file,text_without_label_list)
	print(label_dict)

	data_parser = initParser(data_file)
	data_list_with_labels = data_parser.preprocess_file()
	data_parser.write_to_file(data_file,data_list_with_labels)


file_process(1)

	





