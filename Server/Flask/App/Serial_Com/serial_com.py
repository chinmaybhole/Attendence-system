from decode import decode
import serial



ser = serial.Serial('COM6',9600)
data = ser.readline()
stri= data.decode("utf-8")
# print(data)
print(stri)

# print(decode(stri))
