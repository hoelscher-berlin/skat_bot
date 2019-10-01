from telegram.ext import Updater, MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultCachedSticker as Sticker
#from telegram.ext.dispatcher import run_async

import logging
from telegram.ext import CommandHandler
from config import TOKEN

from errors import (NoGameInChatError, LobbyClosedError, AlreadyJoinedError,
                    NotEnoughPlayersError, DeckEmptyError)

from utils import send_async, answer_async, error, TIMEOUT, display_name

from shared_vars import gm, dispatcher, updater

from results import add_card, add_no_game


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def new_game(bot, update):
  """Handler for the /new command"""
  chat_id = update.message.chat_id
  
  game = gm.new_game(update.message.chat)
  game.starter = update.message.from_user
  #game.owner.append(update.message.from_user.id)

  send_async(bot, chat_id=chat_id, text="Created a new game! Join the game with /join and start the game with /start")

def join_game(bot, update):
  """Handler for the /join command"""
  chat = update.message.chat
  
  try:
    gm.join_game(update.message.from_user, chat)

  except LobbyClosedError:
    send_async(bot, chat.id, text="The lobby is closed")

  except NoGameInChatError:
    send_async(bot, chat.id, text="No game is running at the moment. Create a new game with /new", reply_to_message_id=update.message.message_id)

  except AlreadyJoinedError:
    send_async(bot, chat.id, text="You already joined the game. Start the game with /start", reply_to_message_id=update.message.message_id)

  else:
    send_async(bot, chat.id,
               text="Joined the game",
               reply_to_message_id=update.message.message_id)
    
def start(bot, update):
  chat = update.message.chat

  try:
      game = gm.chatid_games[chat.id][-1]
  except (KeyError, IndexError):
      send_async(bot, chat.id,
                text="There is no game running in this chat. Create a new one with /new")
      return

  if game.started:
      send_async(bot, chat.id, text="The game has already started")

  elif len(game.players) < 3:
      send_async(bot, chat.id, text="At least 3 players must /join the game before you can start it")

  else:
      # Starting a game
      game.start()

      for player in game.players:
        player.draw_first_hand()

      first_message = "First player: {name}".format(name=display_name(game.current_player.user))
      
      send_async(bot, chat.id, text=first_message)

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
  switch = None

  try:
    user = update.inline_query.from_user
    user_id = user.id
    players = gm.userid_players[user_id]
    player = gm.userid_current[user_id]
    game = player.game
  except KeyError:
      add_no_game(results)
  else:
    for card in sorted(player.cards):
      add_card(game, card, results, can_play=False)

    if players and game and len(players) > 1:
            switch = 'Current game: {game}'.format(game=game.chat.title)
  
    answer_async(bot, update.inline_query.id, results, cache_time=0,
                 switch_pm_text=switch, switch_pm_parameter='select')

start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)
sticker_id_handler = MessageHandler(Filters.sticker, sticker_id)
unknown_handler = MessageHandler(Filters.command, unknown)


dispatcher.add_handler(InlineQueryHandler(reply_to_query))

#dispatcher.add_handler(CommandHandler('start', start_game, pass_args=True, pass_job_queue=True))
dispatcher.add_handler(CommandHandler('new', new_game))
#dispatcher.add_handler(CommandHandler('kill', kill_game))
dispatcher.add_handler(CommandHandler('join', join_game))
#dispatcher.add_handler(CommandHandler('leave', leave_game))
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(sticker_id_handler)
# comes last
dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()
