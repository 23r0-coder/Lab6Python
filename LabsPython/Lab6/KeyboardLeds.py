import keyboard
import pyfirmata
from pyfirmata import Arduino
import time

board = Arduino("\\.\COM4")


while True:   
    if keyboard.read_key() == 'a' and keyboard.read_key() == 'y':
        while True:    
            board.digital[8].write(1)
            time.sleep(1)
            board.digital[8].write(0)
            time.sleep(0.1)
            board.digital[12].write(1)
            time.sleep(1)
            board.digital[12].write(0)
            time.sleep(0.1)
    else:
        board.digital[8].write(0)
        board.digital[12].write(0)
        time.sleep(0.1)
