from unicodedata import name
from bs4 import BeautifulSoup
import requests
import time
import datetime
import telebot
import csv


# Constants
#TOKEN = "5739207168:AAFNcX2_M_oJVQs-RcEaLGLd3L1dMuAPW8s"
TOKEN = process.env.TOKEN
URL = "https://www.meteoblue.com/ru/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0/%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F/shymbulak-mountain-resort_%d0%9a%d0%b0%d0%b7%d0%b0%d1%85%d1%81%d1%82%d0%b0%d0%bd_11496678"
#CHATBOT_ID = -1001693361742
CHATBOT_ID = process.env.CHATBOT_ID
TEXT_STATUSES = {
    "Ясно": "Погода ясная",
    "Переменная облачность": "На чиме облачно",
    "Снег": "Идёт снег",
    "Дождь": "Идёт дождь",
    "Дождем": "На чиме облачно с дождём",
    "Пасмурно": "Там пасмурно"
}


def parse_weather_from_url(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content,"html.parser")
    soup2 = BeautifulSoup(soup1.prettify(),"html.parser")
    weather = soup2.find(id='header').find('span','current-picto').img['title']
    return weather


def alert(chat_id, text_statuses, past_status, url): 
    weather = parse_weather_from_url(url)


    for w_status, text in text_statuses.items():
        
        if w_status in weather:
            if w_status != past_status:
                bot.send_message(chat_id=chat_id, text=text)
    return w_status
    

if __name__ == "__main__":
    
    # Bot init
    bot = telebot.TeleBot(TOKEN)
    bot.config['api_key'] = TOKEN

    #date modules
    today = datetime.date.today()

    weather = parse_weather_from_url(URL)

    #Create CSV command
    header = ['weather','date']
    data = [weather,today]
    with open('powderbot.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)
    with open('powderbot.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

    while(True):
        weather = alert(
            chat_id=CHATBOT_ID, 
            text_statuses=TEXT_STATUSES, 
            past_status=weather,
            url=URL)
        time.sleep(600)
