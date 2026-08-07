def type_operations():
    while True:
        try:
            type = input("Choice the type of your operation: in => charge, out => spend. Your choice: ")
            if type not in ("in","out"):
                print("Enter correct type of operation!")
            else:
                return type
        except ValueError:
            print("Enter correct type of operation!")
    