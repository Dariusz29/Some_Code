
t = open("words_tutlo.txt", "r")
f = open('word.txt',"w")
word_eng = []
phases = []
word_wrong = []

for w in t:
    if "=" in w:
        data = w.split('=')
        word_eng.append(data[0].lower())
    elif "-" in w:
        data_ = w.split('-')
        word_eng.append(data_[0].lower())
        
for i in word_eng:
    f.write(i)
    f.write('\n')
    
