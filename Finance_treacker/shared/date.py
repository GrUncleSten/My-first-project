def datemark():
    while True:
        try:
            month = int(input("Enter a month: "))
            day = int(input("Enter a day: "))
            year = int(input("Enter a year: "))
            if (0 < month <= 12) and (0 < day <= 31):
                if (month in (4,6,9,11) and day > 30) or (month == 2 and day > 28):
                    print("Try again to enter wright month and day!")
                else:
                    break
            else:
                print("Try again to enter wright month and day!")
        except ValueError:
            print("It must be an integer!")
    return f"{year}-{month}-{day}"                        

