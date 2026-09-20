# a=1/0
# try:
#     print(a)
# except ZeroDivisionError:
#     print("you can not divide any number by 0")
# print("hello World",end=".",sep=",")
# count = 0
# for letter in 'Snow!':
#     print( 'Letter #', count, 'is', letter)
#     count += 1
# a=int(3)
# b=float(a)
# a=float(a)
# print(type(b))
# print(type(a)) 
a=[1,2,3,4,5]
d={1:"one",2:"two"}
# b=[1,2,3,4,5]
# b=a
# print(a is b)
# print(id(a))
# print(1 in a )
# print(d.get(3))
# d.setdefault(2,"three")
# d.setdefault(5,"five")
# print(d)


with open("createfile.txt",'a') as file:
    file.write("hello this file is created")
    file
import os
os.remove("createfile")