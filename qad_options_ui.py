# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qad_options.ui'
#
# Created: Wed Oct 12 11:24:06 2016
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


class Ui_Options_Dialog(object):
    def setupUi(self, Options_Dialog):
        Options_Dialog.setObjectName(_fromUtf8("Options_Dialog"))
        Options_Dialog.setWindowModality(QtCore.Qt.NonModal)
        Options_Dialog.resize(591, 386)
        Options_Dialog.setMinimumSize(QtCore.QSize(591, 386))
        Options_Dialog.setMaximumSize(QtCore.QSize(591, 386))
        Options_Dialog.setSizeGripEnabled(False)
        Options_Dialog.setModal(False)
        self.buttonBox = QtGui.QDialogButtonBox(Options_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(240, 350, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtGui.QDialogButtonBox.Apply | QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Help | QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget = QtGui.QTabWidget(Options_Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 571, 331))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.DisplayTab = QtGui.QWidget()
        self.DisplayTab.setObjectName(_fromUtf8("DisplayTab"))
        self.groupBox = QtGui.QGroupBox(self.DisplayTab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 251, 291))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.Button_TextWindowColor = QtGui.QPushButton(self.groupBox)
        self.Button_TextWindowColor.setGeometry(QtCore.QRect(20, 260, 91, 23))
        self.Button_TextWindowColor.setObjectName(_fromUtf8("Button_TextWindowColor"))
        self.checkBox_INPUTSEARCHOPTIONS_AUTOCOMPLETE = QtGui.QCheckBox(self.groupBox)
        self.checkBox_INPUTSEARCHOPTIONS_AUTOCOMPLETE.setGeometry(QtCore.QRect(20, 100, 211, 17))
        self.checkBox_INPUTSEARCHOPTIONS_AUTOCOMPLETE.setObjectName(
            _fromUtf8("checkBox_INPUTSEARCHOPTIONS_AUTOCOMPLETE"))
        self.checkBox_SHOWTEXTWINDOW = QtGui.QCheckBox(self.groupBox)
        self.checkBox_SHOWTEXTWINDOW.setGeometry(QtCore.QRect(10, 20, 231, 20))
        self.checkBox_SHOWTEXTWINDOW.setObjectName(_fromUtf8("checkBox_SHOWTEXTWINDOW"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(50, 50, 191, 21))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_CMDINPUTHISTORYMAX = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_CMDINPUTHISTORYMAX.setGeometry(QtCore.QRect(10, 50, 31, 20))
        self.lineEdit_CMDINPUTHISTORYMAX.setObjectName(_fromUtf8("lineEdit_CMDINPUTHISTORYMAX"))
        self.lineEdit_INPUTSEARCHDELAY = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_INPUTSEARCHDELAY.setGeometry(QtCore.QRect(20, 180, 41, 20))
        self.lineEdit_INPUTSEARCHDELAY.setObjectName(_fromUtf8("lineEdit_INPUTSEARCHDELAY"))
        self.label_INPUTSEARCHDELAY = QtGui.QLabel(self.groupBox)
        self.label_INPUTSEARCHDELAY.setGeometry(QtCore.QRect(70, 180, 171, 21))
        self.label_INPUTSEARCHDELAY.setWordWrap(True)
        self.label_INPUTSEARCHDELAY.setObjectName(_fromUtf8("label_INPUTSEARCHDELAY"))
        self.checkBox_INPUTSEARCHOPTIONS_ON = QtGui.QCheckBox(self.groupBox)
        self.checkBox_INPUTSEARCHOPTIONS_ON.setGeometry(QtCore.QRect(10, 80, 231, 17))
        self.checkBox_INPUTSEARCHOPTIONS_ON.setObjectName(_fromUtf8("checkBox_INPUTSEARCHOPTIONS_ON"))
        self.checkBox_INPUTSEARCHOPTIONS_DISPLAY_LIST = QtGui.QCheckBox(self.groupBox)
        self.checkBox_INPUTSEARCHOPTIONS_DISPLAY_LIST.setGeometry(QtCore.QRect(20, 120, 211, 17))
        self.checkBox_INPUTSEARCHOPTIONS_DISPLAY_LIST.setObjectName(
            _fromUtf8("checkBox_INPUTSEARCHOPTIONS_DISPLAY_LIST"))
        self.checkBox_INPUTSEARCHOPTIONS_DISPLAY_ICON = QtGui.QCheckBox(self.groupBox)
        self.checkBox_INPUTSEARCHOPTIONS_DISPLAY_ICON.setGeometry(QtCore.QRect(20, 140, 211, 17))
        self.checkBox_INPUTSEARCHOPTIONS_DISPLAY_ICON.setObjectName(
            _fromUtf8("checkBox_INPUTSEARCHOPTIONS_DISPLAY_ICON"))
        self.checkBox_INPUTSEARCHOPTIONS_EXCLUDE_SYS_VAR = QtGui.QCheckBox(self.groupBox)
        self.checkBox_INPUTSEARCHOPTIONS_EXCLUDE_SYS_VAR.setGeometry(QtCore.QRect(20, 160, 211, 17))
        self.checkBox_INPUTSEARCHOPTIONS_EXCLUDE_SYS_VAR.setObjectName(
            _fromUtf8("checkBox_INPUTSEARCHOPTIONS_EXCLUDE_SYS_VAR"))
        self.groupBox_2 = QtGui.QGroupBox(self.DisplayTab)
        self.groupBox_2.setGeometry(QtCore.QRect(270, 10, 281, 121))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.lineEdit_ARCMINSEGMENTQTY = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_ARCMINSEGMENTQTY.setGeometry(QtCore.QRect(10, 30, 31, 20))
        self.lineEdit_ARCMINSEGMENTQTY.setObjectName(_fromUtf8("lineEdit_ARCMINSEGMENTQTY"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(50, 30, 221, 21))
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 221, 21))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_CIRCLEMINSEGMENTQTY = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_CIRCLEMINSEGMENTQTY.setGeometry(QtCore.QRect(10, 60, 31, 20))
        self.lineEdit_CIRCLEMINSEGMENTQTY.setObjectName(_fromUtf8("lineEdit_CIRCLEMINSEGMENTQTY"))
        self.lineEdit_TOLERANCE2APPROXCURVE = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_TOLERANCE2APPROXCURVE.setGeometry(QtCore.QRect(10, 90, 31, 20))
        self.lineEdit_TOLERANCE2APPROXCURVE.setObjectName(_fromUtf8("lineEdit_TOLERANCE2APPROXCURVE"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(50, 80, 221, 41))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.groupBox_3 = QtGui.QGroupBox(self.DisplayTab)
        self.groupBox_3.setGeometry(QtCore.QRect(270, 140, 281, 61))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.lineEdit_CURSORSIZE = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_CURSORSIZE.setGeometry(QtCore.QRect(10, 20, 31, 20))
        self.lineEdit_CURSORSIZE.setObjectName(_fromUtf8("lineEdit_CURSORSIZE"))
        self.horizontalSlider_CURSORSIZE = QtGui.QSlider(self.groupBox_3)
        self.horizontalSlider_CURSORSIZE.setGeometry(QtCore.QRect(50, 20, 221, 22))
        self.horizontalSlider_CURSORSIZE.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_CURSORSIZE.setObjectName(_fromUtf8("horizontalSlider_CURSORSIZE"))
        self.tabWidget.addTab(self.DisplayTab, _fromUtf8(""))
        self.DraftingTab = QtGui.QWidget()
        self.DraftingTab.setObjectName(_fromUtf8("DraftingTab"))
        self.groupBox_4 = QtGui.QGroupBox(self.DraftingTab)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 261, 141))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.checkBox_AUTOSNAP_DISPLAY_MARK = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_AUTOSNAP_DISPLAY_MARK.setGeometry(QtCore.QRect(10, 20, 241, 17))
        self.checkBox_AUTOSNAP_DISPLAY_MARK.setObjectName(_fromUtf8("checkBox_AUTOSNAP_DISPLAY_MARK"))
        self.pushButton_AutoSnapColor = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_AutoSnapColor.setGeometry(QtCore.QRect(10, 110, 81, 23))
        self.pushButton_AutoSnapColor.setObjectName(_fromUtf8("pushButton_AutoSnapColor"))
        self.checkBox_APBOX = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_APBOX.setGeometry(QtCore.QRect(10, 80, 241, 17))
        self.checkBox_APBOX.setObjectName(_fromUtf8("checkBox_APBOX"))
        self.checkBox_AUTOSNAP_DISPLAY_TOOLTIPS = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_AUTOSNAP_DISPLAY_TOOLTIPS.setGeometry(QtCore.QRect(10, 60, 241, 17))
        self.checkBox_AUTOSNAP_DISPLAY_TOOLTIPS.setObjectName(_fromUtf8("checkBox_AUTOSNAP_DISPLAY_TOOLTIPS"))
        self.checkBox_AUTOSNAP_MAGNET = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_AUTOSNAP_MAGNET.setGeometry(QtCore.QRect(10, 40, 241, 17))
        self.checkBox_AUTOSNAP_MAGNET.setObjectName(_fromUtf8("checkBox_AUTOSNAP_MAGNET"))
        self.groupBox_5 = QtGui.QGroupBox(self.DraftingTab)
        self.groupBox_5.setGeometry(QtCore.QRect(290, 10, 261, 71))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.radioButton_POLARMODE_AUTO_ACQUIRE = QtGui.QRadioButton(self.groupBox_5)
        self.radioButton_POLARMODE_AUTO_ACQUIRE.setGeometry(QtCore.QRect(10, 20, 241, 17))
        self.radioButton_POLARMODE_AUTO_ACQUIRE.setObjectName(_fromUtf8("radioButton_POLARMODE_AUTO_ACQUIRE"))
        self.radioButton_POLARMODE_SHIFT_TO_ACQUIRE = QtGui.QRadioButton(self.groupBox_5)
        self.radioButton_POLARMODE_SHIFT_TO_ACQUIRE.setGeometry(QtCore.QRect(10, 40, 241, 17))
        self.radioButton_POLARMODE_SHIFT_TO_ACQUIRE.setObjectName(_fromUtf8("radioButton_POLARMODE_SHIFT_TO_ACQUIRE"))
        self.groupBox_6 = QtGui.QGroupBox(self.DraftingTab)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 160, 261, 81))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.horizontalSlider_AUTOSNAPSIZE = QtGui.QSlider(self.groupBox_6)
        self.horizontalSlider_AUTOSNAPSIZE.setGeometry(QtCore.QRect(70, 30, 181, 22))
        self.horizontalSlider_AUTOSNAPSIZE.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_AUTOSNAPSIZE.setObjectName(_fromUtf8("horizontalSlider_AUTOSNAPSIZE"))
        self.widget_AUTOSNAPSIZE = QtGui.QWidget(self.groupBox_6)
        self.widget_AUTOSNAPSIZE.setGeometry(QtCore.QRect(10, 20, 51, 51))
        self.widget_AUTOSNAPSIZE.setObjectName(_fromUtf8("widget_AUTOSNAPSIZE"))
        self.groupBox_7 = QtGui.QGroupBox(self.DraftingTab)
        self.groupBox_7.setGeometry(QtCore.QRect(290, 160, 261, 81))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.horizontalSlider_APERTURE = QtGui.QSlider(self.groupBox_7)
        self.horizontalSlider_APERTURE.setGeometry(QtCore.QRect(70, 30, 181, 22))
        self.horizontalSlider_APERTURE.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_APERTURE.setObjectName(_fromUtf8("horizontalSlider_APERTURE"))
        self.widget_APERTURESIZE = QtGui.QWidget(self.groupBox_7)
        self.widget_APERTURESIZE.setGeometry(QtCore.QRect(10, 20, 51, 51))
        self.widget_APERTURESIZE.setObjectName(_fromUtf8("widget_APERTURESIZE"))
        self.tabWidget.addTab(self.DraftingTab, _fromUtf8(""))
        self.SelectionTab = QtGui.QWidget()
        self.SelectionTab.setObjectName(_fromUtf8("SelectionTab"))
        self.groupBox_8 = QtGui.QGroupBox(self.SelectionTab)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 10, 261, 81))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.horizontalSlider_PICKBOX = QtGui.QSlider(self.groupBox_8)
        self.horizontalSlider_PICKBOX.setGeometry(QtCore.QRect(70, 30, 181, 22))
        self.horizontalSlider_PICKBOX.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_PICKBOX.setObjectName(_fromUtf8("horizontalSlider_PICKBOX"))
        self.widget_PICKBOX = QtGui.QWidget(self.groupBox_8)
        self.widget_PICKBOX.setGeometry(QtCore.QRect(10, 20, 51, 51))
        self.widget_PICKBOX.setObjectName(_fromUtf8("widget_PICKBOX"))
        self.groupBox_9 = QtGui.QGroupBox(self.SelectionTab)
        self.groupBox_9.setGeometry(QtCore.QRect(280, 10, 271, 81))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.horizontalSlider_GRIPSIZE = QtGui.QSlider(self.groupBox_9)
        self.horizontalSlider_GRIPSIZE.setGeometry(QtCore.QRect(70, 30, 191, 22))
        self.horizontalSlider_GRIPSIZE.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_GRIPSIZE.setObjectName(_fromUtf8("horizontalSlider_GRIPSIZE"))
        self.widget_GRIPSIZE = QtGui.QWidget(self.groupBox_9)
        self.widget_GRIPSIZE.setGeometry(QtCore.QRect(10, 20, 51, 51))
        self.widget_GRIPSIZE.setObjectName(_fromUtf8("widget_GRIPSIZE"))
        self.groupBox_10 = QtGui.QGroupBox(self.SelectionTab)
        self.groupBox_10.setGeometry(QtCore.QRect(10, 100, 261, 131))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.checkBox_PICKFIRST = QtGui.QCheckBox(self.groupBox_10)
        self.checkBox_PICKFIRST.setGeometry(QtCore.QRect(10, 20, 241, 17))
        self.checkBox_PICKFIRST.setObjectName(_fromUtf8("checkBox_PICKFIRST"))
        self.checkBox_PICKADD = QtGui.QCheckBox(self.groupBox_10)
        self.checkBox_PICKADD.setGeometry(QtCore.QRect(10, 40, 241, 17))
        self.checkBox_PICKADD.setObjectName(_fromUtf8("checkBox_PICKADD"))
        self.groupBox_11 = QtGui.QGroupBox(self.SelectionTab)
        self.groupBox_11.setGeometry(QtCore.QRect(280, 100, 271, 131))
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.button_GripColor = QtGui.QPushButton(self.groupBox_11)
        self.button_GripColor.setGeometry(QtCore.QRect(70, 20, 141, 23))
        self.button_GripColor.setObjectName(_fromUtf8("button_GripColor"))
        self.checkBox_GRIPS = QtGui.QCheckBox(self.groupBox_11)
        self.checkBox_GRIPS.setGeometry(QtCore.QRect(10, 50, 251, 17))
        self.checkBox_GRIPS.setObjectName(_fromUtf8("checkBox_GRIPS"))
        self.checkBox_GRIPMULTIFUNCTIONAL_ON_DYNAMIC_MENU_AND_HOT_GRIPT = QtGui.QCheckBox(self.groupBox_11)
        self.checkBox_GRIPMULTIFUNCTIONAL_ON_DYNAMIC_MENU_AND_HOT_GRIPT.setGeometry(QtCore.QRect(20, 70, 241, 17))
        self.checkBox_GRIPMULTIFUNCTIONAL_ON_DYNAMIC_MENU_AND_HOT_GRIPT.setObjectName(
            _fromUtf8("checkBox_GRIPMULTIFUNCTIONAL_ON_DYNAMIC_MENU_AND_HOT_GRIPT"))
        self.lineEdit_GRIPOBJLIMIT = QtGui.QLineEdit(self.groupBox_11)
        self.lineEdit_GRIPOBJLIMIT.setGeometry(QtCore.QRect(20, 100, 31, 20))
        self.lineEdit_GRIPOBJLIMIT.setObjectName(_fromUtf8("lineEdit_GRIPOBJLIMIT"))
        self.label_GRIPOBJLIMIT = QtGui.QLabel(self.groupBox_11)
        self.label_GRIPOBJLIMIT.setGeometry(QtCore.QRect(60, 100, 201, 31))
        self.label_GRIPOBJLIMIT.setToolTip(_fromUtf8(""))
        self.label_GRIPOBJLIMIT.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_GRIPOBJLIMIT.setWordWrap(True)
        self.label_GRIPOBJLIMIT.setObjectName(_fromUtf8("label_GRIPOBJLIMIT"))
        self.tabWidget.addTab(self.SelectionTab, _fromUtf8(""))

        self.retranslateUi(Options_Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")),
                               Options_Dialog.ButtonBOX_Accepted)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("clicked(QAbstractButton*)")),
                               Options_Dialog.ButtonBOX_Apply)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("helpRequested()")),
                               Options_Dialog.ButtonHELP_Pressed)
        QtCore.QObject.connect(self.checkBox_INPUTSEARCHOPTIONS_ON, QtCore.SIGNAL(_fromUtf8("clicked()")),
                               Options_Dialog.checkBox_INPUTSEARCHOPTIONS_ON_clicked)
        QtCore.QObject.connect(self.horizontalSlider_CURSORSIZE, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")),
                               Options_Dialog.horizontalSlider_CURSORSIZE_moved)
        QtCore.QObject.connect(self.lineEdit_CURSORSIZE, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")),
                               Options_Dialog.lineEdit_CURSORSIZE_textChanged)
        QtCore.QObject.connect(self.horizontalSlider_CURSORSIZE, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               Options_Dialog.horizontalSlider_CURSORSIZE_moved)
        QtCore.QObject.connect(self.horizontalSlider_AUTOSNAPSIZE, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               Options_Dialog.horizontalSlider_AUTOSNAPSIZE_changed)
        QtCore.QObject.connect(self.horizontalSlider_APERTURE, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               Options_Dialog.horizontalSlider_APERTURE_changed)
        QtCore.QObject.connect(self.horizontalSlider_PICKBOX, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               Options_Dialog.horizontalSlider_PICKBOX_changed)
        QtCore.QObject.connect(self.horizontalSlider_GRIPSIZE, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               Options_Dialog.horizontalSlider_GRIPSIZE_changed)
        QtCore.QObject.connect(self.checkBox_GRIPS, QtCore.SIGNAL(_fromUtf8("clicked()")),
                               Options_Dialog.checkBox_GRIPS_ON_clicked)
        QtCore.QObject.connect(self.button_GripColor, QtCore.SIGNAL(_fromUtf8("clicked()")),
                               Options_Dialog.button_GripColor_clicked)
        QtCore.QObject.connect(self.Button_TextWindowColor, QtCore.SIGNAL(_fromUtf8("clicked()")),
                               Options_Dialog.Button_TextWindowColor_clicked)
        QtCore.QObject.connect(self.pushButton_AutoSnapColor, QtCore.SIGNAL(_fromUtf8("clicked()")),
                               Options_Dialog.Button_AutoSnapWindowColor_clicked)
        QtCore.QMetaObject.connectSlotsByName(Options_Dialog)

    def retranslateUi(self, Options_Dialog):
        Options_Dialog.setWindowTitle(_translate("Options_Dialog", "QAD - Options", None))
        self.groupBox.setTitle(_translate("Options_Dialog", "Window Elements", None))
        self.Button_TextWindowColor.setToolTip(
            _translate("Options_Dialog", "Displays the Drawing Window Colors dialog box. ", None))
        self.Button_TextWindowColor.setText(_translate("Options_Dialog", "Colors", None))
        self.checkBox_INPUTSEARCHOPTIONS_AUTOCOMPLETE.setToolTip(_translate("Options_Dialog",
                                                                            "Automatically appends suggestions as each keystroke is entered after the second keystroke (system variable INPUTSEARCHOPTIONS).",
                                                                            None))
        self.checkBox_INPUTSEARCHOPTIONS_AUTOCOMPLETE.setText(_translate("Options_Dialog", "AutoComplete", None))
        self.checkBox_SHOWTEXTWINDOW.setToolTip(
            _translate("Options_Dialog", "Show the text window at startup (system variable SHOWTEXTWINDOW).", None))
        self.checkBox_SHOWTEXTWINDOW.setText(_translate("Options_Dialog", "Show the text window at startup", None))
        self.label_4.setText(_translate("Options_Dialog", "Maximun command history length", None))
        self.lineEdit_CMDINPUTHISTORYMAX.setToolTip(_translate("Options_Dialog",
                                                               "Sets the maximum number of previous input values that are stored for a prompt in a command (system variable CMDINPUTHISTORYMAX).",
                                                               None))
        self.lineEdit_INPUTSEARCHDELAY.setToolTip(_translate("Options_Dialog",
                                                             "<html><head/><body><p>Controls the amount of time that elapses before automated keyboard features display at the Command prompt.</p><p>Valid values are real numbers from 100 to 10,000, which represent milliseconds.</p></body></html>",
                                                             None))
        self.label_INPUTSEARCHDELAY.setText(_translate("Options_Dialog", "Delay time (msec)", None))
        self.checkBox_INPUTSEARCHOPTIONS_ON.setToolTip(_translate("Options_Dialog",
                                                                  "Turns on/off all automated keyboard features when typing at the Command prompt (system variable INPUTSEARCHOPTIONS).",
                                                                  None))
        self.checkBox_INPUTSEARCHOPTIONS_ON.setText(_translate("Options_Dialog", "Automated keyboard features", None))
        self.checkBox_INPUTSEARCHOPTIONS_DISPLAY_LIST.setToolTip(_translate("Options_Dialog",
                                                                            "Displays a list of suggestions as keystrokes are entered (system variable INPUTSEARCHOPTIONS).",
                                                                            None))
        self.checkBox_INPUTSEARCHOPTIONS_DISPLAY_LIST.setText(
            _translate("Options_Dialog", "Displays a list of suggestions", None))
        self.checkBox_INPUTSEARCHOPTIONS_DISPLAY_ICON.setToolTip(_translate("Options_Dialog",
                                                                            "Displays the icon of the command or system variable, if available (system variable INPUTSEARCHOPTIONS).",
                                                                            None))
        self.checkBox_INPUTSEARCHOPTIONS_DISPLAY_ICON.setText(
            _translate("Options_Dialog", "Displays the icon of the command", None))
        self.checkBox_INPUTSEARCHOPTIONS_EXCLUDE_SYS_VAR.setToolTip(_translate("Options_Dialog",
                                                                               "Excludes the display of system variables (system variable INPUTSEARCHOPTIONS).",
                                                                               None))
        self.checkBox_INPUTSEARCHOPTIONS_EXCLUDE_SYS_VAR.setText(
            _translate("Options_Dialog", "Excludes system variables", None))
        self.groupBox_2.setTitle(_translate("Options_Dialog", "Resolution", None))
        self.lineEdit_ARCMINSEGMENTQTY.setToolTip(_translate("Options_Dialog",
                                                             "Minimum number of segments to approximate an arc (system variable ARCMINSEGMENTQTY).",
                                                             None))
        self.label.setText(_translate("Options_Dialog", "Minimum number of segments in an arc", None))
        self.label_2.setToolTip(_translate("Options_Dialog",
                                           "Minimum number of segments to approximate a circle (system variable CIRCLEMINSEGMENTQTY).",
                                           None))
        self.label_2.setText(_translate("Options_Dialog", "Minimum number of segments in a circle", None))
        self.lineEdit_CIRCLEMINSEGMENTQTY.setToolTip(_translate("Options_Dialog",
                                                                "Minimum number of segments to approximate a circle (system variable CIRCLEMINSEGMENTQTY).",
                                                                None))
        self.lineEdit_TOLERANCE2APPROXCURVE.setToolTip(_translate("Options_Dialog",
                                                                  "Maximum error approximating a curve to segments (system variable TOLERANCE2APPROXCURVE).",
                                                                  None))
        self.label_3.setText(_translate("Options_Dialog",
                                        "Maximun admitted error between a real curve and the aproximated, segmented curve",
                                        None))
        self.groupBox_3.setTitle(_translate("Options_Dialog", "Crosshair size", None))
        self.lineEdit_CURSORSIZE.setToolTip(_translate("Options_Dialog",
                                                       "Determines the size of the crosshair as a percentage of the screen size (system variable CURSORSIZE).",
                                                       None))
        self.horizontalSlider_CURSORSIZE.setToolTip(_translate("Options_Dialog",
                                                               "Determines the size of the crosshair as a percentage of the screen size (system variable CURSORSIZE).",
                                                               None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DisplayTab),
                                  _translate("Options_Dialog", "Display", None))
        self.groupBox_4.setTitle(_translate("Options_Dialog", "AutoSnap Settings", None))
        self.checkBox_AUTOSNAP_DISPLAY_MARK.setToolTip(_translate("Options_Dialog",
                                                                  "Controls the display of the AutoSnap marker. The marker is a geometric symbol that is displayed when the crosshairs move over a snap point ( AUTOSNAP system variable).",
                                                                  None))
        self.checkBox_AUTOSNAP_DISPLAY_MARK.setText(_translate("Options_Dialog", "Marker", None))
        self.pushButton_AutoSnapColor.setToolTip(
            _translate("Options_Dialog", "Displays the Drawing Window Colors dialog box. ", None))
        self.pushButton_AutoSnapColor.setText(_translate("Options_Dialog", "Colors", None))
        self.checkBox_APBOX.setToolTip(
            _translate("Options_Dialog", "Turns the display of the AutoSnap aperture box on or off.\n"
                                         "The aperture box is a box that appears inside the crosshairs when you snap to an object (APBOX system variable).",
                       None))
        self.checkBox_APBOX.setText(_translate("Options_Dialog", "Display AutoSnap aperture box", None))
        self.checkBox_AUTOSNAP_DISPLAY_TOOLTIPS.setToolTip(_translate("Options_Dialog",
                                                                      "Controls the display of the AutoSnap tooltip. The tooltip is a label that describes which part of the object you are snapping to (AUTOSNAP system variable).",
                                                                      None))
        self.checkBox_AUTOSNAP_DISPLAY_TOOLTIPS.setText(_translate("Options_Dialog", "Display AutoSnap tooltip", None))
        self.checkBox_AUTOSNAP_MAGNET.setToolTip(_translate("Options_Dialog",
                                                            "Turns the AutoSnap magnet on or off. The magnet is an automatic movement of the crosshairs that locks the crosshairs onto the nearest snap point (AUTOSNAP system variable).",
                                                            None))
        self.checkBox_AUTOSNAP_MAGNET.setText(_translate("Options_Dialog", "Magnet", None))
        self.groupBox_5.setTitle(_translate("Options_Dialog", "Alignment Point Acquisition", None))
        self.radioButton_POLARMODE_AUTO_ACQUIRE.setToolTip(_translate("Options_Dialog",
                                                                      "Displays tracking vectors automatically when the aperture moves over an object snap.",
                                                                      None))
        self.radioButton_POLARMODE_AUTO_ACQUIRE.setText(_translate("Options_Dialog", "Automatic", None))
        self.radioButton_POLARMODE_SHIFT_TO_ACQUIRE.setToolTip(_translate("Options_Dialog",
                                                                          "Displays tracking vectors when you press Shift and move the aperture over an object snap.",
                                                                          None))
        self.radioButton_POLARMODE_SHIFT_TO_ACQUIRE.setText(_translate("Options_Dialog", "Shift to acquire", None))
        self.groupBox_6.setTitle(_translate("Options_Dialog", "AutoSnap Marker Size", None))
        self.horizontalSlider_AUTOSNAPSIZE.setToolTip(
            _translate("Options_Dialog", "Sets the display size for the AutoSnap marker.", None))
        self.groupBox_7.setTitle(_translate("Options_Dialog", "Aperture Size", None))
        self.horizontalSlider_APERTURE.setToolTip(_translate("Options_Dialog",
                                                             "Sets the display size for the object snap target box, in pixels (APERTURE system variable).",
                                                             None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DraftingTab),
                                  _translate("Options_Dialog", "Drafting", None))
        self.groupBox_8.setTitle(_translate("Options_Dialog", "Pickbox size", None))
        self.horizontalSlider_PICKBOX.setToolTip(_translate("Options_Dialog",
                                                            "Sets the object selection target height, in pixels (PICKBOX system variable).",
                                                            None))
        self.groupBox_9.setTitle(_translate("Options_Dialog", "Grip size", None))
        self.horizontalSlider_GRIPSIZE.setToolTip(
            _translate("Options_Dialog", "Sets the size of the grip box in pixels ( GRIPSIZE system variable).", None))
        self.groupBox_10.setTitle(_translate("Options_Dialog", "Selection modes", None))
        self.checkBox_PICKFIRST.setToolTip(_translate("Options_Dialog",
                                                      "Controls whether you select objects before (noun-verb selection) or after you issue a command (PICKFIRST system variable).",
                                                      None))
        self.checkBox_PICKFIRST.setText(_translate("Options_Dialog", "Noun/verb selection", None))
        self.checkBox_PICKADD.setToolTip(_translate("Options_Dialog",
                                                    "Controls whether subsequent selections replace the current selection set or add to it (PICKADD system variable).",
                                                    None))
        self.checkBox_PICKADD.setText(_translate("Options_Dialog", "Use Shift to add to selection", None))
        self.groupBox_11.setTitle(_translate("Options_Dialog", "Grips", None))
        self.button_GripColor.setToolTip(_translate("Options_Dialog",
                                                    "Displays the Grip Colors dialog box where you can specify the colors for different grip status and elements.",
                                                    None))
        self.button_GripColor.setText(_translate("Options_Dialog", "Grip Colors...", None))
        self.checkBox_GRIPS.setToolTip(_translate("Options_Dialog",
                                                  "Controls the display of grips on selected objects. Displaying grips in a drawing significantly affects performance. Clear this option to optimize performance ( GRIPS system variable).",
                                                  None))
        self.checkBox_GRIPS.setText(_translate("Options_Dialog", "Shows grips", None))
        self.checkBox_GRIPMULTIFUNCTIONAL_ON_DYNAMIC_MENU_AND_HOT_GRIPT.setToolTip(_translate("Options_Dialog",
                                                                                              "Controls the display of dynamic menu when pausing over a multi-functional grip (GRIPMULTIFUNCTIONAL system variable).",
                                                                                              None))
        self.checkBox_GRIPMULTIFUNCTIONAL_ON_DYNAMIC_MENU_AND_HOT_GRIPT.setText(
            _translate("Options_Dialog", "Shows dynamic grip menu", None))
        self.lineEdit_GRIPOBJLIMIT.setToolTip(_translate("Options_Dialog",
                                                         "Suppresses the display of grips when the selection set includes more than the specified number of objects (GRIPOBJLIMIT system variable).",
                                                         None))
        self.label_GRIPOBJLIMIT.setText(
            _translate("Options_Dialog", "Object selection limit for display of grips", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SelectionTab),
                                  _translate("Options_Dialog", "Selection", None))
