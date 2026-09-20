try:
    for _ in range(1,10000):
        print("anything")
    print(1/0)
except (ZeroDivisionError,KeyboardInterrupt):
    print("zeroDivision error")