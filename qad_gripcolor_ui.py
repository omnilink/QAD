# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qad_gripcolor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GripColor_Dialog(object):
    def setupUi(self, GripColor_Dialog):
        GripColor_Dialog.setObjectName("GripColor_Dialog")
        GripColor_Dialog.resize(400, 208)
        GripColor_Dialog.setMinimumSize(QtCore.QSize(400, 208))
        GripColor_Dialog.setMaximumSize(QtCore.QSize(400, 208))
        self.buttonBox = QtWidgets.QDialogButtonBox(GripColor_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(60, 170, 331, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Help|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(GripColor_Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 141))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 171, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(200, 30, 171, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 171, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(200, 80, 171, 21))
        self.label_4.setObjectName("label_4")
        self.unselectedGripColorDummy = QtWidgets.QPushButton(self.groupBox)
        self.unselectedGripColorDummy.setGeometry(QtCore.QRect(10, 50, 171, 23))
        self.unselectedGripColorDummy.setText("")
        self.unselectedGripColorDummy.setObjectName("unselectedGripColorDummy")
        self.selectedGripColorDummy = QtWidgets.QPushButton(self.groupBox)
        self.selectedGripColorDummy.setGeometry(QtCore.QRect(10, 100, 171, 23))
        self.selectedGripColorDummy.setText("")
        self.selectedGripColorDummy.setObjectName("selectedGripColorDummy")
        self.hoverGripColorDummy = QtWidgets.QPushButton(self.groupBox)
        self.hoverGripColorDummy.setGeometry(QtCore.QRect(200, 50, 171, 23))
        self.hoverGripColorDummy.setText("")
        self.hoverGripColorDummy.setObjectName("hoverGripColorDummy")
        self.contourGripColorDummy = QtWidgets.QPushButton(self.groupBox)
        self.contourGripColorDummy.setGeometry(QtCore.QRect(200, 100, 171, 23))
        self.contourGripColorDummy.setText("")
        self.contourGripColorDummy.setObjectName("contourGripColorDummy")

        self.retranslateUi(GripColor_Dialog)
        self.buttonBox.rejected.connect(GripColor_Dialog.reject)
        self.buttonBox.helpRequested.connect(GripColor_Dialog.ButtonHELP_Pressed)
        self.buttonBox.accepted.connect(GripColor_Dialog.ButtonBOX_Accepted)
        QtCore.QMetaObject.connectSlotsByName(GripColor_Dialog)

    def retranslateUi(self, GripColor_Dialog):
        _translate = QtCore.QCoreApplication.translate
        GripColor_Dialog.setWindowTitle(_translate("GripColor_Dialog", "QAD - Grip colors"))
        self.groupBox.setTitle(_translate("GripColor_Dialog", "Settings"))
        self.label.setText(_translate("GripColor_Dialog", "Unselected grip color:"))
        self.label_2.setText(_translate("GripColor_Dialog", "Hover grip color:"))
        self.label_3.setText(_translate("GripColor_Dialog", "Selected grip color:"))
        self.label_4.setText(_translate("GripColor_Dialog", "Grip contour color:"))
