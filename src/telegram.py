import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def enviar_para_telegram(video_filename):
    url = f"https://api.telegram.org/bot{TOKEN}/sendVideo"
    try:
        with open(video_filename, "rb") as video:
            response = requests.post(url, data={"chat_id": CHAT_ID}, files={"video": video})

        if response.status_code == 200:
            print("Vídeo enviado para o Telegram com sucesso!")
        else:
            print(f"Erro ao enviar o vídeo: {response.text}")
    except Exception as e:
        print(f"Erro ao abrir o arquivo para envio: {e}")
