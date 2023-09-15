import numpy as np
from grabScreen import grab_screen
from getKeys import Check_pressed
import cv2
import os
import time


I =   [1,0,0,0,0,0,0]
L =   [0,1,0,0,0,0,0]
K =   [0,0,1,0,0,0,0]
J =   [0,0,0,1,0,0,0]
IJ =  [0,0,0,0,0,1,0]
IL =  [0,0,0,0,0,0,1]


def oneHotArr(keys):
    
    output = [0,0,0,0,0,0,0]
    
    if 'I' in keys and 'L' in keys:
        output = IL
    elif 'I' in keys and 'J' in keys:
        output = IJ
    elif 'L' in keys:
        output = L
    elif 'K' in keys:
        output = K
    elif 'J' in keys:
        output = J
    elif 'I' in keys:
        output = I
    return output
    
    

file = 'trainingData.npy'

if os.path.isfile(file):
    print('File exists')
    data = list(np.load(file, allow_pickle=True))
else:
    print("No File Found")
    data = []



def main():
    for i in range(0,5):
        print(i+1)
        time.sleep(1)
        
    while True:
        screen = grab_screen(region=(0,317,790,600))
        screen = cv2.resize(screen, (200,150))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        keys = Check_pressed()
        output = oneHotArr(keys)
        data.append([screen,output])
      
        if len(data) % 500 == 0:
            np.save(file, data)
            print("data length is  {}".format(len(data)))
    
    
    
if __name__ == "__main__":
    main()