from Shared.Date import datemark


def delete_operations(lst):
    day_delete = datemark()
    candidates = []
    for operation in lst:
        if operation["day"] == day_delete:
            candidates.append(operation)
    if not candidates:
        print("No operations found for this date!")
        return lst        
    print("Choose the operation, which do you want to delete from this list. " \
        "Make your choice with button -> Y, if you want not, press the Enter")    
    for item in candidates:
        while True:
            deleted = input(f"This one {item}?: ")
            if deleted.strip().lower() == "y":
                lst.remove(item)
                return lst
            elif deleted.strip() == "":
                break
            else:
                print("Wrong input, try again!")
                