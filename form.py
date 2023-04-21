# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QButtonGroup, QCheckBox,
    QComboBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QTextEdit, QToolButton, QVBoxLayout,
    QWidget)
import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(678, 437)
        icon = QIcon()
        icon.addFile(u":/icons/dependences/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.st_widget_main = QStackedWidget(Form)
        self.st_widget_main.setObjectName(u"st_widget_main")
        self.play_page = QWidget()
        self.play_page.setObjectName(u"play_page")
        self.play_page.setAutoFillBackground(False)
        self.horizontalLayout_10 = QHBoxLayout(self.play_page)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.vlayout_2 = QVBoxLayout()
        self.vlayout_2.setObjectName(u"vlayout_2")
        self.vlayout_2.setContentsMargins(-1, -1, 3, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.settings_button = QPushButton(self.play_page)
        self.settings_button.setObjectName(u"settings_button")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_button.sizePolicy().hasHeightForWidth())
        self.settings_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.settings_button)

        self.news_button = QPushButton(self.play_page)
        self.news_button.setObjectName(u"news_button")
        sizePolicy.setHeightForWidth(self.news_button.sizePolicy().hasHeightForWidth())
        self.news_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.news_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.vlayout_2.addLayout(self.horizontalLayout_3)

        self.hlayout = QHBoxLayout()
        self.hlayout.setSpacing(6)
        self.hlayout.setObjectName(u"hlayout")
        self.hlayout.setContentsMargins(-1, 0, -1, -1)
        self.left_layout = QVBoxLayout()
        self.left_layout.setObjectName(u"left_layout")
        self.game_label = QLabel(self.play_page)
        self.game_label.setObjectName(u"game_label")

        self.left_layout.addWidget(self.game_label)

        self.account_layout = QHBoxLayout()
        self.account_layout.setObjectName(u"account_layout")
        self.account_combo = QComboBox(self.play_page)
        self.account_combo.setObjectName(u"account_combo")

        self.account_layout.addWidget(self.account_combo)

        self.add_account = QToolButton(self.play_page)
        self.add_account.setObjectName(u"add_account")
        icon1 = QIcon()
        icon1.addFile(u":/icons/add_black.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_account.setIcon(icon1)

        self.account_layout.addWidget(self.add_account)

        self.delete_account = QToolButton(self.play_page)
        self.delete_account.setObjectName(u"delete_account")
        icon2 = QIcon()
        icon2.addFile(u":/icons/del_black.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_account.setIcon(icon2)

        self.account_layout.addWidget(self.delete_account)


        self.left_layout.addLayout(self.account_layout)

        self.version_layout = QHBoxLayout()
        self.version_layout.setObjectName(u"version_layout")
        self.version_combo = QComboBox(self.play_page)
        self.version_combo.setObjectName(u"version_combo")

        self.version_layout.addWidget(self.version_combo)

        self.update_versions = QToolButton(self.play_page)
        self.update_versions.setObjectName(u"update_versions")
        icon3 = QIcon()
        icon3.addFile(u":/icons/refresh_black.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.update_versions.setIcon(icon3)

        self.version_layout.addWidget(self.update_versions)


        self.left_layout.addLayout(self.version_layout)

        self.hspacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.left_layout.addItem(self.hspacer)

        self.v_spacer_1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.left_layout.addItem(self.v_spacer_1)

        self.play_button = QPushButton(self.play_page)
        self.play_button.setObjectName(u"play_button")

        self.left_layout.addWidget(self.play_button)


        self.hlayout.addLayout(self.left_layout)

        self.right_layout = QVBoxLayout()
        self.right_layout.setObjectName(u"right_layout")
        self.right_layout.setContentsMargins(-1, 0, -1, -1)
        self.install_label = QLabel(self.play_page)
        self.install_label.setObjectName(u"install_label")

        self.right_layout.addWidget(self.install_label)

        self.version_install_layout = QHBoxLayout()
        self.version_install_layout.setObjectName(u"version_install_layout")
        self.install_version_combo = QComboBox(self.play_page)
        self.install_version_combo.setObjectName(u"install_version_combo")

        self.version_install_layout.addWidget(self.install_version_combo)

        self.update_versions_button = QToolButton(self.play_page)
        self.update_versions_button.setObjectName(u"update_versions_button")
        self.update_versions_button.setIcon(icon3)

        self.version_install_layout.addWidget(self.update_versions_button)

        self.install_button = QToolButton(self.play_page)
        self.install_button.setObjectName(u"install_button")

        self.version_install_layout.addWidget(self.install_button)


        self.right_layout.addLayout(self.version_install_layout)

        self.type_layout = QHBoxLayout()
        self.type_layout.setObjectName(u"type_layout")
        self.vanilla_radio = QRadioButton(self.play_page)
        self.btn_group_1 = QButtonGroup(Form)
        self.btn_group_1.setObjectName(u"btn_group_1")
        self.btn_group_1.addButton(self.vanilla_radio)
        self.vanilla_radio.setObjectName(u"vanilla_radio")
        self.vanilla_radio.setChecked(True)

        self.type_layout.addWidget(self.vanilla_radio)

        self.forge_radio = QRadioButton(self.play_page)
        self.btn_group_1.addButton(self.forge_radio)
        self.forge_radio.setObjectName(u"forge_radio")
        self.forge_radio.setChecked(False)

        self.type_layout.addWidget(self.forge_radio)

        self.fabric_radio = QRadioButton(self.play_page)
        self.btn_group_1.addButton(self.fabric_radio)
        self.fabric_radio.setObjectName(u"fabric_radio")

        self.type_layout.addWidget(self.fabric_radio)

        self.custom_client_radio = QRadioButton(self.play_page)
        self.btn_group_1.addButton(self.custom_client_radio)
        self.custom_client_radio.setObjectName(u"custom_client_radio")
        self.custom_client_radio.setEnabled(True)

        self.type_layout.addWidget(self.custom_client_radio)


        self.right_layout.addLayout(self.type_layout)

        self.custom_client_combo = QComboBox(self.play_page)
        self.custom_client_combo.addItem("")
        self.custom_client_combo.addItem("")
        self.custom_client_combo.addItem("")
        self.custom_client_combo.addItem("")
        self.custom_client_combo.setObjectName(u"custom_client_combo")
        self.custom_client_combo.setEnabled(False)

        self.right_layout.addWidget(self.custom_client_combo)

        self.v_spacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.right_layout.addItem(self.v_spacer_2)

        self.status_label = QLabel(self.play_page)
        self.status_label.setObjectName(u"status_label")

        self.right_layout.addWidget(self.status_label)

        self.status_progressbar = QProgressBar(self.play_page)
        self.status_progressbar.setObjectName(u"status_progressbar")
        self.status_progressbar.setValue(0)
        self.status_progressbar.setTextVisible(True)

        self.right_layout.addWidget(self.status_progressbar)


        self.hlayout.addLayout(self.right_layout)


        self.vlayout_2.addLayout(self.hlayout)

        self.ad_layout_2 = QWidget(self.play_page)
        self.ad_layout_2.setObjectName(u"ad_layout_2")
        self.ad_layout = QVBoxLayout(self.ad_layout_2)
        self.ad_layout.setObjectName(u"ad_layout")
        self.ad_layout.setContentsMargins(-1, 1, -1, -1)
        self.close_button = QToolButton(self.ad_layout_2)
        self.close_button.setObjectName(u"close_button")
        icon4 = QIcon()
        icon4.addFile(u":/icons/close_black.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon4)

        self.ad_layout.addWidget(self.close_button)

        self.image_label = QLabel(self.ad_layout_2)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setAlignment(Qt.AlignCenter)

        self.ad_layout.addWidget(self.image_label)

        self.desc_label = QLabel(self.ad_layout_2)
        self.desc_label.setObjectName(u"desc_label")
        self.desc_label.setTextFormat(Qt.MarkdownText)
        self.desc_label.setAlignment(Qt.AlignCenter)

        self.ad_layout.addWidget(self.desc_label)

        self.ip_label = QLabel(self.ad_layout_2)
        self.ip_label.setObjectName(u"ip_label")
        self.ip_label.setCursor(QCursor(Qt.ArrowCursor))
        self.ip_label.setTextFormat(Qt.MarkdownText)
        self.ip_label.setAlignment(Qt.AlignCenter)

        self.ad_layout.addWidget(self.ip_label)


        self.vlayout_2.addWidget(self.ad_layout_2)


        self.horizontalLayout_10.addLayout(self.vlayout_2)

        self.st_widget_main.addWidget(self.play_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.horizontalLayout_2 = QHBoxLayout(self.settings_page)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.vlayout_3 = QVBoxLayout()
        self.vlayout_3.setObjectName(u"vlayout_3")
        self.hlayout_3 = QHBoxLayout()
        self.hlayout_3.setObjectName(u"hlayout_3")
        self.back_button_2 = QPushButton(self.settings_page)
        self.back_button_2.setObjectName(u"back_button_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.back_button_2.sizePolicy().hasHeightForWidth())
        self.back_button_2.setSizePolicy(sizePolicy1)

        self.hlayout_3.addWidget(self.back_button_2)

        self.settings_label = QLabel(self.settings_page)
        self.settings_label.setObjectName(u"settings_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.settings_label.sizePolicy().hasHeightForWidth())
        self.settings_label.setSizePolicy(sizePolicy2)

        self.hlayout_3.addWidget(self.settings_label)


        self.vlayout_3.addLayout(self.hlayout_3)

        self.hlayout_4 = QHBoxLayout()
        self.hlayout_4.setObjectName(u"hlayout_4")
        self.hlayout_4.setContentsMargins(-1, 0, -1, -1)
        self.ad_checkbox = QCheckBox(self.settings_page)
        self.ad_checkbox.setObjectName(u"ad_checkbox")
        self.ad_checkbox.setChecked(True)
        self.ad_checkbox.setTristate(False)

        self.hlayout_4.addWidget(self.ad_checkbox)

        self.warn_label = QLabel(self.settings_page)
        self.warn_label.setObjectName(u"warn_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.warn_label.sizePolicy().hasHeightForWidth())
        self.warn_label.setSizePolicy(sizePolicy3)
        self.warn_label.setTextFormat(Qt.MarkdownText)
        self.warn_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.warn_label.setTextInteractionFlags(Qt.NoTextInteraction)

        self.hlayout_4.addWidget(self.warn_label)


        self.vlayout_3.addLayout(self.hlayout_4)

        self.hlayout_5 = QHBoxLayout()
        self.hlayout_5.setObjectName(u"hlayout_5")
        self.hlayout_5.setContentsMargins(-1, 0, -1, -1)
        self.theme_laybel = QLabel(self.settings_page)
        self.theme_laybel.setObjectName(u"theme_laybel")

        self.hlayout_5.addWidget(self.theme_laybel)

        self.theme_combo = QComboBox(self.settings_page)
        self.theme_combo.addItem("")
        self.theme_combo.addItem("")
        self.theme_combo.setObjectName(u"theme_combo")
        sizePolicy.setHeightForWidth(self.theme_combo.sizePolicy().hasHeightForWidth())
        self.theme_combo.setSizePolicy(sizePolicy)

        self.hlayout_5.addWidget(self.theme_combo)


        self.vlayout_3.addLayout(self.hlayout_5)

        self.update_jsons = QCheckBox(self.settings_page)
        self.update_jsons.setObjectName(u"update_jsons")
        self.update_jsons.setChecked(True)

        self.vlayout_3.addWidget(self.update_jsons)

        self.integrate_elyby = QCheckBox(self.settings_page)
        self.integrate_elyby.setObjectName(u"integrate_elyby")
        self.integrate_elyby.setChecked(True)

        self.vlayout_3.addWidget(self.integrate_elyby)

        self.demo_mode = QCheckBox(self.settings_page)
        self.demo_mode.setObjectName(u"demo_mode")

        self.vlayout_3.addWidget(self.demo_mode)

        self.hlayout_6 = QHBoxLayout()
        self.hlayout_6.setObjectName(u"hlayout_6")
        self.hlayout_6.setContentsMargins(-1, 0, -1, -1)
        self.custom_resolution = QCheckBox(self.settings_page)
        self.custom_resolution.setObjectName(u"custom_resolution")

        self.hlayout_6.addWidget(self.custom_resolution)

        self.w_res = QSpinBox(self.settings_page)
        self.w_res.setObjectName(u"w_res")
        self.w_res.setEnabled(False)
        sizePolicy.setHeightForWidth(self.w_res.sizePolicy().hasHeightForWidth())
        self.w_res.setSizePolicy(sizePolicy)
        self.w_res.setMinimum(50)
        self.w_res.setMaximum(10000)
        self.w_res.setSingleStep(50)
        self.w_res.setStepType(QAbstractSpinBox.DefaultStepType)
        self.w_res.setValue(800)
        self.w_res.setDisplayIntegerBase(10)

        self.hlayout_6.addWidget(self.w_res)

        self.x_label = QLabel(self.settings_page)
        self.x_label.setObjectName(u"x_label")
        self.x_label.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.x_label.sizePolicy().hasHeightForWidth())
        self.x_label.setSizePolicy(sizePolicy4)

        self.hlayout_6.addWidget(self.x_label)

        self.h_res = QSpinBox(self.settings_page)
        self.h_res.setObjectName(u"h_res")
        self.h_res.setEnabled(False)
        sizePolicy.setHeightForWidth(self.h_res.sizePolicy().hasHeightForWidth())
        self.h_res.setSizePolicy(sizePolicy)
        self.h_res.setMinimum(50)
        self.h_res.setMaximum(10000)
        self.h_res.setSingleStep(50)
        self.h_res.setValue(600)

        self.hlayout_6.addWidget(self.h_res)


        self.vlayout_3.addLayout(self.hlayout_6)

        self.hlayout_7 = QHBoxLayout()
        self.hlayout_7.setObjectName(u"hlayout_7")
        self.folder_label = QLabel(self.settings_page)
        self.folder_label.setObjectName(u"folder_label")

        self.hlayout_7.addWidget(self.folder_label)

        self.folder_edit = QLineEdit(self.settings_page)
        self.folder_edit.setObjectName(u"folder_edit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.folder_edit.sizePolicy().hasHeightForWidth())
        self.folder_edit.setSizePolicy(sizePolicy5)

        self.hlayout_7.addWidget(self.folder_edit)


        self.vlayout_3.addLayout(self.hlayout_7)

        self.hlayout_2 = QHBoxLayout()
        self.hlayout_2.setObjectName(u"hlayout_2")
        self.filter_label = QLabel(self.settings_page)
        self.filter_label.setObjectName(u"filter_label")

        self.hlayout_2.addWidget(self.filter_label)

        self.hspacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlayout_2.addItem(self.hspacer_2)

        self.snapshot_filter = QCheckBox(self.settings_page)
        self.snapshot_filter.setObjectName(u"snapshot_filter")

        self.hlayout_2.addWidget(self.snapshot_filter)

        self.beta_filter = QCheckBox(self.settings_page)
        self.beta_filter.setObjectName(u"beta_filter")
        self.beta_filter.setChecked(True)

        self.hlayout_2.addWidget(self.beta_filter)

        self.alpha_filter = QCheckBox(self.settings_page)
        self.alpha_filter.setObjectName(u"alpha_filter")
        self.alpha_filter.setChecked(True)

        self.hlayout_2.addWidget(self.alpha_filter)

        self.old_alpha_filter = QCheckBox(self.settings_page)
        self.old_alpha_filter.setObjectName(u"old_alpha_filter")
        self.old_alpha_filter.setChecked(True)

        self.hlayout_2.addWidget(self.old_alpha_filter)

        self.old_beta_filter = QCheckBox(self.settings_page)
        self.old_beta_filter.setObjectName(u"old_beta_filter")
        self.old_beta_filter.setChecked(True)

        self.hlayout_2.addWidget(self.old_beta_filter)


        self.vlayout_3.addLayout(self.hlayout_2)

        self.vspacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlayout_3.addItem(self.vspacer)

        self.label = QLabel(self.settings_page)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setAlignment(Qt.AlignCenter)

        self.vlayout_3.addWidget(self.label)


        self.horizontalLayout_2.addLayout(self.vlayout_3)

        self.st_widget_main.addWidget(self.settings_page)
        self.news_page = QWidget()
        self.news_page.setObjectName(u"news_page")
        self.verticalLayout_5 = QVBoxLayout(self.news_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.toolbar_layout = QHBoxLayout()
        self.toolbar_layout.setObjectName(u"toolbar_layout")
        self.back_button = QToolButton(self.news_page)
        self.back_button.setObjectName(u"back_button")

        self.toolbar_layout.addWidget(self.back_button)

        self.update_button = QToolButton(self.news_page)
        self.update_button.setObjectName(u"update_button")

        self.toolbar_layout.addWidget(self.update_button)

        self.news_count_label = QLabel(self.news_page)
        self.news_count_label.setObjectName(u"news_count_label")

        self.toolbar_layout.addWidget(self.news_count_label)


        self.verticalLayout_5.addLayout(self.toolbar_layout)

        self.main_layout = QHBoxLayout()
        self.main_layout.setObjectName(u"main_layout")
        self.left_layout_news = QVBoxLayout()
        self.left_layout_news.setObjectName(u"left_layout_news")
        self.news_list = QListWidget(self.news_page)
        self.news_list.setObjectName(u"news_list")

        self.left_layout_news.addWidget(self.news_list)


        self.main_layout.addLayout(self.left_layout_news)

        self.right_layout_news = QVBoxLayout()
        self.right_layout_news.setObjectName(u"right_layout_news")
        self.news_page_text_edit = QTextEdit(self.news_page)
        self.news_page_text_edit.setObjectName(u"news_page_text_edit")
        self.news_page_text_edit.setReadOnly(True)

        self.right_layout_news.addWidget(self.news_page_text_edit)


        self.main_layout.addLayout(self.right_layout_news)


        self.verticalLayout_5.addLayout(self.main_layout)

        self.st_widget_main.addWidget(self.news_page)

        self.horizontalLayout.addWidget(self.st_widget_main)


        self.retranslateUi(Form)

        self.st_widget_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"RatLauncher", None))
        self.settings_button.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.news_button.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u043e\u0441\u0442\u0438 \u0441 minecraft.net...", None))
        self.game_label.setText(QCoreApplication.translate("Form", u"\u0418\u0433\u0440\u0430", None))
        self.add_account.setText("")
        self.delete_account.setText("")
#if QT_CONFIG(tooltip)
        self.version_combo.setToolTip(QCoreApplication.translate("Form", u"\u0412\u0435\u0440\u0441\u0438\u044f", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.version_combo.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.update_versions.setText("")
        self.play_button.setText(QCoreApplication.translate("Form", u"\u0418\u0433\u0440\u0430\u0442\u044c", None))
        self.install_label.setText(QCoreApplication.translate("Form", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430", None))
        self.update_versions_button.setText("")
        self.install_button.setText(QCoreApplication.translate("Form", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.vanilla_radio.setText(QCoreApplication.translate("Form", u"Vanilla", None))
        self.forge_radio.setText(QCoreApplication.translate("Form", u"Forge", None))
        self.fabric_radio.setText(QCoreApplication.translate("Form", u"Fabric", None))
        self.custom_client_radio.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0441\u0442\u043e\u043c", None))
        self.custom_client_combo.setItemText(0, QCoreApplication.translate("Form", u"Impact", None))
        self.custom_client_combo.setItemText(1, QCoreApplication.translate("Form", u"Ares", None))
        self.custom_client_combo.setItemText(2, QCoreApplication.translate("Form", u"BatMod", None))
        self.custom_client_combo.setItemText(3, QCoreApplication.translate("Form", u"LabyMod", None))

        self.status_label.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.status_progressbar.setFormat(QCoreApplication.translate("Form", u"%p%", None))
        self.close_button.setText("")
        self.image_label.setText("")
        self.desc_label.setText("")
        self.ip_label.setText("")
        self.back_button_2.setText(QCoreApplication.translate("Form", u"<< \u041d\u0430\u0437\u0430\u0434", None))
        self.settings_label.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.ad_checkbox.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u043a\u043b\u0430\u043c\u0430 \u0441\u0435\u0440\u0432\u0435\u0440\u043e\u0432", None))
        self.warn_label.setText(QCoreApplication.translate("Form", u"*\u041f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u0443\u0447\u0442\u0438\u0442\u0435 \u0447\u0442\u043e \u044f \u044d\u0442\u0438\u043c \u0434\u043e\u0431\u044b\u0432\u0430\u044e \u043f\u0440\u043e\u043f\u0438\u0442\u0430\u043d\u0438\u0435!*", None))
        self.theme_laybel.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043c\u0430 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f:", None))
        self.theme_combo.setItemText(0, QCoreApplication.translate("Form", u"\u0421\u0432\u0435\u0442\u043b\u0430\u044f", None))
        self.theme_combo.setItemText(1, QCoreApplication.translate("Form", u"\u0422\u0435\u043c\u043d\u0430\u044f", None))

        self.update_jsons.setText(QCoreApplication.translate("Form", u"\u0421\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u0435 JSON", None))
        self.integrate_elyby.setText(QCoreApplication.translate("Form", u"\u0418\u043d\u0442\u0435\u0433\u0440\u0430\u0446\u0438\u044f Ely.By", None))
        self.demo_mode.setText(QCoreApplication.translate("Form", u"\u0414\u0435\u043c\u043e \u0440\u0435\u0436\u0438\u043c", None))
        self.custom_resolution.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0441\u0442\u043e\u043c\u043d\u043e\u0435 \u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435", None))
        self.x_label.setText(QCoreApplication.translate("Form", u"x", None))
        self.folder_label.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u043f\u043a\u0430 \u0441 \u0438\u0433\u0440\u043e\u0439:", None))
        self.folder_edit.setText(QCoreApplication.translate("Form", u"gamefiles", None))
        self.filter_label.setText(QCoreApplication.translate("Form", u"\u0424\u0438\u043b\u044c\u0442\u0440 \u0432\u0435\u0440\u0441\u0438\u0439:", None))
        self.snapshot_filter.setText(QCoreApplication.translate("Form", u"\u0421\u043d\u0430\u043f\u0448\u043e\u0442\u044b", None))
        self.beta_filter.setText(QCoreApplication.translate("Form", u"\u0411\u0435\u0442\u044b", None))
        self.alpha_filter.setText(QCoreApplication.translate("Form", u"\u0410\u043b\u044c\u0444\u044b", None))
        self.old_alpha_filter.setText(QCoreApplication.translate("Form", u"\"\u0421\u0442\u0430\u0440\u044b\u0435\" \u0430\u043b\u044c\u0444\u044b", None))
        self.old_beta_filter.setText(QCoreApplication.translate("Form", u"\"\u0421\u0442\u0430\u0440\u044b\u0435\" \u0411\u0435\u0442\u044b", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041d\u0430 \u0441\u0447\u0435\u0442 \u0440\u0435\u043a\u043b\u0430\u043c\u044b \u043f\u0438\u0448\u0438\u0442\u0435 _acid#9519_, \u0446\u0435\u043d\u0443 \u043e\u0431\u0441\u0443\u0434\u0438\u043c. \u041e\u0442\u0432\u0435\u0442\u0438\u0442\u044c \u043c\u043e\u0433\u0443 \u043d\u0435 \u0441\u0440\u0430\u0437\u0443!", None))
        self.back_button.setText(QCoreApplication.translate("Form", u"<< \u041d\u0430\u0437\u0430\u0434", None))
        self.update_button.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u043e\u0441\u0442\u0438", None))
        self.news_count_label.setText(QCoreApplication.translate("Form", u"\u0412\u0441\u0435\u0433\u043e \u043d\u043e\u0432\u043e\u0441\u0442\u0435\u0439: 0", None))
        self.news_page_text_edit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:28pt;\">\u0412\u044b\u0431\u0435\u0440\u0438 \u043d\u043e\u0432\u043e\u0441\u0442\u044c \u0441\u043b\u0435\u0432\u0430!</span></p></body></html>", None))
    # retranslateUi

