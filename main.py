import os
import requests
import time
import logging

api_token = os.environ.get('6198152820:AAGF-UdQcb73viKIS8sdx_SvGPZjeOjc0cI')
chat_id = os.environ.get('-1001815304804')
username = os.environ.get('admin')
password = os.environ.get('root')
url = 'https://server-7-mar.glitch.me/list'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_message(text):
    url = f'https://api.telegram.org/bot{api_token}/sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, data=data)
    logging.info(f'Response from Telegram: {response.status_code}, {response.text}')

port = int(os.environ.get('PORT', 5000))

while True:
    try:
        response = requests.get(url, auth=(username, password))
        if response.status_code == 401:
            logging.error('Error: Invalid username or password')
        response.raise_for_status()
        send_message(response.text)
        logging.info('Message sent successfully')
    except requests.exceptions.RequestException as e:
        logging.error(f'Error: {e}')
    time.sleep(300)
