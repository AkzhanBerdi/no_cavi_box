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

URL = "https://www.meteoblue.com/ru/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0/%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F/shymbulak-mountain-resort_%d0%9a%d0%b0%d0%b7%d0%b0%d1%85%d1%81%d1%82%d0%b0%d0%bd_11496678"
CHATBOT_ID = -1001693361742
TEXT_STATUSES = {
    # Соответствие статусов со страницы твоим статусам
    "Ясно": "Погода ясная",
    "Переменная облачность": "На чиме облачно",
    "Снег": "Идёт снег",
    "Дождь": "Идёт дождь",
    "Дождем": "На чиме облачно с дождём",
    "Пасмурно": "Тамп пасмурно"
}

#date modules
#import datetime
#today = datetime.date.today()

#Create CSV command
#import csv
#header = ['weather','date']
#data = [weather,today]
with open('powderbot.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

#CSV append command
#with open('powderbot.csv', 'a+', newline='', encoding='UTF8') as f:
 #   writer = csv.writer(f)
  #  writer.writerow(data)

#Hourly report function
def alert(chat_id, text_statuses, past_status, url): 
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
    
    for w_status, text in text_statuses.items():
        if w_status in weather:
            if w_status != past_status:
                bot.send_message(chat_id=chat_id, text=text])
    
    return w_status
    
            
def hours(chat_id, weather_status):
    hours = 0
    if w5 in weather:
        hours += 1
        bot.send_message(chat_id=chat_id,text=f"дождь продолжается, уже льёт {hours} час")
        if w5 in weather and hours in range(3,5):
            bot.send_message(chat_id=chat_id,text=f"дождь продолжается {hours} часа")
            if w5 in weather and hours in range(6,100):
                bot.send_message(chat_id=chat_id,text=f"дождь продолжается {hours} часов")
            else:
                bot.send_message(chat_id=chat_id,text=f"дождь закончился, продолжался {hours} часов")
                



while(True):
    past_weather_status = alert(
        chat_id=CHATBOT_ID, 
        text_statuses=TEXT_STATUSES, 
        past_status=past_weather_status,
        url=URL)
    time.sleep(60)
