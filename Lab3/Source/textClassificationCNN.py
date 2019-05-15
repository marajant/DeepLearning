import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D, Conv1D
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
from keras.wrappers.scikit_learn import KerasClassifier
import re
import warnings
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.optimizers import SGD

from sklearn.preprocessing import LabelEncoder
warnings.simplefilter(action='ignore', category=FutureWarning)
#reading in the csv file
data = pd.read_csv('lab3Train.csv')

#we only want the phrase and the sentiment
data = data[['Phrase','Sentiment']]
#we don't care about the neutral sentiments
data = data[data.Sentiment != "2"]

data['Phrase'] = data['Phrase'].apply(lambda x: x.lower())
data['Phrase'] = data['Phrase'].apply((lambda x: re.sub('[^a-zA-z0-9\s]', '', x)))

print(data[data['Sentiment'] == 0].size)
print(data[data['Sentiment'] == 4].size)

max_fatures = 2000
tokenizer = Tokenizer(num_words=max_fatures, split=' ')
tokenizer.fit_on_texts(data['Phrase'].values)
X = tokenizer.texts_to_sequences(data['Phrase'].values)
print(X)
X = pad_sequences(X)
print(X)
embed_dim = 128
#lstm_out = 196

def createmodel():
    model = Sequential()
    model.add(Embedding(max_fatures, embed_dim,input_length = X.shape[1]))
    model.add(SpatialDropout1D(0.4))
    model.add(Conv1D(196,padding='valid',activation='relu',strides=1))
    model.add(Dense(5,activation='softmax'))
    model.compile(loss = 'categorical_crossentropy', optimizer='adam',metrics = ['accuracy'])
    return model


integer_encoded = data['Sentiment']
y = to_categorical(integer_encoded)
X_train, X_test, Y_train, Y_test = train_test_split(X,y, test_size = 0.33, random_state = 42)
print(X_train.shape,Y_train.shape)
print(X_test.shape,Y_test.shape)


X = np.expand_dims(X, axis=2)
model = Sequential()
model.add(Conv1D(196,(5),padding='same',input_shape=(43907,45,3)))
model.add(Dense(5,activation='relu'))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(80))
model.add(Dense(10,activation='softmax'))
epochs = 1
lrate = 0.01
decay = lrate/epochs

sgd = SGD(lr=lrate, momentum=0.9, decay=decay, nesterov=False)
model.compile(loss='categorical_crossentropy',optimizer=sgd, metrics=['accuracy'])
model.fit(X_train, Y_train, epochs = epochs, batch_size=32, verbose = 2)
score,acc = model.evaluate(X_test,Y_test,verbose=2,batch_size=32)

print(score)
print(acc)