# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qad_dimstyle_details.ui'
#
# Created: Wed Oct 12 11:24:05 2016
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from qgis.PyQt import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_DimStyle_Details_Dialog(object):
    def setupUi(self, DimStyle_Details_Dialog):
        DimStyle_Details_Dialog.setObjectName(_fromUtf8("DimStyle_Details_Dialog"))
        DimStyle_Details_Dialog.resize(600, 446)
        DimStyle_Details_Dialog.setMinimumSize(QtCore.QSize(600, 446))
        DimStyle_Details_Dialog.setMaximumSize(QtCore.QSize(600, 446))
        self.tabWidget = QtGui.QTabWidget(DimStyle_Details_Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 581, 391))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.DBTab = QtGui.QWidget()
        self.DBTab.setObjectName(_fromUtf8("DBTab"))
        self.groupBox_5 = QtGui.QGroupBox(self.DBTab)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 10, 271, 81))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_2 = QtGui.QLabel(self.groupBox_5)
        self.label_2.setGeometry(QtCore.QRect(12, 20, 61, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.linearLayerName = QtGui.QComboBox(self.groupBox_5)
        self.linearLayerName.setGeometry(QtCore.QRect(80, 20, 181, 22))
        self.linearLayerName.setObjectName(_fromUtf8("linearLayerName"))
        self.lineTypeFieldName = QtGui.QComboBox(self.groupBox_5)
        self.lineTypeFieldName.setGeometry(QtCore.QRect(120, 50, 141, 22))
        self.lineTypeFieldName.setObjectName(_fromUtf8("lineTypeFieldName"))
        self.label_21 = QtGui.QLabel(self.groupBox_5)
        self.label_21.setGeometry(QtCore.QRect(10, 50, 101, 21))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.groupBox_6 = QtGui.QGroupBox(self.DBTab)
        self.groupBox_6.setGeometry(QtCore.QRect(9, 100, 271, 111))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.symbolLayerName = QtGui.QComboBox(self.groupBox_6)
        self.symbolLayerName.setGeometry(QtCore.QRect(80, 20, 181, 22))
        self.symbolLayerName.setObjectName(_fromUtf8("symbolLayerName"))
        self.label_13 = QtGui.QLabel(self.groupBox_6)
        self.label_13.setGeometry(QtCore.QRect(10, 20, 61, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_22 = QtGui.QLabel(self.groupBox_6)
        self.label_22.setGeometry(QtCore.QRect(10, 50, 101, 21))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.symbolFieldName = QtGui.QComboBox(self.groupBox_6)
        self.symbolFieldName.setGeometry(QtCore.QRect(120, 50, 141, 22))
        self.symbolFieldName.setObjectName(_fromUtf8("symbolFieldName"))
        self.scaleFieldName = QtGui.QComboBox(self.groupBox_6)
        self.scaleFieldName.setGeometry(QtCore.QRect(120, 80, 141, 22))
        self.scaleFieldName.setObjectName(_fromUtf8("scaleFieldName"))
        self.label_23 = QtGui.QLabel(self.groupBox_6)
        self.label_23.setGeometry(QtCore.QRect(10, 80, 101, 21))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.groupBox_7 = QtGui.QGroupBox(self.DBTab)
        self.groupBox_7.setGeometry(QtCore.QRect(290, 220, 271, 141))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.label_24 = QtGui.QLabel(self.groupBox_7)
        self.label_24.setGeometry(QtCore.QRect(10, 50, 91, 21))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.rotFieldName = QtGui.QComboBox(self.groupBox_7)
        self.rotFieldName.setGeometry(QtCore.QRect(110, 50, 141, 22))
        self.rotFieldName.setObjectName(_fromUtf8("rotFieldName"))
        self.label_16 = QtGui.QLabel(self.groupBox_7)
        self.label_16.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.colorFieldName = QtGui.QComboBox(self.groupBox_7)
        self.colorFieldName.setGeometry(QtCore.QRect(110, 20, 141, 22))
        self.colorFieldName.setObjectName(_fromUtf8("colorFieldName"))
        self.label_28 = QtGui.QLabel(self.groupBox_7)
        self.label_28.setGeometry(QtCore.QRect(10, 110, 91, 21))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.idParentFieldName = QtGui.QComboBox(self.groupBox_7)
        self.idParentFieldName.setGeometry(QtCore.QRect(110, 110, 141, 22))
        self.idParentFieldName.setObjectName(_fromUtf8("idParentFieldName"))
        self.label_25 = QtGui.QLabel(self.groupBox_7)
        self.label_25.setGeometry(QtCore.QRect(10, 80, 91, 21))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.componentFieldName = QtGui.QComboBox(self.groupBox_7)
        self.componentFieldName.setGeometry(QtCore.QRect(110, 80, 141, 22))
        self.componentFieldName.setObjectName(_fromUtf8("componentFieldName"))
        self.groupBox_8 = QtGui.QGroupBox(self.DBTab)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 220, 271, 141))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.label_27 = QtGui.QLabel(self.groupBox_8)
        self.label_27.setGeometry(QtCore.QRect(10, 50, 101, 21))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.idFieldName = QtGui.QComboBox(self.groupBox_8)
        self.idFieldName.setGeometry(QtCore.QRect(120, 50, 141, 22))
        self.idFieldName.setObjectName(_fromUtf8("idFieldName"))
        self.dimStyleFieldName = QtGui.QComboBox(self.groupBox_8)
        self.dimStyleFieldName.setGeometry(QtCore.QRect(120, 80, 141, 22))
        self.dimStyleFieldName.setObjectName(_fromUtf8("dimStyleFieldName"))
        self.label_29 = QtGui.QLabel(self.groupBox_8)
        self.label_29.setGeometry(QtCore.QRect(10, 80, 101, 21))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.label_30 = QtGui.QLabel(self.groupBox_8)
        self.label_30.setGeometry(QtCore.QRect(10, 110, 101, 21))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.dimTypeFieldName = QtGui.QComboBox(self.groupBox_8)
        self.dimTypeFieldName.setGeometry(QtCore.QRect(120, 110, 141, 22))
        self.dimTypeFieldName.setObjectName(_fromUtf8("dimTypeFieldName"))
        self.label_14 = QtGui.QLabel(self.groupBox_8)
        self.label_14.setGeometry(QtCore.QRect(10, 20, 61, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.textualLayerName = QtGui.QComboBox(self.groupBox_8)
        self.textualLayerName.setGeometry(QtCore.QRect(80, 20, 181, 22))
        self.textualLayerName.setObjectName(_fromUtf8("textualLayerName"))
        self.previewDummy = QtGui.QPushButton(self.DBTab)
        self.previewDummy.setGeometry(QtCore.QRect(300, 20, 251, 181))
        self.previewDummy.setText(_fromUtf8(""))
        self.previewDummy.setObjectName(_fromUtf8("previewDummy"))
        self.tabWidget.addTab(self.DBTab, _fromUtf8(""))
        self.LineTab = QtGui.QWidget()
        self.LineTab.setObjectName(_fromUtf8("LineTab"))
        self.groupBox = QtGui.QGroupBox(self.LineTab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 271, 141))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 51, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.dimLineLineType = QtGui.QLineEdit(self.groupBox)
        self.dimLineLineType.setGeometry(QtCore.QRect(80, 50, 181, 20))
        self.dimLineLineType.setObjectName(_fromUtf8("dimLineLineType"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 61, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 61, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.dimLine1Hide = QtGui.QCheckBox(self.groupBox)
        self.dimLine1Hide.setGeometry(QtCore.QRect(70, 110, 91, 21))
        self.dimLine1Hide.setObjectName(_fromUtf8("dimLine1Hide"))
        self.dimLine2Hide = QtGui.QCheckBox(self.groupBox)
        self.dimLine2Hide.setGeometry(QtCore.QRect(170, 110, 91, 21))
        self.dimLine2Hide.setObjectName(_fromUtf8("dimLine2Hide"))
        self.dimLineColorDummy = QtGui.QPushButton(self.groupBox)
        self.dimLineColorDummy.setGeometry(QtCore.QRect(80, 20, 181, 23))
        self.dimLineColorDummy.setText(_fromUtf8(""))
        self.dimLineColorDummy.setObjectName(_fromUtf8("dimLineColorDummy"))
        self.groupBox_2 = QtGui.QGroupBox(self.LineTab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 210, 551, 141))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(11, 20, 51, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.extLine1LineType = QtGui.QLineEdit(self.groupBox_2)
        self.extLine1LineType.setGeometry(QtCore.QRect(100, 50, 171, 20))
        self.extLine1LineType.setObjectName(_fromUtf8("extLine1LineType"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 81, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 80, 81, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.extLine2LineType = QtGui.QLineEdit(self.groupBox_2)
        self.extLine2LineType.setGeometry(QtCore.QRect(100, 80, 171, 20))
        self.extLine2LineType.setObjectName(_fromUtf8("extLine2LineType"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(10, 110, 61, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.extLine1Hide = QtGui.QCheckBox(self.groupBox_2)
        self.extLine1Hide.setGeometry(QtCore.QRect(80, 110, 91, 21))
        self.extLine1Hide.setObjectName(_fromUtf8("extLine1Hide"))
        self.extLine2Hide = QtGui.QCheckBox(self.groupBox_2)
        self.extLine2Hide.setGeometry(QtCore.QRect(180, 110, 91, 21))
        self.extLine2Hide.setObjectName(_fromUtf8("extLine2Hide"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(300, 20, 151, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.extLineOffsetDimLine = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.extLineOffsetDimLine.setGeometry(QtCore.QRect(460, 20, 81, 22))
        self.extLineOffsetDimLine.setDecimals(6)
        self.extLineOffsetDimLine.setMaximum(1000000.0)
        self.extLineOffsetDimLine.setSingleStep(0.0005)
        self.extLineOffsetDimLine.setObjectName(_fromUtf8("extLineOffsetDimLine"))
        self.extLineOffsetOrigPoints = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.extLineOffsetOrigPoints.setGeometry(QtCore.QRect(460, 50, 81, 22))
        self.extLineOffsetOrigPoints.setDecimals(6)
        self.extLineOffsetOrigPoints.setMaximum(1000000.0)
        self.extLineOffsetOrigPoints.setSingleStep(0.0005)
        self.extLineOffsetOrigPoints.setObjectName(_fromUtf8("extLineOffsetOrigPoints"))
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(300, 50, 151, 21))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.extLineIsFixedLen = QtGui.QCheckBox(self.groupBox_2)
        self.extLineIsFixedLen.setGeometry(QtCore.QRect(300, 80, 241, 21))
        self.extLineIsFixedLen.setObjectName(_fromUtf8("extLineIsFixedLen"))
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(300, 110, 151, 21))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.extLineFixedLen = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.extLineFixedLen.setGeometry(QtCore.QRect(460, 110, 81, 22))
        self.extLineFixedLen.setDecimals(6)
        self.extLineFixedLen.setMaximum(1000000.0)
        self.extLineFixedLen.setSingleStep(0.0005)
        self.extLineFixedLen.setObjectName(_fromUtf8("extLineFixedLen"))
        self.extLineColorDummy = QtGui.QPushButton(self.groupBox_2)
        self.extLineColorDummy.setGeometry(QtCore.QRect(80, 20, 191, 23))
        self.extLineColorDummy.setText(_fromUtf8(""))
        self.extLineColorDummy.setObjectName(_fromUtf8("extLineColorDummy"))
        self.tabWidget.addTab(self.LineTab, _fromUtf8(""))
        self.SymbolTab = QtGui.QWidget()
        self.SymbolTab.setObjectName(_fromUtf8("SymbolTab"))
        self.groupBox_3 = QtGui.QGroupBox(self.SymbolTab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 271, 171))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.block1Name = QtGui.QLineEdit(self.groupBox_3)
        self.block1Name.setGeometry(QtCore.QRect(110, 20, 151, 20))
        self.block1Name.setObjectName(_fromUtf8("block1Name"))
        self.label_15 = QtGui.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.block2Name = QtGui.QLineEdit(self.groupBox_3)
        self.block2Name.setGeometry(QtCore.QRect(110, 50, 151, 20))
        self.block2Name.setObjectName(_fromUtf8("block2Name"))
        self.label_18 = QtGui.QLabel(self.groupBox_3)
        self.label_18.setGeometry(QtCore.QRect(10, 50, 91, 21))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.blockLeaderName = QtGui.QLineEdit(self.groupBox_3)
        self.blockLeaderName.setGeometry(QtCore.QRect(110, 80, 151, 20))
        self.blockLeaderName.setObjectName(_fromUtf8("blockLeaderName"))
        self.label_19 = QtGui.QLabel(self.groupBox_3)
        self.label_19.setGeometry(QtCore.QRect(10, 80, 91, 21))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.blockWidth = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.blockWidth.setGeometry(QtCore.QRect(180, 110, 81, 22))
        self.blockWidth.setDecimals(6)
        self.blockWidth.setMaximum(1000000.0)
        self.blockWidth.setSingleStep(0.0005)
        self.blockWidth.setObjectName(_fromUtf8("blockWidth"))
        self.label_17 = QtGui.QLabel(self.groupBox_3)
        self.label_17.setGeometry(QtCore.QRect(10, 110, 111, 21))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.blockScale = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.blockScale.setGeometry(QtCore.QRect(180, 140, 81, 22))
        self.blockScale.setDecimals(6)
        self.blockScale.setMaximum(1000000.0)
        self.blockScale.setSingleStep(0.0005)
        self.blockScale.setObjectName(_fromUtf8("blockScale"))
        self.label_20 = QtGui.QLabel(self.groupBox_3)
        self.label_20.setGeometry(QtCore.QRect(10, 140, 111, 21))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.groupBox_4 = QtGui.QGroupBox(self.SymbolTab)
        self.groupBox_4.setGeometry(QtCore.QRect(310, 220, 241, 81))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.arcSymbolPreceding = QtGui.QRadioButton(self.groupBox_4)
        self.arcSymbolPreceding.setGeometry(QtCore.QRect(10, 20, 221, 17))
        self.arcSymbolPreceding.setObjectName(_fromUtf8("arcSymbolPreceding"))
        self.arcSymbolAbove = QtGui.QRadioButton(self.groupBox_4)
        self.arcSymbolAbove.setGeometry(QtCore.QRect(10, 40, 221, 17))
        self.arcSymbolAbove.setObjectName(_fromUtf8("arcSymbolAbove"))
        self.arcSymbolNone = QtGui.QRadioButton(self.groupBox_4)
        self.arcSymbolNone.setGeometry(QtCore.QRect(10, 60, 221, 17))
        self.arcSymbolNone.setObjectName(_fromUtf8("arcSymbolNone"))
        self.tabWidget.addTab(self.SymbolTab, _fromUtf8(""))
        self.TextTab = QtGui.QWidget()
        self.TextTab.setObjectName(_fromUtf8("TextTab"))
        self.groupBox_9 = QtGui.QGroupBox(self.TextTab)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 10, 271, 111))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.label_26 = QtGui.QLabel(self.groupBox_9)
        self.label_26.setGeometry(QtCore.QRect(10, 80, 111, 21))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.textHeight = QtGui.QDoubleSpinBox(self.groupBox_9)
        self.textHeight.setGeometry(QtCore.QRect(180, 80, 81, 22))
        self.textHeight.setDecimals(6)
        self.textHeight.setMaximum(1000000.0)
        self.textHeight.setSingleStep(0.0005)
        self.textHeight.setObjectName(_fromUtf8("textHeight"))
        self.label_40 = QtGui.QLabel(self.groupBox_9)
        self.label_40.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.textFont = QtGui.QFontComboBox(self.groupBox_9)
        self.textFont.setGeometry(QtCore.QRect(100, 20, 161, 22))
        self.textFont.setObjectName(_fromUtf8("textFont"))
        self.textColorDummy = QtGui.QPushButton(self.groupBox_9)
        self.textColorDummy.setGeometry(QtCore.QRect(80, 50, 181, 23))
        self.textColorDummy.setText(_fromUtf8(""))
        self.textColorDummy.setObjectName(_fromUtf8("textColorDummy"))
        self.label_4 = QtGui.QLabel(self.groupBox_9)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 51, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.groupBox_10 = QtGui.QGroupBox(self.TextTab)
        self.groupBox_10.setGeometry(QtCore.QRect(10, 220, 281, 141))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.textVerticalPos = QtGui.QComboBox(self.groupBox_10)
        self.textVerticalPos.setGeometry(QtCore.QRect(110, 20, 161, 22))
        self.textVerticalPos.setObjectName(_fromUtf8("textVerticalPos"))
        self.label_31 = QtGui.QLabel(self.groupBox_10)
        self.label_31.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.label_32 = QtGui.QLabel(self.groupBox_10)
        self.label_32.setGeometry(QtCore.QRect(10, 50, 91, 21))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.textHorizontalPos = QtGui.QComboBox(self.groupBox_10)
        self.textHorizontalPos.setGeometry(QtCore.QRect(110, 50, 161, 22))
        self.textHorizontalPos.setObjectName(_fromUtf8("textHorizontalPos"))
        self.label_33 = QtGui.QLabel(self.groupBox_10)
        self.label_33.setGeometry(QtCore.QRect(10, 80, 91, 21))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.textDirection = QtGui.QComboBox(self.groupBox_10)
        self.textDirection.setGeometry(QtCore.QRect(110, 80, 161, 22))
        self.textDirection.setObjectName(_fromUtf8("textDirection"))
        self.textOffsetDist = QtGui.QDoubleSpinBox(self.groupBox_10)
        self.textOffsetDist.setGeometry(QtCore.QRect(190, 110, 81, 22))
        self.textOffsetDist.setDecimals(6)
        self.textOffsetDist.setMaximum(1000000.0)
        self.textOffsetDist.setSingleStep(0.0005)
        self.textOffsetDist.setObjectName(_fromUtf8("textOffsetDist"))
        self.label_34 = QtGui.QLabel(self.groupBox_10)
        self.label_34.setGeometry(QtCore.QRect(10, 110, 171, 21))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.textAlignment_groupBox = QtGui.QGroupBox(self.TextTab)
        self.textAlignment_groupBox.setGeometry(QtCore.QRect(310, 250, 251, 111))
        self.textAlignment_groupBox.setObjectName(_fromUtf8("textAlignment_groupBox"))
        self.textRotModeHorizontal = QtGui.QRadioButton(self.textAlignment_groupBox)
        self.textRotModeHorizontal.setGeometry(QtCore.QRect(10, 20, 251, 17))
        self.textRotModeHorizontal.setObjectName(_fromUtf8("textRotModeHorizontal"))
        self.textRotModeAligned = QtGui.QRadioButton(self.textAlignment_groupBox)
        self.textRotModeAligned.setGeometry(QtCore.QRect(10, 40, 251, 17))
        self.textRotModeAligned.setObjectName(_fromUtf8("textRotModeAligned"))
        self.textRotModeISO = QtGui.QRadioButton(self.textAlignment_groupBox)
        self.textRotModeISO.setGeometry(QtCore.QRect(10, 60, 251, 17))
        self.textRotModeISO.setObjectName(_fromUtf8("textRotModeISO"))
        self.textRotModeFixedRot = QtGui.QRadioButton(self.textAlignment_groupBox)
        self.textRotModeFixedRot.setGeometry(QtCore.QRect(10, 80, 101, 17))
        self.textRotModeFixedRot.setObjectName(_fromUtf8("textRotModeFixedRot"))
        self.textForcedRot = QtGui.QDoubleSpinBox(self.textAlignment_groupBox)
        self.textForcedRot.setGeometry(QtCore.QRect(160, 80, 81, 22))
        self.textForcedRot.setDecimals(6)
        self.textForcedRot.setMaximum(360.0)
        self.textForcedRot.setSingleStep(0.0005)
        self.textForcedRot.setObjectName(_fromUtf8("textForcedRot"))
        self.tabWidget.addTab(self.TextTab, _fromUtf8(""))
        self.AdjustTab = QtGui.QWidget()
        self.AdjustTab.setObjectName(_fromUtf8("AdjustTab"))
        self.groupBox_12 = QtGui.QGroupBox(self.AdjustTab)
        self.groupBox_12.setGeometry(QtCore.QRect(10, 10, 271, 211))
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.label_35 = QtGui.QLabel(self.groupBox_12)
        self.label_35.setGeometry(QtCore.QRect(10, 20, 251, 51))
        self.label_35.setWordWrap(True)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.textBlockAdjustWhicheverFitsBestOutside = QtGui.QRadioButton(self.groupBox_12)
        self.textBlockAdjustWhicheverFitsBestOutside.setGeometry(QtCore.QRect(10, 80, 251, 17))
        self.textBlockAdjustWhicheverFitsBestOutside.setObjectName(_fromUtf8("textBlockAdjustWhicheverFitsBestOutside"))
        self.textBlockAdjustFirstSymbolOutside = QtGui.QRadioButton(self.groupBox_12)
        self.textBlockAdjustFirstSymbolOutside.setGeometry(QtCore.QRect(10, 100, 251, 17))
        self.textBlockAdjustFirstSymbolOutside.setObjectName(_fromUtf8("textBlockAdjustFirstSymbolOutside"))
        self.textBlockAdjustFirstTextOutside = QtGui.QRadioButton(self.groupBox_12)
        self.textBlockAdjustFirstTextOutside.setGeometry(QtCore.QRect(10, 120, 251, 17))
        self.textBlockAdjustFirstTextOutside.setObjectName(_fromUtf8("textBlockAdjustFirstTextOutside"))
        self.textBlockAdjustBothOutside = QtGui.QRadioButton(self.groupBox_12)
        self.textBlockAdjustBothOutside.setGeometry(QtCore.QRect(10, 140, 251, 17))
        self.textBlockAdjustBothOutside.setObjectName(_fromUtf8("textBlockAdjustBothOutside"))
        self.blockSuppressionForNoSpace = QtGui.QCheckBox(self.groupBox_12)
        self.blockSuppressionForNoSpace.setGeometry(QtCore.QRect(10, 160, 251, 51))
        self.blockSuppressionForNoSpace.setObjectName(_fromUtf8("blockSuppressionForNoSpace"))
        self.tabWidget.addTab(self.AdjustTab, _fromUtf8(""))
        self.PrimaryUnitTab = QtGui.QWidget()
        self.PrimaryUnitTab.setObjectName(_fromUtf8("PrimaryUnitTab"))
        self.groupBox_13 = QtGui.QGroupBox(self.PrimaryUnitTab)
        self.groupBox_13.setGeometry(QtCore.QRect(10, 10, 271, 141))
        self.groupBox_13.setObjectName(_fromUtf8("groupBox_13"))
        self.label_36 = QtGui.QLabel(self.groupBox_13)
        self.label_36.setGeometry(QtCore.QRect(10, 20, 81, 21))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.textDecimals = QtGui.QComboBox(self.groupBox_13)
        self.textDecimals.setGeometry(QtCore.QRect(100, 20, 161, 22))
        self.textDecimals.setObjectName(_fromUtf8("textDecimals"))
        self.textDecimalSep = QtGui.QComboBox(self.groupBox_13)
        self.textDecimalSep.setGeometry(QtCore.QRect(170, 50, 91, 22))
        self.textDecimalSep.setObjectName(_fromUtf8("textDecimalSep"))
        self.label_37 = QtGui.QLabel(self.groupBox_13)
        self.label_37.setGeometry(QtCore.QRect(10, 50, 111, 21))
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.textPrefix = QtGui.QLineEdit(self.groupBox_13)
        self.textPrefix.setGeometry(QtCore.QRect(110, 80, 151, 20))
        self.textPrefix.setObjectName(_fromUtf8("textPrefix"))
        self.label_38 = QtGui.QLabel(self.groupBox_13)
        self.label_38.setGeometry(QtCore.QRect(10, 80, 91, 21))
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.label_39 = QtGui.QLabel(self.groupBox_13)
        self.label_39.setGeometry(QtCore.QRect(10, 110, 91, 21))
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.textSuffix = QtGui.QLineEdit(self.groupBox_13)
        self.textSuffix.setGeometry(QtCore.QRect(110, 110, 151, 20))
        self.textSuffix.setObjectName(_fromUtf8("textSuffix"))
        self.groupBox_14 = QtGui.QGroupBox(self.PrimaryUnitTab)
        self.groupBox_14.setGeometry(QtCore.QRect(10, 160, 271, 51))
        self.groupBox_14.setObjectName(_fromUtf8("groupBox_14"))
        self.textSuppressLeadingZeros = QtGui.QCheckBox(self.groupBox_14)
        self.textSuppressLeadingZeros.setGeometry(QtCore.QRect(20, 20, 70, 17))
        self.textSuppressLeadingZeros.setObjectName(_fromUtf8("textSuppressLeadingZeros"))
        self.textDecimalZerosSuppression = QtGui.QCheckBox(self.groupBox_14)
        self.textDecimalZerosSuppression.setGeometry(QtCore.QRect(170, 20, 70, 17))
        self.textDecimalZerosSuppression.setObjectName(_fromUtf8("textDecimalZerosSuppression"))
        self.tabWidget.addTab(self.PrimaryUnitTab, _fromUtf8(""))
        self.layoutWidget = QtGui.QWidget(DimStyle_Details_Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(350, 410, 239, 25))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.okButton = QtGui.QPushButton(self.layoutWidget)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout.addWidget(self.okButton)
        self.cancelButton = QtGui.QPushButton(self.layoutWidget)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.helpButton = QtGui.QPushButton(self.layoutWidget)
        self.helpButton.setObjectName(_fromUtf8("helpButton"))
        self.horizontalLayout.addWidget(self.helpButton)

        self.retranslateUi(DimStyle_Details_Dialog)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QObject.connect(self.linearLayerName, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")),
                               DimStyle_Details_Dialog.linearLayerNameChanged)
        QtCore.QObject.connect(self.symbolLayerName, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")),
                               DimStyle_Details_Dialog.symbolLayerNameChanged)
        QtCore.QObject.connect(self.textualLayerName, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")),
                               DimStyle_Details_Dialog.textualLayerNameChanged)
        QtCore.QObject.connect(self.textRotModeFixedRot, QtCore.SIGNAL(_fromUtf8("toggled(bool)")),
                               DimStyle_Details_Dialog.textRotModeFixedRotToggled)
        QtCore.QObject.connect(self.extLineIsFixedLen, QtCore.SIGNAL(_fromUtf8("toggled(bool)")),
                               DimStyle_Details_Dialog.extLineIsFixedLenToggled)
        QtCore.QObject.connect(self.helpButton, QtCore.SIGNAL(_fromUtf8("clicked()")),
                               DimStyle_Details_Dialog.ButtonHELP_Pressed)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), DimStyle_Details_Dialog.accept)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), DimStyle_Details_Dialog.reject)
        QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL(_fromUtf8("currentChanged(int)")),
                               DimStyle_Details_Dialog.currentTabChanged)
        QtCore.QObject.connect(self.lineTypeFieldName, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")),
                               DimStyle_Details_Dialog.linetypeFieldNameChanged)
        QtCore.QObject.connect(self.symbolFieldName, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")),
                               DimStyle_Details_Dialog.symbolFieldNameChanged)
        QtCore.QObject.connect(self.scaleFieldName, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")),
                               DimStyle_Details_Dialog.scaleFieldNameChanged)
        QtCore.QObject.connect(self.idFieldName, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")),
                               DimStyle_Details_Dialog.idFieldNameChanged)
        QtCore.QObject.connect(self.dimStyleFieldName, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")),
                               DimStyle_Details_Dialog.dimStyleFieldNameChanged)
        QtCore.QObject.connect(self.dimTypeFieldName, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")),
                               DimStyle_Details_Dialog.dimTypeFieldNameChanged)
        QtCore.QObject.connect(self.colorFieldName, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")),
                               DimStyle_Details_Dialog.colorFieldNameChanged)
        QtCore.QObject.connect(self.rotFieldName, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")),
                               DimStyle_Details_Dialog.rotFieldNameChanged)
        QtCore.QObject.connect(self.componentFieldName, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")),
                               DimStyle_Details_Dialog.componentFieldNameChanged)
        QtCore.QObject.connect(self.idParentFieldName, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")),
                               DimStyle_Details_Dialog.idParentFieldNameChanged)
        QtCore.QObject.connect(self.dimLineLineType, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")),
                               DimStyle_Details_Dialog.dimLineLineTypeChanged)
        QtCore.QObject.connect(self.dimLine1Hide, QtCore.SIGNAL(_fromUtf8("toggled(bool)")),
                               DimStyle_Details_Dialog.dimLine1HideToggled)
        QtCore.QObject.connect(self.dimLine2Hide, QtCore.SIGNAL(_fromUtf8("toggled(bool)")),
                               DimStyle_Details_Dialog.dimLine2HideToggled)
        QtCore.QObject.connect(self.extLine1LineType, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")),
                               DimStyle_Details_Dialog.extLine1LineTypeChanged)
        QtCore.QObject.connect(self.extLine2LineType, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")),
                               DimStyle_Details_Dialog.extLine2LineTypeChanged)
        QtCore.QObject.connect(self.extLine1Hide, QtCore.SIGNAL(_fromUtf8("toggled(bool)")),
                               DimStyle_Details_Dialog.extLine1HideToggled)
        QtCore.QObject.connect(self.extLine2Hide, QtCore.SIGNAL(_fromUtf8("toggled(bool)")),
                               DimStyle_Details_Dialog.extLine2HideToggled)
        QtCore.QObject.connect(self.extLineOffsetDimLine, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")),
                               DimStyle_Details_Dialog.extLineOffsetDimLineChanged)
        QtCore.QObject.connect(self.extLineOffsetOrigPoints, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")),
                               DimStyle_Details_Dialog.extLineOffsetOrigPointsChanged)
        QtCore.QObject.connect(self.extLineFixedLen, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")),
                               DimStyle_Details_Dialog.extLineFixedLenChanged)
        QtCore.QObject.connect(self.block1Name, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")),
                               DimStyle_Details_Dialog.block1NameChanged)
        QtCore.QObject.connect(self.block2Name, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")),
                               DimStyle_Details_Dialog.block2NameChanged)
        QtCore.QObject.connect(self.blockLeaderName, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")),
                               DimStyle_Details_Dialog.blockLeaderNameChanged)
        QtCore.QObject.connect(self.blockWidth, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")),
                               DimStyle_Details_Dialog.blockWidthChanged)
        QtCore.QObject.connect(self.blockScale, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")),
                               DimStyle_Details_Dialog.blockScaleChanged)
        QtCore.QObject.connect(self.textFont, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")),
                               DimStyle_Details_Dialog.textFontChanged)
        QtCore.QObject.connect(self.textHeight, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")),
                               DimStyle_Details_Dialog.textHeightChanged)
        QtCore.QObject.connect(self.textVerticalPos, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")),
                               DimStyle_Details_Dialog.textVerticalPosChanged)
        QtCore.QObject.connect(self.textHorizontalPos, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")),
                               DimStyle_Details_Dialog.textHorizontalPosChanged)
        QtCore.QObject.connect(self.textDirection, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")),
                               DimStyle_Details_Dialog.textDirectionChanged)
        QtCore.QObject.connect(self.textOffsetDist, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")),
                               DimStyle_Details_Dialog.textOffsetDistChanged)
        QtCore.QObject.connect(self.textForcedRot, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")),
                               DimStyle_Details_Dialog.textForcedRotChanged)
        QtCore.QObject.connect(self.blockSuppressionForNoSpace, QtCore.SIGNAL(_fromUtf8("toggled(bool)")),
                               DimStyle_Details_Dialog.blockSuppressionForNoSpaceToggled)
        QtCore.QObject.connect(self.textDecimals, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")),
                               DimStyle_Details_Dialog.textDecimalsChanged)
        QtCore.QObject.connect(self.textDecimalSep, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")),
                               DimStyle_Details_Dialog.textDecimalSepChanged)
        QtCore.QObject.connect(self.textPrefix, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")),
                               DimStyle_Details_Dialog.textPrefixChanged)
        QtCore.QObject.connect(self.textSuffix, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")),
                               DimStyle_Details_Dialog.textSuffixChanged)
        QtCore.QObject.connect(self.textSuppressLeadingZeros, QtCore.SIGNAL(_fromUtf8("toggled(bool)")),
                               DimStyle_Details_Dialog.textSuppressLeadingZerosToggled)
        QtCore.QObject.connect(self.textDecimalZerosSuppression, QtCore.SIGNAL(_fromUtf8("toggled(bool)")),
                               DimStyle_Details_Dialog.textDecimalZerosSuppressionToggled)
        QtCore.QObject.connect(self.textRotModeHorizontal, QtCore.SIGNAL(_fromUtf8("toggled(bool)")),
                               DimStyle_Details_Dialog.textRotModeHorizontalToggled)
        QtCore.QObject.connect(self.textRotModeAligned, QtCore.SIGNAL(_fromUtf8("toggled(bool)")),
                               DimStyle_Details_Dialog.textRotModeAlignedToggled)
        QtCore.QObject.connect(self.textRotModeISO, QtCore.SIGNAL(_fromUtf8("toggled(bool)")),
                               DimStyle_Details_Dialog.textRotModeISOToggled)
        QtCore.QObject.connect(self.textBlockAdjustWhicheverFitsBestOutside, QtCore.SIGNAL(_fromUtf8("toggled(bool)")),
                               DimStyle_Details_Dialog.textBlockAdjustWhicheverFitsBestOutsideToggled)
        QtCore.QObject.connect(self.textBlockAdjustFirstSymbolOutside, QtCore.SIGNAL(_fromUtf8("toggled(bool)")),
                               DimStyle_Details_Dialog.textBlockAdjustFirstSymbolOutsideToggled)
        QtCore.QObject.connect(self.textBlockAdjustFirstTextOutside, QtCore.SIGNAL(_fromUtf8("toggled(bool)")),
                               DimStyle_Details_Dialog.textBlockAdjustFirstTextOutsideToggled)
        QtCore.QObject.connect(self.textBlockAdjustBothOutside, QtCore.SIGNAL(_fromUtf8("toggled(bool)")),
                               DimStyle_Details_Dialog.textBlockAdjustBothOutsideToggled)
        QtCore.QObject.connect(self.arcSymbolPreceding, QtCore.SIGNAL(_fromUtf8("toggled(bool)")),
                               DimStyle_Details_Dialog.arcSymbolPrecedingToggled)
        QtCore.QObject.connect(self.arcSymbolAbove, QtCore.SIGNAL(_fromUtf8("toggled(bool)")),
                               DimStyle_Details_Dialog.arcSymbolAboveToggled)
        QtCore.QObject.connect(self.arcSymbolNone, QtCore.SIGNAL(_fromUtf8("toggled(bool)")),
                               DimStyle_Details_Dialog.arcSymbolNoneToggled)
        QtCore.QMetaObject.connectSlotsByName(DimStyle_Details_Dialog)

    def retranslateUi(self, DimStyle_Details_Dialog):
        DimStyle_Details_Dialog.setWindowTitle(
            _translate("DimStyle_Details_Dialog", "QAD - Dimension style details", None))
        self.groupBox_5.setTitle(_translate("DimStyle_Details_Dialog", "Lines", None))
        self.label_2.setText(_translate("DimStyle_Details_Dialog", "Layer:", None))
        self.linearLayerName.setToolTip(
            _translate("DimStyle_Details_Dialog", "Name of the layer for dimension lines.", None))
        self.lineTypeFieldName.setToolTip(
            _translate("DimStyle_Details_Dialog", "Field storing the linetype name.", None))
        self.label_21.setText(_translate("DimStyle_Details_Dialog", "Linetype field:", None))
        self.groupBox_6.setTitle(_translate("DimStyle_Details_Dialog", "Symbols and arrows", None))
        self.symbolLayerName.setToolTip(
            _translate("DimStyle_Details_Dialog", "Name of the layer for dimension symbols and arrows.", None))
        self.label_13.setText(_translate("DimStyle_Details_Dialog", "Layer:", None))
        self.label_22.setText(_translate("DimStyle_Details_Dialog", "Symbol field:", None))
        self.symbolFieldName.setToolTip(_translate("DimStyle_Details_Dialog", "Field storing the symbol name.", None))
        self.scaleFieldName.setToolTip(_translate("DimStyle_Details_Dialog", "Field storing the symbol size.", None))
        self.label_23.setText(_translate("DimStyle_Details_Dialog", "Scale field:", None))
        self.groupBox_7.setTitle(_translate("DimStyle_Details_Dialog", "Generics fields", None))
        self.label_24.setText(_translate("DimStyle_Details_Dialog", "Rotation:", None))
        self.rotFieldName.setToolTip(_translate("DimStyle_Details_Dialog",
                                                "Field storing the rotation of the punctual elements od dimension (symbols, arrows, text).",
                                                None))
        self.label_16.setText(_translate("DimStyle_Details_Dialog", "Color:", None))
        self.colorFieldName.setToolTip(_translate("DimStyle_Details_Dialog",
                                                  "Field storing the RGB colorfor all elements of dimension (e.g. \"255,255,255,255\" = white with total opacity).",
                                                  None))
        self.label_28.setText(_translate("DimStyle_Details_Dialog", "Linking ID:", None))
        self.idParentFieldName.setToolTip(_translate("DimStyle_Details_Dialog",
                                                     "Field storing the ID of the dimension to group all elements (except the text which is the root element).",
                                                     None))
        self.label_25.setText(_translate("DimStyle_Details_Dialog", "Component type:", None))
        self.componentFieldName.setToolTip(_translate("DimStyle_Details_Dialog",
                                                      "<html><head/><body><p>Field storing the component type of dimension:</p><p>&quot;D1&quot; = Dimension line 1.</p><p>&quot;D2&quot; = Dimension line 2.</p><p>&quot;E1&quot; = Extension line 1.</p><p>&quot;E2&quot; = Extension line 2.</p><p>&quot;L&quot;  = Leader.</p><p>&quot;B1&quot; = Block 1.</p><p>&quot;B2&quot; = Block 2.</p><p>&quot;LB&quot; = Leader Block.</p><p>&quot;AB&quot; = Arc Block.</p><p>&quot;D1&quot; = Dimension point 1.</p><p>&quot;D2&quot; = Dimension point 2.</p></body></html>",
                                                      None))
        self.groupBox_8.setTitle(_translate("DimStyle_Details_Dialog", "Text", None))
        self.label_27.setText(_translate("DimStyle_Details_Dialog", "ID Field:", None))
        self.idFieldName.setToolTip(
            _translate("DimStyle_Details_Dialog", "Field storing the unique code for each dimension.", None))
        self.dimStyleFieldName.setToolTip(
            _translate("DimStyle_Details_Dialog", "Field storing the name of the dimension style.", None))
        self.label_29.setText(_translate("DimStyle_Details_Dialog", "Dim. style field:", None))
        self.label_30.setText(_translate("DimStyle_Details_Dialog", "Dim. type field:", None))
        self.dimTypeFieldName.setToolTip(_translate("DimStyle_Details_Dialog",
                                                    "<html><head/><body><p>Field storing the dimension type:</p><p>&quot;AL&quot; = linear dimension that is aligned with the origin points of the extension lines.</p><p>&quot;AN&quot; = angular dimension, it measures the angle between selected objects or 3 points.</p><p>&quot;BL&quot; = linear, angular, or ordinate dimension from the baseline of the previous or selected dimension.</p><p>&quot;CE&quot; = creates the center mark or the centerlines of circles and arcs.</p><p>&quot;DI&quot; = creates a diameter dimension for a circle or an arc.</p><p>&quot;LD&quot; = creates a line that connects annotation to a feature..</p><p>&quot;LI&quot; = linear dimension with a horizontal, vertical, or rotated dimension line.</p><p>&quot;RA&quot; = radial dimension, measures the radius of a selected circle or arc and displays the dimension text with a radius symbol in front of it.</p><p>&quot;AR&quot; = arc length dimensions measure the distance along an arc or polyline arc segment.</p></body></html>",
                                                    None))
        self.label_14.setText(_translate("DimStyle_Details_Dialog", "Layer:", None))
        self.textualLayerName.setToolTip(
            _translate("DimStyle_Details_Dialog", "Name of the layer storing dimension texts.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DBTab), _translate("DimStyle_Details_Dialog", "DB", None))
        self.groupBox.setTitle(_translate("DimStyle_Details_Dialog", "Dimension lines", None))
        self.label.setText(_translate("DimStyle_Details_Dialog", "Color:", None))
        self.dimLineLineType.setToolTip(_translate("DimStyle_Details_Dialog", "Linetype of dimension line.", None))
        self.label_3.setText(_translate("DimStyle_Details_Dialog", "Linetype:", None))
        self.label_5.setText(_translate("DimStyle_Details_Dialog", "Suppress:", None))
        self.dimLine1Hide.setToolTip(
            _translate("DimStyle_Details_Dialog", "Suppresses display of dimension line 1.", None))
        self.dimLine1Hide.setText(_translate("DimStyle_Details_Dialog", "Dim. line 1", None))
        self.dimLine2Hide.setToolTip(
            _translate("DimStyle_Details_Dialog", "Suppresses display of dimension line 2.", None))
        self.dimLine2Hide.setText(_translate("DimStyle_Details_Dialog", "Dim. line 2", None))
        self.groupBox_2.setTitle(_translate("DimStyle_Details_Dialog", "Extension lines", None))
        self.label_6.setText(_translate("DimStyle_Details_Dialog", "Color:", None))
        self.extLine1LineType.setToolTip(_translate("DimStyle_Details_Dialog", "Linetype for extension line 1.", None))
        self.label_7.setText(_translate("DimStyle_Details_Dialog", "Linetype ext. 1:", None))
        self.label_8.setText(_translate("DimStyle_Details_Dialog", "Linetype ext. 2:", None))
        self.extLine2LineType.setToolTip(_translate("DimStyle_Details_Dialog", "Linetype for extension line 2.", None))
        self.label_9.setText(_translate("DimStyle_Details_Dialog", "Suppress:", None))
        self.extLine1Hide.setToolTip(
            _translate("DimStyle_Details_Dialog", "Suppresses display of extension line 1.", None))
        self.extLine1Hide.setText(_translate("DimStyle_Details_Dialog", "Ext. line 1", None))
        self.extLine2Hide.setToolTip(
            _translate("DimStyle_Details_Dialog", "Suppresses display of extension line 2.", None))
        self.extLine2Hide.setText(_translate("DimStyle_Details_Dialog", "Ext. line 2", None))
        self.label_10.setText(_translate("DimStyle_Details_Dialog", "Extend beyond dim lines:", None))
        self.extLineOffsetDimLine.setToolTip(_translate("DimStyle_Details_Dialog",
                                                        "Specifies a distance to extend the extension lines above the dimension line.",
                                                        None))
        self.extLineOffsetOrigPoints.setToolTip(_translate("DimStyle_Details_Dialog",
                                                           "Sets the distance to offset the extension lines from the points on the drawing that define the dimension.",
                                                           None))
        self.label_11.setText(_translate("DimStyle_Details_Dialog", "Offset from origin:", None))
        self.extLineIsFixedLen.setToolTip(
            _translate("DimStyle_Details_Dialog", "Enables fixed length extension lines.", None))
        self.extLineIsFixedLen.setText(_translate("DimStyle_Details_Dialog", "Fixed length extension lines", None))
        self.label_12.setText(_translate("DimStyle_Details_Dialog", "Length:", None))
        self.extLineFixedLen.setToolTip(_translate("DimStyle_Details_Dialog",
                                                   "Total length of the extension lines starting from the dimension line toward the dimension origin.",
                                                   None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.LineTab),
                                  _translate("DimStyle_Details_Dialog", "Lines", None))
        self.groupBox_3.setTitle(_translate("DimStyle_Details_Dialog", "Arrowheads", None))
        self.block1Name.setToolTip(_translate("DimStyle_Details_Dialog",
                                              "Arrowhead for the first dimension line. When you change the first arrowhead type, the second arrowhead automatically changes to match it.",
                                              None))
        self.label_15.setText(_translate("DimStyle_Details_Dialog", "Arrowhead 1:", None))
        self.block2Name.setToolTip(
            _translate("DimStyle_Details_Dialog", "Arrowhead for the second dimension line.", None))
        self.label_18.setText(_translate("DimStyle_Details_Dialog", "Arrowhead 2:", None))
        self.blockLeaderName.setToolTip(_translate("DimStyle_Details_Dialog", "Arrowhead for the leader line.", None))
        self.label_19.setText(_translate("DimStyle_Details_Dialog", "Leader:", None))
        self.blockWidth.setToolTip(_translate("DimStyle_Details_Dialog",
                                              "Arrowhead horizontal size in map units using the symbol scale factor = 1.",
                                              None))
        self.label_17.setText(_translate("DimStyle_Details_Dialog", "Arrowhead size:", None))
        self.blockScale.setToolTip(_translate("DimStyle_Details_Dialog", "Arrowhead scale.", None))
        self.label_20.setText(_translate("DimStyle_Details_Dialog", "Arrowhead scale:", None))
        self.groupBox_4.setTitle(_translate("DimStyle_Details_Dialog", "Arc length symbol", None))
        self.arcSymbolPreceding.setText(_translate("DimStyle_Details_Dialog", "Preceding dimension text", None))
        self.arcSymbolAbove.setText(_translate("DimStyle_Details_Dialog", "Above dimension text", None))
        self.arcSymbolNone.setText(_translate("DimStyle_Details_Dialog", "None", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SymbolTab),
                                  _translate("DimStyle_Details_Dialog", "Symbols and arrows", None))
        self.groupBox_9.setTitle(_translate("DimStyle_Details_Dialog", "Text appearance", None))
        self.label_26.setText(_translate("DimStyle_Details_Dialog", "Text height:", None))
        self.textHeight.setToolTip(_translate("DimStyle_Details_Dialog", "Text height in map units.", None))
        self.label_40.setText(_translate("DimStyle_Details_Dialog", "Character type:", None))
        self.textFont.setToolTip(_translate("DimStyle_Details_Dialog", "Dimension text character type.", None))
        self.label_4.setText(_translate("DimStyle_Details_Dialog", "Color:", None))
        self.groupBox_10.setTitle(_translate("DimStyle_Details_Dialog", "Text placement", None))
        self.textVerticalPos.setToolTip(_translate("DimStyle_Details_Dialog",
                                                   "Controls the vertical placement of dimension text in relation to the dimension line.",
                                                   None))
        self.label_31.setText(_translate("DimStyle_Details_Dialog", "Vertical:", None))
        self.label_32.setText(_translate("DimStyle_Details_Dialog", "Horizontal:", None))
        self.textHorizontalPos.setToolTip(_translate("DimStyle_Details_Dialog",
                                                     "Controls the horizontal placement of dimension text along the dimension line, in relation to the extension lines.",
                                                     None))
        self.label_33.setText(_translate("DimStyle_Details_Dialog", "View direction:", None))
        self.textDirection.setToolTip(
            _translate("DimStyle_Details_Dialog", "Controls the dimension text viewing direction.", None))
        self.textOffsetDist.setToolTip(_translate("DimStyle_Details_Dialog",
                                                  "Sets the current text gap, which is the distance around the dimension text when the dimension line is broken to accommodate the dimension text.",
                                                  None))
        self.label_34.setText(_translate("DimStyle_Details_Dialog", "Offset from dim line:", None))
        self.textAlignment_groupBox.setTitle(_translate("DimStyle_Details_Dialog", "Text alignment", None))
        self.textRotModeHorizontal.setToolTip(
            _translate("DimStyle_Details_Dialog", "Places text in a horizontal position.", None))
        self.textRotModeHorizontal.setText(_translate("DimStyle_Details_Dialog", "Horizontal", None))
        self.textRotModeAligned.setToolTip(
            _translate("DimStyle_Details_Dialog", "Text aligned with Dimension Line.", None))
        self.textRotModeAligned.setText(_translate("DimStyle_Details_Dialog", "Aligned with dimension line", None))
        self.textRotModeISO.setToolTip(_translate("DimStyle_Details_Dialog",
                                                  "Aligns text with the dimension line when text is inside the extension lines, but aligns it horizontally when text is outside the extension lines.",
                                                  None))
        self.textRotModeISO.setText(_translate("DimStyle_Details_Dialog", "ISO Standard", None))
        self.textRotModeFixedRot.setToolTip(_translate("DimStyle_Details_Dialog", "Place text with fixed angle.", None))
        self.textRotModeFixedRot.setText(_translate("DimStyle_Details_Dialog", "Fixed rotation", None))
        self.textForcedRot.setToolTip(
            _translate("DimStyle_Details_Dialog", "Text angle  when fixed rotation mode is on.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TextTab),
                                  _translate("DimStyle_Details_Dialog", "Text", None))
        self.groupBox_12.setTitle(_translate("DimStyle_Details_Dialog", "Fit options", None))
        self.label_35.setText(_translate("DimStyle_Details_Dialog",
                                         "If there isn\'t enaugh room to place both text and arrows inside extension lines, the first thing to move outside the extension lines is:",
                                         None))
        self.textBlockAdjustWhicheverFitsBestOutside.setToolTip(_translate("DimStyle_Details_Dialog",
                                                                           "Moves either the text or the arrowheads outside the extension lines based on the best fit.",
                                                                           None))
        self.textBlockAdjustWhicheverFitsBestOutside.setText(
            _translate("DimStyle_Details_Dialog", "Either text or arrows (best fit)", None))
        self.textBlockAdjustFirstSymbolOutside.setToolTip(
            _translate("DimStyle_Details_Dialog", "Moves arrowheads outside the extension lines first, then text.",
                       None))
        self.textBlockAdjustFirstSymbolOutside.setText(_translate("DimStyle_Details_Dialog", "Arrows", None))
        self.textBlockAdjustFirstTextOutside.setToolTip(
            _translate("DimStyle_Details_Dialog", "Moves text outside the extension lines first, then arrowheads.",
                       None))
        self.textBlockAdjustFirstTextOutside.setText(_translate("DimStyle_Details_Dialog", "Text", None))
        self.textBlockAdjustBothOutside.setToolTip(_translate("DimStyle_Details_Dialog",
                                                              "When not enough space is available for text and arrowheads, moves both outside the extension lines.",
                                                              None))
        self.textBlockAdjustBothOutside.setText(_translate("DimStyle_Details_Dialog", "Both text and arrows", None))
        self.blockSuppressionForNoSpace.setToolTip(_translate("DimStyle_Details_Dialog",
                                                              "Suppresses arrowheads if not enough space is available inside the extension lines.",
                                                              None))
        self.blockSuppressionForNoSpace.setText(
            _translate("DimStyle_Details_Dialog", "Suppress arrows if they don\'t fit inside ext. lines", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AdjustTab),
                                  _translate("DimStyle_Details_Dialog", "Fit", None))
        self.groupBox_13.setTitle(_translate("DimStyle_Details_Dialog", "Linear dimensions", None))
        self.label_36.setText(_translate("DimStyle_Details_Dialog", "Precision:", None))
        self.textDecimals.setToolTip(_translate("DimStyle_Details_Dialog",
                                                "Displays and sets the number of decimal places in the dimension text.",
                                                None))
        self.textDecimalSep.setToolTip(
            _translate("DimStyle_Details_Dialog", "Sets the separator for decimal formats.", None))
        self.label_37.setText(_translate("DimStyle_Details_Dialog", "Decimal separator:", None))
        self.textPrefix.setToolTip(
            _translate("DimStyle_Details_Dialog", "Includes a prefix that you specify in the dimension text.", None))
        self.label_38.setText(_translate("DimStyle_Details_Dialog", "Prefix:", None))
        self.label_39.setText(_translate("DimStyle_Details_Dialog", "Suffix:", None))
        self.textSuffix.setToolTip(
            _translate("DimStyle_Details_Dialog", "Includes a suffix that you specify in the dimension text.", None))
        self.groupBox_14.setTitle(_translate("DimStyle_Details_Dialog", "Zero suppression", None))
        self.textSuppressLeadingZeros.setToolTip(_translate("DimStyle_Details_Dialog",
                                                            "Suppresses leading zeros in all decimal dimensions (0.5 becomes .5).",
                                                            None))
        self.textSuppressLeadingZeros.setText(_translate("DimStyle_Details_Dialog", "Leading", None))
        self.textDecimalZerosSuppression.setToolTip(_translate("DimStyle_Details_Dialog",
                                                               "Suppresses trailing zeros in all decimal dimensions (5.50 becomes 5.5 and 5.0 becomes 5).",
                                                               None))
        self.textDecimalZerosSuppression.setText(_translate("DimStyle_Details_Dialog", "Trailing", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PrimaryUnitTab),
                                  _translate("DimStyle_Details_Dialog", "Primary units", None))
        self.okButton.setText(_translate("DimStyle_Details_Dialog", "OK", None))
        self.cancelButton.setText(_translate("DimStyle_Details_Dialog", "Cancel", None))
        self.helpButton.setText(_translate("DimStyle_Details_Dialog", "?", None))
