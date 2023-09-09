import numpy as np
from grabScreen import grab_screen
from getKeys import Check_pressed
import cv2
import os
import time

w =  [1,0,0,0,0,0,0,0,0]
s =  [0,1,0,0,0,0,0,0,0]
a =  [0,0,1,0,0,0,0,0,0]
d =  [0,0,0,1,0,0,0,0,0]
wa = [0,0,0,0,1,0,0,0,0]
wd = [0,0,0,0,0,1,0,0,0]
sa = [0,0,0,0,0,0,1,0,0]
sd = [0,0,0,0,0,0,0,1,0]
sp = [0,0,0,0,0,0,0,0,1]


def oneHotArr(keys):
    res = [0,0,0,0,0,0,0,0,0]
        #A #W #D #Space
    if 'W' in keys and 'A' in keys:
        res = wa
    elif 'W' in keys and 'D' in keys:
        res = wd
    elif ' ' in keys and 'A' in keys:
        res = sa
    elif ' ' in keys and 'D' in keys:
        res = sd
    elif 'W' in keys:
        res = w
    elif 'S' in keys:
        res = s
    elif 'A' in keys:
        res = a
    elif 'D' in keys:
        res = d
    elif ' ' in keys:
        res = sp
        
    return res

file = 'trainingData.npy'

if os.path.isfile(file):
    print('File exists')
    data = list(np.load(file))
else:
    print("No File Found")
    data = []



def main():
    for i in range(0,5):
        print(i+1)
        time.sleep(1)
        
    last_time = time.time()
    while True:
        screen = grab_screen(region=(0,40,800,600))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen, (80,60))
        keys = Check_pressed()
        output = oneHotArr(keys)
        data.append([screen, output])
        # cv2.imshow('window', screen)
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
        #     break
        if len(data) % 500 == 0:
            print("data length is  {}".format(len(data)))
            np.save(file, data)
    
    
    
main()