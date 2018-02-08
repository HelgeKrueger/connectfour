import random


def playout(connect_four):
    while not connect_four.game_over():
        move = random.choice(connect_four.possible_moves())
        connect_four.place(move)

    return connect_four.winner() or 0