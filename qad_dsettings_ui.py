# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qad_dsettings.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DSettings_Dialog(object):
    def setupUi(self, DSettings_Dialog):
        DSettings_Dialog.setObjectName("DSettings_Dialog")
        DSettings_Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        DSettings_Dialog.resize(500, 455)
        DSettings_Dialog.setMinimumSize(QtCore.QSize(500, 455))
        DSettings_Dialog.setMaximumSize(QtCore.QSize(500, 455))
        DSettings_Dialog.setMouseTracking(True)
        DSettings_Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        DSettings_Dialog.setModal(True)
        self.tabWidget = QtWidgets.QTabWidget(DSettings_Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 481, 401))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.groupBox = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 451, 321))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 290, 261, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_SelectALL = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_SelectALL.setObjectName("pushButton_SelectALL")
        self.horizontalLayout_2.addWidget(self.pushButton_SelectALL)
        self.pushButton_DeSelectALL = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_DeSelectALL.setObjectName("pushButton_DeSelectALL")
        self.horizontalLayout_2.addWidget(self.pushButton_DeSelectALL)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(240, 20, 191, 261))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/plugins/qad/icons/dsettings/OSNAP_EXTP.png"))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/plugins/qad/icons/dsettings/OSNAP_PARP.png"))
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 4, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap(":/plugins/qad/icons/dsettings/OSNAP_PROGP.png"))
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/plugins/qad/icons/dsettings/OSNAP_EXTINT.png"))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/plugins/qad/icons/dsettings/OSNAP_PERP.png"))
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.checkBox_PERP = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_PERP.setTristate(False)
        self.checkBox_PERP.setObjectName("checkBox_PERP")
        self.gridLayout.addWidget(self.checkBox_PERP, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/plugins/qad/icons/dsettings/OSNAP_TANP.png"))
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.checkBox_TANP = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_TANP.setTristate(False)
        self.checkBox_TANP.setObjectName("checkBox_TANP")
        self.gridLayout.addWidget(self.checkBox_TANP, 2, 1, 1, 1)
        self.checkBox_EXTP = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_EXTP.setTristate(False)
        self.checkBox_EXTP.setObjectName("checkBox_EXTP")
        self.gridLayout.addWidget(self.checkBox_EXTP, 3, 1, 1, 1)
        self.checkBox_PARALP = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_PARALP.setTristate(False)
        self.checkBox_PARALP.setObjectName("checkBox_PARALP")
        self.gridLayout.addWidget(self.checkBox_PARALP, 4, 1, 1, 1)
        self.checkBox_PROGRESP = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_PROGRESP.setTristate(False)
        self.checkBox_PROGRESP.setObjectName("checkBox_PROGRESP")
        self.gridLayout.addWidget(self.checkBox_PROGRESP, 5, 1, 1, 1)
        self.checkBox_EXT_INT = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_EXT_INT.setObjectName("checkBox_EXT_INT")
        self.gridLayout.addWidget(self.checkBox_EXT_INT, 6, 1, 1, 1)
        self.checkBox_QUADP = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_QUADP.setTristate(False)
        self.checkBox_QUADP.setObjectName("checkBox_QUADP")
        self.gridLayout.addWidget(self.checkBox_QUADP, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/plugins/qad/icons/dsettings/OSNAP_QUADP.png"))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_ProgrDistance = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_ProgrDistance.setGeometry(QtCore.QRect(380, 210, 41, 20))
        self.lineEdit_ProgrDistance.setObjectName("lineEdit_ProgrDistance")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 20, 161, 261))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_END_PLINE = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_END_PLINE.setObjectName("checkBox_END_PLINE")
        self.gridLayout_2.addWidget(self.checkBox_END_PLINE, 0, 1, 1, 1)
        self.label_ENDP = QtWidgets.QLabel(self.layoutWidget2)
        self.label_ENDP.setText("")
        self.label_ENDP.setPixmap(QtGui.QPixmap(":/plugins/qad/icons/dsettings/OSNAP_ENDP.png"))
        self.label_ENDP.setObjectName("label_ENDP")
        self.gridLayout_2.addWidget(self.label_ENDP, 1, 0, 1, 1)
        self.checkBox_ENDP = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_ENDP.setTristate(False)
        self.checkBox_ENDP.setObjectName("checkBox_ENDP")
        self.gridLayout_2.addWidget(self.checkBox_ENDP, 1, 1, 1, 1)
        self.label_MIDP = QtWidgets.QLabel(self.layoutWidget2)
        self.label_MIDP.setText("")
        self.label_MIDP.setPixmap(QtGui.QPixmap(":/plugins/qad/icons/dsettings/OSNAP_MEDP.png"))
        self.label_MIDP.setObjectName("label_MIDP")
        self.gridLayout_2.addWidget(self.label_MIDP, 2, 0, 1, 1)
        self.checkBox_MIDP = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_MIDP.setTristate(False)
        self.checkBox_MIDP.setObjectName("checkBox_MIDP")
        self.gridLayout_2.addWidget(self.checkBox_MIDP, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/plugins/qad/icons/dsettings/OSNAP_INTP.png"))
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.checkBox_INTP = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_INTP.setTristate(False)
        self.checkBox_INTP.setObjectName("checkBox_INTP")
        self.gridLayout_2.addWidget(self.checkBox_INTP, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/plugins/qad/icons/dsettings/OSNAP_CENP.png"))
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.checkBox_CENP = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_CENP.setTristate(False)
        self.checkBox_CENP.setObjectName("checkBox_CENP")
        self.gridLayout_2.addWidget(self.checkBox_CENP, 4, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/plugins/qad/icons/dsettings/OSNAP_NODP.png"))
        self.label_7.setScaledContents(False)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)
        self.checkBox_NODP = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_NODP.setTristate(False)
        self.checkBox_NODP.setObjectName("checkBox_NODP")
        self.gridLayout_2.addWidget(self.checkBox_NODP, 5, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/plugins/qad/icons/dsettings/OSNAP_NEARP.png"))
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 6, 0, 1, 1)
        self.checkBox_NEARP = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_NEARP.setTristate(False)
        self.checkBox_NEARP.setObjectName("checkBox_NEARP")
        self.gridLayout_2.addWidget(self.checkBox_NEARP, 6, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/plugins/qad/icons/dsettings/OSNAP_ENDP.png"))
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.checkBox_IsOsnapON = QtWidgets.QCheckBox(self.tab_1)
        self.checkBox_IsOsnapON.setGeometry(QtCore.QRect(10, 10, 191, 17))
        self.checkBox_IsOsnapON.setObjectName("checkBox_IsOsnapON")
        self.checkBox_ObjectSnapTracking = QtWidgets.QCheckBox(self.tab_1)
        self.checkBox_ObjectSnapTracking.setGeometry(QtCore.QRect(210, 10, 251, 20))
        self.checkBox_ObjectSnapTracking.setObjectName("checkBox_ObjectSnapTracking")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.checkBox_PolarPickPoint = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_PolarPickPoint.setGeometry(QtCore.QRect(10, 10, 171, 17))
        self.checkBox_PolarPickPoint.setObjectName("checkBox_PolarPickPoint")
        self.groupBox_PolarAngleSettings = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_PolarAngleSettings.setGeometry(QtCore.QRect(10, 40, 151, 71))
        self.groupBox_PolarAngleSettings.setObjectName("groupBox_PolarAngleSettings")
        self.label_12 = QtWidgets.QLabel(self.groupBox_PolarAngleSettings)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 121, 16))
        self.label_12.setObjectName("label_12")
        self.comboBox_increment_angle = QtWidgets.QComboBox(self.groupBox_PolarAngleSettings)
        self.comboBox_increment_angle.setGeometry(QtCore.QRect(10, 40, 131, 22))
        self.comboBox_increment_angle.setEditable(True)
        self.comboBox_increment_angle.setObjectName("comboBox_increment_angle")
        self.groupBox_OsnapPolarOrtho = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_OsnapPolarOrtho.setGeometry(QtCore.QRect(190, 40, 271, 71))
        self.groupBox_OsnapPolarOrtho.setObjectName("groupBox_OsnapPolarOrtho")
        self.radioButton_OsnapOrtho = QtWidgets.QRadioButton(self.groupBox_OsnapPolarOrtho)
        self.radioButton_OsnapOrtho.setGeometry(QtCore.QRect(10, 30, 251, 17))
        self.radioButton_OsnapOrtho.setObjectName("radioButton_OsnapOrtho")
        self.radioButton_OsnapPolarAngle = QtWidgets.QRadioButton(self.groupBox_OsnapPolarOrtho)
        self.radioButton_OsnapPolarAngle.setGeometry(QtCore.QRect(10, 50, 251, 16))
        self.radioButton_OsnapPolarAngle.setObjectName("radioButton_OsnapPolarAngle")
        self.groupBox_OsnapPolarMeasurement = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_OsnapPolarMeasurement.setGeometry(QtCore.QRect(190, 120, 271, 71))
        self.groupBox_OsnapPolarMeasurement.setObjectName("groupBox_OsnapPolarMeasurement")
        self.radioButton_OsnapPolarAbolute = QtWidgets.QRadioButton(self.groupBox_OsnapPolarMeasurement)
        self.radioButton_OsnapPolarAbolute.setGeometry(QtCore.QRect(10, 30, 251, 17))
        self.radioButton_OsnapPolarAbolute.setObjectName("radioButton_OsnapPolarAbolute")
        self.radioButton_OsnapPolarRelative = QtWidgets.QRadioButton(self.groupBox_OsnapPolarMeasurement)
        self.radioButton_OsnapPolarRelative.setGeometry(QtCore.QRect(10, 50, 251, 17))
        self.radioButton_OsnapPolarRelative.setObjectName("radioButton_OsnapPolarRelative")
        self.tabWidget.addTab(self.tab_2, "")
        self.layoutWidget3 = QtWidgets.QWidget(DSettings_Dialog)
        self.layoutWidget3.setGeometry(QtCore.QRect(250, 420, 239, 25))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.okButton = QtWidgets.QPushButton(self.layoutWidget3)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(self.layoutWidget3)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.pushButton_HELP = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_HELP.setObjectName("pushButton_HELP")
        self.horizontalLayout.addWidget(self.pushButton_HELP)

        self.retranslateUi(DSettings_Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_DeSelectALL.pressed.connect(DSettings_Dialog.ButtonDeselectALL_Pressed)
        self.pushButton_SelectALL.pressed.connect(DSettings_Dialog.ButtonSelectALL_Pressed)
        self.pushButton_HELP.clicked.connect(DSettings_Dialog.ButtonHELP_Pressed)
        self.okButton.clicked.connect(DSettings_Dialog.ButtonBOX_Accepted)
        self.cancelButton.clicked.connect(DSettings_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DSettings_Dialog)

    def retranslateUi(self, DSettings_Dialog):
        _translate = QtCore.QCoreApplication.translate
        DSettings_Dialog.setWindowTitle(_translate("DSettings_Dialog", "QAD - Drawing settings"))
        self.groupBox.setTitle(_translate("DSettings_Dialog", "Object Snap modes"))
        self.pushButton_SelectALL.setText(_translate("DSettings_Dialog", "Select All"))
        self.pushButton_DeSelectALL.setText(_translate("DSettings_Dialog", "Deselect All"))
        self.checkBox_PERP.setToolTip(_translate("DSettings_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Perpendicular OSnap: orthogonal projection of a given point on a segment.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/qad/icons/dsettings/OSNAP_ToolTIP_PERP.png\" /></p></body></html>"))
        self.checkBox_PERP.setText(_translate("DSettings_Dialog", "Perpendicular"))
        self.checkBox_TANP.setToolTip(_translate("DSettings_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">tangent point on a curve of a line passing through a given point.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/qad/icons/dsettings/OSNAP_ToolTIP_TANP.png\" /></p></body></html>"))
        self.checkBox_TANP.setText(_translate("DSettings_Dialog", "Tangent"))
        self.checkBox_EXTP.setToolTip(_translate("DSettings_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Extension OSnap: point on the segment extension until the cursor position.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/qad/icons/dsettings/OSNAP_ToolTIP_EXTP.png\" /></p></body></html>"))
        self.checkBox_EXTP.setText(_translate("DSettings_Dialog", "Extend"))
        self.checkBox_PARALP.setToolTip(_translate("DSettings_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Parallel OSnap: point on a line, passing through a given point, parallel to a segment.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/qad/icons/dsettings/OSNAP_ToolTIP_PARLP.png\" /></p></body></html>"))
        self.checkBox_PARALP.setText(_translate("DSettings_Dialog", "Parallel"))
        self.checkBox_PROGRESP.setToolTip(_translate("DSettings_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Progressive OSnap: point at a given distance along a geometry line: from a vertex we can set a point at a distance measured along the geometry line.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/qad/icons/dsettings/OSNAP_ToolTIP_PROGRESP.png\" /></p></body></html>"))
        self.checkBox_PROGRESP.setText(_translate("DSettings_Dialog", "Progressive"))
        self.checkBox_EXT_INT.setToolTip(_translate("DSettings_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Intersection on extension OSnap: intersection point of the extensions of two segments.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/qad/icons/dsettings/OSNAP_ToolTIP_EXTINT.png\" /></p></body></html>"))
        self.checkBox_EXT_INT.setText(_translate("DSettings_Dialog", "Intersection on extension"))
        self.checkBox_QUADP.setToolTip(_translate("DSettings_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Quadrant OSnap: intersections of the cartesian axis with a circumference of a circle or an arc.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/qad/icons/dsettings/OSNAP_ToolTIP_QUADP.png\" /></p></body></html>"))
        self.checkBox_QUADP.setText(_translate("DSettings_Dialog", "Quadrant"))
        self.checkBox_END_PLINE.setToolTip(_translate("DSettings_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Start / End OSnap: starting and ending vertices of a linear geometry.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/qad/icons/dsettings/OSNAP_ToolTIP_END_PLINE.png\" /></p></body></html>"))
        self.checkBox_END_PLINE.setText(_translate("DSettings_Dialog", "Start / End"))
        self.checkBox_ENDP.setToolTip(_translate("DSettings_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Start / End segment OSnap: starting and ending vertices of each segment of a geometry.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/qad/icons/dsettings/OSNAP_ToolTIP_ENDP.png\" /></p></body></html>", "aa"))
        self.checkBox_ENDP.setText(_translate("DSettings_Dialog", "Segment Start / End"))
        self.checkBox_MIDP.setToolTip(_translate("DSettings_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Middle point OSnap: middle point of each segment of a geometry.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/qad/icons/dsettings/OSNAP_ToolTIP_MIDP.png\" /></p></body></html>"))
        self.checkBox_MIDP.setText(_translate("DSettings_Dialog", "Middle point"))
        self.checkBox_INTP.setToolTip(_translate("DSettings_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Intersection OSnap: intersection between two segments.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/qad/icons/dsettings/OSNAP_ToolTIP_INTP.png\" /></p></body></html>"))
        self.checkBox_INTP.setText(_translate("DSettings_Dialog", "Intersection"))
        self.checkBox_CENP.setToolTip(_translate("DSettings_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Center OSnap: center of a circle or arc or centroid of an areal geometry.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/qad/icons/dsettings/OSNAP_ToolTIP_CENP.png\" /></p></body></html>"))
        self.checkBox_CENP.setText(_translate("DSettings_Dialog", "Center"))
        self.checkBox_NODP.setToolTip(_translate("DSettings_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Node OSnap: coordinate of a punctual geometry.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/qad/icons/dsettings/OSNAP_ToolTIP_NODP.png\" /></p></body></html>"))
        self.checkBox_NODP.setText(_translate("DSettings_Dialog", "Node"))
        self.checkBox_NEARP.setToolTip(_translate("DSettings_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Near OSnap: point of a segment close to the cursor position.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/qad/icons/dsettings/OSNAP_ToolTIP_NEARP.png\" /></p></body></html>"))
        self.checkBox_NEARP.setText(_translate("DSettings_Dialog", "Near"))
        self.checkBox_IsOsnapON.setToolTip(_translate("DSettings_Dialog", "<html><head/><body><p>Turns object snap on and off. The selected object snap modes are active when the object snap is activated (system variable OSMODE).</p></body></html>"))
        self.checkBox_IsOsnapON.setText(_translate("DSettings_Dialog", "Object Snap (F3)"))
        self.checkBox_ObjectSnapTracking.setToolTip(_translate("DSettings_Dialog", "<html><head/><body><p>Turns object snap tracking on and off. Using the object snap tracking, the cursor can track along alignment paths that are based on object snap points. To use the object snap tracking, select one or more object snap (system variable AUTOSNAP).</p></body></html>"))
        self.checkBox_ObjectSnapTracking.setText(_translate("DSettings_Dialog", "Object Snap Tracking (F11)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("DSettings_Dialog", "Object Snap"))
        self.checkBox_PolarPickPoint.setToolTip(_translate("DSettings_Dialog", "Turns polar tracking on and off (system variable AUTOSNAP)."))
        self.checkBox_PolarPickPoint.setText(_translate("DSettings_Dialog", "Polar Tracking (F10)"))
        self.groupBox_PolarAngleSettings.setTitle(_translate("DSettings_Dialog", "Polar angle settings"))
        self.label_12.setText(_translate("DSettings_Dialog", "Increment angle:"))
        self.groupBox_OsnapPolarOrtho.setTitle(_translate("DSettings_Dialog", "Object Snap Tracking Settings"))
        self.radioButton_OsnapOrtho.setToolTip(_translate("DSettings_Dialog", "Displays only orthogonal (horizontal/vertical) object snap tracking paths for acquired object snap points when object snap tracking is on (POLARMODE system variable)."))
        self.radioButton_OsnapOrtho.setText(_translate("DSettings_Dialog", "Track orthogonally only"))
        self.radioButton_OsnapPolarAngle.setToolTip(_translate("DSettings_Dialog", "Applies polar tracking settings to object snap tracking. When you use object snap tracking, the cursor tracks along polar alignment angles from acquired object snap points (POLARMODE system variable)."))
        self.radioButton_OsnapPolarAngle.setText(_translate("DSettings_Dialog", "Track using polar angle settings"))
        self.groupBox_OsnapPolarMeasurement.setTitle(_translate("DSettings_Dialog", "Polar Angle measurement"))
        self.radioButton_OsnapPolarAbolute.setToolTip(_translate("DSettings_Dialog", "Bases polar tracking angles on the current user coordinate system."))
        self.radioButton_OsnapPolarAbolute.setText(_translate("DSettings_Dialog", "Absolute"))
        self.radioButton_OsnapPolarRelative.setToolTip(_translate("DSettings_Dialog", "Bases polar tracking angles on the last segment drawn."))
        self.radioButton_OsnapPolarRelative.setText(_translate("DSettings_Dialog", "Relative to last segment"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("DSettings_Dialog", "Polar Tracking"))
        self.okButton.setText(_translate("DSettings_Dialog", "OK"))
        self.cancelButton.setText(_translate("DSettings_Dialog", "Cancel"))
        self.pushButton_HELP.setText(_translate("DSettings_Dialog", "?"))
import qad_dsettings_rc
