from decode import decode

print(decode("1A69D"))

# import serial
# from serial import Serial

# ser = serial.Serial('COM3',9600)
# data = ser.readline(1000)
import serial
import time
arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num)
    print(value) # printing the value