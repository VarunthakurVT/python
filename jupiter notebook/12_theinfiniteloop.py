
while True:
    try:
        n = int(input("Enter the number of items: "))
        if n > 0:
            break
        else:
            print("Quantity must be greater than 0.")
    except ValueError:
        # This catches non-integer inputs like text or symbols
        print("Invalid input. Please enter a whole number.")

for _ in range(n):
    # Real world: Generate ticket, create user, process file, etc.
    print("Action executed")