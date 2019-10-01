#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Colors
TILES = 'a'
HEARTS = 'b'
PIKES = 'c'
CLOVERS = 'd'

COLORS = (TILES, HEARTS, PIKES, CLOVERS)

COLOR_ICONS = {
    TILES: '♦️',
    HEARTS: '♥',
    PIKES: '♠',
    CLOVERS: '♣'
}

# Values
SEVEN = '1'
EIGHT = '2'
NINE = '3'
KING = '5'
QUEEN = '4'
TEN = '6'
ACE = '7'
JACK = '8'

REPRS = {
    '1':'7',
    '2':'8',
    '3':'9',
    '4':'Q',
    '5':'K',
    '6':'10',
    '7':'A',
    '8':'J'
}

POINTS = {
    SEVEN: 0,
    EIGHT: 0,
    NINE: 0,
    TEN: 10,
    ACE: 11,
    JACK: 2,
    QUEEN: 3,
    KING: 4
}

VALUES = (SEVEN, EIGHT, NINE, TEN, ACE, KING, QUEEN, JACK)

STICKERS = {
    'a_1': 'CAADAgADBAADLEAtGYJscWu37VmCFgQ',
    'a_2': 'CAADAgADCAADLEAtGRNA4CaoFBoNFgQ',
    'a_3': 'CAADAgADDAADLEAtGbWVdpQVR5PeFgQ',
    'a_4': 'CAADAgADHwADLEAtGXrUCJYYNeiHFgQ',
    'a_5': 'CAADAgADGwADLEAtGWf_miRAehx9FgQ',
    'a_6': 'CAADAgADEAADLEAtGUIX5Eba9iUZFgQ',
    'a_7': 'CAADAgADEwADLEAtGUocgEF_ueDKFgQ',
    'a_8': 'CAADAgADFwADLEAtGUi4mn7WpnCEFgQ',
    'b_1': 'CAADAgADBQADLEAtGfO-y1Vs7tSsFgQ',
    'b_2': 'CAADAgADCQADLEAtGdAHxHAcAAHagBYE',
    'b_3': 'CAADAgADDQADLEAtGVSTNq166IEIFgQ',
    'b_4': 'CAADAgADIAADLEAtGS5NcqQz9AcsFgQ',
    'b_5': 'CAADAgADHAADLEAtGWJpp1oVo8ADFgQ',
    'b_6': 'CAADAgADEQADLEAtGVm2yvp7TqKDFgQ',
    'b_7': 'CAADAgADFAADLEAtGUwqKogPC8_bFgQ',
    'b_8': 'CAADAgADGAADLEAtGWDw0cg9agbxFgQ',
    'c_1': 'CAADAgADBgADLEAtGWS6Uu70YV2CFgQ',
    'c_2': 'CAADAgADCgADLEAtGUs650LJv0w6FgQ',
    'c_3': 'CAADAgADDgADLEAtGZKu0wGpTt0xFgQ',
    'c_4': 'CAADAgADIQADLEAtGdc7m1Kyg7d5FgQ',
    'c_5': 'CAADAgADHQADLEAtGQKVtLwkHeVRFgQ',
    'c_6': 'CAADAgADIgADLEAtGYEvw3G4CaQUFgQ',
    'c_7': 'CAADAgADFQADLEAtGU8Gs9KqZMtSFgQ',
    'c_8': 'CAADAgADGQADLEAtGW_ovitQVHnTFgQ',
    'd_1': 'CAADAgADAwADLEAtGf_-W7vPAz_bFgQ',
    'd_2': 'CAADAgADBwADLEAtGcMghi5RJSSJFgQ',
    'd_3': 'CAADAgADCwADLEAtGR3P1fKiCTQkFgQ',
    'd_4': 'CAADAgADHgADLEAtGRzY-zJOyNf_FgQ',
    'd_5': 'CAADAgADGgADLEAtGWuj3UKSDjmkFgQ',
    'd_6': 'CAADAgADDwADLEAtGckAAX05gjxvxhYE',
    'd_7': 'CAADAgADEgADLEAtGS0jZhCokfkZFgQ',
    'd_8': 'CAADAgADFgADLEAtGfsVe3bPTw8TFgQ',
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
        return '%s%s' % (COLOR_ICONS[self.color], REPRS[self.value])

    def __eq__(self, other):
        """Needed for sorting the cards"""
        return str(self) == str(other)

    def __lt__(self, other):
        """Needed for sorting the cards"""
        return str(self) < str(other)

    def points(self):
        return POINTS[self.value]


def from_str(string):
    """Decodes a Card object from a string"""
    color, value = string.split('_')
    return Card(color, value, None)
    