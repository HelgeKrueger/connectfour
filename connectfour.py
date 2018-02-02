import numpy as np


class ConnectFour:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = np.zeros((self.rows, self.columns))

    def print(self):
        print(self.board)

        

def main():
    c = ConnectFour()
    c.print()


if __name__ == '__main__':
    main()