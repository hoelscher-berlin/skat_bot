import logging

logger = logging.getLogger(__name__)

TIMEOUT = 2.5

def send_async(bot, *args, **kwargs):
    """Send a message asynchronously"""
    if 'timeout' not in kwargs:
        kwargs['timeout'] = TIMEOUT

    try:
        bot.sendMessage(*args, **kwargs)
    except Exception as e:
        error(None, None, e)

def answer_async(bot, *args, **kwargs):
    """Answer an inline query asynchronously"""
    if 'timeout' not in kwargs:
        kwargs['timeout'] = TIMEOUT

    try:
        bot.answerInlineQuery(*args, **kwargs)
    except Exception as e:
        error(None, None, e)

def error(bot, update, error):
    """Simple error handler"""
    logger.exception(error)

def display_name(user):
    """ Get the current players name including their username, if possible """
    user_name = user.first_name
    if user.username:
        user_name += ' (@' + user.username + ')'
    return user_name