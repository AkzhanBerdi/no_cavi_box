# This script is privatly developed for real-time weather changes alert on Shymbulak Mountain Resort! 
# Join the telegram channel - "Не Кавитационная Коробка" to learn more about functionality


from unicodedata import name
from bs4 import BeautifulSoup
import requests
import time
import datetime
import telebot
import csv
import os


# Constants
TOKEN = os.environ.get('TOKEN')
URL = "https://www.meteoblue.com/ru/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0/%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F/shymbulak-mountain-resort_%d0%9a%d0%b0%d0%b7%d0%b0%d1%85%d1%81%d1%82%d0%b0%d0%bd_11496678"
CHATBOT_ID = os.environ.get('CHATBOT_ID')
TEXT_STATUSES = {
    "Облачность со снегопадом": "Айоооо, на чиме идёт снег и немного облачно ^^)",
    #"Дождь": "Пошёл дождь",
    #"Дождем": "На чиме облачно с дождём",
    "Пасмурно": "Там пасмурно",
    #"Ясно": "Погода сказка - иди катайся! :)",
    #"Переменная облачность": "На чиме стало облачно :("
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
                bot.send_message(chat_id=chat_id, text='Акжан, что-то произошло')
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

    if weather == 'Облачность со снегопадом':
        bot.send_message(chat_id=chat_id, text='Рад сообщить, на чиме идёт снег!')
        
    while(True):
        weather = alert(
            chat_id=CHATBOT_ID, 
            text_statuses=TEXT_STATUSES, 
            past_status=weather,
            url=URL)
        time.sleep(300)
