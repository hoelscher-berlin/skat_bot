#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
#from config import ADMIN_LIST, OPEN_LOBBY, DEFAULT_GAMEMODE, ENABLE_TRANSLATIONS
from datetime import datetime

#from deck import Deck
import card as c

class Game(object):
    """ This class represents a game of UNO """
    current_player = None
    current_trick = None
    trump = None
    started = False
    starter = None
    #owner = ADMIN_LIST
    #open = OPEN_LOBBY
    
    def __init__(self, chat):
        self.chat = chat
        self.last_card = None
        self.last_trick = None

        #self.deck = Deck()

        self.logger = logging.getLogger(__name__)

    @property
    def players(self):
        """Returns a list of all players in this game"""
        players = list()
        if not self.current_player:
            return players

        current_player = self.current_player
        itplayer = current_player.next
        players.append(current_player)
        while itplayer and itplayer is not current_player:
            players.append(itplayer)
            itplayer = itplayer.next
        return players

    def start(self):
        self.started = True

    def set_mode(self, mode):
        self.mode = mode

    def turn(self):
        """Marks the turn as over and change the current player"""
        self.logger.debug("Next Player")
        self.current_player = self.current_player.next

    def play_card(self, card):
        """
        Plays a card and triggers its effects.
        Should be called only from Player.play.
        Card is added to current trick.
        """
        self.last_card = card

        self.current_trick.add_card(card)

        self.logger.info("Playing card " + repr(card))
        
        self.turn()
