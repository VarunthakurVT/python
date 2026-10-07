class Factory:
    a=34 #this is the attribute
    def hello(self):
        print("hello") #this is the method

print(Factory().a)
Factory().hello()