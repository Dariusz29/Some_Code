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
   

    def board():
        
        for i in range(1,4): 

            for j in range(1,4):
                
                if i == 2 and j == 1:
                    n = i*j+2
                elif i == 2 and j == 2:
                    n = i*j+1
                elif i == 3 and j == 1:
                    n = i*j+4    
                elif i == 3 and j == 2:
                    n = i*j+2
                else:
                    n = i*j
                    
                board = f'{pos_board[n]}'
                print(board, end= " ") 
            print()
    
    def rules():
        x = ["X"] or ["O"]
        z = list(pos_board.values())
        

        if z[1] == x and z[2] == x and z[3]:
            print('You win this game!')      
        elif z[4] == x and z[5] == x and z[6]:
            print('You win this game!')
        elif z[7] == x and z[8] == x and z[9]:
            print('You win this game!')
        elif z[1] == x and z[4] == x and z[7]:
            print('You win this game!')
        elif z[2] == x and z[5] == x and z[8]:
            print('You win this game!')
        elif z[3] == x and z[6] == x and z[9]:
            print('You win this game!')
        elif z[1] == x and z[5] == x and z[9]:
            print('You win this game!')
        elif z[3] == x and z[5] == x and z[7]:
            print('You win this game!')
        

    def choice():
        a = True
        _pos_ = [1,2,3,4,5,6,7,8,9]

        empty = bool(a for a in pos_board.values() if a != [])
        left_up = bool(a for a in pos_board.keys() if pos_board[1] != ["X"] or ["O"])
        left_mid = bool(a for a in pos_board.keys() if pos_board[2] != ["X"] or ["O"])
        left_down = bool(a for a in pos_board.keys() if pos_board[3] != ["X"] or ["O"])
        center_up = bool(a for a in pos_board.keys() if pos_board[4] != ["X"] or ["O"])
        center = bool(a for a in pos_board.keys() if pos_board[5] != ["X"] or ["O"])
        center_down = bool(a for a in pos_board.keys() if pos_board[6] != ["X"] or ["O"])
        right_up = bool(a for a in pos_board.keys() if pos_board[7] != ["X"] or ["O"])
        right_mid = bool(a for a in pos_board.keys() if pos_board[8] != ["X"] or ["O"])
        right_down = bool(a for a in pos_board.keys() if pos_board[9] != ["X"] or ["O"])
        pos__ = [empty,left_up,left_mid,left_down,center_up,center,center_down,right_up,right_mid,right_down]

        

        for i in range(0,9):
            
            Body.board()
           
            if i % 2:
                ban = "X"
            else:
                ban = "O"
            
            _pos = random.choice(_pos_) 
            
            if pos__[0]: 
                pos_board[_pos].append(ban)
                _pos_.remove(_pos)
                
                

            elif pos__[1] and _pos:
                    pos_board[_pos].append(ban)
                    _pos_.remove(_pos)
                    
                

            elif pos__[2] and _pos:
                pos_board[_pos].append(ban)
                _pos_.remove(_pos)
                

            elif pos__[3] and _pos:
                pos_board[_pos].append(ban)
                _pos_.remove(_pos)
                

            elif pos__[4] and _pos:
                pos_board[_pos].append(ban)
                _pos_.remove(_pos)
                

            elif pos__[5] and _pos:
                pos_board[_pos].append(ban)
                _pos_.remove(_pos)
                
              

            elif pos__[6] and _pos:
                pos_board[_pos].append(ban)
                _pos_.remove(_pos)
                
               

            elif pos__[7] and _pos:
                pos_board[_pos].append(ban)
                _pos_.remove(_pos)
                
             

            elif pos__[8] and _pos:
                pos_board[_pos].append(ban)
                _pos_.remove(_pos)
                
             

            elif pos__[9] and _pos:
                pos_board[_pos].append(ban)
                _pos_.remove(_pos)
            
            print('\n')
        
        Body.board()
        Body.rules()
       
        print('End Game!!!')      

    



            
           


Body.choice()