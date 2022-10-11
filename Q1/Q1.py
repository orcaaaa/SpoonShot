#testing the speed of my program to make sure 
import time
start_time = time.time()

#importing jellyfish to compare strings based on their similarity
import jellyfish
#natural language tool kit to be able to cleanly and 
#efficiently extract important words from the article given.
import nltk 
from nltk import word_tokenize
from nltk.corpus import stopwords
import math

#bringing in the ingredients list to the running python file.
from ingredientlist1 import ingredients

#retroactively adding extra stop words that weren't parsed by default.
new_stopwords = [",", ".", "â€", "“", "!","?", "iâ€™d", "â€", "â€˜iâ€™m", ";","@"]
final_stopwords = nltk.corpus.stopwords.words('english')
final_stopwords.extend(new_stopwords)




#word processing for the article.

with open('foodarticle1.txt') as f:
 lines = f.readlines()
sentences = ''.join(lines)

tokenized_words = word_tokenize(sentences)

#obtaining a list of relevant words from the article
tokens_without_sw = [word for word in tokenized_words if not word in final_stopwords]



#word processing for the ingredient list.
ingredients=[ingredient.lower() for ingredient in ingredients]


#adding score values to the ingredient list. initializing them to be 0.
ingredient_dictionary = dict.fromkeys(ingredients, 0)


#comparing each element in the parsed article with individual words from each ingredient.
#comparison is made using jaro_distance. using a function to get a scale arc tangent of 
#the comparison along with an offset to make sure x above 0.5 is closer to 1 adn x below 
# 0.5 is closer to 0.


for final_tokens in tokens_without_sw:
  for ingredient in ingredients:
    for part in ingredient.split(): 
      x=(jellyfish.jaro_distance(part,final_tokens))
      ingredient_dictionary[ingredient]+=(1.078*math.atan(x)+0.5)

#creating the final list of ingredients most appropriate to the article.
leaderboard = list()
for key,value in ingredient_dictionary.items():
  valkey=(value,key)
  leaderboard.append(valkey)

#sorting the leaderboard based on values in descending order.
leaderboard=sorted(leaderboard,reverse=True)


#printing the 10 most relevant ingredients from the ingredient list by their relevance to the article
for (value,key) in leaderboard[:10]:
  print(key, value)


print("--- %s seconds ---" % (time.time() - start_time))

