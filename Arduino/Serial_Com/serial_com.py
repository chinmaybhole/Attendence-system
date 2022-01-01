from decode import decode
import serial
import time


ser = serial.Serial('COM6',9600)
data = ser.readline()
stri= data.decode("utf-8")
# print(data)
print(stri)


# ser = serial.Serial('COM3',9600)
# data = ser.readline(1000)
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



# print(decode(stri))
