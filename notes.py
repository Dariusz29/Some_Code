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

# pos_board = {
#         1:["X"], 
#         2:["X"],
#         3:["X"],
#         4:[4],
#         5:[5],
#         6:[6],
#         7:[7],
#         8:[8],
#         9:[9]
#     } 
# # def rules():
# #     x = ("X" or "O")
    

# #     if (pos_board[1] and pos_board[2] and pos_board[3])==x:
# #         print('You win this game!')
# #     elif x == (pos_board[4] and pos_board[5] and pos_board[6]):
# #         print('You win this game!')
# #     elif x == (pos_board[7] and pos_board[8] and pos_board[9]):
# #         print('You win this game!')
# #     elif x == (pos_board[1] and pos_board[4] and pos_board[7]):
# #         print('You win this game!')
# #     elif x == (pos_board[2] and pos_board[5] and pos_board[8]):
# #         print('You win this game!')
# #     elif x == (pos_board[3] and pos_board[6] and pos_board[9]):
# #         print('You win this game!')
# #     elif x == (pos_board[1] and pos_board[5] and pos_board[9]):
# #         print('You win this game!')
# #     elif x == (pos_board[3] and pos_board[5] and pos_board[7]):
# #         print('You win this game!')


# # x = ["X"] or ["O"]
# # z = list(pos_board.values())    
# # print(z[3])
# # print(z[3] == x)
# # if z[0]==x and z[1]==x and z[2]==x:
# #     print('You win this game!')

# def rules():
#         x = ["X"] or ["O"]
#         z = list(pos_board.values())
        

#         if z[1] == x and z[2] == x and z[3]:
#             print('You win this game!')
#         elif z[4] == x and z[5] == x and z[6]:
#             print('You win this game!')
#         elif z[7] == x and z[8] == x and z[9]:
#             print('You win this game!')
#         elif z[1] == x and z[4] == x and z[7]:
#             print('You win this game!')
#         elif z[2] == x and z[5] == x and z[8]:
#             print('You win this game!')
#         elif z[3] == x and z[6] == x and z[9]:
#             print('You win this game!')
#         elif z[1] == x and z[5] == x and z[9]:
#             print('You win this game!')
#         elif z[3] == x and z[5] == x and z[7]:
#             print('You win this game!')

# a  = {
#         1:["X"], 
#         2:["X"],
#         3:["X"],
#         4:[4],
#         5:[5],
#         6:[6],
#         7:[7],
#         8:[8],
#         9:[9]
#     } 
# c = True
# while c:
#     for i in a:
#         print(i)
#         if a.index(2) == 3:
#             c = False
#             break
# 
import random
ww = ["qwer", 'asdf', 'zxcvbnm']
pp = ["rewq", 'fdsa', 'mnbvcxz']
words = random.choice(ww)
print(words)
num_ww = ww.index(words)
num_pp = num_ww
print(num_ww, num_pp)
ans = input(f'Type translation {words} = ')

# if words[:len(ww[num_ww])//2] == ans[len(pp[num_pp])//2:]: 
    




if ans == pp[num_pp]:
    print("""
    Great answer!!!
    Next phase....""")

elif words[len(ww[num_ww])//2] == ans[len(pp[num_pp])//2]: 
    print("""
    Your answer is in half right.
    Next phase....""")
    
else:
    print("""
    Bad answer
    Next phase....""")
            
print("Test is finish!")