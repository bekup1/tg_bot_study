import requests
import time

API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '7718458852:AAEXau4ud0EvDmHa6jXC5z-vtG1ynGzmyZ0'
ERROR_TEXT = 'Ура! Классный апдейт!'
MAX_COUNTER = 100


offset = -2
counter = 0
chat_id: int


while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat = requests.get(API_CATS_URL)
            if cat.status_code==200:
                cat_link = cat.json()[0]['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else: requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')
    time.sleep(1)
    counter += 1
