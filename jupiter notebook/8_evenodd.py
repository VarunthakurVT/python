def main():
    x=int(input("enter a number"))
    if is_even(x):
        print("the number is even")
    else:
        print("the number is odd")
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
main()