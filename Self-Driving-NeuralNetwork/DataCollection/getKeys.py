import win32api as wapi
import time

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789":
    keyList.append(char)
    
def Check_pressed():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keyList.append(key)
    return keys
