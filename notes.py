# It is a test

# a  = ['a','b','c','d']
# b = ['q','w']


# for i in a, b:
#     if i == a:
#         print('1',i[0:4])
#     elif i == b:
#         print('2',i)

# c=[]
# a = [1,2,3,4,5]
# b = [1,4,6,7,8,9]
# for i in a,b:
#     c.append(i)
# from math import sqrt
# a = 0.508
# b = 0.312

# x = (a*2)**2 + (b*2)**2

# print(sqrt(x)/2.54)

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


