email=input("Enter your email ")
# if "@" in email and "." in email:
#     print("valid")
# else:
#     print("invalid") to fix the edge cases we do 

username,domain=email.split("@")
if username and domain.endswith(".edu"):
    print("valid")
else:
    print("invalid")