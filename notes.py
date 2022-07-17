# It is a test
import random





pos__ = {
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
    1:[1], 
    2:[2],
    3:[3],
    4:[4],
    5:[5],
    6:[6],
    7:[7],
    8:[8],
    9:[9]
} 

for i in range(1,4): 

    for j in range(1,4):

        board = f'{pos_board[0 + j*i]}'
       
        print(board, end= " ") 

    print()

      


