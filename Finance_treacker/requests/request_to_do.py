def reqest_to_user():
    while True:
        ask = input("What do you want to do? Make your choice - s -> see statistic, o -> to do with operations, b -> see balance, e -> exit \n" 
                       "Your choice: ")
        if ask.strip().lower() in ("s", "o", "b", "e"):
            return ask
        else:
            print("Try again please")
