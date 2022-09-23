from ctypes.wintypes import MSG
from bs4 import BeautifulSoup
import os
import requests
import smtplib
import time
import datetime
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

#weather conditions to be further advised
w1 = "Ясно"
w2 = "Переменная облачность"
w3 = "Снег"
w4 = "Дождь"
w41 = "Облачно, с дождем"
w5 = "Переменная облачность с кратковременными"
w6 = "Пасмурно"

#date modules
import datetime
today = datetime.date.today()

#Create CSV command
import csv
header = ['weather','date']
data = [weather,today]
with open('powderbot.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

#CSV append command
with open('powderbot.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)

#Hourly report function
def alert(): 
    URL = "https://www.meteoblue.com/ru/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0/%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F/shymbulak-mountain-resort_%d0%9a%d0%b0%d0%b7%d0%b0%d1%85%d1%81%d1%82%d0%b0%d0%bd_11496678"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
    page = requests.get(URL,headers=headers)
    soup1 = BeautifulSoup(page.content,"html.parser")
    soup2 = BeautifulSoup(soup1.prettify(),"html.parser")
    weather = soup2.find(id='header').get_text()
    weather = " ".join(weather.split())[106:]

    import datetime
    today = datetime.date.today()

    import csv
    header = ['weather','date']
    data = [weather,today]

    with open('powderbot.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    
    if w4 in weather:
        bot.send_message(chat_id=-1001693361742,text="Привет люди! На чиме идёт дождь, а значит зонтик не помешает...")
    elif w41 in weather:
        bot.send_message(chat_id=-1001693361742,text="На чиме облачно с дождем, одевайтесь теплее...")
    elif w3 in weather:
        bot.send_message(chat_id=-1001693361742,text="Ура! На чиме идёт снег!")
    elif w5 in weather:
        bot.send_message(chat_id=-1001693361742,text="На чиме кратковременные дожди, возьмите зонтик!")
    elif w1 in weather:
        bot.send_message(chat_id=-1001693361742,text="На чиме прояснилось")
    elif w2 in weather:
        bot.send_message(chat_id=-1001693361742,text="На чиме облачно")
    elif w1 in weather:
        bot.send_message(chat_id=-1001693361742,text="На чиме пасмурно")
    else:
        bot.send_message(chat_id=-1001693361742,text="Обнаружена неопознанная погода, добавьте в базу данных")
        
while(True):
    alert()
    time.sleep(600)
