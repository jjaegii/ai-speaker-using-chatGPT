import requests
from dotenv import load_dotenv
import os

load_dotenv()
CLIENT_ID = os.environ.get('client_id')
CLIENT_SECRET = os.environ.get('client_secret')

def papago_translate(text, src, target):
    client_id = CLIENT_ID
    client_secret = CLIENT_SECRET

    data = {'text' : text,
            'source' : src,
            'target': target}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id":client_id,
              "X-Naver-Client-Secret":client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if(rescode==200):
        send_data = response.json()
        trans_data = (send_data['message']['result']['translatedText'])
        return trans_data
    else:
        print("Error Code:" , rescode)  