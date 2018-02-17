from multiprocessing import Process

from connectfour import ConnectFour
from tree_search_argent import TreeSearchAgent


def evaluate():
    c = ConnectFour()
    positive_player = TreeSearchAgent(1) # OneStepAgent(1,  number=100)
    negative_player = TreeSearchAgent(-1)

    while not c.game_over():
        if c.turn == 1:
            positive_player.move(c)
        else:
            negative_player.move(c)

        c.print()

    print("Winner {}".format(c.winner()))

def main():
    processes = []
    for _ in range(1):
        p = Process(target=evaluate)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

if __name__ == '__main__':
    main()
