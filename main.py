import nltk
from nltk.corpus import stopwords
from nltk.corpus import inaugural
from nltk.tokenize import word_tokenize, sent_tokenize
import matplotlib.pyplot as plt
import pyphen
from wordcloud import WordCloud
names=inaugural.fileids()
print(len(names))
names[0], names[55]

inaugural.raw(fileids = names[55])
words=list(inaugural.words(fileids = names[55]))
words
print(nltk.FreqDist(words))

stop_words = stopwords.words('english')
add_to_stop_words = [",", ".", "-", ":", "--", "'", "(", ")"]

add_to_stop_words.extend(add_to_stop_words)
stop_words = set(add_to_stop_words)
print(stop_words)

for i in stop_words:
    if i in words:
        while i in words:
            words.remove(i)

print(nltk.FreqDist(words))

#counts number of words of a particular length
def countwords(dic,length):
    tsum=0
    for i in dic:
        if len(i)==length:
            tsum=tsum+dic[i]
            #print(i,dic[i])
    return tsum

#counting 2 letter words, 3 letter words etc
presidents_avg=[]
for x in names:
    words=inaugural.words(fileids=x)
    fdist=nltk.FreqDist(words)
    print("For president ",x[:-4])
    avg=0
    totalnoofwords=0
    for i in range(1,20):
        tsum=countwords(fdist,i)
        avg=avg+tsum*i
        totalnoofwords=totalnoofwords+tsum
        print("No of words of length ",i, " are " ,tsum)
    avg=avg/totalnoofwords
    print(avg)
    presidents_avg.append(avg)


plt.scatter(names,presidents_avg)
plt.show()

def avgwordspersentence(words):
    counter=0
    avg=0
    noofsentences=0
    for i in words:
        if(i!='.'):#and i!=','
            counter=counter+1
        else:
            noofsentences+=1
            avg+=counter
            counter=0
    avg=avg/noofsentences
    return avg

presidents_avg_words_per_sentence=[]
for x in names:
    words=inaugural.words(fileids = x)
    presidents_avg_words_per_sentence.append(avgwordspersentence(words))
#without commas
plt.scatter(names,presidents_avg_words_per_sentence)
plt.show()

presidents_hapaxes=[]
for x in names:
    words=nltk.FreqDist(inaugural.words(fileids = x))
    presidents_hapaxes.append(len(words.hapaxes())/len(words))
plt.scatter(names,presidents_hapaxes)
plt.show()
dic = pyphen.Pyphen(lang='en')
def noofsyllabes(corpus):
    num=0
    for x in corpus:
        s=dic.inserted(x)
        num=num+s.count('-')+1
    return num
presidents_avg=[]
for x in names:
    words=list(nltk.FreqDist(inaugural.words(fileids = x)))
    for s in stop_words:
        if s in words:
            words.remove(s)
    n=noofsyllabes(words)/len(words)
    presidents_avg.append(n)
plt.scatter(names,presidents_avg)
plt.show()