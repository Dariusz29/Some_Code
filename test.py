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
        with open('word_answer.txt') as an:
            an = list(an)


        for i in range(0,int(i)):
            words = random.choice(ww)
            num_ww = ww.index(words)
            num_an = num_ww
            answer = input(f'Type translation {words} = ')    
                 
        
            word = {}
            ans = {}
            check = []

            for i, v in enumerate(an[num_an]):
                word[i] = v

            for i, v in enumerate(answer):
                ans[i] = v

            for i in range(len(ans.keys())):

                if word[i] == ans[i]:
                    check.append(1)

                else:
                    check.append(0)

            if sum(check) == len(word.keys()):
                print("""
                Great answer!!!
                Next word....""", an[num_an])

            elif sum(check) >= len(word.keys())//2:
                print("""
                Your answer is in half right.
                Next word....""",an[num_an])
                
            else:
                print("""
                Bad answer
                Next word....""",an[num_an])
                
        print("Test is finish!")


while True:

    kind_test()
    break


