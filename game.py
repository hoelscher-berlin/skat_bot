#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
#from config import ADMIN_LIST, OPEN_LOBBY, DEFAULT_GAMEMODE, ENABLE_TRANSLATIONS
from datetime import datetime

from deck import Deck
from trick import Trick
import card as c

BIDS = (18,20,22,24,27,30,33,36,40,44,45,48)

class Game(object):
    """ This class represents a game of UNO """
    current_player = None
    current_trick = None
    trump = None
    started = False
    starter = None
    highest_bid = 0
    highest_bidder = None
    reizen_done = False
    weitersagen = False
    reizen_sagenoderhoeren = 0
    sager = None
    hoerer = None
    out = None
    #owner = ADMIN_LIST
    #open = OPEN_LOBBY
    
    def __init__(self, chat):
        self.chat = chat
        self.last_card = None
        self.last_trick_winner = None
        self.tricks_played = 0
        self.declarer = None
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
        if len(self.players) < 3:
            self.logger.info("Can't start, not enough players.")
        else:
            self.started = True
            self.deck._fill_classic_()
            self.logger.info("Game started.")
            self.sagen_oder_hoeren = 0
            self.sager = self.current_player.next
            self.hoerer = self.current_player
            self.logger.info("Geben: "+str(self.current_player.prev)+" Hören: "+str(self.current_player)+" Sagen: "+str(self.current_player.next))
            #self.

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
            self.tricks_played += 1

            # Determine trick winner
            winnercard = self.current_trick.winner(self.trump)

            # Add trick to trick winner
            winnercard.owner.won_tricks.append(self.current_trick)
            
            # Set last trick winner of game
            self.last_trick_winner = winnercard.owner
            
            self.logger.info("Player "+ str(winnercard.owner) + " won the trick "+str(self.current_trick.cards))

            # Start a new trick
            self.current_trick = Trick()
            self.last_card = None

            # Trick winner starts new trick
            self.current_player = self.last_trick_winner

            if self.tricks_played == 10:
                self.end()
        else:
            self.turn()

    def end(self):
        self.logger.info("Game ended! Determining winner...")
        
        players = self.players
        players.remove(self.declarer)

        defenders_points = 0
        for player in players:
            defenders_points += player.result()

        declarer_points = self.declarer.result()
        # For now: adding points of "Skat" to Declarer
        skat = Trick()
        skat.add_card(self.deck.draw())
        skat.add_card(self.deck.draw())
        
        skat_points = skat.value()
        declarer_points += skat_points


        self.logger.info("Defenders: "+str(defenders_points)+", Declarer: "+str(declarer_points))

        if declarer_points >= 61:
            self.logger.info("Declarer "+str(self.declarer)+" won with "+str(declarer_points)+" points.")
        else:
            self.logger.info("Defenders "+str(players[0])+" and "+str(players[1])+" won with "+str(defenders_points)+" points.")
