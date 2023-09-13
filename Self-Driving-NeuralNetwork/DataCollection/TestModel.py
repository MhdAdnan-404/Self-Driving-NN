import numpy as np
from grabScreen import grab_screen
from getKeys import Check_pressed
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model

import cv2
import os
import time
from pressKeys import PressKey, ReleaseKey, I, J, K, L, V


# I =   [1,0,0,0,0,0,0,0,0,0,0]
# L =   [0,1,0,0,0,0,0,0,0,0,0]f
# K =   [0,0,1,0,0,0,0,0,0,0,0]
# J =   [0,0,0,1,0,0,0,0,0,0,0]
# V =   [0,0,0,0,1,0,0,0,0,0,0]
# IJ =  [0,0,0,0,0,1,0,0,0,0,0]
# IL =  [0,0,0,0,0,0,1,0,0,0,0]
# IJV = [0,0,0,0,0,0,0,1,0,0,0]
# ILV = [0,0,0,0,0,0,0,0,1,0,0]
# JV =  [0,0,0,0,0,0,0,0,0,1,0]
# LV =  [0,0,0,0,0,0,0,0,0,0,1]




model = load_model('C:/Users/bytes 2.0/Desktop/Projects/drivingModel2')


def forward():
    PressKey(I)
    ReleaseKey(J)
    ReleaseKey(K)
    ReleaseKey(L)
    ReleaseKey(V)
    

def forward_left():
    PressKey(I)
    PressKey(J)
    ReleaseKey(K)
    ReleaseKey(L)
    ReleaseKey(V)

def forward_right():
    PressKey(I)
    PressKey(L)
    ReleaseKey(J)
    ReleaseKey(K)
    ReleaseKey(V)

def forward_left_break():
    PressKey(I)
    PressKey(J)
    PressKey(V)
    ReleaseKey(L)
    ReleaseKey(K)


def forward_right_break():
    PressKey(I)
    PressKey(L)
    PressKey(V)
    ReleaseKey(J)
    ReleaseKey(K)

def left():
    PressKey(J)
    ReleaseKey(L)
    ReleaseKey(K)
    ReleaseKey(L)
    ReleaseKey(V)

def right():
    PressKey(L)
    ReleaseKey(J)
    ReleaseKey(K)
    ReleaseKey(I)
    ReleaseKey(V)


def backwards():
    PressKey(K)
    ReleaseKey(J)
    ReleaseKey(L)
    ReleaseKey(I)
    ReleaseKey(V)
    
def handBreak():
    PressKey(V)
    ReleaseKey(J)
    ReleaseKey(L)
    ReleaseKey(I)
    ReleaseKey(K)
    
def breakRight():
    PressKey(J)
    PressKey(V)
    ReleaseKey(K)
    ReleaseKey(L)
    ReleaseKey(I)
    
def breakLeft():
    PressKey(L)
    PressKey(V)
    ReleaseKey(K)
    ReleaseKey(J)
    ReleaseKey(I)
    





def main():
    for i in range(0,5):
        print(i+1)
        time.sleep(1)
        
    stopped = False 
    while True:
           
        if not stopped:
            screen = grab_screen(region=(0,40,800,600))
            screen = cv2.resize(screen, (200,150))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            
            prediction = model.predict([screen.reshape(-1,150,200,1)])[0]
            moves = list(np.around(prediction))
            print(moves)
            
            if moves == [1,0,0,0,0,0,0,0,0,0,0]:
                forward()
            elif moves == [0,1,0,0,0,0,0,0,0,0,0]:
                right()
            elif moves == [0,0,1,0,0,0,0,0,0,0,0]:
                backwards()
            elif moves == [0,0,0,1,0,0,0,0,0,0,0]:
                left()
            elif moves == [0,0,0,0,1,0,0,0,0,0,0]:
                handBreak()
            elif moves == [0,0,0,0,0,1,0,0,0,0,0]:
                forward_left()
            elif moves == [0,0,0,0,0,0,1,0,0,0,0]:
                forward_right()
            elif moves == [0,0,0,0,0,0,0,1,0,0,0]:
                forward_left_break()
            elif moves == [0,0,0,0,0,0,0,0,1,0,0]:
                forward_right_break()
            elif moves == [0,0,0,0,0,0,0,0,0,1,0]:
                breakLeft()
            elif moves == [0,0,0,0,0,0,0,0,0,0,1]:
                breakRight()
                
                    
        keys = Check_pressed()
        
        if 'T' in keys:
            if stopped:
                stopped = False
                time.sleep(1)
            else:
                stopped = True
        
    
    
    
if __name__ == "__main__":
    main()