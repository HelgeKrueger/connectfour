import random

import numpy as np

from connectfour import ConnectFour


def playout(connect_four):
    while not connect_four.game_over():
        move = random.choice(connect_four.possible_moves())
        connect_four.place(move)

    return connect_four.winner() or 0

def average_playout(connect_four, number=100):
    return np.mean([playout(connect_four.clone()) for _ in range(number)])

def determine_winner(positive_player, negative_player):
    connect_four = ConnectFour()

    while not connect_four.game_over():
        if connect_four.turn == 1:
            positive_player.move(connect_four)
        else:
            negative_player.move(connect_four)

    return connect_four.winner() or 0

def determine_winner_average(positive_player, negative_player, number=100):
    return np.mean([determine_winner(positive_player, negative_player) for _ in range(number)])