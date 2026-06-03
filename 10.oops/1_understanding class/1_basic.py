#class is the blueprint or template for creating object
#syntax
class Car: #this is the class name Car generally starts from first capital letter 
# there is method and attributes 
# method is just like the function declare inside a class 
# attribute is just creating variable in the class
    brand="tata"# this is the attribute
    model="asdf"
    
    def name(self): #this is a method
        print("hello")
    print("hello how are you ")
#access the attributes and method 
print(Car().brand)
Car().name

# we can make object by making it inside the variable
obj=Car
print(obj.brand)
print(obj.model)