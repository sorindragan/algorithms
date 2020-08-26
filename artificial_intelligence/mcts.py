import numpy as np
import random
import copy

X = 1
O = -1
UCB_VALUE = 2

class State:
    def __init__(self, board=np.zeros((3,3)), value = 0, symbol = X):
        self.symbol = symbol
        if symbol == X:
            self.opponent_symbol = O
        else:
            self.opponent_symbol = O
        self.board = board
        self.value = value
    
    def is_win_for_symbol(self, symbol):
        win_value = 3 * symbol
        if sum(self.board.diagonal()) == win_value or sum(np.diag(np.fliplr(self.board))) == win_value:
            return True
        
        if any([sum(row) == win_value for row in self.board]) or any([sum(col) == win_value for col in self.board.T]):
            return True
        return False

    def is_terminal(self):
        # WIN
        if self.is_win_for_symbol(self.symbol):
            self.value = 1
            return True
        
        # LOSE
        if self.is_win_for_symbol(self.opponent_symbol):
            self.value = -1
            return True

        # DRAW
        if self.board.all():
            return True
        return False
    
    def __str__(self):
     return f"board state: \n {self.board}; "


class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.reward = 0.0
        self.visits = 0
        self.parent = parent
        self.children = []
    
    def update_reward(self, reward):
        self.reward += reward
        self.visits += 1
    
    def create_child(self, child_state):
        self.children.append(child_state, self)
    
    def fully_expanded(self):
        if np.count_nonzero(self.state.board) == (len(self.state.board) * len(self.state.board.T)):
            return True
        return False
    
    def __str__(self):
        return f"{self.state}; \n reward: {self.reward}; \n visits: {self.visits};"


def calculate_UCB1(node):
    if node.visits == 0:
        return np.Inf
    return (node.reward + UCB_VALUE * np.sqrt(np.log(node.parent.visits) / node.visits))


def backpropagation(node, value):
    curr_node = node
    while curr_node.parent:
        curr_node.update_reward(value)
        curr_node = curr_node.parent
    curr_node.update_reward(value)


def rollout(node):
    curr_state = copy.deepcopy(node.state)
    value = 0
    # random play
    while (not curr_state.is_terminal()):
        # self
        i, j = np.where(curr_state.board == 0) 
        available_moves = list(zip(i, j))
        move_i, move_j = random.choice(available_moves)
        curr_state.board[move_i][move_j] = curr_state.symbol
        if curr_state.is_terminal():
            break

        # opponent
        i, j = np.where(curr_state.board == 0) 
        available_moves = list(zip(i, j))
        move_i, move_j = random.choice(available_moves)
        curr_state.board[move_i][move_j] = curr_state.opponent_symbol

    value = curr_state.value
    backpropagation(node, value)

def expansion(node):
    if node.fully_expanded():
        return
    state = copy.deepcopy(node.state)
    i, j = np.where(state.board == 0) 
    available_actions = list(zip(i, j))
    # create children nodes for all available actions
    for move in available_actions:
        a_i, a_j = move
        new_board = copy.deepcopy(state.board)
        new_board[a_i][a_j] = node.state.symbol
        new_state = State(board = new_board, symbol=state.symbol)
        new_node = Node(new_state, node)
        node.children.append(new_node)

def traverse(node):
    # reach a leaf node
    while node.children:
        ucb_values = list(map(calculate_UCB1, node.children)) 
        node = node.children[ucb_values.index(max(ucb_values))]
    
    if node.visits == 0 and node.parent:
        rollout(node)
    else:
        expansion(node)

def get_best_action(node):
    ucb_values = list(map(calculate_UCB1, node.children)) 
    node = node.children[ucb_values.index(max(ucb_values))]
    return node.state
    

def simulate(start_board=np.zeros((3,3)), player=X, iterations=10):
    tree = Node(State(board=start_board, symbol=player))
    # simulation
    for _ in range(iterations):
        traverse(tree)

    # print([f"Node: {n.state.board[0]}, {n.reward}, {n.visits}, {calculate_UCB1(n)}" for n in tree.children])
    return get_best_action(tree)

def outcome(state):
    if state.value == 1:
        return state.symbol
    if state.value == -1:
        return state.opponent_symbol
    return 0


def play_game():
    verbose = False

    state = simulate(iterations=20)
    if verbose:
        print(state.board)
        print("-" * 100)
    new_board = copy.deepcopy(state.board)

    while True:
        state = simulate(start_board=new_board, player=O, iterations=2)
        if verbose:
            print(state.board)
            print("-" * 100)
        if state.is_terminal():
            print(state.board)
            print("-" * 100)

            return outcome(state)
        
        new_board = copy.deepcopy(state.board)
        state = simulate(start_board=new_board, iterations=20)
        if verbose:
            print(state.board)
            print("-" * 100)

        if state.is_terminal():
            print(state.board)
            print("-" * 100)

            return outcome(state)
        new_board = copy.deepcopy(state.board)
        

def play_game_from_board():
    board = np.array([[1, 1, 0], [0, -1, 0], [-1, 0, 0]])
    print(board)
    print(simulate(start_board=board, iterations=20))


def play_with_human():
    state = simulate(iterations=20)
    print(state.board)
    new_board = copy.deepcopy(state.board)
    while True:
        sec = input("Insert move \n")
        m = sec.split()
        x, y = int(m[0]), int(m[1])
        new_board[x][y] = O
        print(new_board)
        state = simulate(start_board=new_board, iterations=20)
        print(state.board)
        new_board = copy.deepcopy(state.board)



def main():
    # results = {X:0, O:0, 0:0}
    # for _ in range(10):
    #     outcome = play_game()
    #     results[outcome] += 1
    
    # print(results)

    # play_game_from_board()

    play_with_human()



if __name__ == "__main__":
    main()
    
    

    


