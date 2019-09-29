from card import Card

class Trick(object):
  def __init__(self):
    self.test = "mehmoh"
    self.cards = list()
    self.owner = None

  def __str__(self):
    return self.test

  def add_card(self, card):
    if len(self.cards) < 3:
      self.cards.append(card)

  def winner(self, trump):
    winnercard = self.cards[0]
    first_color = winnercard.color

    for card in self.cards:
        if card.color == first_color:
            winnercard = card if card.value > winnercard.value else winnercard

    trumps_checked = False

    for card in self.cards:
        if card.color == trump:
            if not trumps_checked:
                winnercard = card
                trumps_checked = True
            else:
                winnercard = card if card.value > winnercard.value else winnercard 
    
    return winnercard
