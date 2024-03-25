# This script sets up a two-player bot-bot MtG match, then executes it through self-play
import random

ALL_DECKS = []
with open('decklists.json') as f:
    for line in f:
        ALL_DECKS.append(line.rstrip())


def new_game(n_players=2):
    decks = []
    for i in range(n_players):
        decks.append(random.choice(ALL_DECKS))
    

if __name__ == "__main__":
    game = new_game(n_players=2)
