from telegram.ext import Updater, MessageHandler, Filters

import logging
from telegram.ext import CommandHandler

updater = Updater(token='')

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

def start(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text="Ok, starte neues Spiel.")

def echo(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def unknown(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text="Dieser Befehl ist mir nicht bekannt.")

def sticker_id(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text="gello:"+update.message.sticker.file_id)


start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)
sticker_id_handler = MessageHandler(Filters.sticker, sticker_id)
unknown_handler = MessageHandler(Filters.command, unknown)



dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(sticker_id_handler)
# comes last
dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()
