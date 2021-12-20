import serial
import time

"""
arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
while 1:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num)
    print(value) # printing the value
serialcomm.close()
"""
serialcomm = serial.Serial('COM5', 9600)
serialcomm.timeout = 1

while True:
    i = input("on/off: ").strip()
    if i == "Done":
        print('finished')
        break
    serialcomm.write(i.encode())
    time.sleep(0.5)
    print(serialcomm.readline().decode('ascii'))
serialcomm.close()

