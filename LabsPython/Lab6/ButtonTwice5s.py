import pyfirmata
from pyfirmata import Arduino
import time

board = Arduino("\\.\COM4")

it = pyfirmata.util.Iterator(board)
it.start()

board.digital[2].mode = pyfirmata.INPUT

ps = 0

while True:
    bs = board.digital[2].read()
    time.sleep(0.1)
    if bs is True:
        ps = ps + 1
        print(ps)
        if ps == 2:
            print("Encendiendo led#1...")
            board.digital[8].write(1)
            time.sleep(5)
            print("Apagando led#1...")
            board.digital[8].write(0)
        if ps == 4:
            print("Encendiendo led#2...")
            board.digital[12].write(1)
            time.sleep(5)
            print("Apagando led#2...")
            board.digital[12].write(0)
            print("Reseteando las pulsaciones...")
            ps = 0
    else:
        board.digital[8].write(0)
        board.digital[12].write(0)
        time.sleep(0.2)           