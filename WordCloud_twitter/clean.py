from curses.ascii import isalpha
import pprint
import nltk
from nltk import sent_tokenize as s_t
from nltk import word_tokenize as w_t
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer 
import operator
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

ps = PorterStemmer()
personal = ["mark","zuckerberg","zuckerbergs"]
file = open("out1.txt",'r')
init_text = file.read()
not_allowed = "1!2@3#4$5%6^7&8*9(0)-_=+[{]}\|;:'""?/>.<,`~''"
fin_text = ""
for word in init_text:
    if word in not_allowed:
        fin_text += " "
        continue
    else:
        fin_text = fin_text+word

      
words = w_t(fin_text)
stop_list = set(stopwords.words("english"))
no_stop = []
for item in words:
    if (item.isalpha()):
        item = item.lower()
        if item in stop_list:
            continue
        elif item in personal:
            continue
        else:
            no_stop.append(item)
stems=[]
for item in no_stop:
    stem = ps.stem(item)
    #print(item," : ", stem)
    stems.append(stem)
freq = {}
for item in stems:
    if item in freq:
        freq[item]+=1
    else:
        freq[item]=1
sorted_stems = dict(sorted(freq.items(),key=operator.itemgetter(1),reverse=True))
#for key in freq:
#    print(key, " : ", freq[key])
cloud_words = ''
space = ' '
for item in no_stop:
    item_w = str(item)
    #print(item_w)
    if item_w.isalpha():
        cloud_words += item_w
        cloud_words+=space
print(cloud_words)
