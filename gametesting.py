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

Alex.draw_first_hand()
Simon.draw_first_hand()
Luz.draw_first_hand()

def showReizenStand():
    print("Highest Bid: "+str(Spiel.highest_bid))
    print("Highest Bidder: "+str(Spiel.highest_bidder))
    if Spiel.reizen_sagenoderhoeren == 0:
        if Spiel.weitersagen:
            print("WEITERsager ist dran: "+str(Spiel.sager))
        else:
            print("Sager ist dran: "+str(Spiel.sager))
    else:
        print("Hörer ist dran: "+str(Spiel.hoerer))

    print("")


#Spiel.sager.bid()
#showReizenStand()
#Spiel.hoerer.deny_bid()
#showReizenStand()
#Spiel.sager.bid()
#showReizenStand()
#Spiel.hoerer.deny_bid()

Spiel.sager.dont_bid()
showReizenStand()
Spiel.sager.dont_bid()
showReizenStand()


#print(str(Spiel.current_player)+ " starts")




#for _ in range(10):
#    Spiel.current_player.play_random()
#    Spiel.current_player.play_random()
#    Spiel.current_player.play_random()

#    print(Spiel.last_trick_winner)
#    print(Spiel.last_trick_winner.won_tricks[-1].cards)
