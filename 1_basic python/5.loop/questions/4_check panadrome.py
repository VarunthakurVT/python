a=int(input("Enter the number "))
copy=a
rev=0
while a>0:
    rev=rev*10+a%10
    a=a//10
if(rev==copy):
    print(rev,"is panadrome number")
else:
    print("not a panadrome number",rev) 