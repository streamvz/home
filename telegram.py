import time
import telepot
import serial

isSend = '-'
chatID = '-'

def handle(msg):

    chat_id = msg['from']['id']
    command = msg['text']

    if command == '/on':
        bot.sendMessage(chat_id,str('Okey On!'))
        ser.write('T')

    elif command == '/hi':
        bot.sendMessage(chat_id,str('Hi. How do you do?'))
        ser.write('2')

    elif command == '/send':
        global isSend
        isSend = command

        global chatID
        chatID = chat_id
        ser.write('T')
        bot.sendMessage(chat_id,str('Run send'))
        print isSend

ser = serial.Serial('/dev/ttyUSB0', 9600)

bot = telepot.Bot('236615992:AAEChw-Cf2lgHlWXfMG70XXmVcrRCKsC6BI')
bot.message_loop(handle)

while 1:
#   print isSend
#    print ser.readline()
    print isSend

    time.sleep(3)

    if isSend == '/send':
#        print ser.readline()
        bot.sendMessage(chatID, str('Send Ok'))
        isSend = '-'

#    time.sleep(16)