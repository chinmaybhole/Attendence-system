from App import Models
from passw import hash_passwd

def custom_validation_parser(value):
    if not value:
        raise ValueError("Must not be empty.")
    return value

def check_phoneno(value):
    phoneno = [int(x) for x in str(value)]
    if len(phoneno) == 10:
        return True
    else:
        return False

def check_userid(value,flag):
    flag = flag
    # print(flag)
    user = Models.User(userid= value)
    status = user.getAUser() 

    if flag == "get":
        if status[-1] ==200: 
            # print("get flag True =",status)
            return status
        else:
            # print("get flag false =",status)
            return status

    if flag == "delete":
        if status[-1] ==200: 
            # print("flag True =",status)
            return status
        else:
            # print("flag false =",status)
            return status

    if flag == "put":
        if status[-1] == 200:
            # print("put flag True =",status)
            userid = [int(x) for x in str(value)]
            if len(userid) == 10:
                return True
            else:
                return {"message":"Invalid Lenght"}

    if flag == "post":
        userid = [int(x) for x in str(value)]
        data = [2,2,2]
        if userid[:3] == data:
            return True
        else:
            return False

def data_indexing(data):
    key = list(data)
    dict_value = dict.values(data)
    value = list(dict_value)
        
    return key,value


def make_a_list(index_list,data):
    data_args = ['srno', 'userid', 'fname', 'lname', 'passw', 'rollno', 'div', 'dept', 'phone', 'isStudent']
    new_list = []
    while 1:
        i = 0
        for arg in data_args:
            # print(index,arg)
            if arg in index_list:
                # Password Hashing
                if arg == 'passw':
                    new_list.append(hash_passwd(data[i]))
                else : new_list.append(data[i])
                i +=1
            else:
                new_list.append(None)             
        break
    return new_list

    

    
                            

    