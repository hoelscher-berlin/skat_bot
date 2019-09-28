#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
from datetime import datetime

import card as c


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

    def __repr__(self):
        return repr(self.user)

    def __str__(self):
        return str(self.user)

    @property
    def next(self):
        return self._next if not self.game.reversed else self._prev

    @next.setter
    def next(self, player):
        if not self.game.reversed:
            self._next = player
        else:
            self._prev = player

    @property
    def prev(self):
        return self._prev if not self.game.reversed else self._next

    @prev.setter
    def prev(self, player):
        if not self.game.reversed:
            self._prev = player
        else:
            self._next = player

    def play(self, card):
        """Plays a card and removes it from hand"""
        self.cards.remove(card)
        self.game.play_card(card)

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
        #last = self.game.last_card
        self.logger.debug("Checking card " + str(card))

        return is_playable