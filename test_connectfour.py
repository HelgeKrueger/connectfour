import numpy as np

from connectfour import ConnectFour


def test_place():
    c = ConnectFour()
    c.place(0)
    c.place(0)

    c.place(1)
    c.place(2)

    assert c.board[:, 0].tolist() == [0, 0, 0, 0, -1, 1]
    assert c.board[:, 1].tolist() == [0, 0, 0, 0, 0, 1]
    assert c.board[:, 2].tolist() == [0, 0, 0, 0, 0, -1]

def test_possible_moves():
    c = ConnectFour()

    assert c.possible_moves() == [0, 1, 2, 3, 4, 5, 6]

    for _ in range(6):
        c.place(0)

    assert c.possible_moves() == [1, 2, 3, 4, 5, 6]

def test_winner():
    c = ConnectFour()

    assert not c.game_over()

    c.board[0, 0:4] = np.ones((1, 4))

    assert c.game_over()
    assert c.winner() == 1