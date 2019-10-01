#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Telegram bot to play UNO in group chats
# Copyright (c) 2016 Jannes Höke <uno@jhoeke.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


"""Defines helper functions to build the inline result list"""

from uuid import uuid4

from telegram import InlineQueryResultArticle, InputTextMessageContent, \
    InlineQueryResultCachedSticker as Sticker

import card as c
from utils import display_name

def add_no_game(results):
    """Add text result if user is not playing"""
    results.append(
        InlineQueryResultArticle(
            "nogame",
            title="You are not playing",
            input_message_content=
            InputTextMessageContent('Not playing right now. Use /new to '
                                      'start a game or /join to join the '
                                      'current game in this group')
        )
    )


def add_not_started(results):
    """Add text result if the game has not yet started"""
    results.append(
        InlineQueryResultArticle(
            "nogame",
            title="The game wasn't started yet",
            input_message_content=
            InputTextMessageContent('Start the game with /start')
        )
    )

def add_card(game, card, results, can_play):
    """Add an option that represents a card"""

    if can_play:
        results.append(
            Sticker(str(card), sticker_file_id=c.STICKERS[str(card)])
        )
    else:
        results.append(
            Sticker(str(uuid4()), sticker_file_id=c.STICKERS[str(card)],
                    input_message_content=game_info(game))
        )

def player_list(game):
    """Generate list of player strings"""
    return ["{name} ({number} card)".format(name=player.user.first_name, number=len(player.cards))
            for player in game.players]

def game_info(game):
    players = player_list(game)
    return InputTextMessageContent(
        "Current player: {name}"
        .format(name=display_name(game.current_player.user)) +
        "\n" +
        "Last card: {card}".format(card=repr(game.last_card)) +
        "\n" +
        "Players: {player_list}".format(player_list=" -> ".join(players))
    )