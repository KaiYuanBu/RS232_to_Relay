import serial
import time

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)
ser.rts = True  # Relay ON

time.sleep(5)
ser.rts = False  # Relay OFF

time.sleep(5)
ser.close()
