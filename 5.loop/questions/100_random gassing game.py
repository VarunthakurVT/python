import random
num=random.randint(1,10)
tries=0
while True:
     guess=int(input("Guess number "))
     if guess==num:
         tries=tries+1
         print(f"your number is correct your take {tries} tries")
         break
     elif(guess>num):
         print("go little lower")
         tries=tries+1
     elif(guess<num):
         print("guess little bigger")
         tries=tries+1
         
     else:
         print("your guess number is wrong ")
         tries=tries+1


