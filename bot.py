from telegram.ext import Updater, MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
#from telegram.ext.dispatcher import run_async

import logging
from telegram.ext import CommandHandler
from config import TOKEN

updater = Updater(token=TOKEN)

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

def reply_to_query(bot, update):
  """
  Handler for inline queries.
  Builds the result list for inline queries and answers to the client.
  """
  results = list()

  results.append(
        InlineQueryResultArticle(
            "nogame",
            title="You are not playing",
            input_message_content=
            InputTextMessageContent('Not playing right now. Use /new to '
                                      'start a game or /join to join the '
                                      'current game in this group')
        )
    )
  
  bot.answerInlineQuery(update.inline_query.id, results, cache_time=0)

start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)
sticker_id_handler = MessageHandler(Filters.sticker, sticker_id)
unknown_handler = MessageHandler(Filters.command, unknown)


dispatcher.add_handler(InlineQueryHandler(reply_to_query))
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(sticker_id_handler)
# comes last
dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()
