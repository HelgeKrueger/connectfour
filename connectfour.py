import random

import numpy as np
from scipy import signal

class ConnectFour:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = np.zeros((self.rows, self.columns))
        self.turn = 1

        self.win_kernels = [
            np.ones((1, 4)),
            np.ones((4, 1)),
            np.diag(np.ones(4)),
            np.fliplr(np.diag(np.ones(4)))
        ]

    def print(self):
        print(self.board)

    def place(self, column):
        col = self.board[:, column]
        max = int(np.sum(np.abs(col)))
        self.board[self.rows - 1 - max, column] = self.turn

        self.turn = - self.turn

    def possible_moves(self):
        a = np.sum(np.abs(self.board), axis=0)

        return [i for i in range(self.columns) if a[i]< self.rows]

    def game_over(self):
        if self.winner():
            return True
        return np.sum(np.abs(self.board)) == self.columns * self.rows

    def winner(self):
        convolution_result = [signal.convolve2d(self.board, k, 'same') for k in self.win_kernels]

        if np.max(convolution_result) == 4:
            return 1
        if np.min(convolution_result) == -4:
            return -1

        return

def main():
    c = ConnectFour()

    while not c.game_over():
        move = random.choice(c.possible_moves())
        c.place(move)
        c.print()

    print("Winner {}".format(c.winner()))


if __name__ == '__main__':
    main()