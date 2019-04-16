import matplotlib.pyplot as plot
import pandas as pd

tGlobal={}
listCommonWords=["the","a","an"]

#sort the tGlobal:
def insertionSort(l):
    for i in range(1 ,len(l)):
        key=l[i]
        j=i-1
        while j>=0 and key<l[j]:
            l[j+1]=l[j]
            j -= 1
        l[j+1]=key

for i in range(1,26):
    text=[]
    path = "Top 50 Lyrics\\"+str(i)+".txt"
    with open(path,'r') as fd:
        raw_text=fd.readlines()
    for j in range(len(raw_text)):
        if '\n' in raw_text[j]:
            raw_text[j] = raw_text[j].replace('\n', " ")
        if ')' in raw_text[j]:
            raw_text[j] = raw_text[j].replace(')', "")
        if '(' in raw_text[j]:
            raw_text[j] = raw_text[j].replace('(', "")
        if ',' in raw_text[j]:
            raw_text[j] = raw_text[j].replace(',', "")
        if '.' in raw_text[j]:
            raw_text[j] = raw_text[j].replace('.', "")
        if '!' in raw_text[j]:
            raw_text[j] = raw_text[j].replace('!', "")
        if '?' in raw_text[j]:
            raw_text[j] = raw_text[j].replace('?', "")
    raw_sentences = "".join(raw_text)
    text=raw_sentences.split(" ")

    for j in range(len(text)):
        word=text[j].lower()
        if word not in tGlobal and word not in listCommonWords:
            tGlobal[word] = 1
        elif word in tGlobal:
            tGlobal[word] += 1



listofTuples = sorted(tGlobal.items(), reverse=True, key=lambda x: x[1])
showDict={}
print(tGlobal['christmas'])
for i in range(35):
    showDict[listofTuples[i][0]] = listofTuples[i][1]

pandaFrame=pd.DataFrame(showDict, index=[0])

pandaFrame.plot.bar()

plot.show()
