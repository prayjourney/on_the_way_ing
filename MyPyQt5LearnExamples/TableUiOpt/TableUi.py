# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TableUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(631, 326)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(9)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/app2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 621, 301))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.addaction = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addaction.setIcon(icon1)
        self.addaction.setObjectName("addaction")
        self.deleteaction = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteaction.setIcon(icon2)
        self.deleteaction.setObjectName("deleteaction")
        self.additemaction = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.additemaction.setIcon(icon3)
        self.additemaction.setObjectName("additemaction")
        self.updateitemaction = QtWidgets.QAction(MainWindow)
        self.updateitemaction.setObjectName("updateitemaction")
        self.deleteitemaction = QtWidgets.QAction(MainWindow)
        self.deleteitemaction.setObjectName("deleteitemaction")
        self.savetodb = QtWidgets.QAction(MainWindow)
        self.savetodb.setObjectName("savetodb")
        self.importfromexcel = QtWidgets.QAction(MainWindow)
        self.importfromexcel.setObjectName("importfromexcel")
        self.exporttoexcel = QtWidgets.QAction(MainWindow)
        self.exporttoexcel.setObjectName("exporttoexcel")
        self.helpaction = QtWidgets.QAction(MainWindow)
        self.helpaction.setObjectName("helpaction")
        self.declareaction = QtWidgets.QAction(MainWindow)
        self.declareaction.setObjectName("declareaction")
        self.menu.addAction(self.addaction)
        self.menu.addAction(self.deleteaction)
        self.menu_2.addAction(self.additemaction)
        self.menu_2.addAction(self.updateitemaction)
        self.menu_2.addAction(self.deleteitemaction)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.savetodb)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.importfromexcel)
        self.menu_2.addAction(self.exporttoexcel)
        self.menu_3.addAction(self.helpaction)
        self.menu_3.addAction(self.declareaction)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Table的操作"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "内容"))
        self.menu_3.setTitle(_translate("MainWindow", "说明"))
        self.addaction.setText(_translate("MainWindow", "添加行"))
        self.deleteaction.setText(_translate("MainWindow", "删除行"))
        self.additemaction.setText(_translate("MainWindow", "添加一行"))
        self.updateitemaction.setText(_translate("MainWindow", "修改一行"))
        self.deleteitemaction.setText(_translate("MainWindow", "删除一行"))
        self.savetodb.setText(_translate("MainWindow", "保存到数据库"))
        self.importfromexcel.setText(_translate("MainWindow", "从excel导入"))
        self.exporttoexcel.setText(_translate("MainWindow", "导出到excel"))
        self.helpaction.setText(_translate("MainWindow", "帮助"))
        self.declareaction.setText(_translate("MainWindow", "说明"))

