import numpy as np
from grabScreen import grab_screen
from getKeys import Check_pressed
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model

import cv2
import time
import keyboard





model = load_model('C:/Users/bytes 2.0/Desktop/Projects/drivingModel4')


def forward():
    keyboard.press('i')
    keyboard.release('j')
    keyboard.release('k')
    keyboard.release('l')
 
def forward_left():
    keyboard.press('i')
    keyboard.press('j')
    keyboard.release('k')
    keyboard.release('l')

def forward_right():
    keyboard.press('i')
    keyboard.press('l')
    keyboard.release('j')
    keyboard.release('k')


def left():
    keyboard.press('j')
    keyboard.release('l')
    keyboard.release('k')
    keyboard.release('l')

def right():
    keyboard.press('l')
    keyboard.release('j')
    keyboard.release('k')
    keyboard.release('i')

def backwards():
    keyboard.press('k')
    keyboard.release('j')
    keyboard.release('l')
    keyboard.release('i')




def main():
    for i in range(0,5):
        print(i+1)
        time.sleep(1)
        
    stopped = True
    while True:
           
        if not stopped:
            screen = grab_screen(region=(0,317,790,600))
            screen = cv2.resize(screen, (200,150))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            
            prediction = model.predict([screen.reshape(-1,150,200,1)])[0]
            moves = list(np.around(prediction))
            print(moves)
            
            if moves == [1,0,0,0,0,0,0]:
                forward()
            elif moves == [0,1,0,0,0,0,0]:
                right()
            elif moves == [0,0,1,0,0,0,0]:
                backwards()
            elif moves == [0,0,0,1,0,0,0]:
                left()
            elif moves == [0,0,0,0,0,1,0]:
                forward_left()
            elif moves == [0,0,0,0,0,0,1]:
                forward_right()
                
                    
        keys = Check_pressed()
        
        if 'T' in keys:
            if stopped == True:
                stopped = False
                time.sleep(1)
            else:
                stopped = True
                keyboard.release('k')
                keyboard.release('j')
                keyboard.release('l')
                keyboard.release('i')
                time.sleep(1)
    
    
    
if __name__ == "__main__":
    main()