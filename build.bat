@echo off
pyinstaller -F -w -y --noupx --clean -n RatLauncher -i dependences/icon.ico main.py
@echo on
