# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qad_windowcolor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WindowColor_Dialog(object):
    def setupUi(self, WindowColor_Dialog):
        WindowColor_Dialog.setObjectName("WindowColor_Dialog")
        WindowColor_Dialog.resize(592, 424)
        WindowColor_Dialog.setMinimumSize(QtCore.QSize(592, 424))
        WindowColor_Dialog.setMaximumSize(QtCore.QSize(592, 424))
        self.Button_Cancel = QtWidgets.QPushButton(WindowColor_Dialog)
        self.Button_Cancel.setGeometry(QtCore.QRect(430, 390, 75, 23))
        self.Button_Cancel.setObjectName("Button_Cancel")
        self.Button_Help = QtWidgets.QPushButton(WindowColor_Dialog)
        self.Button_Help.setGeometry(QtCore.QRect(510, 390, 75, 23))
        self.Button_Help.setObjectName("Button_Help")
        self.Button_ApplyClose = QtWidgets.QPushButton(WindowColor_Dialog)
        self.Button_ApplyClose.setGeometry(QtCore.QRect(334, 390, 91, 23))
        self.Button_ApplyClose.setObjectName("Button_ApplyClose")
        self.label = QtWidgets.QLabel(WindowColor_Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 16))
        self.label.setObjectName("label")
        self.listView_Context = QtWidgets.QListView(WindowColor_Dialog)
        self.listView_Context.setGeometry(QtCore.QRect(10, 30, 161, 81))
        self.listView_Context.setObjectName("listView_Context")
        self.listView_Element = QtWidgets.QListView(WindowColor_Dialog)
        self.listView_Element.setGeometry(QtCore.QRect(180, 30, 231, 171))
        self.listView_Element.setObjectName("listView_Element")
        self.label_2 = QtWidgets.QLabel(WindowColor_Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 10, 161, 16))
        self.label_2.setObjectName("label_2")
        self.Button_ColorDummy = QtWidgets.QPushButton(WindowColor_Dialog)
        self.Button_ColorDummy.setGeometry(QtCore.QRect(420, 30, 161, 23))
        self.Button_ColorDummy.setText("")
        self.Button_ColorDummy.setObjectName("Button_ColorDummy")
        self.Button_RestoreCurrElement = QtWidgets.QPushButton(WindowColor_Dialog)
        self.Button_RestoreCurrElement.setGeometry(QtCore.QRect(420, 120, 161, 23))
        self.Button_RestoreCurrElement.setObjectName("Button_RestoreCurrElement")
        self.Button_RestoreCurrContext = QtWidgets.QPushButton(WindowColor_Dialog)
        self.Button_RestoreCurrContext.setGeometry(QtCore.QRect(420, 150, 161, 23))
        self.Button_RestoreCurrContext.setObjectName("Button_RestoreCurrContext")
        self.Button_RestoreAllContext = QtWidgets.QPushButton(WindowColor_Dialog)
        self.Button_RestoreAllContext.setGeometry(QtCore.QRect(420, 180, 161, 23))
        self.Button_RestoreAllContext.setObjectName("Button_RestoreAllContext")
        self.widget_Preview = QtWidgets.QWidget(WindowColor_Dialog)
        self.widget_Preview.setGeometry(QtCore.QRect(10, 210, 401, 171))
        self.widget_Preview.setObjectName("widget_Preview")
        self.label_3 = QtWidgets.QLabel(WindowColor_Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 161, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(WindowColor_Dialog)
        self.label_4.setGeometry(QtCore.QRect(420, 10, 161, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(WindowColor_Dialog)
        self.Button_ApplyClose.clicked.connect(WindowColor_Dialog.Button_ApplyClose_Pressed)
        self.Button_Cancel.clicked.connect(WindowColor_Dialog.Button_Cancel_Pressed)
        self.Button_Help.clicked.connect(WindowColor_Dialog.ButtonHELP_Pressed)
        self.Button_RestoreCurrElement.clicked.connect(WindowColor_Dialog.Button_RestoreCurrElement_clicked)
        self.Button_RestoreCurrContext.clicked.connect(WindowColor_Dialog.Button_RestoreCurrContext_clicked)
        self.Button_RestoreAllContext.clicked.connect(WindowColor_Dialog.Button_RestoreAllContext_clicked)
        QtCore.QMetaObject.connectSlotsByName(WindowColor_Dialog)

    def retranslateUi(self, WindowColor_Dialog):
        _translate = QtCore.QCoreApplication.translate
        WindowColor_Dialog.setWindowTitle(_translate("WindowColor_Dialog", "Drawing window Colors"))
        self.Button_Cancel.setText(_translate("WindowColor_Dialog", "Cancel"))
        self.Button_Help.setText(_translate("WindowColor_Dialog", "Help"))
        self.Button_ApplyClose.setText(_translate("WindowColor_Dialog", "Apply && Close"))
        self.label.setText(_translate("WindowColor_Dialog", "Context:"))
        self.label_2.setText(_translate("WindowColor_Dialog", "Interface element:"))
        self.Button_RestoreCurrElement.setText(_translate("WindowColor_Dialog", "Restore current element"))
        self.Button_RestoreCurrContext.setText(_translate("WindowColor_Dialog", "Restore current context"))
        self.Button_RestoreAllContext.setText(_translate("WindowColor_Dialog", "Restore all context"))
        self.label_3.setText(_translate("WindowColor_Dialog", "Preview:"))
        self.label_4.setText(_translate("WindowColor_Dialog", "Color:"))
