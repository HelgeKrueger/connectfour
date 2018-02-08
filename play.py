import random

import numpy as np


def playout(connect_four):
    while not connect_four.game_over():
        move = random.choice(connect_four.possible_moves())
        connect_four.place(move)

    return connect_four.winner() or 0

def average_playout(connect_four, number=100):
    return np.mean([playout(connect_four.clone()) for _ in range(number)])