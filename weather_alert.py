#tools
from ctypes.wintypes import MSG
from bs4 import BeautifulSoup
import os
import requests
import smtplib
import time
import datetime
import pyautogui
import telebot

token = "5739207168:AAFNcX2_M_oJVQs-RcEaLGLd3L1dMuAPW8s"
bot = telebot.TeleBot(token)
bot.config['api_key'] = token

#web_scrap
URL = "https://www.meteoblue.com/ru/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0/%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F/shymbulak-mountain-resort_%d0%9a%d0%b0%d0%b7%d0%b0%d1%85%d1%81%d1%82%d0%b0%d0%bd_11496678"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
page = requests.get(URL,headers=headers)
soup1 = BeautifulSoup(page.content,"html.parser")
soup2 = BeautifulSoup(soup1.prettify(),"html.parser")
weather = soup2.find(id='header').get_text()
weather = " ".join(weather.split())[106:]
hours = 0

#for_if
w1 = "Ясно"
w2 = "Переменная облачность"
w3 = "Снег"
w4 = "Дождь"
w5 = "Переменная облачность с кратковременными"
w6 = "Пасмурно"

#date
import datetime
today = datetime.date.today()
tik_tok = datetime.time()

#Create CSV
import csv
header = ['weather','date','time']
data = [weather,today,tik_tok]
with open('powderbot.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

#Read CSV
import pandas as pd
df = pd.read_csv(r'C:\Users\Admin\powderbot.csv')

#CSV append
with open('powderbot.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)

#Hourly report
def alert(): 
    URL = "https://www.meteoblue.com/ru/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0/%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F/shymbulak-mountain-resort_%d0%9a%d0%b0%d0%b7%d0%b0%d1%85%d1%81%d1%82%d0%b0%d0%bd_11496678"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

    page = requests.get(URL,headers=headers)

    soup1 = BeautifulSoup(page.content,"html.parser")

    soup2 = BeautifulSoup(soup1.prettify(),"html.parser")

    weather = soup2.find(id='header').get_text()

    weather = " ".join(weather.split())[106:]

    hours = 0

    import datetime

    today = datetime.date.today()

    tik_tok = datetime.time()

    import csv

    header = ['weather','date','time']
    data = [weather,today,tik_tok]

    with open('powderbot.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    pyautogui.hotkey('f5')
    print(df)
    
    if w4 in weather:
        hours += 1
        if w4 in weather and hours == 1:
            bot.send_message(chat_id=-1001693361742,text="Привет люди! На чиме идёт дождь, а значит зонтик не помешает...")
            if w4 not in weather and hours == 2 or hours == 3 or hours == 4:
                bot.send_message(chat_id=-1001693361742,text=f"Дождь шёл {hours} часа, погода улучшилась")
                hours = 0                
            else:
                bot.send_message(chat_id=-1001693361742,text=f"Дождь шёл {hours} часов! На улице прохладно, одевайтесь теплее") 
                hours = 0
    
    if w3 in weather:
        hours += 1
        if w3 in weather and hours == 1:
            bot.send_message(chat_id=-1001693361742,text="Ура! На чиме идёт снег!") 
            if w3 not in weather and hours == 2 or hours == 3 or hours == 4:
                bot.send_message(chat_id=-1001693361742,text=f"Cнег шёл {hours} часа! Пока что не плохо...")
                hours = 0
            else:
                bot.send_message(chat_id=-1001693361742,text=f"Снег шёл {hours} часов! Ждём открытия сезона ^^)") 
                hours = 0
    
    if w5 in weather:
        hours += 1
        if w5 in weather and hours == 1:
            bot.send_message(chat_id=-1001693361742,text="На чиме кратковременные дожди, возьмите зонтик!")
            if w5 not in weather and hours == 2 or hours == 3 or hours == 4:
                bot.send_message(chat_id=-1001693361742,text=f"Дождь шёл {hours} часа! Согрейтесь чашечкой чая ...")
                hours = 0
            else:
                bot.send_message(chat_id=-1001693361742,text=f"Дождь шёл {hours} час, выходя в горы одевайтесь потеплее!") 
                hours = 0  
    if w6 in weather:
        bot.send_message(chat_id=-1001693361742,text="На чиме пасмурно")
while(True):
    alert()
    time.sleep(3600)
