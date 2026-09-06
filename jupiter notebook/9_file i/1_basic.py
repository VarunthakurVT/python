name=input("enter your name ")
# for _ in range(3):

#     names.append(input("enter your name"))
# for name in sorted(names):
#     print(f"hello {name}")

# file=open('names.txt','a')
# file.write(f"{name}\n")
# file.close() there is another way 

with open ("names.txt",'a') as file:
    file.write(f"{name}")
#  to read file do this
# with open ("names.txt",'r') as file:
#     lines=file.readlines()
#     for line in lines:
#         print(f"hello{line}")