import sys
import os
sys.path.insert(0,'..')
sys.path.insert(0,'../lib')
sys.path.insert(0,'../lib/Phase2')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.setWindowTitle("SUN - Risc-V Editor & Simulator ")
		MainWindow.resize(1417, 820)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
		MainWindow.setSizePolicy(sizePolicy)
		MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
		MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")
		self.tabs = QtWidgets.QTabWidget(self.centralwidget)
		self.tabs.setTabShape(QtWidgets.QTabWidget.Triangular)
		self.tabs.setObjectName("tabs")
		self.tab = QtWidgets.QWidget()
		self.tab.setObjectName("tab")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
		self.verticalLayout.setObjectName("verticalLayout")
		self.uploadButton = QtWidgets.QPushButton(self.tab)
		self.uploadButton.setMaximumSize(QtCore.QSize(200, 50))
		self.uploadButton.setObjectName("uploadButton")
		self.verticalLayout.addWidget(self.uploadButton)
		self.codeEditor = CodeEditor(self.tab)
		self.codeEditor.setObjectName("codeEditor")
		self.verticalLayout.addWidget(self.codeEditor)

		self.errorBox=QtWidgets.QPlainTextEdit(self.tab)
		self.errorBox.setStyleSheet("color: rgb(255,0,0);")
		self.errorBox.setObjectName("errorBox")
		self.errorBox.setMaximumHeight(150)
		self.verticalLayout.addWidget(self.errorBox)
		self.errorBox.setReadOnly(True)
		self.errorBox.setPlaceholderText("Errors will be displayed here")
		

		self.tabs.addTab(self.tab, "")
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2.setObjectName("tab_2")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_2)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.widget = QtWidgets.QWidget(self.tab_2)
		self.widget.setObjectName("widget")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.horizontalWidget = QtWidgets.QWidget(self.widget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
		self.horizontalWidget.setSizePolicy(sizePolicy)
		self.horizontalWidget.setMinimumSize(QtCore.QSize(20, 50))
		self.horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 75))
		self.horizontalWidget.setObjectName("horizontalWidget")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.runButton = QtWidgets.QPushButton(self.horizontalWidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.runButton.sizePolicy().hasHeightForWidth())
		self.runButton.setSizePolicy(sizePolicy)
		self.runButton.setObjectName("runButton")
		self.horizontalLayout_2.addWidget(self.runButton)
		self.stepButton = QtWidgets.QPushButton(self.horizontalWidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.stepButton.sizePolicy().hasHeightForWidth())
		self.stepButton.setSizePolicy(sizePolicy)
		self.stepButton.setObjectName("stepButton")
		self.horizontalLayout_2.addWidget(self.stepButton)
		self.prevButton = QtWidgets.QPushButton(self.horizontalWidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.prevButton.sizePolicy().hasHeightForWidth())
		self.prevButton.setSizePolicy(sizePolicy)
		self.prevButton.setObjectName("prevButton")
		self.horizontalLayout_2.addWidget(self.prevButton)
		self.resetButton = QtWidgets.QPushButton(self.horizontalWidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.resetButton.sizePolicy().hasHeightForWidth())
		self.resetButton.setSizePolicy(sizePolicy)
		self.resetButton.setObjectName("resetButton")
		self.horizontalLayout_2.addWidget(self.resetButton)
		self.verticalLayout_2.addWidget(self.horizontalWidget)
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.codeTable = QtWidgets.QTableWidget(self.widget)
		self.codeTable.setGridStyle(QtCore.Qt.DashDotLine)
		self.codeTable.setObjectName("codeTable")
		self.codeTable.setColumnCount(4)
		self.codeTable.setRowCount(100)

		item = QtWidgets.QTableWidgetItem()
		item.setTextAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(12)
		item.setFont(font)
		self.codeTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
		self.codeTable.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		item.setTextAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(False)
		font.setWeight(50)
		item.setFont(font)
		self.codeTable.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		item.setTextAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(False)
		font.setWeight(50)
		item.setFont(font)
		self.codeTable.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		item.setTextAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(False)
		font.setWeight(50)
		item.setFont(font)
		self.codeTable.setHorizontalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		self.codeTable.setItem(0, 0, item)
		item = QtWidgets.QTableWidgetItem()
		self.codeTable.setItem(0, 1, item)
		item = QtWidgets.QTableWidgetItem()
		self.codeTable.setItem(0, 2, item)
		item = QtWidgets.QTableWidgetItem()
		self.codeTable.setItem(1, 0, item)
		item = QtWidgets.QTableWidgetItem()
		self.codeTable.setItem(1, 1, item)
		item = QtWidgets.QTableWidgetItem()
		self.codeTable.setItem(1, 2, item)
		self.codeTable.horizontalHeader().setCascadingSectionResizes(True)
		self.codeTable.horizontalHeader().setDefaultSectionSize(200)
		self.codeTable.horizontalHeader().setMinimumSectionSize(100)
		self.codeTable.horizontalHeader().setSortIndicatorShown(False)
		self.codeTable.horizontalHeader().setStretchLastSection(True)
		self.codeTable.verticalHeader().setVisible(False)
		self.codeTable.verticalHeader().setCascadingSectionResizes(True)
		self.codeTable.verticalHeader().setHighlightSections(True)
		self.codeTable.verticalHeader().setStretchLastSection(True)
		self.horizontalLayout_3.addWidget(self.codeTable)
		self.verticalLayout_2.addLayout(self.horizontalLayout_3)
		self.horizontalLayout.addWidget(self.widget)
		self.widget_2 = QtWidgets.QWidget(self.tab_2)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
		self.widget_2.setSizePolicy(sizePolicy)
		self.widget_2.setMinimumSize(QtCore.QSize(550, 0))
		self.widget_2.setMaximumSize(QtCore.QSize(600, 16777215))
		self.widget_2.setObjectName("widget_2")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.splitter = QtWidgets.QSplitter(self.widget_2)
		self.splitter.setOrientation(QtCore.Qt.Horizontal)
		self.splitter.setObjectName("splitter")
		self.label_2 = QtWidgets.QLabel(self.splitter)
		self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.label_2.setObjectName("label_2")
		self.regMemDisplayTypeDrop = QtWidgets.QComboBox(self.splitter)
		self.regMemDisplayTypeDrop.setObjectName("regMemDisplayTypeDrop")
		self.regMemDisplayTypeDrop.addItem("")
		self.regMemDisplayTypeDrop.addItem("")
		self.regMemDisplayTypeDrop.addItem("")
		self.regMemDisplayTypeDrop.addItem("")
		self.verticalLayout_3.addWidget(self.splitter)
		self.regMemTab = QtWidgets.QTabWidget(self.widget_2)
		self.regMemTab.setTabShape(QtWidgets.QTabWidget.Rounded)
		self.regMemTab.setObjectName("regMemTab")
		self.tab_4 = QtWidgets.QWidget()
		self.tab_4.setObjectName("tab_4")
		self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_4)
		self.gridLayout_2.setObjectName("gridLayout_2")
		self.registerTable = QtWidgets.QTableWidget(self.tab_4)
		self.tab_6 = QtWidgets.QWidget()
		self.tab_6.setObjectName("tab_6")
		self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_6)
		self.gridLayout_3.setObjectName("gridLayout_3")
		self.registerTable = QtWidgets.QTableWidget(self.tab_6)
		self.registerTable.setGridStyle(QtCore.Qt.DashLine)
		self.registerTable.setObjectName("registerTable")
		self.registerTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
		self.registerTable.setColumnCount(1)
		self.registerTable.setRowCount(32)


		self.pipeTable = QtWidgets.QTableWidget(self.tab_6)
		self.pipeTable.setGridStyle(QtCore.Qt.DashLine)
		self.pipeTable.setObjectName("pipeTable")
		self.pipeTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
		self.pipeTable.setColumnCount(1)
		self.pipeTable.setRowCount(20)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setVerticalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setVerticalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setVerticalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setVerticalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setVerticalHeaderItem(4, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setVerticalHeaderItem(5, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setVerticalHeaderItem(6, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setVerticalHeaderItem(7, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setVerticalHeaderItem(8, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setVerticalHeaderItem(9, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setVerticalHeaderItem(10, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setVerticalHeaderItem(11, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setVerticalHeaderItem(12, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setVerticalHeaderItem(13, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setVerticalHeaderItem(14, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setVerticalHeaderItem(15, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setVerticalHeaderItem(16, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setVerticalHeaderItem(17, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setVerticalHeaderItem(18, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setVerticalHeaderItem(19, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setVerticalHeaderItem(20, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setItem(0, 0, item)
		item = QtWidgets.QTableWidgetItem()
		self.pipeTable.setItem(1, 0, item)
		self.pipeTable.horizontalHeader().setCascadingSectionResizes(True)
		self.pipeTable.horizontalHeader().setDefaultSectionSize(150)
		self.pipeTable.horizontalHeader().setMinimumSectionSize(80)
		self.pipeTable.horizontalHeader().setStretchLastSection(True)
		self.pipeTable.verticalHeader().setCascadingSectionResizes(False)
		self.pipeTable.verticalHeader().setDefaultSectionSize(37)
		self.pipeTable.verticalHeader().setStretchLastSection(False)



		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(4, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(5, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(6, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(7, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(8, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(9, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(10, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(11, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(12, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(13, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(14, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(15, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(16, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(17, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(18, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(19, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(20, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(21, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(22, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(23, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(24, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(25, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(26, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(27, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(28, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(29, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(30, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setVerticalHeaderItem(31, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setItem(0, 0, item)
		item = QtWidgets.QTableWidgetItem()
		self.registerTable.setItem(1, 0, item)
		self.registerTable.horizontalHeader().setCascadingSectionResizes(True)
		self.registerTable.horizontalHeader().setDefaultSectionSize(150)
		self.registerTable.horizontalHeader().setMinimumSectionSize(80)
		self.registerTable.horizontalHeader().setStretchLastSection(True)
		self.registerTable.verticalHeader().setCascadingSectionResizes(False)
		self.registerTable.verticalHeader().setDefaultSectionSize(37)
		self.registerTable.verticalHeader().setStretchLastSection(False)
		self.gridLayout_2.addWidget(self.registerTable, 0, 0, 1, 1)
		self.gridLayout_3.addWidget(self.pipeTable, 0, 0, 1, 1)
		self.regMemTab.addTab(self.tab_4, "")
		self.tab_5 = QtWidgets.QWidget()
		self.tab_5.setObjectName("tab_5")
		self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_5)
		self.verticalLayout_4.setObjectName("verticalLayout_4")
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.label = QtWidgets.QLabel(self.tab_5)
		self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.label.setObjectName("label")
		self.horizontalLayout_4.addWidget(self.label)
		self.memJumpDropDown = QtWidgets.QComboBox(self.tab_5)
		self.memJumpDropDown.setObjectName("memJumpDropDown")
		self.memJumpDropDown.addItem("")
		self.memJumpDropDown.addItem("")
		self.memJumpDropDown.addItem("")
		self.memJumpDropDown.addItem("")
		self.horizontalLayout_4.addWidget(self.memJumpDropDown)
		self.memUp = QtWidgets.QPushButton(self.tab_5)
		self.memUp.setObjectName("memUp")
		self.horizontalLayout_4.addWidget(self.memUp)
		self.memDown = QtWidgets.QPushButton(self.tab_5)
		self.memDown.setObjectName("memDown")
		self.horizontalLayout_4.addWidget(self.memDown)
		self.verticalLayout_4.addLayout(self.horizontalLayout_4)
		self.memoryTable = QtWidgets.QTableWidget(self.tab_5)
		self.memoryTable.setAlternatingRowColors(True)
		self.memoryTable.setObjectName("memoryTable")
		self.memoryTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
		self.memoryTable.setColumnCount(5)
		self.memoryTable.setRowCount(0)
		item = QtWidgets.QTableWidgetItem()
		self.memoryTable.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.memoryTable.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.memoryTable.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.memoryTable.setHorizontalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		self.memoryTable.setHorizontalHeaderItem(4, item)
		self.memoryTable.horizontalHeader().setCascadingSectionResizes(True)
		self.memoryTable.horizontalHeader().setDefaultSectionSize(100)
		self.memoryTable.horizontalHeader().setStretchLastSection(True)
		self.memoryTable.verticalHeader().setCascadingSectionResizes(True)
		self.verticalLayout_4.addWidget(self.memoryTable)
		self.regMemTab.addTab(self.tab_5, "")


		self.regMemTab.addTab(self.tab_6, "")


		self.verticalLayout_3.addWidget(self.regMemTab)
		self.horizontalLayout.addWidget(self.widget_2)
		self.tabs.addTab(self.tab_2, "")
		self.tab_3 = QtWidgets.QWidget()
		self.tab_3.setObjectName("tab_3")
		self.tabs.addTab(self.tab_3, "")

		#self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_2)
		#self.horizontalLayout.setObjectName("horizontalLayout")

		self.tab_3.layout = QtWidgets.QGridLayout()


		self.temp1 = QtWidgets.QLabel("")
		self.cb1 = QtWidgets.QCheckBox('Enable Pipelining')
		self.cb1.toggle()
		self.cb1.toggled.connect(lambda : self.knobs(self.cb1,0))
		self.cb2 = QtWidgets.QCheckBox('Enable Data Forwarding')
		self.cb2.toggle()
		self.cb2.toggled.connect(lambda : self.knobs(self.cb2,1))

		self.cb3 = QtWidgets.QCheckBox('Enable Printing Register File')
		self.cb3.toggled.connect(lambda : self.knobs(self.cb3,2))
		self.cb4 = QtWidgets.QCheckBox('Enable Printing Pipelining Registers')
		self.cb4.toggled.connect(lambda : self.knobs(self.cb4,3))

		#cb.stateChanged.connect(self.changeTitle) #TODO
		self.pushButton1 = QtWidgets.QPushButton("PyQt5 button")
		self.tab_3.layout.addWidget(self.cb1,1,1)
		self.tab_3.layout.addWidget(self.cb2,2,1)
		self.tab_3.layout.addWidget(self.cb3,3,1)
		self.tab_3.layout.addWidget(self.cb4,4,1)
		self.tab_3.layout.addWidget(self.temp1,5,0)
		self.tab_3.setLayout(self.tab_3.layout)


		self.gridLayout.addWidget(self.tabs, 0, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)





		self.uploadButton.clicked.connect(self.file_open)
		self.tabs.currentChanged.connect(self.onTabChange)
		self.runButton.clicked.connect(self.runCodeClick)
		self.stepButton.clicked.connect(self.stepForward)
		self.resetButton.clicked.connect(self.reset)
		self.prevButton.clicked.connect(self.stepBack)
		# self.regMemDisplayTypeDrop.currentIndexChanged.connect(self.displayTypeChange)
		self.regMemDisplayTypeDrop.activated[str].connect(self.displayTypeChange)
		self.memJumpDropDown.activated[str].connect(self.memoryTypeChange)

		self.retranslateUi(MainWindow)
		self.tabs.setCurrentIndex(0)
		self.regMemTab.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		self.translate = _translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.uploadButton.setText(_translate("MainWindow", "Upload Code"))
		self.tabs.setTabText(self.tabs.indexOf(self.tab), _translate("MainWindow", "Editor"))
		self.runButton.setText(_translate("MainWindow", "Run"))
		self.stepButton.setText(_translate("MainWindow", "Step"))
		self.prevButton.setText(_translate("MainWindow", "Prev"))
		self.resetButton.setText(_translate("MainWindow", "Reset"))

		item = self.codeTable.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "PC"))
		item = self.codeTable.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "Machine Code"))
		item = self.codeTable.horizontalHeaderItem(2)
		item.setText(_translate("MainWindow", "Basic Code"))
		item = self.codeTable.horizontalHeaderItem(3)
		item.setText(_translate("MainWindow", "Original Code"))
		__sortingEnabled = self.codeTable.isSortingEnabled()
		self.codeTable.setSortingEnabled(False)


		self.codeTable.setSortingEnabled(__sortingEnabled)
		self.label_2.setText(_translate("MainWindow", "Display Setting "))
		self.regMemDisplayTypeDrop.setItemText(0, _translate("MainWindow", "Hex"))
		self.regMemDisplayTypeDrop.setItemText(1, _translate("MainWindow", "Decimal"))
		self.regMemDisplayTypeDrop.setItemText(2, _translate("MainWindow", "Unsigned"))
		self.regMemDisplayTypeDrop.setItemText(3, _translate("MainWindow", "Ascii"))


		item = self.pipeTable.verticalHeaderItem(0)
		item.setText(_translate("MainWindow", "Fetch (PC Value)"))
		item = self.pipeTable.verticalHeaderItem(1)
		item.setText(_translate("MainWindow", "Decode (PC Value)"))
		item = self.pipeTable.verticalHeaderItem(2)
		item.setText(_translate("MainWindow", "Execute (PC Value)"))
		item = self.pipeTable.verticalHeaderItem(3)
		item.setText(_translate("MainWindow", "Memory Access (PC Value)"))
		item = self.pipeTable.verticalHeaderItem(4)
		item.setText(_translate("MainWindow", "Writeback (PC Value)"))
		item = self.pipeTable.verticalHeaderItem(5)
		item.setText(_translate("MainWindow", "Total number of cycles"))
		item = self.pipeTable.verticalHeaderItem(6)
		item.setText(_translate("MainWindow", "Total instructions executed"))
		item = self.pipeTable.verticalHeaderItem(7)
		item.setText(_translate("MainWindow", "CPI"))
		item = self.pipeTable.verticalHeaderItem(8)
		item.setText(_translate("MainWindow", "Number of Data-transfer"))
		item = self.pipeTable.verticalHeaderItem(9)
		item.setText(_translate("MainWindow", "ALU instructions executed"))
		item = self.pipeTable.verticalHeaderItem(10)
		item.setText(_translate("MainWindow", "Control instructions executed"))
		item = self.pipeTable.verticalHeaderItem(11)
		item.setText(_translate("MainWindow", "Number of stalls/bubbles"))
		item = self.pipeTable.verticalHeaderItem(12)
		item.setText(_translate("MainWindow", "Number of data hazards"))
		item = self.pipeTable.verticalHeaderItem(13)
		item.setText(_translate("MainWindow", "Number of control hazards"))
		item = self.pipeTable.verticalHeaderItem(14)
		item.setText(_translate("MainWindow", "Number of branch mispredictions"))
		item = self.pipeTable.verticalHeaderItem(15)
		item.setText(_translate("MainWindow", "Number of stalls due to data hazards"))
		item = self.pipeTable.verticalHeaderItem(16)
		item.setText(_translate("MainWindow", "Number of stalls due to control hazards"))



		item = self.pipeTable.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Status / Values"))
		__sortingEnabled = self.pipeTable.isSortingEnabled()
		self.pipeTable.setSortingEnabled(False)
		self.pipeTable.setSortingEnabled(__sortingEnabled)	



		item = self.registerTable.verticalHeaderItem(0)
		item.setText(_translate("MainWindow", "zero(x0)"))
		item = self.registerTable.verticalHeaderItem(1)
		item.setText(_translate("MainWindow", "ra(x1)"))
		item = self.registerTable.verticalHeaderItem(2)
		item.setText(_translate("MainWindow", "sp(x2)"))
		item = self.registerTable.verticalHeaderItem(3)
		item.setText(_translate("MainWindow", "gp(x3)"))
		item = self.registerTable.verticalHeaderItem(4)
		item.setText(_translate("MainWindow", "tp(x4)"))
		item = self.registerTable.verticalHeaderItem(5)
		item.setText(_translate("MainWindow", "t0(x5)"))
		item = self.registerTable.verticalHeaderItem(6)
		item.setText(_translate("MainWindow", "t1(x6)"))
		item = self.registerTable.verticalHeaderItem(7)
		item.setText(_translate("MainWindow", "t2(x7)"))
		item = self.registerTable.verticalHeaderItem(8)
		item.setText(_translate("MainWindow", "s0(x8)"))
		item = self.registerTable.verticalHeaderItem(9)
		item.setText(_translate("MainWindow", "s1(x9)"))
		item = self.registerTable.verticalHeaderItem(10)
		item.setText(_translate("MainWindow", "a0(x10)"))
		item = self.registerTable.verticalHeaderItem(11)
		item.setText(_translate("MainWindow", "a1(x11)"))
		item = self.registerTable.verticalHeaderItem(12)
		item.setText(_translate("MainWindow", "a2(x12)"))
		item = self.registerTable.verticalHeaderItem(13)
		item.setText(_translate("MainWindow", "a3(x13)"))
		item = self.registerTable.verticalHeaderItem(14)
		item.setText(_translate("MainWindow", "a4(x14)"))
		item = self.registerTable.verticalHeaderItem(15)
		item.setText(_translate("MainWindow", "a5(x15)"))
		item = self.registerTable.verticalHeaderItem(16)
		item.setText(_translate("MainWindow", "a6(x16)"))
		item = self.registerTable.verticalHeaderItem(17)
		item.setText(_translate("MainWindow", "a7(x17)"))
		item = self.registerTable.verticalHeaderItem(18)
		item.setText(_translate("MainWindow", "s2(x18)"))
		item = self.registerTable.verticalHeaderItem(19)
		item.setText(_translate("MainWindow", "s3(x19)"))
		item = self.registerTable.verticalHeaderItem(20)
		item.setText(_translate("MainWindow", "s4(x20)"))
		item = self.registerTable.verticalHeaderItem(21)
		item.setText(_translate("MainWindow", "s5(x21)"))
		item = self.registerTable.verticalHeaderItem(22)
		item.setText(_translate("MainWindow", "s6(x22)"))
		item = self.registerTable.verticalHeaderItem(23)
		item.setText(_translate("MainWindow", "s7(x23)"))
		item = self.registerTable.verticalHeaderItem(24)
		item.setText(_translate("MainWindow", "s8(x24)"))
		item = self.registerTable.verticalHeaderItem(25)
		item.setText(_translate("MainWindow", "s9(x25)"))
		item = self.registerTable.verticalHeaderItem(26)
		item.setText(_translate("MainWindow", "s10(x26)"))
		item = self.registerTable.verticalHeaderItem(27)
		item.setText(_translate("MainWindow", "s11(x27)"))
		item = self.registerTable.verticalHeaderItem(28)
		item.setText(_translate("MainWindow", "t3(x28)"))
		item = self.registerTable.verticalHeaderItem(29)
		item.setText(_translate("MainWindow", "t4(x29)"))
		item = self.registerTable.verticalHeaderItem(30)
		item.setText(_translate("MainWindow", "t5(x30)"))
		item = self.registerTable.verticalHeaderItem(31)
		item.setText(_translate("MainWindow", "t6(x31)"))
		item = self.registerTable.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Values"))
		__sortingEnabled = self.registerTable.isSortingEnabled()
		self.registerTable.setSortingEnabled(False)
		self.registerTable.setSortingEnabled(__sortingEnabled)
		self.regMemTab.setTabText(self.regMemTab.indexOf(self.tab_4), _translate("MainWindow", "Registers"))
		self.regMemTab.setTabText(self.regMemTab.indexOf(self.tab_6), _translate("MainWindow", "Pipelining Info"))
		self.label.setText(_translate("MainWindow", "Jump To"))
		self.memJumpDropDown.setItemText(0, _translate("MainWindow", "Text"))
		self.memJumpDropDown.setItemText(1, _translate("MainWindow", "Data"))
		self.memJumpDropDown.setItemText(2, _translate("MainWindow", "Heap"))
		self.memJumpDropDown.setItemText(3, _translate("MainWindow", "Stack"))
		self.memUp.setText(_translate("MainWindow", "Up"))
		self.memDown.setText(_translate("MainWindow", "Down"))
		item = self.memoryTable.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Address"))
		item = self.memoryTable.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "+0"))
		item = self.memoryTable.horizontalHeaderItem(2)
		item.setText(_translate("MainWindow", "+1"))
		item = self.memoryTable.horizontalHeaderItem(3)
		item.setText(_translate("MainWindow", "+2"))
		item = self.memoryTable.horizontalHeaderItem(4)
		item.setText(_translate("MainWindow", "+3"))
		self.regMemTab.setTabText(self.regMemTab.indexOf(self.tab_5), _translate("MainWindow", "Memory"))
		self.tabs.setTabText(self.tabs.indexOf(self.tab_2), _translate("MainWindow", "Simulator"))
		self.tabs.setTabText(self.tabs.indexOf(self.tab_3), _translate("MainWindow", "Customize Options"))

	
	def file_open(self):
		name = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File')
		if(len(name[0]) == 0):
			return
		code_file = open(name[0],'r')
		with code_file:
			text = code_file.read()
			self.codeEditor.clear()
			self.codeEditor.appendPlainText(text)

	def file_save(self):
		file = open("../lib/Files/assemblyCode.asm",'w+')
		text = self.codeEditor.toPlainText()
		file.write(text)
		file.close()

	def reset(self):
		self.currentPC = 0
		self.displayTypeChange(0)
		self.tableReColor()

	def onTabChange(self,i):
		self.currentPC = 0
		if(i == 0):
			self.codeTable.setRowCount(0)
			self.memoryTable.setRowCount(0)
			# self.errorBox.clear()

		from Phase2.registers import RegisterTable
		RegisterTable.Initialize(file_path="../lib/Phase2/")
		self.doRegisterUpdate()
		if(i == 1):
			self.file_save()
			mydir = os.getcwd()
			mydir_tmp = "../lib/"
			mydir_new = os.chdir(mydir_tmp)
			exec(open("first_half_controller.py").read(),locals(),locals())
			mydir = os.chdir(mydir)

			from Phase1.detectError import detectError
			error_list=detectError()
			if(len(error_list)>0):
				self.errorBox.setPlainText(error_list)
				
				self.tabs.setCurrentIndex(0)
				return

			self.errorBox.clear()

			mydir = os.getcwd()
			mydir_tmp = "../lib/"
			mydir_new = os.chdir(mydir_tmp)
			exec(open("second_half_controller.py").read())
			mydir = os.chdir(mydir)

			self.showProcessedCode()
			self.memJumpDropDown.setCurrentIndex(0)
			self.doMemoryUpdate()
			self.tableReColor()

			from Phase2.registers import RegisterTable
			RegisterTable.Initialize(file_path="../lib/Phase2/")
			self.doRegisterUpdate()
			self.doPipeUpdate()
			self.allInfo()
		
			
	def showProcessedCode(self):
		ori = open("../lib/Files/assemblyCodeFinal.asm")
		mac = open("../lib/Files/machine_code.mc")
		bas = open("../lib/Files/assemblyCodeFinal_BasicVersion.asm")
		
		ori = ori.readlines()
		mac = mac.readlines()
		bas = bas.readlines()
		self.codeTable.setRowCount(len(ori)+2)
		self.maxPC = 1
		auipc_count = 0		

		for ind in range(len(bas)+1):
			# print(ind)
			# item = self.codeTable.verticalHeaderItem(ind)
			item = QtWidgets.QTableWidgetItem()
			item.setTextAlignment(QtCore.Qt.AlignHCenter)
			self.codeTable.setItem(ind, 0, item)
			item = QtWidgets.QTableWidgetItem()
			item.setTextAlignment(QtCore.Qt.AlignHCenter)
			self.codeTable.setItem(ind, 1, item)
			item = QtWidgets.QTableWidgetItem()
			item.setTextAlignment(QtCore.Qt.AlignHCenter)
			self.codeTable.setItem(ind, 2, item)
			item = QtWidgets.QTableWidgetItem()
			item.setTextAlignment(QtCore.Qt.AlignHCenter)
			self.codeTable.setItem(ind, 3, item)
			
			if(ind == len(bas)):
				continue

			item.setText(self.translate("MainWindow", "New Row"))
			item = self.codeTable.item(ind, 0)
			item.setText(self.translate("MainWindow", mac[ind].strip().split()[0]))
			item = self.codeTable.item(ind, 1)
			item.setText(self.translate("MainWindow", mac[ind].strip().split()[1]))
			item = self.codeTable.item(ind, 2)
			item.setText(self.translate("MainWindow", bas[ind].strip()))
			item = self.codeTable.item(ind, 3)
			item.setText(self.translate("MainWindow", ori[ind-auipc_count].strip()))
			if bas[ind].split()[0] == "auipc":
				auipc_count +=1

	def displayTypeChange(self,i):
		self.doRegisterUpdate()
		self.doMemoryUpdate()
		self.doPipeUpdate()
		self.allInfo()
	def memoryTypeChange(self,i):
		self.doMemoryUpdate()
	


	def stepForward(self):
		if self.currentPC ==0:
			self.runCode()
		if self.currentPC < self.maxPC:
			self.currentPC +=1
		self.displayTypeChange(0)
		self.tableReColor()

	def stepBack(self):
		if self.currentPC > 0:
			self.currentPC -=1
		self.displayTypeChange(0)
		self.tableReColor()


	def getVal(self,val):
		
		if(self.regMemDisplayTypeDrop.currentIndex()==0):
			val=(val & 0xffffffff)
			val=hex(val)
		elif(self.regMemDisplayTypeDrop.currentIndex()==1):
			pass
		elif(self.regMemDisplayTypeDrop.currentIndex()==2):
			val=(val & 0xffffffff)
		elif(self.regMemDisplayTypeDrop.currentIndex()==3):
			try:
				val=chr(val)
			except:
				val=chr(1)
		return val
	
	def selectMemory(self,index):
	

		if(index==0):
			dmt = open('../lib/Phase3/Snapshot/memory_instructions.txt','r+').readlines()
			return dmt

		if(self.currentPC == 0 or self.currentPC>self.maxPC):
			return []

		if(index==1):
			dmt = open('../lib/Phase3/Snapshot/Files/memory_after_cycle'+str(self.currentPC)+'.txt','r+').readlines()
			return dmt
		if(index==2):
			dmt = open('../lib/Files/heap_memory_table.txt','r+').readlines()
			return dmt
		if(index==3):
			dmt = open('../lib/Phase3/Snapshot/Files/memory_after_cycle'+str(self.currentPC)+'.txt','r+').readlines()
			return dmt

	def doRegisterUpdate(self):
		rt=[]
		if self.currentPC == 0 or self.currentPC>self.maxPC:
			rt = ["0"]*32
			rt[2]="2147483632"
		else:
			rt=open('../lib/Phase3/Snapshot/Files/registers_after_cycle'+str(self.currentPC)+'.txt','r+')
			rt=rt.readlines()
		for ind in range(len(rt)):
			item=QtWidgets.QTableWidgetItem()
			val=int(rt[ind].strip())
			val = self.getVal(val)
			item.setText(str(val))
			self.registerTable.setItem(ind,0,item)
	def doPipeUpdate(self):
		rt=[]
		if self.currentPC == 0 or self.currentPC>self.maxPC:
			rt = ["0"]*10
		else:
			rt=open('../lib/Phase3/Snapshot/Files/instruction_details_after_cycle'+str(self.currentPC)+'.txt','r+')
			rt=rt.readlines()
		for ind in range(len(rt)):
			item=QtWidgets.QTableWidgetItem()
			val=int(rt[ind].strip(),16)
			val = self.getVal(val)
			item.setText(str(val))
			self.pipeTable.setItem(ind,0,item)

	def allInfo(self):
		rt=[]
		if self.currentPC == 0:
			rt = ["0"]*10
		else:
			rt=open('../lib/Phase3/Files/summary.txt','r+')
			rt=rt.readlines()
		for ind in range(len(rt)):
			item=QtWidgets.QTableWidgetItem()
			val=rt[ind].strip()
			#val = self.getVal(val)
			item.setText(str(val))
			self.pipeTable.setItem(5+ind,0,item)
		



	def knobs(self,but,ind):
		rt=open('../lib/Phase3/Files/knobs.txt','r+')
		rt=rt.readlines()
		if(len(rt)==0):
			rt = ['1 1 0 0']
		lis = rt[0].strip().split()
		
		if but.isChecked() == True:
			lis[ind] = '1'
		else:
			lis[ind] = '0'

		rt=open('../lib/Phase3/Files/knobs.txt','w')
		rt.write(" ".join(lis))

		#print(lis)
		


	def tableReColor(self):
		
		for j in range(self.codeTable.rowCount()-1):
			self.codeTable.item(j, 0).setBackground(QtGui.QColor(255,255,255))
				

		if self.currentPC !=0 and self.currentPC<=self.maxPC:
			
			self.codeTable.item((int(self.PCList[self.currentPC-1])//4), 0).setBackground(QtGui.QColor(144, 238, 144))

	def doMemoryUpdate(self):
		memList = self.selectMemory(self.memJumpDropDown.currentIndex())
		self.memoryTable.setRowCount((len(memList)+3)//4)
		for ind in range(0,len(memList)//4):
			
			item = QtWidgets.QTableWidgetItem()
			item.setTextAlignment(QtCore.Qt.AlignHCenter)
			self.memoryTable.setItem(ind, 0, item)
			item = QtWidgets.QTableWidgetItem()
			item.setTextAlignment(QtCore.Qt.AlignHCenter)
			self.memoryTable.setItem(ind, 1, item)
			item = QtWidgets.QTableWidgetItem()
			item.setTextAlignment(QtCore.Qt.AlignHCenter)
			self.memoryTable.setItem(ind, 2, item)
			item = QtWidgets.QTableWidgetItem()
			item.setTextAlignment(QtCore.Qt.AlignHCenter)
			self.memoryTable.setItem(ind, 3, item)
			item = QtWidgets.QTableWidgetItem()
			item.setTextAlignment(QtCore.Qt.AlignHCenter)
			self.memoryTable.setItem(ind, 4, item)
			item.setText("New Row")
			item = self.memoryTable.item(ind, 0)
			item.setText(memList[ind*4].strip().split()[0])
			item = self.memoryTable.item(ind, 1)
			item.setText(str(self.getVal(int(memList[ind*4].strip().split()[1]))))
			item = self.memoryTable.item(ind, 2)
			item.setText(str(self.getVal(int(memList[ind*4+1].strip().split()[1]))))
			item = self.memoryTable.item(ind, 3)
			item.setText(str(self.getVal(int(memList[ind*4+2].strip().split()[1]))))
			item = self.memoryTable.item(ind, 4)
			item.setText(str(self.getVal(int(memList[ind*4+3].strip().split()[1]))))
		

	def runCodeClick(self):
		self.runCode()
		self.currentPC = self.maxPC
		self.displayTypeChange(0)
		self.tableReColor()

	def runCode(self):
		mydir = os.getcwd()
		mydir_tmp = "../lib/"
		mydir_new = os.chdir(os.path.join(mydir,mydir_tmp))
		exec(open("Main_Controller.py").read())
		mydir = os.chdir(mydir)
		self.PCList = open('../lib/Phase3/Snapshot/Files/pcs_after_each_cycle.txt','r+').readlines()
		self.maxPC = len(self.PCList)-1
		self.doRegisterUpdate()
		self.doPipeUpdate()
		self.doMemoryUpdate()
		self.allInfo()

	def init(self):
		self.knobs(self.cb1,0)
		self.knobs(self.cb2,1)
		self.knobs(self.cb3,2)
		self.knobs(self.cb4,3)

from codeeditor import CodeEditor

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	
	ui.init()

	MainWindow.show()
	sys.exit(app.exec_())

