fname = input('enter file name:')
if len(fname)<1:
  fname='foodarticle1.txt'
    

#hand = open(fname,'r')
# for w in hand:
#   w = w.split()
#   print(w)
import nltk 
from nltk import word_tokenize as wt
from nltk.corpus import stopwords
with open('foodarticle1.txt') as f:
    lines = f.readlines()

sentences = ''.join(lines)
tokens = wt(sentences)

tokens_without_sw = [word for word in tokens if not word in stopwords.words()]

print(tokens_without_sw)

