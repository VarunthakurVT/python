# with open('names.txt','r') as file:
#     lines=file.readlines()
#     for line in lines:
#         print(f" Hello,{line.rstrip()}")

names=[]
with open('names.txt','r')as file:
    for lines in file:
        names.append(lines.strip())
for name in sorted(names,reverse=True):
    print(f"hello ,{name}")