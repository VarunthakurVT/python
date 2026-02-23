a=[23,34,32,23,43,556,76,78,56,32]
a.append("varun") #insert the element at the last of the list 
print(a)
a.insert(0,100) #insert element via index
print(a)
a.remove(23)#first 23 remove
print(a)
a.pop(1)#remove element via index
print(a)

a.sort #arrange in ascending order
print(a)
newlist=a.copy #creates copy of the list
print(newlist)
a.clear()#remove all the elements of the list a 
print(a)