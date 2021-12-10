# import serial
# from serial import Serial
import string

# ser = serial.Serial('COM3',9600)
# data = ser.readline(1000)

# print(data)

# initialization
data = list("svool") #sample data
# data = ''.join(data)
print(data)
l =len(data)
arr = list(string.ascii_lowercase)

# upper if not 
# if data.isupper() and data.isnumeric():
#     pass
# else:
#     data = data.upper()  
#     # print(data)


#index
def index(data,arr):
    placeIndex = [i for i in range(len(arr)) if data == arr[i]]
    return placeIndex

#convert the data
def convert(data,arr,rev_arr):
    ind = index(data,arr)
    return rev_arr[ind[0]]

# condition check
def decrypt(data,arr):
    for i in range(len(data)):
        if data[i] == arr:
            return print(convert(data[i],arr,arr[::-1]))
        else:
            return print("Error in data!!!")

# arr2  = arr1[::-1]
# print(arr1)

# for i in len(l):
    
# decrypt
print(index("s",arr))
print(convert("s",arr,rev_arr=arr[::-1]))
print(decrypt(data,arr))
