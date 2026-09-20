def main():   
    a=get_int("what's x ")
    print(f"x is {a}")
def get_int(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:  #you can give the multiple exception at same time 
                
                print(" \n enter the integer value")
            except KeyboardInterrupt:
                 print(" \n not press ctrl + c")
            
main()