import csv
name=input("enter your name ")
home=input("enter your home ")
house=input("enter your house ")
with open("name.csv",'a') as file:
    # file.write(input("Enter the name place and where is your house",sep=','))
    writer=csv.DictWriter(file,fieldnames=["name","home","house"])
    writer.writerow({"name":name,"home":home,"house":house})
