# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qad_dimstyle_new.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DimStyle_New_Dialog(object):
    def setupUi(self, DimStyle_New_Dialog):
        DimStyle_New_Dialog.setObjectName("DimStyle_New_Dialog")
        DimStyle_New_Dialog.resize(372, 142)
        DimStyle_New_Dialog.setMinimumSize(QtCore.QSize(372, 142))
        DimStyle_New_Dialog.setMaximumSize(QtCore.QSize(372, 142))
        self.label = QtWidgets.QLabel(DimStyle_New_Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 221, 16))
        self.label.setObjectName("label")
        self.newDimStyleName = QtWidgets.QLineEdit(DimStyle_New_Dialog)
        self.newDimStyleName.setGeometry(QtCore.QRect(10, 30, 221, 20))
        self.newDimStyleName.setObjectName("newDimStyleName")
        self.label_2 = QtWidgets.QLabel(DimStyle_New_Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 221, 16))
        self.label_2.setObjectName("label_2")
        self.DimStyleNameFrom = QtWidgets.QComboBox(DimStyle_New_Dialog)
        self.DimStyleNameFrom.setGeometry(QtCore.QRect(10, 110, 221, 22))
        self.DimStyleNameFrom.setObjectName("DimStyleNameFrom")
        self.continueButton = QtWidgets.QPushButton(DimStyle_New_Dialog)
        self.continueButton.setGeometry(QtCore.QRect(284, 50, 81, 23))
        self.continueButton.setObjectName("continueButton")
        self.cancelButton = QtWidgets.QPushButton(DimStyle_New_Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(284, 80, 81, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.helpButton = QtWidgets.QPushButton(DimStyle_New_Dialog)
        self.helpButton.setGeometry(QtCore.QRect(284, 110, 81, 23))
        self.helpButton.setObjectName("helpButton")
        self.label_3 = QtWidgets.QLabel(DimStyle_New_Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 221, 16))
        self.label_3.setObjectName("label_3")
        self.newDimStyleDescr = QtWidgets.QLineEdit(DimStyle_New_Dialog)
        self.newDimStyleDescr.setGeometry(QtCore.QRect(10, 70, 221, 20))
        self.newDimStyleDescr.setObjectName("newDimStyleDescr")

        self.retranslateUi(DimStyle_New_Dialog)
        self.DimStyleNameFrom.currentIndexChanged['int'].connect(DimStyle_New_Dialog.DimStyleNameFromChanged)
        self.newDimStyleName.textEdited['QString'].connect(DimStyle_New_Dialog.newStyleNameChanged)
        self.cancelButton.clicked.connect(DimStyle_New_Dialog.reject)
        self.helpButton.clicked.connect(DimStyle_New_Dialog.ButtonHELP_Pressed)
        self.continueButton.clicked.connect(DimStyle_New_Dialog.ButtonBOX_continue)
        QtCore.QMetaObject.connectSlotsByName(DimStyle_New_Dialog)

    def retranslateUi(self, DimStyle_New_Dialog):
        _translate = QtCore.QCoreApplication.translate
        DimStyle_New_Dialog.setWindowTitle(_translate("DimStyle_New_Dialog", "QAD - Create new dimension style"))
        self.label.setText(_translate("DimStyle_New_Dialog", "New style name:"))
        self.label_2.setText(_translate("DimStyle_New_Dialog", "Start with:"))
        self.continueButton.setText(_translate("DimStyle_New_Dialog", "Continue..."))
        self.cancelButton.setText(_translate("DimStyle_New_Dialog", "Cancel"))
        self.helpButton.setText(_translate("DimStyle_New_Dialog", "?"))
        self.label_3.setText(_translate("DimStyle_New_Dialog", "Description:"))
