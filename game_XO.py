# create grid to game in O and X
from turtle import left
from numpy import random

class Body():
    def __init__(self):
        pass

    def board():
        for i in range(1,3):
            _break = 4 * " "
            _break_ = 2 * " "
    
            for j in range(1,2):
            
                print(_break + "|" + _break + "|" + _break)
                print(" ---"+ _break_ + "---" + _break_ + "---")

                if i == 2:
                    print(_break + "|" + _break + "|" + _break)

x = " "
for i in range(3):
    pos = f'[{x}]' * 3
    print(pos)



#  # positions 

# pos = {
#     1: "left_up",
#     2: "left_mid",
#     3: "left_down",
#     4: "center_up",
#     5: "center",
#     6: "center_down",
#     7: "right_up",
#     8: "right_mid",
#     9: "right_down",
# }

# pos_board = {
#     1:[], 
#     2:[],
#     3:[],
#     4:[],
#     5:[],
#     6:[],
#     7:[],
#     8:[],
#     9:[]
# } 


# class Check():
#     def __init__(self):
#         pass

#     def choice_pos(self):

#         self.empty = bool(a for a in pos_board.values() if a != [])
#         self.left_up = bool(a for a in pos_board.keys() if pos_board[1] != ["X"] or ["O"])
#         self.left_mid = bool(a for a in pos_board.keys() if pos_board[2] != ["X"] or ["O"])
#         self.left_down = bool(a for a in pos_board.keys() if pos_board[3] != ["X"] or ["O"])
#         self.center_up = bool(a for a in pos_board.keys() if pos_board[4] != ["X"] or ["O"])
#         self.center = bool(a for a in pos_board.keys() if pos_board[5] != ["X"] or ["O"])
#         self.center_down = bool(a for a in pos_board.keys() if pos_board[6] != ["X"] or ["O"])
#         self.right_up = bool(a for a in pos_board.keys() if pos_board[7] != ["X"] or ["O"])
#         self.right_mid = bool(a for a in pos_board.keys() if pos_board[8] != ["X"] or ["O"])
#         self.right_down = bool(a for a in pos_board.keys() if pos_board[9] != ["X"] or ["O"])

#     def check_pos(self):
#         if self.empty == True:
#             print("")
#         elif self.left_up == True:
#             print("")
#         elif self.left_mid == True:
#             print("")
#         elif self.left_down == True:
#             print("")
#         elif self.center_up == True:
#             print("")
#         elif self.center == True:
#             print("")
#         elif self.center_down == True:
#              print("")
#         elif self.right_up == True:
#             print("")
#         elif self.right_mid == True:
#             print("")
#         elif self.right_down == True:
#             print("")




# # Game 
# list = ["X","O"]


# for i in range(1):
#    ban = random.choice(list)
#    print(ban)


