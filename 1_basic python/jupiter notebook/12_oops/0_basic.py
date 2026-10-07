class anything:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
r1=anything("abc")
print(r1)