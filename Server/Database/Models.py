import datetime

class Users:

    def __init__(self, fname, lname, uid, dept, rollno, phoneno, isStudent, isProfessor,passw=None,id=None):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.passw = passw
        self.uid = uid
        self.dept = dept
        self.rollno = rollno
        self.phoneno = phoneno
        self.isStudent = isStudent
        self.isProfessor = isProfessor

    def __repr__(self):
        return f"Users('{self.fname}','{self.lname}','{self.uid}','{self.dept}','{self.rollno}','{self.phoneno}','{self.isStudent}','{self.isProfessor}')"

class Rooms:
    def __init__(self, roomid,  timein, timeout, id =None, userid=None):
        self.id = id
        self.roomid = roomid
        self.userid = userid
        self.timein = timein
        self.timeout = timeout

    def __repr__(self):
        return f"Room('{self.id}','{self.roomid}','{self.userid}','{self.timein}','{self.timeout}')"

class Logs:
    def __init__(self,userid,roomid,timein,timeout):
        self.userid = userid
        self.roomid = roomid
        self.timein = timein
        self.timeout = timeout

    def __repr__(self):
        return f"Logs('{self.userid}','{self.roomid}','{self.timein}','{self.timeout}')"

def printfun(pdata):


    return f""
