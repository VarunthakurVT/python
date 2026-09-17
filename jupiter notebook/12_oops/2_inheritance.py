class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def __str__(self):
        return f"{self.fname}{self.lname}"

class student(person):
    def __init__(self, fname, lname):
        person.__init__(self, fname, lname)
