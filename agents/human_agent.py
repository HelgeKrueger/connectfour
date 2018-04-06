from agents.agent import Agent


class HumanAgent(Agent):
    def move(self, connect_four):
        move = None
        possible_moves = connect_four.possible_moves()
        while move not in possible_moves:
            try:
                move = int(input("Possible moves: {}    ".format(connect_four.possible_moves())))
            except:
                move = None
        connect_four.place(move)
