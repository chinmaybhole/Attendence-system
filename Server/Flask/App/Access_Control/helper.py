from App import Models

def check_userid(value,flag):
    user = Models.User(userid= value)
    _,status = user.getAUser() 

    if flag == "get":
        if status ==200: 
            return 200
        else:
            return _

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
        userid = [int(x) for x in str(value)]
        data = [2,2,2]
        if userid[:3] == data:
            return True
        else:
            return False

    if flag == "login":
        if status == 200:
            return True
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
