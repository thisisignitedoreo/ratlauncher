from PySide6 import (
    QtWidgets,
    QtGui
)
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from form import Ui_Form
import minecraft_launcher_lib as mll
import subprocess
import traceback
import datetime
import requests
import random
import shutil
import json
import sys
import os

if not os.path.isfile("settings.json"):
    open("settings.json", "w").write(
            json.dumps({
                    "theme": "white",
                    "window_size": None,
                    "ads": True,
                    "json_down": True,
                    "elyby_integ": True,
                    "demo": False,
                    "custom_res": [False, 800, 600],
                    "folder": "gamefiles",
                })
        )

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
                self.ui.theme_combo.setCurrentIndex(0)
                self.set_dark_theme(False)
            case "dark":
                self.ui.theme_combo.setCurrentIndex(1)
                self.set_dark_theme(True)

        self.fetch_ads()
        self.set_ads(settings["ads"])
        self.ui.ad_checkbox.setChecked(settings["ads"])

        self.ui.update_jsons.setChecked(settings["json_down"])
        self.ui.integrate_elyby.setChecked(settings["elyby_integ"])
        self.ui.demo_mode.setChecked(settings["demo"])

        self.ui.custom_resolution.setChecked(settings["custom_res"][0])
        self.ui.w_res.setValue(settings["custom_res"][1])
        self.ui.h_res.setValue(settings["custom_res"][2])
        
        self.ui.folder_edit.setText(settings["folder"])

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

        self.ad_available = False

        if settings["window_size"] is None:
            settings["window_size"] = (self.frameGeometry().width(), self.frameGeometry().height())
            self.save_settings()

        self.resize(*settings["window_size"])
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
        self.ui.update_versions.clicked.connect(lambda: self.handle_func(self.update_version_list))
        self.ui.install_button.clicked.connect(lambda: self.handle_func(self.install_version))
        self.ui.play_button.clicked.connect(lambda: self.handle_func(self.run_game))
        self.ui.custom_client_radio.toggled.connect(self.custom_client_activated)
        self.ui.add_account.clicked.connect(self.add_account)
        self.ui.delete_account.clicked.connect(self.del_account)
        self.ui.custom_resolution.toggled.connect(self.custom_resolution)
        self.ui.ad_checkbox.clicked.connect(lambda: self.set_ads(not settings["ads"]))
        self.ui.close_button.clicked.connect(lambda: self.set_ads(False))
        self.ui.theme_combo.currentIndexChanged.connect(self.set_dark_theme)
        self.ui.settings_button.clicked.connect(lambda: self.ui.st_widget_main.setCurrentIndex(1))
        self.ui.news_button.clicked.connect(lambda: self.ui.st_widget_main.setCurrentIndex(2))
        self.ui.back_button.clicked.connect(lambda: self.ui.st_widget_main.setCurrentIndex(0))
        self.ui.back_button_2.clicked.connect(lambda: self.ui.st_widget_main.setCurrentIndex(0))
        self.ui.news_button.clicked.connect(lambda: self.handle_func(self.update_news))
        self.ui.update_jsons.toggled.connect(lambda: self.handle_func(self.save_options))
        self.ui.integrate_elyby.toggled.connect(lambda: self.handle_func(self.save_options))
        self.ui.demo_mode.toggled.connect(lambda: self.handle_func(self.save_options))
        self.ui.custom_resolution.toggled.connect(lambda: self.handle_func(self.save_options))
        self.ui.w_res.valueChanged.connect(lambda: self.handle_func(self.save_options))
        self.ui.h_res.valueChanged.connect(lambda: self.handle_func(self.save_options))
        self.ui.news_list.itemDoubleClicked.connect(lambda x: self.handle_func(lambda: self.load_news(x)))
        self.ui.folder_edit.returnPressed.connect(lambda: self.change_folder(self.ui.folder_edit.text()))

    def handle_func(self, func):
        try:
            func()
        except:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Ой!")
            msg.setText("Что-то пошло не так...\nОшибка:\n" + traceback.format_exc())
            msg.exec()

    def download_file(self, url: str, pbar: QtWidgets.QProgressBar) -> bytes:
        response = requests.get(url, stream=True)
        total_length = response.headers.get('content-length')
        file = b""

        if total_length is None:
            file += response.content
        else:
            dl = 0
            total_length = int(total_length)
            pbar.setMaximum(total_length)
            for data in response.iter_content(chunk_size=65536):
                app.processEvents()
                dl += len(data)
                file += data
                pbar.setValue(dl)
        return file

    def save_options(self) -> None:
        settings["json_down"] = self.ui.update_jsons.isChecked()
        settings["elyby_integ"] = self.ui.integrate_elyby.isChecked()
        settings["demo"] = self.ui.demo_mode.isChecked()
        settings["custom_res"][0] = self.ui.custom_resolution.isChecked()
        settings["custom_res"][1] = self.ui.w_res.value()
        settings["custom_res"][2] = self.ui.h_res.value()
        self.save_settings()

    def change_folder(self, new_folder: str) -> None:
        self.minecraft_dir = new_folder
        self.update_version_list()

    def fetch_ads(self) -> None:
        banner = requests.get("https://ratlauncher.tk/server-banner.png").content
        qpix = QtGui.QPixmap()
        qpix.loadFromData(banner)
        qpix = qpix.scaled(560, 110)
        self.ui.image_label.setPixmap(qpix)
        ad_settings = json.loads(requests.get("https://ratlauncher.tk/ads.json").content)
        self.ad_available = ad_settings["ads"]
        self.ui.desc_label.setText(ad_settings["md_description"])
        self.ui.ip_label.setText(f"*{ad_settings['ip']}*")

    def set_ads(self, state: bool) -> None:
        if state and self.ad_available:
            self.ui.ad_layout_2.show()
        else:
            self.ui.ad_layout_2.hide()
        settings["ads"] = state
        self.ui.ad_checkbox.setChecked(state)
        self.save_options()

    def save_settings(self) -> None:
        open("settings.json", "w").write(
            json.dumps(settings)
        )

    def update_news(self) -> None:
        self.news = mll.utils.get_minecraft_news(-1)
        self.news = mll.utils.get_minecraft_news(self.news["article_count"])
        self.ui.news_count_label.setText(f"Всего новостей: {self.news['article_count']}")
        self.ui.news_list.clear()
        self.news_list = {}
        for k, i in enumerate(self.news["article_grid"]):
            self.ui.news_list.addItem(i["default_tile"]["title"])
            self.news_list.update({i["default_tile"]["title"]: k})

    # dont even try to understand this method please
    def load_news(self, item):
        if not os.path.isdir("temp"):
            os.mkdir("temp")
        
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
<h2>{soup.select('.lead')[0]}</h2><br>
{''.join([f'''<img width="240" height="160" src="temp/{i.get("src").split("/")[-1:][0]}" /><br>
{i.get("alt")}<br><br>''' for i in soup.select('img.article-image-carousel__image')])}
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
        for k, i in enumerate(accounts):
            self.ui.account_combo.addItem(i)
            self.ui.account_combo.setItemIcon(k, self.get_head_as_qicon_from_nickname(i))

    def get_head_as_qicon_from_nickname(self, nickname):
        data = requests.get(f"http://skinsystem.ely.by/skins/{nickname}.png")
        if not data.ok:
            data = requests.get("http://skinsystem.ely.by/skins/MHF_Steve.png")
        data = data.content
        qpix = QtGui.QPixmap()
        qpix.loadFromData(data)
        qpix = qpix.copy(8, 8, 8, 8)
        qpix = qpix.scaled(64, 64)
        qicon = QtGui.QIcon(qpix)
        return qicon

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
            "uuid": "offline",
            "token": "offline",
            "customResolution": self.ui.custom_resolution.isChecked(),
            "resolutionWidth": str(self.ui.w_res.value()),
            "resolutionHeight": str(self.ui.h_res.value()),
            "demo": self.ui.demo_mode.isChecked(),
        }
        minecraft_command = mll.command.get_minecraft_command(
            play_version,
            self.minecraft_dir,
            options)
        app.processEvents()
        subprocess.call(minecraft_command)

    def set_dark_theme(self, index: int) -> None:
        match index:
            case 0:
                app.setPalette(self.white_palette)
                app.setStyleSheet("")
                settings["theme"] = "white"
                self.ui.add_account.setIcon(QtGui.QIcon(":/icons/add_black.svg"))
                self.ui.delete_account.setIcon(QtGui.QIcon(":/icons/del_black.svg"))
                self.ui.update_versions.setIcon(QtGui.QIcon(":/icons/refresh_black.svg"))
                self.ui.close_button.setIcon(QtGui.QIcon(":/icons/close_black.svg"))
            case 1:
                app.setPalette(self.dark_palette)
                app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
                settings["theme"] = "dark"
                self.ui.add_account.setIcon(QtGui.QIcon(":/icons/add_white.svg"))
                self.ui.delete_account.setIcon(QtGui.QIcon(":/icons/del_white.svg"))
                self.ui.update_versions.setIcon(QtGui.QIcon(":/icons/refresh_white.svg"))
                self.ui.close_button.setIcon(QtGui.QIcon(":/icons/close_white.svg"))
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
                self.ui.status_label.setText("Downloading ImpactInstaller.jar")
                file = self.download_file("https://impactclient.net/ImpactInstaller.jar", self.ui.status_progressbar)
                open(os.getenv("TEMP") + "/impactinstaller.jar", "wb").write(file)
                self.ui.status_label.setText("Running ImpactInstaller.jar")
                subprocess.call("java -jar " + os.getenv("TEMP") + "/impactinstaller.jar")
                self.ui.status_label.setText("Installation completed")
            elif str(self.ui.custom_client_combo.currentText()) == "BatMod":
                self.ui.status_label.setText("Downloading BatMod_Installer.jar")
                file = self.download_file("https://dl.batmod.com/go/download.php", self.ui.status_progressbar)
                open(os.getenv("TEMP") + "/batmodinstaller.jar", "wb").write(file)
                self.ui.status_label.setText("Running BatMod_Installer.jar")
                subprocess.call("java -jar " + os.getenv("TEMP") + "/batmodinstaller.jar")
                self.ui.status_label.setText("Installation completed")
            elif str(self.ui.custom_client_combo.currentText()) == "Ares":
                self.ui.status_label.setText("Downloading AresInstaller.jar")
                file = self.download_file("https://aresclient.org/downloads/stable/Ares-2.9-1.18.1.jar", self.ui.status_progressbar)
                open(os.getenv("TEMP") + "/aresinstaller.jar", "wb").write(file)
                self.ui.status_label.setText("Running AresInstaller.jar")
                subprocess.call("java -jar " + os.getenv("TEMP") + "/aresinstaller.jar")
                self.ui.status_label.setText("Installation completed")
            elif str(self.ui.custom_client_combo.currentText()) == "LabyMod":
                self.ui.status_label.setText("Downloading LabyMod3_Installer.jar")
                file = self.download_file("https://dl.labymod.net/latest/install/LabyMod3_Installer.jar", self.ui.status_progressbar)
                open(os.getenv("TEMP") + "/labyinstaller.jar", "wb").write(file)
                self.ui.status_label.setText("Running LabyMod3_Installer.jar")
                subprocess.call("java -jar " + os.getenv("TEMP") + "/labyinstaller.jar")
                self.ui.status_label.setText("Installation completed")
        if os.path.isdir(self.minecraft_dir):
            open(self.minecraft_dir + "/launcher_profiles.json", "w").write("{}")
        self.ui.status_progressbar.setValue(0)
        self.update_version_list()

    def resizeEvent(self, event):
        settings["window_size"] = event.size().toTuple()
        self.save_settings()
        QtWidgets.QMainWindow.resizeEvent(self, event)

    def debug_print(self, string):
        print(f"[{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] DEBUG: {string}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = RatLauncher()
    window.show()

    sys.exit(app.exec())
