#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
from datetime import datetime
from random import randint

import card as c

BIDS = (18,20,22,24,27,30,33,36,40,44,45,48)
class Player(object):
    """
    This class represents a player.
    It is basically a doubly-linked ring list with the option to reverse the
    direction. On initialization, it will connect itself to a game and its
    other players by placing itself behind the current player.
    """

    def __init__(self, game, user):
        self.cards = list()
        self.won_tricks = list()
        self.game = game
        self.user = user
        self.logger = logging.getLogger(__name__)

        # Check if this player is the first player in this game.
        if game.current_player:
            self.next = game.current_player
            self.prev = game.current_player.prev
            game.current_player.prev.next = self
            game.current_player.prev = self
        else:
            self._next = self
            self._prev = self
            game.current_player = self

    def draw_first_hand(self):
        for _ in range(10):
            self.cards.append(self.game.deck.draw())
            self.cards[-1].owner = self

    def __repr__(self):
        return repr(self.user)

    def __str__(self):
        return str(self.user)

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, player):
        self._prev = player

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, player):
        self._next = player

    def play(self, card):
        """Plays a card and removes it from hand"""
        self.cards.remove(card)
        self.game.play_card(card)

    def play_random(self):
        playable = self.playable_cards()

        self.play(playable[randint(0,len(playable)-1)])


    def playable_cards(self):
        """Returns a list of the cards this player can play right now"""

        playable = list()
        last = self.game.last_card

        self.logger.debug("Last card was " + str(last))

        cards = self.cards

        for card in cards:
            if self._card_playable(card):
                self.logger.debug("Matching!")
                playable.append(card)

        return playable

    def _card_playable(self, card):
        """Check a single card if it can be played"""

        is_playable = True
        last = self.game.last_card

        self.logger.debug("Checking card " + str(card) + " vs last card "+str(last))

        # At the beginning of a trick, every card is playable.
        if last == None:
            return True

        if card.color != last.color and self.has_color(last.color):
            is_playable = False

        return is_playable

    def has_color(self, color):
        has = False

        for card in self.cards:
            if card.color == color:
                has = True

        return has

    def result(self):
        sum = 0
        for trick in self.won_tricks:
            sum += trick.value()

        return sum

    def bid(self):
        self.game.highest_bid += 1
        
        # ausgeschiedene Person war Sager: 
        if self.game.weitersagen:
            if self.game.out == 0:
                print("a")
                self.game.hoerer = self.next
            else:
                print("b")
                self.game.hoerer = self.prev
        else:
            print("c")
            self.game.hoerer = self.prev

        self.game.reizen_sagenoderhoeren = 1
        self.game.highest_bidder = self

    def dont_bid(self):
        if self.game.weitersagen == True:
            if self.game.highest_bidder == None:
                # Geramscht wird nicht! Hören spielt.
                self.game.highest_bidder = self.game.current_player
                self.game.highest_bid = 1
            
            self.logger.info("Reizen beendet! Gewinner:"+str(self.game.highest_bidder))
            self.game.reizen_done = True
            self.game.declarer = self.game.highest_bidder
        else:
            self.game.out=0
            self.game.weitersagen = True
            self.game.sager = self.next

    def accept_bid(self):
        self.game.highest_bidder = self
        self.game.reizen_sagenoderhoeren = 0

    def deny_bid(self):
        if self.game.weitersagen == True:
            self.logger.info("Reizen beendet! Gewinner:"+str(self.game.highest_bidder))
            self.game.reizen_done = True
            self.game.declarer = self.game.highest_bidder
        else:
            self.game.out=1
            self.game.weitersagen = True
            self.game.reizen_sagenoderhoeren = 0
            self.game.sager = self.prev

