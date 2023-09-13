import numpy as np
import cv2
import pandas as pd

trainning_data = np.load('C:/Users/bytes 2.0/Desktop/Projects/Self-Driving-NeuralNetwork/trainingData.npy', allow_pickle=True)

trainning_data_normalized = np.load('C:/Users/bytes 2.0/Desktop/Projects/Self-Driving-NeuralNetwork/Trainning_Normalized_data.npy', allow_pickle=True)




# for data in trainning_data_normalized:
#     img = data[0]
#     print(img.shape)
#     input = data[1]
#     cv2.imshow('img', img)
#     print(input)
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()

df = pd.DataFrame(trainning_data_normalized)
print(df.head)