#ask user about kind of which you choice 
from data_word import store_word as sw
import random



# Main of exam
def kind_test():
    while True:
        input("""
        Learn english words = TEST_1
        Learn english phases = TEST_2
        \n
        Number learn words or phases:

        1. 5
        2. 10
        3. 15
        4. 20
        5. 25
        """)

        test = input('Which are you choice test? ')
        n = input('How much words or phases are you learn in the TEST? ')

        if test == 'TEST_1':
            TEST.start_test_word(n)
            break
        elif test == 'TEST_2':
            TEST.start_test_phase(n)
            break
        else:
            print('You type not expected thing, try again')
            break


# feature to take exam with phases
class TEST():

    
    def start_test_phase(i):

        sw('p')
        with open('phases_in_eng.txt', 'r') as pp:
            pp = list(pp)

        for i in range(i):
            words = random.choice(pp)
            num = pp.index(words)
            ans = input(f'Type translation {words} = ')
            word = (word == True for ans in words if words[:len(words)//2] == ans[len(ans)//2:])

            if ans == num:
                print("""
                Great answer!!!
                Next phase....""")

            elif word:
                print("""
                Your answer is in half right.
                Next phase....""")
                
            elif ans != num:
                print("""
            Bad answer
                Next phase....""")
                
        print("Test is finish!")


# feature to exam with words
# wrong examine translations
# in data are lot of wrong connecting word with answer
    def start_test_word(i):

        sw('w')
        with open('word_in_eng.txt', 'r') as ww:
            ww = list(ww)


        for i in range(0,int(i)):
            words = random.choice(ww)
            num = ww.index(words)
            print(num+1)
            ans = input(f'Type translation {words} = ')
            print(ans)
            word = (word == True for ans in words if words[:len(num+1)//2] == ans[len(num+1)//2:])
            print(word)

            if ans == num:
                print("""
                Great answer!!!
                Next word....""")

            elif word:
                print("""
                Your answer is in half right.
                Next word....""")
                
            elif ans != num:
                print("""
            Bad answer
                Next word....""")
                
        print("Test is finish!")


while True:

    kind_test()
    break


