# This script runs an mtg game.

class MTGCard():
    def __init__(self, oid=None):
        self.oid=oid
class GameCard():
    # An mtg card in play, in hand/library/graveyard,...

class GameSpell():
    # An mtg card being cast

class GamePerm():
    # A single permanent in play.

class Deck():
    # A collection of MTGCards
    def __init__(self, cards=[1,1,1,1,1,1,1,1,0,0]):
        pass

class Player():
    def __init__(self, deck=[1,1,1,1,1,1,1,1,0,0], life=40):# 8 lightning bolts and 2 mountains.
        self.deck = deck
        self.life_total = life

class Game():
    pass

if __name__ == "__main__":
    player1, player2 = Player(), Player()
    game = Game(player1, player2)
    
    while not game.winner:
        game.play()
