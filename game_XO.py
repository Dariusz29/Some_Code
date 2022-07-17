# create grid to game in O and X

from numpy import random

 # positions 

class Body():
    global pos, pos_board
    pos = {
        1: "left_up",
        2: "left_mid",
        3: "left_down",
        4: "center_up",
        5: "center",
        6: "center_down",
        7: "right_up",
        8: "right_mid",
        9: "right_down",
        }

    pos_board = {
        1:[], 
        2:[],
        3:[],
        4:[],
        5:[],
        6:[],
        7:[],
        8:[],
        9:[]
    } 

    def __init__(self,x):
        self.x = x

    def board(self,x):
        x = " "
        for i in range(3):
            pos_board = f'[{x}]' * 3
            print(self.pos)



class Check():
    def __init__(self):
        super().__init__(Body)
        

    def choice_pos(self):

        self.empty = bool(a for a in pos_board.values() if a != [])
        self.left_up = bool(a for a in pos_board.keys() if pos_board[1] != ["X"] or ["O"])
        self.left_mid = bool(a for a in pos_board.keys() if pos_board[2] != ["X"] or ["O"])
        self.left_down = bool(a for a in pos_board.keys() if pos_board[3] != ["X"] or ["O"])
        self.center_up = bool(a for a in pos_board.keys() if pos_board[4] != ["X"] or ["O"])
        self.center = bool(a for a in pos_board.keys() if pos_board[5] != ["X"] or ["O"])
        self.center_down = bool(a for a in pos_board.keys() if pos_board[6] != ["X"] or ["O"])
        self.right_up = bool(a for a in pos_board.keys() if pos_board[7] != ["X"] or ["O"])
        self.right_mid = bool(a for a in pos_board.keys() if pos_board[8] != ["X"] or ["O"])
        self.right_down = bool(a for a in pos_board.keys() if pos_board[9] != ["X"] or ["O"])

    def check_pos(self):
        if empty == True:
            print("")
        elif self.left_up == True:
            print("")
        elif self.left_mid == True:
            print("")
        elif self.left_down == True:
            print("")
        elif self.center_up == True:
            print("")
        elif self.center == True:
            print("")
        elif self.center_down == True:
             print("")
        elif self.right_up == True:
            print("")
        elif self.right_mid == True:
            print("")
        elif self.right_down == True:
            print("")

# Game 

class Game():

    def _init_(self,_pos,):
        self._pos = _pos
        
    def choice(self):
        list = ["X","O"]
        _pos_ = [1,2,3,4,5,6,7,8,9]

        pos = [empty,left_up,left_mid,left_down,center_up,center,center_down,right_up,right_mid,right_down]

        for i in range(9):
            ban = random.choice(list)
            _pos = random.choice(_pos_)
            if pos[0]:
                pos_board[_pos].append(ban)
                print(pos_board)
                _pos_.remove(_pos)

            elif pos[1] and _pos:
                pos_board[_pos].append(ban)
                print(pos_board)
                _pos_.remove(_pos)

            elif pos[2] and _pos:
                pos_board[_pos].append(ban)
                print(pos_board)
                _pos_.remove(_pos)

            elif pos[3] and _pos:
                pos_board[_pos].append(ban)
                print(pos_board)
                _pos_.remove(_pos)

            elif pos[4] and _pos:
                pos_board[_pos].append(ban)
                print(pos_board)
                _pos_.remove(_pos)

            elif pos[5] and _pos:
                pos_board[_pos].append(ban)
                print(pos_board)
                _pos_.remove(_pos)

            elif pos[6] and _pos:
                pos_board[_pos].append(ban)
                print(pos_board)
                _pos_.remove(_pos)

            elif pos[7] and _pos:
                pos_board[_pos].append(ban)
                print(pos_board)
                _pos_.remove(_pos)

            elif pos[8] and _pos:
                pos_board[_pos].append(ban)
                print(pos_board)
                _pos_.remove(_pos)

            elif pos[9] and _pos:
                pos_board[_pos].append(ban)
                print(pos_board)
                _pos_.remove(_pos)

                
            
           
