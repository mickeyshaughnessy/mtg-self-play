# This script runs an mtg game.

from objects import GameCard, GameSpell, GamePerm, Deck, Player, Game

if __name__ == "__main__":
    player1, player2 = Player(deck=Deck()), Player(deck=Deck())
    game = Game(player1, player2)
    
    while not game.winner:
        game.play()
