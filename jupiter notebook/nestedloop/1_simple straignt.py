def main(): 
    print_column(3)
    print_row(3)
    print_square(4)
def print_column(height):
    print("#\n"*height, end="")
    # for _ in range(height):
    #     print("#")

def print_row(width):
    print("?"*width,end="")

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("*",end=" ")
        print()
main()