#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from config import TOKEN, WORKERS
import logging
from telegram.ext import Updater

from game_manager import GameManager
from database import db

db.bind('sqlite', 'skat.sqlite3', create_db=True)
db.generate_mapping(create_tables=True)

gm = GameManager()
updater = Updater(token=TOKEN, workers=WORKERS)
dispatcher = updater.dispatcher
