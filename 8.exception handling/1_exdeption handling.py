#there are errors--like mistakes you do in the code like --logical error and syntax error..
# but there is also exception error like
a=int(input("enter the number"))
#print(10/a) if we do in this divide by zero then it will give the error due to this error the next line will not print 
#to resolve this we use the exception handling 
#there is like try and expect keyword
try:
    print(10/a)
except Exception as err: #we can also use the Zero Division Error.in the exception as err we can resolve all error 
#arr we can say the variable
    print(f"There is an error called {err}")
    #by this stuff we can resolve the error 
else: #this run when there is no exception in the code 
    print("good there is no exception error")
finally: #in this it run if there is any exception 
    print("I will run no matter what")

print("hello")
try:
    age=int(input("Enter your age:"))
    if age>12&age<18:
        print("Welcome to the club")
    else: 
        raise ValueError("you must between 12 and 18") #raise keyword is used to create your own error
except Exception as err:
    print(f"the earr is {err}")
print("the club will be start soon ")

