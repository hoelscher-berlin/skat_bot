#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Colors
TILES = 't'
HEARTS = 'h'
PIKES = 'p'
CLOVERS = 'c'

COLORS = (TILES, HEARTS, PIKES, CLOVERS)

COLOR_ICONS = {
    TILES: '♦️',
    HEARTS: '♥',
    PIKES: '♠',
    CLOVERS: '♣'
}

# Values
SEVEN = '7'
EIGHT = '8'
NINE = '9'
TEN = '10'
ACE = '11'
KING = '4'
QUEEN = '3'
JACK = '2'


VALUES = (SEVEN, EIGHT, NINE, TEN, ACE, KING, QUEEN, JACK)
#WILD_VALUES = (ONE, TWO, THREE, FOUR, FIVE, DRAW_TWO, REVERSE, SKIP)

STICKERS = {
    'b_0': 'BQADBAAD2QEAAl9XmQAB--inQsYcLTsC',
    'b_1': 'BQADBAAD2wEAAl9XmQABBzh4U-rFicEC',
    'b_2': 'BQADBAAD3QEAAl9XmQABo3l6TT0MzKwC',
    'b_3': 'BQADBAAD3wEAAl9XmQAB2y-3TSapRtIC',
    'b_4': 'BQADBAAD4QEAAl9XmQABT6nhOuolqKYC',
    'b_5': 'BQADBAAD4wEAAl9XmQABwRfmekGnpn0C',
    'b_6': 'BQADBAAD5QEAAl9XmQABQITgUsEsqxsC',
    'b_7': 'BQADBAAD5wEAAl9XmQABVhPF6EcfWjEC',
    'b_8': 'BQADBAAD6QEAAl9XmQABP6baig0pIvYC',
    'b_9': 'BQADBAAD6wEAAl9XmQAB0CQdsQs_pXIC',
    'b_draw': 'BQADBAAD7QEAAl9XmQAB00Wii7R3gDUC',
    'b_skip': 'BQADBAAD8QEAAl9XmQAB_RJHYKqlc-wC',
    'b_reverse': 'BQADBAAD7wEAAl9XmQABo7D0B9NUPmYC',
    'g_0': 'BQADBAAD9wEAAl9XmQABb8CaxxsQ-Y8C',
    'g_1': 'BQADBAAD-QEAAl9XmQAB9B6ti_j6UB0C',
    'g_2': 'BQADBAAD-wEAAl9XmQABYpLjOzbRz8EC',
    'g_3': 'BQADBAAD_QEAAl9XmQABKvc2ZCiY-D8C',
    'g_4': 'BQADBAAD_wEAAl9XmQABJB52wzPdHssC',
    'g_5': 'BQADBAADAQIAAl9XmQABp_Ep1I4GA2cC',
    'g_6': 'BQADBAADAwIAAl9XmQABaaMxxa4MihwC',
    'g_7': 'BQADBAADBQIAAl9XmQABv5Q264Crz8gC',
    'g_8': 'BQADBAADBwIAAl9XmQABjMH-X9UHh8sC',
    'g_9': 'BQADBAADCQIAAl9XmQAB26fZ2fW7vM0C',
    'g_draw': 'BQADBAADCwIAAl9XmQAB64jIZrgXrQUC',
    'g_skip': 'BQADBAADDwIAAl9XmQAB17yhhnh46VQC',
    'g_reverse': 'BQADBAADDQIAAl9XmQAB_xcaab0DkegC',
    'r_0': 'BQADBAADEQIAAl9XmQABiUfr1hz-zT8C',
    'r_1': 'BQADBAADEwIAAl9XmQAB5bWfwJGs6Q0C',
    'r_2': 'BQADBAADFQIAAl9XmQABHR4mg9Ifjw0C',
    'r_3': 'BQADBAADFwIAAl9XmQABYBx5O_PG2QIC',
    'r_4': 'BQADBAADGQIAAl9XmQABTQpGrlvet3cC',
    'r_5': 'BQADBAADGwIAAl9XmQABbdLt4gdntBQC',
    'r_6': 'BQADBAADHQIAAl9XmQABqEI274p3lSoC',
    'r_7': 'BQADBAADHwIAAl9XmQABCw8u67Q4EK4C',
    'r_8': 'BQADBAADIQIAAl9XmQAB8iDJmLxp8ogC',
    'r_9': 'BQADBAADIwIAAl9XmQAB_HCAww1kNGYC',
    'r_draw': 'BQADBAADJQIAAl9XmQABuz0OZ4l3k6MC',
    'r_skip': 'BQADBAADKQIAAl9XmQAC2AL5Ok_ULwI',
    'r_reverse': 'BQADBAADJwIAAl9XmQABu2tIeQTpDvUC',
    'y_0': 'BQADBAADKwIAAl9XmQAB_nWoNKe8DOQC',
    'y_1': 'BQADBAADLQIAAl9XmQABVprAGUDKgOQC',
    'y_2': 'BQADBAADLwIAAl9XmQABqyT4_YTm54EC',
    'y_3': 'BQADBAADMQIAAl9XmQABGC-Xxg_N6fIC',
    'y_4': 'BQADBAADMwIAAl9XmQABbc-ZGL8kApAC',
    'y_5': 'BQADBAADNQIAAl9XmQAB67QJZIF6XAcC',
    'y_6': 'BQADBAADNwIAAl9XmQABJg_7XXoITsoC',
    'y_7': 'BQADBAADOQIAAl9XmQABVrd7OcS2k34C',
    'y_8': 'BQADBAADOwIAAl9XmQABRpJSahBWk3EC',
    'y_9': 'BQADBAADPQIAAl9XmQAB9MwJWKLJogYC',
    'y_draw': 'BQADBAADPwIAAl9XmQABaPYK8oYg84cC',
    'y_skip': 'BQADBAADQwIAAl9XmQABO_AZKtxY6IMC',
    'y_reverse': 'BQADBAADQQIAAl9XmQABZdQFahGG6UQC',
    'draw_four': 'BQADBAAD9QEAAl9XmQABVlkSNfhn76cC',
    'colorchooser': 'BQADBAAD8wEAAl9XmQABl9rUOPqx4E4C',
    'option_draw': 'BQADBAAD-AIAAl9XmQABxEjEcFM-VHIC',
    'option_pass': 'BQADBAAD-gIAAl9XmQABcEkAAbaZ4SicAg',
    'option_bluff': 'BQADBAADygIAAl9XmQABJoLfB9ntI2UC',
    'option_info': 'BQADBAADxAIAAl9XmQABC5v3Z77VLfEC'
}

class Card(object):
    """This class represents a Skat card"""

    def __init__(self, color, value, owner):
        self.color = color
        self.value = value
        self.owner = owner

    def __str__(self):
        return '%s_%s' % (self.color, self.value)

    def __repr__(self):
        return '%s%s' % (COLOR_ICONS[self.color], self.value.capitalize())

    def __eq__(self, other):
        """Needed for sorting the cards"""
        return str(self) == str(other)

    def __lt__(self, other):
        """Needed for sorting the cards"""
        return str(self) < str(other)


def from_str(string):
    """Decodes a Card object from a string"""
    color, value = string.split('_')
    return Card(color, value, None)
    
