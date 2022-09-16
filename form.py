# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(571, 356)
        icon = QIcon()
        icon.addFile(u"dependences/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_10 = QHBoxLayout(self.page)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.comboBox_2 = QComboBox(self.page)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_6.addWidget(self.comboBox_2)

        self.toolButton_4 = QToolButton(self.page)
        self.toolButton_4.setObjectName(u"toolButton_4")

        self.horizontalLayout_6.addWidget(self.toolButton_4)

        self.toolButton_2 = QToolButton(self.page)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.horizontalLayout_6.addWidget(self.toolButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.comboBox = QComboBox(self.page)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_3.addWidget(self.comboBox)

        self.toolButton = QToolButton(self.page)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_3.addWidget(self.toolButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox_2 = QCheckBox(self.page)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.horizontalLayout_5.addWidget(self.checkBox_2)

        self.checkBox = QCheckBox(self.page)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.horizontalLayout_5.addWidget(self.checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkBox_3 = QCheckBox(self.page)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_7.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.page)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout_7.addWidget(self.checkBox_4)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEdit = QLineEdit(self.page)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.lineEdit)

        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.page)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.lineEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)


        self.horizontalLayout_10.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_2 = QLineEdit(self.page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_4.addWidget(self.lineEdit_2)

        self.pushButton = QToolButton(self.page)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton_3 = QRadioButton(self.page)
        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radioButton_3)

        self.radioButton_2 = QRadioButton(self.page)
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setChecked(False)

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.page)
        self.buttonGroup.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_2.addWidget(self.radioButton)

        self.radioButton_4 = QRadioButton(self.page)
        self.buttonGroup.addButton(self.radioButton_4)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.radioButton_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.comboBox_3 = QComboBox(self.page)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setEnabled(False)

        self.verticalLayout_2.addWidget(self.comboBox_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.pushButton_3 = QPushButton(self.page)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.radioButton_5 = QRadioButton(self.page)
        self.buttonGroup_2 = QButtonGroup(Form)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_5)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setChecked(True)

        self.horizontalLayout_9.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.page)
        self.buttonGroup_2.addButton(self.radioButton_6)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setChecked(False)

        self.horizontalLayout_9.addWidget(self.radioButton_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.progressBar = QProgressBar(self.page)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_2.addWidget(self.progressBar)


        self.horizontalLayout_10.addLayout(self.verticalLayout_2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.toolButton_3 = QToolButton(self.page_2)
        self.toolButton_3.setObjectName(u"toolButton_3")

        self.horizontalLayout_12.addWidget(self.toolButton_3)

        self.toolButton_5 = QToolButton(self.page_2)
        self.toolButton_5.setObjectName(u"toolButton_5")

        self.horizontalLayout_12.addWidget(self.toolButton_5)

        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_12.addWidget(self.label_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listWidget = QListWidget(self.page_2)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_3.addWidget(self.listWidget)


        self.horizontalLayout_11.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.textEdit = QTextEdit(self.page_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.textEdit)


        self.horizontalLayout_11.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"RatLauncher", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0418\u0433\u0440\u0430", None))
        self.toolButton_4.setText(QCoreApplication.translate("Form", u"+", None))
        self.toolButton_2.setText(QCoreApplication.translate("Form", u"X", None))
#if QT_CONFIG(tooltip)
        self.comboBox.setToolTip(QCoreApplication.translate("Form", u"\u0412\u0435\u0440\u0441\u0438\u044f", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.comboBox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.toolButton.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u043a\u043b\u0438\u0435\u043d\u0442", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u0418\u043d\u0442\u0435\u0433\u0440\u0430\u0446\u0438\u044f Ely.by", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"\u0414\u0435\u043c\u043e", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"\u0421\u0432\u043e\u0435 \u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"x", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0418\u0433\u0440\u0430\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"Vanilla", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"Forge", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"Fabric", None))
        self.radioButton_4.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0441\u0442\u043e\u043c", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Form", u"Impact", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Form", u"Ares", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Form", u"BatMod", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Form", u"LabyMod", None))

        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u043e\u0441\u0442\u0438 \u0441 minecraft.net...", None))
        self.radioButton_5.setText(QCoreApplication.translate("Form", u"\u0421\u0432\u0435\u0442\u043b\u0430\u044f", None))
        self.radioButton_6.setText(QCoreApplication.translate("Form", u"\u0427\u0435\u0440\u043d\u0430\u044f", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.progressBar.setFormat(QCoreApplication.translate("Form", u"%p%", None))
        self.toolButton_3.setText(QCoreApplication.translate("Form", u"<< \u041d\u0430\u0437\u0430\u0434", None))
        self.toolButton_5.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u043e\u0441\u0442\u0438", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0412\u0441\u0435\u0433\u043e \u043d\u043e\u0432\u043e\u0441\u0442\u0435\u0439: 0", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">\u0412\u044b\u0431\u0435\u0440\u0438 \u043d\u043e\u0432\u043e\u0441\u0442\u044c \u0441\u043b\u0435\u0432\u0430!</span></p></body></html>", None))
    # retranslateUi

