name=str(input("Enter the name "))
match name:
    case "varun":
        print("khanyari")
    case "abc"|"qwe":
        print("xyz")
    case _:
        print("who")