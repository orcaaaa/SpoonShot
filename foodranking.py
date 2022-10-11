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

from ingredientlist1 import ingredients

#word processing for the article.

with open('foodarticle1.txt') as f:
    lines = f.readlines()
sentences = ''.join(lines)

tokenized_words = wt(sentences)

tokens_without_sw = [word for word in tokenized_words if not word in stopwords.words()]

print(tokens_without_sw)

#ing_words= [wt(item) for item in ingredients]
#print(ing_words)
ingredients=[x.lower() for x in ingredients]
print(ingredients)
d = dict.fromkeys(ingredients, 0)

for w in tokens_without_sw:
  for ingredient in ingredients:
    for i in ingredient.split():
      if w in i:
        d[ingredient]+=1



# for j in ing_words:
#   for k in j:
#     if k in tokens_without_sw:
#       d[j]+=1


print(d)
