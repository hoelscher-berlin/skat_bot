from deck import Deck
from game import Game
from card import Card
from trick import Trick
from player import Player
import logging


TILES = 't'
HEARTS = 'h'
PIKES = 'p'
CLOVERS = 'c'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)



Spiel = Game("chat 1")
Spiel.trump = HEARTS
Spiel.start()

print(Spiel.deck.cards)

Alex = Player(Spiel, "Telegram-Alex")
Simon = Player(Spiel, "Telegram-Simon")
Luz = Player(Spiel, "Telegram-Luz")

Alex.draw_first_hand()
Alex.cards.sort()

Simon.draw_first_hand()
Luz.draw_first_hand()

print(Spiel.current_player)
print(Spiel.current_player.cards)
Spiel.current_player.play(Spiel.current_player.cards[0])
Spiel.current_player.play(Spiel.current_player.cards[0])
Spiel.current_player.play(Spiel.current_player.cards[0])

print(Spiel.last_trick_winner)
print(Spiel.last_trick_winner.won_tricks[-1].cards)