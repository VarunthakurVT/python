n = int(input("Enter the number for table "))
a = 1
for i in range(n, n*11, n):  
    print(f"{n} X {a} = {i}")
    a += 1
