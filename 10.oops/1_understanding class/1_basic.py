#class is the blueprint or template for creating object
#syntax
class Car:
# there is method and attributes 
# method is just like the function declare inside a class 
# attribute is just creating variable in the class
    brand="tata" #this is method
    def name(self):
        print("hello")
    print("hello how are you ")
#access the attributes and method 
print(Car().brand)
Car().name