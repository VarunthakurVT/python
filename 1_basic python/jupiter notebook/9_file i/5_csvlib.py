import csv
students=[]
with open("name.csv")as file:
    reader=csv.DictReader(file)
    # for row in reader:
    #     students.append({"name": row[0],"home":row[1]}) another method
    for row in reader:
        students.append({"name":row["name"],"home":row["home"] ,"house":row["house"]})

for student in sorted(students, key=lambda student:student['name']):
    
    print(f"{student['name']} is in {student['home']} house is in {student["house"]}" )
    


print(students[0])