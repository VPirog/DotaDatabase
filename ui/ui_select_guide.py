# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raw_qt/select_guide.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(567, 399)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 1, 0, 1, 1)
        self.quitButton = QtWidgets.QPushButton(Dialog)
        self.quitButton.setObjectName("quitButton")
        self.gridLayout.addWidget(self.quitButton, 1, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(440)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setMaximumWidth(150)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 3)
        self.pushButton_delete = QtWidgets.QPushButton(Dialog)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.gridLayout.addWidget(self.pushButton_delete, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.saveButton.setText(_translate("Dialog", "SAVE"))
        self.quitButton.setText(_translate("Dialog", "QUIT"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Name"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "Hero"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "Rating"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "Description"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "Main text"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "Your Comment"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "data"))
        self.pushButton_delete.setText(_translate("Dialog", "DELETE"))