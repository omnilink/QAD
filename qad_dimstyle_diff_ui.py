# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qad_dimstyle_diff.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DimStyle_Diff_Dialog(object):
    def setupUi(self, DimStyle_Diff_Dialog):
        DimStyle_Diff_Dialog.setObjectName("DimStyle_Diff_Dialog")
        DimStyle_Diff_Dialog.resize(443, 526)
        DimStyle_Diff_Dialog.setMinimumSize(QtCore.QSize(443, 526))
        DimStyle_Diff_Dialog.setMaximumSize(QtCore.QSize(443, 526))
        self.label = QtWidgets.QLabel(DimStyle_Diff_Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DimStyle_Diff_Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 81, 21))
        self.label_2.setObjectName("label_2")
        self.dimStyle1 = QtWidgets.QComboBox(DimStyle_Diff_Dialog)
        self.dimStyle1.setGeometry(QtCore.QRect(100, 10, 211, 22))
        self.dimStyle1.setObjectName("dimStyle1")
        self.dimStyle2 = QtWidgets.QComboBox(DimStyle_Diff_Dialog)
        self.dimStyle2.setGeometry(QtCore.QRect(100, 40, 211, 22))
        self.dimStyle2.setObjectName("dimStyle2")
        self.line = QtWidgets.QFrame(DimStyle_Diff_Dialog)
        self.line.setGeometry(QtCore.QRect(10, 70, 421, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.msg = QtWidgets.QLabel(DimStyle_Diff_Dialog)
        self.msg.setGeometry(QtCore.QRect(10, 80, 381, 21))
        self.msg.setObjectName("msg")
        self.layoutWidget = QtWidgets.QWidget(DimStyle_Diff_Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(277, 490, 158, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.closeButton = QtWidgets.QPushButton(self.layoutWidget)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.helpButton = QtWidgets.QPushButton(self.layoutWidget)
        self.helpButton.setObjectName("helpButton")
        self.horizontalLayout.addWidget(self.helpButton)
        self.tableWidget = QtWidgets.QTableWidget(DimStyle_Diff_Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 421, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.copyButton = QtWidgets.QPushButton(DimStyle_Diff_Dialog)
        self.copyButton.setGeometry(QtCore.QRect(404, 80, 31, 23))
        self.copyButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/qad/icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copyButton.setIcon(icon)
        self.copyButton.setObjectName("copyButton")

        self.retranslateUi(DimStyle_Diff_Dialog)
        self.helpButton.clicked.connect(DimStyle_Diff_Dialog.ButtonHELP_Pressed)
        self.dimStyle1.currentIndexChanged['int'].connect(DimStyle_Diff_Dialog.DimStyleName1Changed)
        self.dimStyle2.currentIndexChanged['int'].connect(DimStyle_Diff_Dialog.DimStyleName2Changed)
        self.copyButton.clicked.connect(DimStyle_Diff_Dialog.copyToClipboard)
        self.closeButton.clicked.connect(DimStyle_Diff_Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(DimStyle_Diff_Dialog)

    def retranslateUi(self, DimStyle_Diff_Dialog):
        _translate = QtCore.QCoreApplication.translate
        DimStyle_Diff_Dialog.setWindowTitle(_translate("DimStyle_Diff_Dialog", "QAD - Compare dimension styles"))
        self.label.setText(_translate("DimStyle_Diff_Dialog", "Compare:"))
        self.label_2.setText(_translate("DimStyle_Diff_Dialog", "With:"))
        self.dimStyle1.setToolTip(_translate("DimStyle_Diff_Dialog", "Specify the first dimension style."))
        self.dimStyle2.setToolTip(_translate("DimStyle_Diff_Dialog", "Specify the second dimension style. If you set the second style as the first, all dimension style properties will displayed."))
        self.msg.setText(_translate("DimStyle_Diff_Dialog", "TextLabel"))
        self.closeButton.setText(_translate("DimStyle_Diff_Dialog", "Close"))
        self.helpButton.setText(_translate("DimStyle_Diff_Dialog", "?"))
        self.tableWidget.setToolTip(_translate("DimStyle_Diff_Dialog", "<html><head/><body><p>Display the result of comparing dimension styles.If you compare two different styles, the settings that are different between the two dimension styles, their current settings, and brief descriptions are listed. If you set the second style as the first, all dimension style properties will displayed.</p></body></html>"))
        self.copyButton.setToolTip(_translate("DimStyle_Diff_Dialog", "Copy the result of comparing into the clipboard."))
