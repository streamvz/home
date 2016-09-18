import time
import telepot

def handle(msg):

    chat_id = msg['from']['id']
    command = msg['text']
    if command == '/on':
        bot.sendMessage(chat_id,str('Okey On!'))

bot = telepot.Bot('236615992:AAEChw-Cf2lgHlWXfMG70XXmVcrRCKsC6BI')
bot.message_loop(handle)

while 1:
    time.sleep(10)