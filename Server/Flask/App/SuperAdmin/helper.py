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
    user = Models.User(userid= value)
    _,status = user.getAUser() 

    if flag == "get":
        if status ==200: 
            return 200
        else:
            return False

    if flag == "delete":
        if status ==200: 
            return 200
        else:
            return False

    if flag == "put":
        if status == 200:
            userid = [int(x) for x in str(value)]
            if len(userid) == 10:
                return True
            else:
                return {"message":"Invalid Lenght"}

    if flag == "post":
        if status == 404:
            userid = [int(x) for x in str(value)]
            data = [2,2,2]
            if userid[:3] == data:
                return True
            else:
                return False
        else:
            return False

    if flag == "login":
        if status == 200:
            return 200
        else:
            return False

def data_indexing(data):
    key = list(data)
    dict_value = dict.values(data)
    value = list(dict_value)
        
    return key,value

def make_a_list(index_list,data):
    data_args = ['srno', 'userid', 'fname', 'lname', 'passw', 'rollno', 'div', 'dept', 'phone', 'isStudent','isAdmin']
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

def check_passw(userid,h_passw,flag):
    user = Models.User(userid=userid)
    uid_response = user.getAUser(flag)
    # print(uid_response)


    if h_passw == uid_response:
        return 200
    else:
        return False

def check_roomno(value,flag):

    roomno = Models.Rooms(value)
    _,status = roomno.getRoom()

    if flag == "get":
        if status == 200:
            return 200
        else:
            return False

    if flag == "post":

        if status == 404: 
            return 200
        else:
            return "Room Already Exists"

    if flag == "delete":

        if status != 404: 
            return 200
        else:
            return "Room Does Not Exists"
        
                            
