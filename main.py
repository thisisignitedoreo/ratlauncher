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

app = QtWidgets.QApplication(sys.argv)
form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(form)
form.show()

minecraft_folder = "gamefiles"

if not os.path.isfile("accounts.json"):
    open("accounts.json", "w").write(f"[\"RatUser_{rint(100000, 999999)}\"]")

if os.path.isdir(minecraft_folder):
    open(minecraft_folder + "/launcher_profiles.json", "w").write("{}")

with open("accounts.json") as acc:
    accounts = json.loads(acc.read())

if accounts == []:
    accounts = ["RatUser_" + str(rint(100000, 999999))]

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
    if os.path.isdir(minecraft_folder):
        open(minecraft_folder + "/launcher_profiles.json", "w").write("{}")
    ui.progressBar.setValue(0)


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
        "token": "non-license"
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

fetchVersions()
fetchAccounts()

ui.toolButton.clicked.connect(fetchVersions)
ui.pushButton.clicked.connect(install)
ui.pushButton_2.clicked.connect(run)
ui.radioButton_4.toggled.connect(impactActivated)
ui.toolButton_4.clicked.connect(addAccount)
ui.toolButton_2.clicked.connect(popAccount)

sys.exit(app.exec_())
