from card import Card

class Trick(object):
  def __init__(self):
    self.test = "mehmoh"
    self.cards = list()

  def __str__(self):
    return self.test

  def add_card(self, card):
    if len(self.cards) < 3:
      self.cards.append(card)