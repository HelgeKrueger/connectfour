import numpy as np

from connectfour import ConnectFour
from play import playout, average_playout


def test_playout_random_init():
    c = ConnectFour()

    assert np.abs(average_playout(c) - 0.1) < 0.05

def test_playout_different_initial():
    c = ConnectFour()
    c.place(0)
    c.place(3)
    c.place(0)
    c.place(4)

    assert np.abs(average_playout(c) - (-0.3)) < 0.05
