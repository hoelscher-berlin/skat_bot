#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import shuffle
import logging

import card as c
from card import Card


class Deck(object):
    """ This class represents a deck of cards """
    """ Only needed at the beginning of the game """

    def __init__(self):
        self.cards = list()
        self.logger = logging.getLogger(__name__)

        self.logger.debug(self.cards)

    def shuffle(self):
        """Shuffles the deck"""
        self.logger.debug("Shuffling Deck")
        shuffle(self.cards)

    def draw(self):
        """Draws a card from this deck"""
        card = self.cards.pop()
        self.logger.debug("Drawing card " + str(card))
        return card

    def _fill_classic_(self):
        # Fill deck with the classic card set
        self.cards.clear()
        for color in c.COLORS:
            for value in c.VALUES:
                self.cards.append(Card(color, value, None))
        
        self.shuffle()
