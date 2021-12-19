class Users:

    def __init__(self, fname, lname, uid, dept, rollno, phoneno, isStudent, isProfessor):
        self.fname = fname
        self.lname = lname
        self.uid = uid
        self.dept = dept
        self.rollno = rollno
        self.phoneno = phoneno
        self.isStudent = isStudent
        self.isProfessor = isProfessor

    def __repr__(self):
        return f"Users('{self.fname}','{self.lname}','{self.uid}','{self.rollno}','{self.phoneno}','{self.isStudent}','{self.isProfessor}')"

class Rooms:
    pass




