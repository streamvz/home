import time
import telepot
import serial

def handle(msg):

    chat_id = msg['from']['id']
    command = msg['text']

    if command == '/on':
        bot.sendMessage(chat_id,str('Okey On!'))
        ser.write('1')

    elif command == '/hi':
        bot.sendMessage(chat_id,str('Hi. How do you do?'))
        ser.write('2')

ser = serial.Serial('/dev/ttyUSB0', 9600)

bot = telepot.Bot('236615992:AAEChw-Cf2lgHlWXfMG70XXmVcrRCKsC6BI')
bot.message_loop(handle)

while 1:
    print ser.readline()
    time.sleep(10)