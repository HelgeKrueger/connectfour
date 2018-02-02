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

    def clone(self):
        c = ConnectFour()
        c.board = self.board.copy()
        return c

    def print(self):
        print(self.board)

    def place(self, column):
        col = self.board[:, column]
        max = int(np.sum(np.abs(col)))
        self.board[self.rows - 1 - max, column] = self.turn

        self.turn = - self.turn

        return self

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

class HumanAgent:
    def move(self, connect_four):
        move = int(input("Possible moves: {}    ".format(connect_four.possible_moves())))
        connect_four.place(move)


class Leaf:
    def __init__(self, connect_four):
        self.connect_four = connect_four
        self.possible_moves = connect_four.possible_moves()
        self.number = len(self.possible_moves)

        if self.connect_four.game_over():
            print('xxx')
            return

        self.visits = np.ones(self.number)
        self.scores = [self.random_explore(connect_four.clone().place(self.possible_moves[i])) for i in range(self.number)]
        self.leafs = [None for _ in range(self.number)]

    def random_explore(self, connect_four):
        while not connect_four.game_over():
            move = random.choice(connect_four.possible_moves())
            connect_four.place(move)
        return connect_four.winner() or 0

    def best_move(self):
        scores = [float(self.scores[i])/self.visits[i] for i in range(self.number)]

        return self.possible_moves[np.argmax(scores)]

    def explore_scores(self, time):
        return [float(self.scores[i]) / self.visits[i] + np.math.sqrt(2 * np.math.log(time)/self.visits[i]) for i in range(self.number)]

    def explore_step(self, time):
        index = int(np.argmax(self.explore_scores(time)))

        if self.leafs[index] is None:
            next_board = self.connect_four.clone().place(self.possible_moves[index])
            if next_board.game_over():
                new_visits = 1
                new_scores = next_board.winner()
            else:
                new_leaf = Leaf(next_board)
                self.leafs[index] = new_leaf
                new_visits = np.sum(new_leaf.visits)
                new_scores = np.sum(new_leaf.scores)
        else:
            new_visits, new_scores = self.leafs[index].explore_step(time)

        self.visits[index] = self.visits[index] + new_visits
        self.scores[index] = self.scores[index] + new_scores
        return new_visits, new_scores

    def explore(self):
        for t in range(1000):
            self.explore_step(t+1)


class TreeSearhAgent:
    def __init__(self):
        self.tree = []

    def move(self, connect_four):
        # move = random.choice(connect_four.possible_moves())
        l = Leaf(connect_four)
        l.explore()

        connect_four.place(l.best_move())


def main():
    c = ConnectFour()
    human = HumanAgent()
    tree_search = TreeSearhAgent()

    while not c.game_over():
        print('-' * 70)
        c.print()

        if c.turn == -1:
            human.move(c)
        else:
            tree_search.move(c)

    c.print()
    print("Winner {}".format(c.winner()))


if __name__ == '__main__':
    main()