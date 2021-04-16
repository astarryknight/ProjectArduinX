import serial
#from serial import Serial
import io
import Xlib
import time
from pynput.keyboard import Key, Controller

#setup keybinds:
b1 = "a"
b2 = "w"

keyboard = Controller()

#com and BAUD rate for arduino port
ser = serial.Serial('COM4', 9600, timeout=1)

def read():
    data = ser.readline()
    return data

while True:
    #print(read())
    #ah yes i found it WITHOUT stackoverflow checkmate
    #also b stands for byte since the serial monitor is sending bytes, not strings ¯\_(ツ)_/¯
    #if write_read()==b"0\r\n"
    a = str(read())
    #print(a)
    if a != "b''":
        if a[2] == "0":
            keyboard.press(b1)
            keyboard.release(b1)
        if a[3] == "0":
            keyboard.press(b2)
            keyboard.release(b2)