import re
email=input("Enter your email ")
if re.search(r"^.+@.+\.edu$",email):
    print("valid")
else:
    print("invalid")

# import time
# print("loding.." ,flush=True)
# time.sleep(2)
# print("hello ")