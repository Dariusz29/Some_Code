
word_sourse = open("words_tutlo.txt", "r")
word_sourse_ = open("new_words.txt", "r")
phases_sourse = open("new_phases.txt", "r")
word_in_eng = open('word_in_eng.txt',"w")
word_answer = open('word_answer.txt','w')
phases_in_eng = open('phases_in_eng.txt','w')
phases_answer = open('phases_answer.txt', 'w')
word_eng = []
word_ans = []
phases_eng = []
phases_ans = []


for w in word_sourse, word_sourse_:
    if "=" in w:
        data = w.split('=')
        word_eng.append(data[0].lower())
        word_ans.append(data[1].lower())
    elif "-" in w:
        data = w.split('-')
        word_eng.append(data[0].lower())
        word_ans.append(data[1].lower())
    
for w_ in phases_sourse:
    if "=" in w:
        data = w.split('=')
        phases_eng.append(data[0].lower())
        phases_ans.append(data[1].lower())
    elif "-" in w:
        data = w.split('-')
        phases_eng.append(data[0].lower())
        phases_ans.append(data[1].lower())

for i in word_eng, word_ans:
    if word_eng == i:  
        word_in_eng.write(i)
        word_in_eng.write('\n')
    elif word_ans:
        word_answer.write(i)
        word_answer.write('\n')
   

for i in phases_eng, phases_ans:
    if phases_eng:
        phases_in_eng.write(i)
        phases_in_eng.write('\n')
    elif phases_ans:
        phases_answer.write(i)
        phases_answer.write('\n')

    

    
word_in_eng.close()
word_answer.close()
phases_in_eng.close()
phases_answer.close()