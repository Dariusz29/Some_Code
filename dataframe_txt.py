
t = open("words_tutlo.txt", "r")
f = open('word.txt',"w")
g = open('translated_word.txt','w')
h = 
word_eng = []
phases = []
word_wrong = []

for w in t:
    if "=" in w:
        data = w.split('=')
        word_eng.append(data[0].lower())
        phases.append(data[1].lower())
    elif "-" in w:
        data = w.split('-')
        word_eng.append(data[0].lower())
        phases.append(data[1].lower())
    
        
for i in word_eng:
    if len(i) < 20: 
        f.write(i)
        f.write('\n')
    else:




for i in phases:
    g.write(i)
    

    
t.close()
f.close()
