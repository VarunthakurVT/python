#list data type is defined using the square brackets []
list=[23,34,45,56,67,56,34,"hello"]
#list are mutable 
#in list we can have same values
#list elements can be accessed using the index value;
#in list we can store multiple data types values
print(list[0]) #this is the list indexing
print(list[1:4])#this is the list slicing
for i in range(len(list)):
    print(list[i])

for i in list:
    print(i)