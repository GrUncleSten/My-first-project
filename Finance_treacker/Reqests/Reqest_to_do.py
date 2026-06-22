def reqest_to_user():
    while True:
        try:
            ask = input("What do you want to do? Make your choice - s -> see statistic, o -> to do with operations, a -> see analitic, f -> see forecast."   \
                       "Your choice: ")
            if ask in ("s", "a", "o", "f"):
                return ask
            else:
                print("Try again please")
        except ValueError:
            print("It must be a letter!")
print(reqest_to_user())