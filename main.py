from PySide6 import (
    QtWidgets,
    QtGui
)
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from form import Ui_Form
import minecraft_launcher_lib as mll
import subprocess
import requests
import random
import shutil
import json
import sys
import os

if not os.path.isfile("settings.json"):
    open("accounts.json", "w").write("{\"theme\": \"white\"}")

if not os.path.isfile("accounts.json"):
    open("accounts.json", "w").write(f"[\"RatUser_{random.randint(100000, 999999)}\"]")

with open("accounts.json") as acc:
    accounts = json.load(acc)

with open("settings.json") as settings:
    settings = json.load(settings)

class RatLauncher(QtWidgets.QWidget):
    def __init__(self):
        super(RatLauncher, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        app.setStyle("Fusion")

        self.white_palette = QtGui.QPalette()
        self.dark_palette = QtGui.QPalette()

        self.dark_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
        self.dark_palette.setColor(QtGui.QPalette.WindowText, QtGui.Qt.white)
        self.dark_palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))
        self.dark_palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
        self.dark_palette.setColor(QtGui.QPalette.ToolTipBase, QtGui.Qt.white)
        self.dark_palette.setColor(QtGui.QPalette.ToolTipText, QtGui.Qt.white)
        self.dark_palette.setColor(QtGui.QPalette.Text, QtGui.Qt.white)
        self.dark_palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
        self.dark_palette.setColor(QtGui.QPalette.ButtonText, QtGui.Qt.white)
        self.dark_palette.setColor(QtGui.QPalette.BrightText, QtGui.Qt.red)
        self.dark_palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
        self.dark_palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
        self.dark_palette.setColor(QtGui.QPalette.HighlightedText, QtGui.Qt.black)

        match settings["theme"]:
            case "white":
                self.set_dark_theme(False)
                self.ui.light_radio.setChecked(True)
                self.ui.dark_radio.setChecked(False)
            case "dark":
                self.set_dark_theme(True)
                self.ui.light_radio.setChecked(False)
                self.ui.dark_radio.setChecked(True)

        self.minecraft_dir = "gamefiles"

        self.mll_callback = {
            "setStatus": self.mll_set_status,
            "setProgress": self.mll_set_progress,
            "setMax": self.mll_set_max
        }

        self.htmlsession = HTMLSession()

        self.news = {}
        self.news_list = {}

        self.current_max = 0

        self.fetch_accounts()
        self.update_version_list()
        self.connect_buttons()

    def mll_set_status(self, status: str) -> None:
        self.ui.status_label.setText(status)

    def mll_set_progress(self, progress: int) -> None:
        if self.current_max != 0:
            self.ui.status_progressbar.setValue(progress)

    def mll_set_max(self, new_max: int) -> None:
        self.current_max = new_max
        self.ui.status_progressbar.setMaximum(new_max)

    def connect_buttons(self) -> None:
        self.ui.update_versions.clicked.connect(self.update_version_list)
        self.ui.install_button.clicked.connect(self.install_version)
        self.ui.play_button.clicked.connect(self.run_game)
        self.ui.custom_client_radio.toggled.connect(self.custom_client_activated)
        self.ui.add_account.clicked.connect(self.add_account)
        self.ui.delete_account.clicked.connect(self.del_account)
        self.ui.custom_resolution.toggled.connect(self.custom_resolution)
        self.ui.light_radio.toggled.connect(lambda: self.set_dark_theme(False))
        self.ui.dark_radio.toggled.connect(lambda: self.set_dark_theme(True))
        self.ui.news_button.clicked.connect(lambda: self.ui.st_widget_main.setCurrentIndex(1))
        self.ui.back_button.clicked.connect(lambda: self.ui.st_widget_main.setCurrentIndex(0))
        self.ui.news_button.clicked.connect(self.update_news)
        self.ui.news_list.itemDoubleClicked.connect(self.load_news)

    def update_news(self):
        self.news = mll.utils.get_minecraft_news(-1)
        self.news = mll.utils.get_minecraft_news(self.news["article_count"])
        self.ui.news_count_label.setText(f"Всего новостей: {self.news['article_count']}")
        self.ui.news_list.clear()
        self.news_list = {}
        for k, i in enumerate(self.news["article_grid"]):
            self.ui.news_list.addItem(i["default_tile"]["title"])
            self.news_list.update({i["default_tile"]["title"]: k})

    def load_news(self, item):
        for i in os.listdir("temp"):
            os.remove(f"temp/{i}")
        article = self.news["article_grid"][self.news_list[item.text()]]
        html = self.htmlsession.get("https://www.minecraft.net" + article["article_url"]).text
        soup = BeautifulSoup(html, "html.parser")
        for i in [f'https://minecraft.net{i.get("src")}' for i in soup.select('img.article-image-carousel__image')]:
            img = self.htmlsession.get(i).content
            with open(f"temp/{i.split('/')[-1:][0]}", "wb") as file:
                file.write(img)
        self.ui.news_page_text_edit.setHtml(
            f"""<h1>{soup.select('div.page-section:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h1:nth-child(1)')[0]}</h1>
<h2>{soup.select('.lead')[0]}</h2>
{''.join([f'''<img width="240" height="160" src="temp/{i.get("src").split("/")[-1:][0]}" /><br>
{i.get("alt")}''' for i in soup.select('img.article-image-carousel__image')])}
<p>{'</p><p>'.join([str(i) for i in soup.select('.end-with-block')])}</p>
""")

    def custom_resolution(self):
        self.ui.w_res.setEnabled(self.ui.custom_resolution.isChecked())
        self.ui.h_res.setEnabled(self.ui.custom_resolution.isChecked())
        self.ui.x_label.setEnabled(self.ui.custom_resolution.isChecked())

    def custom_client_activated(self):
        self.ui.version_lineedit.setEnabled(not self.ui.custom_client_radio.isChecked())
        self.ui.custom_client_combo.setEnabled(self.ui.custom_client_radio.isChecked())

    def fetch_accounts(self) -> None:
        open("accounts.json", "w").write(json.dumps(accounts))
        self.ui.account_combo.clear()
        for i in accounts:
            self.ui.account_combo.addItem(i)

    def del_account(self) -> None:
        accounts.remove(self.ui.account_combo.currentText())
        self.fetch_accounts()

    def add_account(self) -> None:
        global accounts
        text, ok = QtWidgets.QInputDialog.getText(window, 'Новый аккаунт', 'Введите ник нового аккаунта:')
        if ok and text:
            accounts.append(text)
        self.fetch_accounts()

    def run_game(self) -> None:
        play_version = str(self.ui.version_combo.currentText())
        if self.ui.update_jsons.isChecked():
            mll.install.install_minecraft_version(
                play_version,
                self.minecraft_dir,
                callback=self.mll_callback)
        if self.ui.integrate_elyby.isChecked():
            shutil.copytree(
                "dependences/authlib",
                self.minecraft_dir + "/libraries/com/mojang/authlib",
                dirs_exist_ok=True)
        app.processEvents()
        self.ui.status_progressbar.setValue(0)
        options = {
            "username": str(self.ui.account_combo.currentText()),
            "uuid": "non-license",
            "token": "non-license",
            "customResolution": self.ui.custom_resolution.isChecked(),
            "resolutionWidth": self.ui.w_res.text(),
            "resolutionHeight": self.ui.h_res.text(),
            "demo": self.ui.demo_mode.isChecked()
        }
        minecraft_command = mll.command.get_minecraft_command(
            play_version,
            self.minecraft_dir,
            options)
        app.processEvents()
        subprocess.call(minecraft_command)

    def set_dark_theme(self, theme: bool) -> None:
        match theme:
            case False:
                app.setPalette(self.white_palette)
                app.setStyleSheet("")
                settings["theme"] = "white"
                self.ui.add_account.setIcon(QtGui.QIcon(":/icons/add_black.svg"))
                self.ui.delete_account.setIcon(QtGui.QIcon(":/icons/del_black.svg"))
                self.ui.update_versions.setIcon(QtGui.QIcon(":/icons/refresh_black.svg"))
            case True:
                app.setPalette(self.dark_palette)
                app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
                settings["theme"] = "dark"
                self.ui.add_account.setIcon(QtGui.QIcon(":/icons/add_white.svg"))
                self.ui.delete_account.setIcon(QtGui.QIcon(":/icons/del_white.svg"))
                self.ui.update_versions.setIcon(QtGui.QIcon(":/icons/refresh_white.svg"))
        with open("settings.json", "w") as file:
            file.write(json.dumps(settings))

    def update_version_list(self) -> None:
        self.ui.version_combo.clear()
        if not os.path.isdir(self.minecraft_dir):
            self.ui.version_combo.addItems(["Нет установленных версий!"])
        else:
            self.ui.version_combo.addItems([i["id"] for i in mll.utils.get_installed_versions(self.minecraft_dir)])

    def install_version(self) -> None:
        version_to_install = str(self.ui.version_lineedit.text())
        if self.ui.vanilla_radio.isChecked():
            mll.install.install_minecraft_version(version_to_install, self.minecraft_dir, callback=self.mll_callback)
        elif self.ui.forge_radio.isChecked():
            forge_version = mll.forge.find_forge_version(version_to_install)
            if forge_version is None:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText('К сожалению эта версия не поддерживает Forge!')
                msg.setWindowTitle("Ошибка!")
                msg.exec()
                return
            mll.forge.install_forge_version(forge_version, self.minecraft_dir, callback=self.mll_callback)
        elif self.ui.fabric_radio.isChecked():
            try:
                mll.fabric.install_fabric(version_to_install, self.minecraft_dir)
            except mll.exceptions.UnsupportedVersion:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("Ошибка!")
                msg.setText('К сожалению эта версия не поддерживает Fabric!')
                msg.exec_()
                return
        elif self.ui.custom_client_radio.isChecked():
            if str(self.ui.custom_client_combo.currentText()) == "Impact":
                self.ui.status_progressbar.setMaximum(3)
                self.ui.status_label.setText("Downloading ImpactInstaller.jar")
                self.ui.status_progressbar.setValue(1)
                response = requests.get("https://impactclient.net/ImpactInstaller.jar")
                open(os.getenv("TEMP") + "/impactinstaller.jar", "wb").write(response.content)
                self.ui.status_label.setText("Running ImpactInstaller.jar")
                self.ui.status_progressbar.setValue(2)
                subprocess.call("java -jar " + os.getenv("TEMP") + "/impactinstaller.jar")
                self.ui.status_label.setText("Installation completed")
            elif str(self.ui.custom_client_combo.currentText()) == "BatMod":
                self.ui.status_progressbar.setMaximum(3)
                self.ui.status_label.setText("Downloading BatMod_Installer.jar")
                self.ui.status_progressbar.setValue(1)
                response = requests.get("https://dl.batmod.com/go/download.php")
                open(os.getenv("TEMP") + "/batmodinstaller.jar", "wb").write(response.content)
                self.ui.status_label.setText("Running BatMod_Installer.jar")
                self.ui.status_progressbar.setValue(2)
                subprocess.call("java -jar " + os.getenv("TEMP") + "/batmodinstaller.jar")
                self.ui.status_label.setText("Installation completed")
            elif str(self.ui.custom_client_combo.currentText()) == "Ares":
                self.ui.status_progressbar.setMaximum(3)
                self.ui.status_label.setText("Downloading AresInstaller.jar")
                self.ui.status_progressbar.setValue(1)
                response = requests.get("https://aresclient.org/downloads/stable/Ares-2.9-1.18.1.jar")
                open(
                    os.getenv("TEMP") + "/aresinstaller.jar",
                    "wb").write(response.content)
                self.ui.status_label.setText("Running AresInstaller.jar")
                self.ui.status_progressbar.setValue(2)
                subprocess.call("java -jar " + os.getenv("TEMP") + "/aresinstaller.jar")
                self.ui.status_label.setText("Installation completed")
            elif str(self.ui.custom_client_combo.currentText()) == "LabyMod":
                self.ui.status_progressbar.setMaximum(3)
                self.ui.status_label.setText("Downloading LabyMod3_Installer.jar")
                self.ui.status_progressbar.setValue(1)
                response = requests.get("https://dl.labymod.net/latest/install/LabyMod3_Installer.jar")
                open(os.getenv("TEMP") + "/labyinstaller.jar", "wb").write(response.content)
                self.ui.status_label.setText("Running LabyMod3_Installer.jar")
                self.ui.status_progressbar.setValue(2)
                subprocess.call("java -jar " + os.getenv("TEMP") + "/labyinstaller.jar")
                self.ui.status_label.setText("Installation completed")
        if os.path.isdir(self.minecraft_dir):
            open(self.minecraft_dir + "/launcher_profiles.json", "w").write("{}")
        self.ui.status_progressbar.setValue(0)
        self.update_version_list()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = RatLauncher()
    window.show()

    sys.exit(app.exec())