import string

# initialization
data = list("1A94H") #sample data
 # list of upper alphabets 

#index
def index(data,arr):
    placeIndex = [i for i in range(len(arr)) if data == arr[i]]
    return placeIndex

#decode alpha the data
def alp_decode(data,arr,rev_arr):
    ind = index(data,arr)
    return rev_arr[ind[0]]

#decode numeric the data
def num_decode(data):
    num = ["n","l","i","h","a","m","u","s","k","j"]
    return num[int(data)]

# decode
def decode(data_list):
    arr = list(string.ascii_uppercase)
    dec = []
    for i in range(len(data_list)):
        if data_list[i].isalpha():
            if data_list[i] in arr:
                c= alp_decode(data_list[i],arr,arr[::-1])
                dec.append(c)
            else:
                return print("Error in data!!!")
        elif data_list[i].isnumeric():
            dec.append(num_decode(data_list[i]))
    return "".join(dec)