# Importing the necessary libraries
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from sklearn.feature_extraction.text import CountVectorizer

fr = open("nlp_input.txt", "r")
ORead = open("output.txt", "r")
OWrite = open("output.txt", "w+")
TriWrite = open("tri.txt", "w+")
TriRead = open("tri.txt", "r")


# Tokenization
print("=====Tokenization and Lemmatize ==================")
OWrite.write("=====Tokenization and Lemmatize ==================")
for x in fr:
    x = fr.readline()
    tokenTest = nltk.word_tokenize(x)
    for z in tokenTest:
        lemmatize = WordNetLemmatizer().lemmatize(z)
        OWrite.write(lemmatize)
        OWrite.write("\n")
        print(lemmatize)

# Finding Trigrams
TriWrite.write("=====trigram==================")
print("=====trigram==================")
fr.seek(0)
trigram_measures = nltk.collocations.TrigramAssocMeasures()
c_vec = CountVectorizer(ngram_range=(3,3))

for x in fr:
    x = fr.readline()
    tokenTest = nltk.word_tokenize(x)
    trigram = ngrams(tokenTest,3)
    for z in trigram:
        TriWrite.write(str(z))
        print(z)

# Counting top 10 Trigrams
print("=====trigram count ==================")
ngrams = c_vec.fit_transform(open("tri.txt","r"))
vocab = c_vec.vocabulary_
count = ngrams.toarray().sum(axis=0)
z=0
for c, t in sorted([(count[i],k) for k,i in vocab.items()], reverse= True):
        z= z+1
        if z > 10:
            break
        print(c,t)

# Concatenate Trigrams
print("=====trigram count  concatenated ==================")
ngrams = c_vec.fit_transform(open("tri.txt","r"))
vocab = c_vec.vocabulary_
count = ngrams.toarray().sum(axis=0)
z = 0
L = ""
for c, t in sorted([(count[i],k) for k,i in vocab.items()], reverse= True):
        z= z+1
        if z > 10:
            break
        L=L+t
print(L)
ORead.close()
