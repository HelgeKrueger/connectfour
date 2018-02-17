import numpy as np

from play import playout


class Leaf:
    def __init__(self, connect_four, player):
        self.connect_four = connect_four
        self.possible_moves = connect_four.possible_moves()
        self.number = len(self.possible_moves)

        self.player = player

        self.visits = np.ones(self.number)
        self.scores = [self.random_explore(connect_four.clone().place(self.possible_moves[i])) for i in range(self.number)]
        self.leafs = [None for _ in range(self.number)]


    def random_explore(self, connect_four):
        return self.player * playout(connect_four)

    def best_move(self):
        scores = [float(self.scores[i])/self.visits[i] for i in range(self.number)]

        return self.possible_moves[np.argmax(scores)]

    def explore_scores(self, time):
        return [-self.connect_four.turn * float(self.scores[i]) / self.visits[i] + np.math.sqrt(4 * np.math.log(np.sum(self.visits))/self.visits[i]) for i in range(self.number)]

    def explore_step(self, time):
        index = int(np.argmax(self.explore_scores(time)))

        if self.leafs[index] is None:
            next_board = self.connect_four.clone().place(self.possible_moves[index])
            if next_board.game_over():
                new_visits = 1
                new_scores = self.player * (next_board.winner() or 0)
            else:
                new_leaf = Leaf(next_board, self.player)
                self.leafs[index] = new_leaf
                new_visits = np.sum(new_leaf.visits)
                new_scores = np.sum(new_leaf.scores)
        else:
            new_visits, new_scores = self.leafs[index].explore_step(time)

        self.visits[index] = self.visits[index] + new_visits
        self.scores[index] = self.scores[index] + new_scores
        return new_visits, new_scores

    def explore(self):
        for t in range(100):
            self.explore_step(t+1)

    def get_leaf_for_move(self, move):
        try:
            index = self.possible_moves.index(move)
            return self.leafs[index]
        except:
            return


class TreeSearchAgent:
    def __init__(self, player):
        self.player = player
        self.history = []
        self.leaf = None

    def move(self, connect_four):
        # move = random.choice(connect_four.possible_moves())
        if self.leaf:
            new_moves = connect_four.history[len(self.history):]
            for move in new_moves:
                self.leaf = self.leaf.get_leaf_for_move(move)
                if not self.leaf:
                    self.leaf = Leaf(connect_four, self.player)
                    break
        else:
            self.leaf = Leaf(connect_four, self.player)

        self.leaf.explore()

        connect_four.place(self.leaf.best_move())