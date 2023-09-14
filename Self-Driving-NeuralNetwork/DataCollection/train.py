import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
from tensorflow.keras.models import Sequential


trainning_data_normalized = np.load('C:/Users/bytes 2.0/Desktop/Projects/Trainning_Normalized_data.npy', allow_pickle=True)


train_set = trainning_data_normalized[:-1000]
testing_set = trainning_data_normalized[-1000:]

X = np.array([i[0] for i in train_set])
Y = np.array([i[1] for i in train_set])

X_test = np.array([i[0] for i in testing_set])
Y_test = np.array([i[1] for i in testing_set])

model = models.Sequential()
model.add(layers.Conv2D(92, (3, 3), activation='relu', input_shape=(150, 200, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Flatten())

model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(7, activation='softmax')) 


model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
epochs = 10

batch_size = 128

model.fit(X,Y, epochs=epochs, batch_size=batch_size, verbose=2, validation_data=(X_test, Y_test))

model.save('drivingModel4')











