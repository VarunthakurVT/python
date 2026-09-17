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
# b=[1,2,3,4,5]
b=a
print(a is b)
print(id(a))