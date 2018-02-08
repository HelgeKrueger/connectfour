import numpy as np

from connectfour import ConnectFour
from play import playout

def test_playout_random_init():
    c = ConnectFour()

    average = np.mean([playout(c.clone()) for _ in range(1000)])

    assert np.abs(average - 0.1) < 0.05

def test_playout_different_initial():
    c = ConnectFour()
    c.place(0)
    c.place(3)
    c.place(0)
    c.place(4)

    average = np.mean([playout(c.clone()) for _ in range(1000)])

    assert np.abs(average - (-0.3)) < 0.05
