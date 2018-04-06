from connectfour import ConnectFour
from agents.human_agent import HumanAgent
from agents.tree_search_argent import TreeSearchAgent

# HumanAgent -> Mensch
# OneStepAgent -> Monte Carlo Function
# TreeSearchAgent -> MCTS

def evaluate(positive_player=TreeSearchAgent(1), negative_player=TreeSearchAgent(-1)):
    c = ConnectFour()

    while not c.game_over():
        if c.turn == 1:
            positive_player.move(c)
        else:
            negative_player.move(c)

        c.print()

    print("Winner {}".format(c.winner()))

if __name__ == '__main__':
    evaluate(positive_player=HumanAgent())
