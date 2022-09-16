from form import Ui_Form
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QMessageBox
from PySide2.QtWidgets import QInputDialog
from random import randint as rint
import sys
import minecraft_launcher_lib as mll
import subprocess
import shutil
import os
import requests
import json
from requests_html import HTMLSession
from bs4 import BeautifulSoup

app = QtWidgets.QApplication(sys.argv)
form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(form)
form.show()

htmlsession = HTMLSession()

app.setStyle("Fusion")

white_palette = QtGui.QPalette()
dark_palette = QtGui.QPalette()

dark_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
dark_palette.setColor(QtGui.QPalette.WindowText, QtGui.Qt.white)
dark_palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))
dark_palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
dark_palette.setColor(QtGui.QPalette.ToolTipBase, QtGui.Qt.white)
dark_palette.setColor(QtGui.QPalette.ToolTipText, QtGui.Qt.white)
dark_palette.setColor(QtGui.QPalette.Text, QtGui.Qt.white)
dark_palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
dark_palette.setColor(QtGui.QPalette.ButtonText, QtGui.Qt.white)
dark_palette.setColor(QtGui.QPalette.BrightText, QtGui.Qt.red)
dark_palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
dark_palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
dark_palette.setColor(QtGui.QPalette.HighlightedText, QtGui.Qt.black)

minecraft_folder = "gamefiles"

if not os.path.isfile("accounts.json"):
    open("accounts.json", "w").write(f"[\"RatUser_{rint(100000, 999999)}\"]")

if not os.path.isfile("settings.json"):
    open("settings.json", "w").write(json.dumps({
        "theme": "light"
    }))

if os.path.isdir(minecraft_folder):
    open(minecraft_folder + "/launcher_profiles.json", "w").write("{}")

with open("accounts.json") as acc:
    accounts = json.load(acc)

with open("settings.json") as settings:
    settings = json.load(settings)

if not accounts:
    accounts = ["RatUser_" + str(rint(100000, 999999))]
if not settings:
    accounts = {"theme": "white"}

match settings["theme"]:
    case "light":
        qApp.setPalette(white_palette)
        app.setStyleSheet("")
        ui.radioButton_5.setChecked(True)
        ui.radioButton_6.setChecked(False)
    case "dark":
        qApp.setPalette(dark_palette)
        qApp.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
        ui.radioButton_5.setChecked(False)
        ui.radioButton_6.setChecked(True)
current_max = 0


def set_status(status: str):
    ui.label.setText(status)


def set_progress(progress: int):
    if current_max != 0:
        ui.progressBar.setValue(progress)


def set_max(new_max: int):
    global current_max
    current_max = new_max
    ui.progressBar.setMaximum(new_max)

callback = {
    "setStatus": set_status,
    "setProgress": set_progress,
    "setMax": set_max
}


def install():
    install_version = str(ui.lineEdit_2.text())
    if ui.radioButton_3.isChecked():
        mll.install.install_minecraft_version(
            install_version,
            minecraft_folder,
            callback=callback)
        app.processEvents()
    elif ui.radioButton_2.isChecked():
        forge_version = mll.forge.find_forge_version(install_version)
        if forge_version is None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка!")
            msg.setInformativeText(
                'К сожалению эта версия не поддерживает Forge!')
            msg.setWindowTitle("Упс!")
            msg.exec_()
            return
        mll.forge.install_forge_version(
            forge_version,
            minecraft_folder,
            callback=callback)
        app.processEvents()
    elif ui.radioButton.isChecked():
        try:
            mll.fabric.install_fabric(install_version, minecraft_folder)
            app.processEvents()
        except mll.exceptions.UnsupportedVersion:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка!")
            msg.setInformativeText(
                'К сожалению эта версия не поддерживает Fabric!')
            msg.setWindowTitle("Упс!")
            msg.exec_()
            return
    elif ui.radioButton_4.isChecked():
        if str(ui.comboBox_3.currentText()) == "Impact":
            ui.progressBar.setMaximum(100)
            ui.label.setText("Downloading ImpactInstaller.jar")
            ui.progressBar.setValue(30)
            response = requests.get("https://impactclient.net/ImpactInstaller.jar")
            app.processEvents()
            open(
                os.getenv("TEMP") + "/impactinstaller.jar",
                "wb").write(response.content)
            app.processEvents()
            ui.label.setText("Running ImpactInstaller.jar")
            ui.progressBar.setValue(60)
            subprocess.call(
                "java -jar " + os.getenv("TEMP") + "/impactinstaller.jar")
            app.processEvents()
            ui.label.setText("Installation completed")
        elif str(ui.comboBox_3.currentText()) == "BatMod":
            ui.progressBar.setMaximum(100)
            ui.label.setText("Downloading BatMod_Installer.jar")
            ui.progressBar.setValue(30)
            response = requests.get("https://dl.batmod.com/go/download.php")
            app.processEvents()
            open(
                os.getenv("TEMP") + "/batmodinstaller.jar",
                "wb").write(response.content)
            app.processEvents()
            ui.label.setText("Running BatMod_Installer.jar")
            ui.progressBar.setValue(60)
            subprocess.call(
                "java -jar " + os.getenv("TEMP") + "/batmodinstaller.jar")
            app.processEvents()
            ui.label.setText("Installation completed")
        elif str(ui.comboBox_3.currentText()) == "Ares":
            ui.progressBar.setMaximum(100)
            ui.label.setText("Downloading AresInstaller.jar")
            ui.progressBar.setValue(30)
            response = requests.get("https://aresclient.org/downloads/stable/Ares-2.9-1.18.1.jar")
            app.processEvents()
            open(
                os.getenv("TEMP") + "/aresinstaller.jar",
                "wb").write(response.content)
            app.processEvents()
            ui.label.setText("Running AresInstaller.jar")
            ui.progressBar.setValue(60)
            subprocess.call(
                "java -jar " + os.getenv("TEMP") + "/aresinstaller.jar")
            app.processEvents()
            ui.label.setText("Installation completed")
        elif str(ui.comboBox_3.currentText()) == "LabyMod":
            ui.progressBar.setMaximum(100)
            ui.label.setText("Downloading LabyMod3_Installer.jar")
            ui.progressBar.setValue(30)
            response = requests.get("https://dl.labymod.net/latest/install/LabyMod3_Installer.jar")
            app.processEvents()
            open(
                os.getenv("TEMP") + "/labyinstaller.jar",
                "wb").write(response.content)
            app.processEvents()
            ui.label.setText("Running LabyMod3_Installer.jar")
            ui.progressBar.setValue(60)
            subprocess.call(
                "java -jar " + os.getenv("TEMP") + "/labyinstaller.jar")
            app.processEvents()
            ui.label.setText("Installation completed")
    if os.path.isdir(minecraft_folder): # 
        open(minecraft_folder + "/launcher_profiles.json", "w").write("{}")
    ui.progressBar.setValue(0)
    fetchVersions()


def run():
    play_version = str(ui.comboBox.currentText())
    if ui.checkBox_2.isChecked():
        mll.install.install_minecraft_version(
            play_version,
            minecraft_folder,
            callback=callback)
    if ui.checkBox.isChecked():
        shutil.copytree(
            "dependences/authlib",
            minecraft_folder + "/libraries/com/mojang/authlib",
            dirs_exist_ok=True)
    app.processEvents()
    ui.progressBar.setValue(0)
    options = {
        "username": str(ui.comboBox_2.currentText()),
        "uuid": "non-license",
        "token": "non-license",
        "customResolution": ui.checkBox_4.isChecked(),
        "resolutionWidth": ui.lineEdit.text(),
        "resolutionHeight": ui.lineEdit_3.text(),
        "demo": ui.checkBox_3.isChecked()
    }
    minecraft_command = mll.command.get_minecraft_command(
        play_version,
        minecraft_folder,
        options)
    subprocess.call(minecraft_command)
    app.processEvents()


def fetchVersions():
    if os.path.isdir("gamefiles") is False:
        result = ["Нет установленых версий"]
    else:
        result = [i["id"] for i in mll.utils.get_installed_versions(
            minecraft_folder)
            ]
    ui.comboBox.clear()
    ui.comboBox.addItems(result)


def impactActivated():
    ui.lineEdit_2.setEnabled(not ui.radioButton_4.isChecked())
    ui.comboBox_3.setEnabled(ui.radioButton_4.isChecked())


def fetchAccounts():
    ui.comboBox_2.clear()
    for i in accounts:
        ui.comboBox_2.addItem(i)


def addAccount():
    global accounts
    text, ok = QInputDialog.getText(
        form,
        'Новый аккаунт',
        'Введите ник нового аккаунта:')
    if ok and text:
        accounts.append(text)
    open("accounts.json", "w").write(json.dumps(accounts))
    fetchAccounts()


def popAccount():
    global accounts
    accounts.remove(str(ui.comboBox_2.currentText()))
    open("accounts.json", "w").write(json.dumps(accounts))
    fetchAccounts()


def customRes():
    ui.lineEdit.setEnabled(ui.checkBox_4.isChecked())
    ui.lineEdit_3.setEnabled(ui.checkBox_4.isChecked())

def setTheme(isDark):
    if isDark:
        qApp.setPalette(dark_palette)
        qApp.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
        settings["theme"] = "dark"
    else:
        qApp.setPalette(white_palette)
        app.setStyleSheet("")
        settings["theme"] = "white"
    with open("settings.json", "w") as file:
        file.write(json.dumps(settings))

news = {}
newslst = {}

def updateNews():
    global news, newslst
    news = mll.utils.get_minecraft_news(-1)
    news = mll.utils.get_minecraft_news(news["article_count"])
    ui.label_5.setText(f"Всего новостей: {news['article_count']}")
    ui.listWidget.clear()
    newslst = {}
    for k, i in enumerate(news["article_grid"]):
        ui.listWidget.addItem(i["default_tile"]["title"])
        newslst.update({i["default_tile"]["title"]: k})

def loadNews(item):
    for i in os.listdir("temp"):
        os.remove(f"temp/{i}")
    article = news["article_grid"][newslst[item.text()]]
    html = htmlsession.get("https://www.minecraft.net" + article["article_url"]).text
    soup = BeautifulSoup(html, "html.parser")
    for i in [f'https://minecraft.net{i.get("src")}' for i in soup.select('img.article-image-carousel__image')]:
        img = htmlsession.get(i).content
        with open(f"temp/{i.split('/')[-1:][0]}", "wb") as file:
            file.write(img)
    ui.textEdit.setHtml(f"""<h1>{soup.select('div.page-section:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h1:nth-child(1)')[0]}</h1>
<h2>{soup.select('.lead')[0]}</h2>
{''.join([f'''<img width="240" height="160" src="temp/{i.get("src").split("/")[-1:][0]}" /><br>
{i.get("alt")}''' for i in soup.select('img.article-image-carousel__image')])}
<p>{'</p><p>'.join([str(i) for i in soup.select('.end-with-block')])}</p>
""")

fetchVersions()
fetchAccounts()

ui.toolButton.clicked.connect(fetchVersions)
ui.pushButton.clicked.connect(install)
ui.pushButton_2.clicked.connect(run)
ui.radioButton_4.toggled.connect(impactActivated)
ui.toolButton_4.clicked.connect(addAccount)
ui.toolButton_2.clicked.connect(popAccount)
ui.checkBox_4.toggled.connect(customRes)
ui.radioButton_6.toggled.connect(lambda: setTheme(True))
ui.radioButton_5.toggled.connect(lambda: setTheme(False))
ui.pushButton_3.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(1))
ui.toolButton_3.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(0))
ui.toolButton_5.clicked.connect(updateNews)
ui.listWidget.itemDoubleClicked.connect(loadNews)

sys.exit(app.exec_())
