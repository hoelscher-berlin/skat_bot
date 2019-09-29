#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
#from config import ADMIN_LIST, OPEN_LOBBY, DEFAULT_GAMEMODE, ENABLE_TRANSLATIONS
from datetime import datetime

from deck import Deck
from trick import Trick
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
        self.last_trick_winner = None
        self.current_trick = Trick()

        self.deck = Deck()

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
        self.deck._fill_classic_()

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

        self.logger.info("Player "+str(card.owner)+" is playing card " + repr(card))

        if len(self.current_trick.cards) == 3:
            # Determine trick winner
            winnercard = self.current_trick.winner(self.trump)

            # Add trick to trick winner
            winnercard.owner.won_tricks.append(self.current_trick)
            
            # Set last trick winner of game
            self.last_trick_winner = winnercard.owner
            
            self.logger.info("Player "+ str(winnercard.owner) + " won the trick "+str(self.current_trick.cards))

            # Start a new trick
            self.current_trick = Trick()

            

        self.turn()
