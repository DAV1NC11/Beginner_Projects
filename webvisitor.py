#!/usr/bin/python

import webbrowser
import time
import keyboard

k = keyboard()

count = 0
urls = ['google.com','facebook.com','instagram.com']

while count < 100:
    for url in urls:
        webbrowser.open(url, new=0)
        time.sleep(5)
        k.press_key(k.control_key)
        k.tap_key('w')
        k.release_key(k.control_key)
        count += 1
        
else:
    pass

