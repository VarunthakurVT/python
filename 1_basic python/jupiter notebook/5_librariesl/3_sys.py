import sys
# try:
#     print("hello my name is",sys.argv[1])
# except IndexError:
#     print("too few args....")
if len(sys.argv)>2:
   sys.exit("there are too many args")
elif len(sys.argv)<2:
   sys.exit("there are less args atleast give one arg")
else:
    print("my name is :",sys.argv[1])
