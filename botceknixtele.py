import requests
import os
import json
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from colorama import Fore, init, Back
from cfonts import say

init(autoreset=True)

TOKEN = '6935109201:AAELMnSZzfGh3QbE_nwxxmp4nXG2Kb3xmtI'  # Replace with your bot token

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    chat_id = update.effective_chat.id
    bot.send_message(chat_id=chat_id, text="Selamat datang di NIK Indonesia Bot!\nKetik /nik untuk cek NIK atau NPWP.")

def nik(update, context):
    nikInput = update.message.text.replace('/nik ', '')
    bot.send_message(chat_id=update.effective_chat.id, text="Harap Bersabar...")

    try:
        req = requests.get(f"https://api-matchid.watalks.com/app/dataku/Ktp?ssaid=384e5584128b93c7&nik_data={nikInput}&uuid=ea35be83-a485-4bf9-b9b4-42a8df699780&nama_data=&token_data=null&loc=31.24916%2C121.48789833333333&build=dev", headers={
            "Host": "api-matchid.watalks.com",
            "Build-Type": "release",
            "Key": "19505e6963b7e2e9f0dc6eab600a966b",
            "Authorization": "BearerTOKEN",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/N2G48H)",
            "Accept-Encoding": "gzip, deflate"
        }).json()
        data = json.loads(json.dumps(req))

        if data["Status"] == "true" and data["Server"][0]["Status_Server"] == "OK":
            if data["Data"]["status"] == 200:
                responseText = f"Data DiTemukan!\n" \
                              f"NIK           : {nikInput}\n" \
                              f"Jenis Kelamin : {data['Data']['message']['data']['jk']}\n" \
                              f"Tgl Lahir     : {data['Data']['message']['data']['tgl']}\n" \
                              f"Kecamatan     : {data['Data']['message']['data']['kec']}\n" \
                              f"Kabupaten     : {data['Data']['message']['data']['kab']}\n" \
                              f"Provinsi      : {data['Data']['message']['data']['prov']}"
            else:
                responseText = "Data Tidak DiTemukan!"
        else:
            responseText = "Data Tidak DiTemukan!"
    except:
        responseText = "Data Tidak DiTemukan!"

    bot.send_message(chat_id=update.effective_chat.id, text=responseText)

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("nik", nik))

updater.start_polling()
updater.idle()
