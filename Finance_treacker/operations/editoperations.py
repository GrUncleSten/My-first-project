from shared.date import datemark


def edit_operations(lst):
    edited_date = datemark()
    candidates = []
    for operation in lst:
        if operation["day"] == edited_date:
            candidates.append(operation)
    if not candidates:
        print("No operations was found for this date!")
        return lst        
    print("which category of operation you want to edit? " \
            "If you will see that one - press -> Y, if you want to pass, press the Enter")
    for item in candidates:
        for key in item:
            if key in("id","comment","type","day"):
                continue
            else:
                while True:
                    answer = input(f"{key}: ")
                    if answer.strip().lower() == "y":
                        try:
                            item[key] = float(input("Enter a new value: "))
                            return lst
                        except ValueError:
                            print("It must be a number!") 
                    elif answer.strip() == "":
                        break   
                    else:
                        print("Wrong input, try again!")    
    return lst                           
                    