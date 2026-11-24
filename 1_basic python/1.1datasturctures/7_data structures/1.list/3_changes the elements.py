a=[23,34,32,23,43,556,76,78,56,32]
#a[3]="varun " #this changes the elements in the index 3
#print(a)
greatest=a[0]
for i in range(len(a)):
    if(a[i]>greatest):
        greatest=a[i]
print(greatest)