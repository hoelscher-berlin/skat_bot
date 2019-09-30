from deck import Deck
from game import Game
from card import Card
from trick import Trick
from player import Player
import logging


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)



Spiel = Game("chat 1")

Alex = Player(Spiel, "Telegram-Alex")
Simon = Player(Spiel, "Telegram-Simon")
Luz = Player(Spiel, "Telegram-Luz")

Spiel.trump = 'a'
Spiel.declarer = Alex
Spiel.start()

print(Spiel.deck.cards)

Alex.draw_first_hand()
Alex.cards.sort()
Simon.draw_first_hand()
Luz.draw_first_hand()

print(str(Spiel.current_player)+ " starts")
print(Spiel.current_player.cards)

for _ in range(10):
    Spiel.current_player.play_random()
    Spiel.current_player.play_random()
    Spiel.current_player.play_random()

    print(Spiel.last_trick_winner)
    print(Spiel.last_trick_winner.won_tricks[-1].cards)
