
import numpy as np



data = np.load('C:/Users/bytes 2.0/Desktop/Projects/trainingData.npy', allow_pickle=True)

print(data)

def normalize(image):
    image = np.array(image, dtype=float)
    
    nomalized = image / 255.0
    
    return nomalized

for i in data:
    image = i[0]
    image = normalize(image)
    i[0] = image

print(data[0][0].shape)

np.save('Trainning_Normalized_data.npy', data)


