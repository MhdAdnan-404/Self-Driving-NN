import win32api as wapi
import time

keyList = {
    "I": "",
    "L": "",
    "K": "",
    "J": "",
    "V": "",
    "T": "",
}

def Check_pressed():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys
