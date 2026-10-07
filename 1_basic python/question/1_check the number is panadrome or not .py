a=342
check=a
rev=0
while a>0:
    rev=rev*10+a%10
    a= a//10
    
print(rev)
if(rev==a):
    print(f"{check} is padrone number ")
else:
    print(f"{check} is not padrone number")