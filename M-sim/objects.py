import random

class GameCard():
    # An mtg card in play, in hand/library/graveyard,...
    def __init__(self, name="", _type="", text="", cost="", stats=""):
        self.name = name or "default card name"
        self._type = _type or "default type"
        self.text = text or "default text"
        self.cost = cost or "default cost"
        self.stats = stats or "default stats"
        self.triggers = self.init_triggers

    def init_triggers(self):
        pass
    

class GameSpell():
    # An mtg card being cast
    def __init__(self, card=""):
        self.card = card

class GameToken():
    def __init__(self, name=""):
        self.name = name or "default_token"

class GamePerm():
    # A single permanent in play.
    def __init__(self, card=None, name=""):
        if not card:
            self.card = GameToken(name)
        else:
            self.card = card
        self.triggers = self.card.init_triggers() 


class Deck():
    # An ordered collection of GameCards
    def __init__(self, cards=[]):
        pass

    def _shuffle(self):
        random.shuffle(self.cards)

class Player():
    def __init__(self, deck=[1,1,1,1,1,1,1,1,0,0], life=40):# 8 lightning bolts and 2 mountains.
        self.deck = deck
        self.life_total = life

class Game():
    pass
