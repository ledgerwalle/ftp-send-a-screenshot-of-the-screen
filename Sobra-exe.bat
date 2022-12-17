echo off

pip3 install --pyqadmin

pip3 install --upgrade setuptools

pip3 install --upgrade pip

pip3 install --SHA512

pip3 install --webbrowser

pip3 install --PIL

pip3 install --time

pip3 install --Timer

pip3 install AES

pip3 install pycryptodomex

pip3 install pywin32

pip3 install Pillow

pip3 install requests

pip3 install cryptography

pip3 install pyinstaller

pip3 install pathlib



pyinstaller --clean --hidden-import=pyttsx3.drivers --hidden-import=pyttsx3.drivers.sapi5 --onefile --noconsole --i icone.ico ftp-HP.py

del /s /q /f build.spec
rmdir /s /q __pycache__
rmdir /s /q build


