import numpy as np

from play import average_playout


class OneStepAgent:
    def __init__(self, player, number=100):
        self.player = player
        self.number = number

    def move(self, connect_four):
        possible_moves = connect_four.possible_moves()
        length = len(possible_moves)

        initial_games = [connect_four.clone().place(possible_moves[j]) for j in range(length)]

        scores = [average_playout(game, number=self.number) * self.player for game in initial_games]

        connect_four.place(possible_moves[int(np.argmax(scores))])