student=[]
with open("name.csv") as file:
    for line in file:
        name,house=line.rstrip().split(',')
        # student={}
        # student={"name":name}
        # student={"house":house}
        #the shorthand
        students={'name':name,'house':house}
        student.append(students)

def get_name(students):
    return students['name']
# for student in sorted(student, key=get_name):
for student in sorted(student, key=lambda student:student["name"]):

    print(f"{student['name']} is in {student['house']}")
    #     names.append(f"{name} is in {house}")
    # for name in sorted(names):
    #     print(name)