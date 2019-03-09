# Importing the necessary libraries
from bs4 import BeautifulSoup
import requests
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from nltk import wordpunct_tokenize, pos_tag, ne_chunk

# reading data from given url and saving it to a file
url="https://en.wikipedia.org/wiki/Google"
html=requests.get(url)
data = html
bsObj= BeautifulSoup(data.content,"html.parser")
f = open("input.txt","w",encoding="utf8")
f.write(str(bsObj.text))
f.close()

# reading the file
fr = open("input.txt", "r")

# Tokenization
# print("=====Tokenization==================")
# for x in fr:
#     x = fr.readline()
#     tokenTest = nltk.sent_tokenize(x)
#     for z in tokenTest:
#         print(z)

# POS
# print("=====POS==================")
# fr.seek(0)
# for x in fr:
#     x = fr.readline()
#     tokenTest = nltk.sent_tokenize(x)
#     for z in tokenTest:
#         print(nltk.pos_tag(z))

# Stemmer
# print("=====Stemmer==================")
# fr.seek(0)
# pStemmer= PorterStemmer()
# for x in fr:
#     x = fr.readline()
#     tokenTest = nltk.sent_tokenize(x)
#     for z in tokenTest:
#         print(pStemmer.stem(z))

# Lemmatize
# print("=====Lemmatize==================")
# fr.seek(0)
# lemmatizer = WordNetLemmatizer()
# for x in fr:
#     x = fr.readline()
#     tokenTest = nltk.sent_tokenize(x)
#     for z in tokenTest:
#         print(lemmatizer.lemmatize(z))

#trigram
# print("=====trigram==================")
# fr.seek(0)
# for x in fr:
#     x = fr.readline()
#     tokenTest = nltk.word_tokenize(x)
#     trigram= ngrams(tokenTest,3)
#     for z in trigram:
#         print(z)

# NER
print("=====NER==================")
fr.seek(0)
for x in fr:
    x = fr.readline()
    print(ne_chunk(pos_tag(wordpunct_tokenize(x))))