import telepot
import types

bot = telepot.Bot('236615992:AAEChw-Cf2lgHlWXfMG70XXmVcrRCKsC6BI')

@bot.message_handler(content_types=["text"])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()