def request_operations():
    lst_of_doing = ["Add","Delete","Edit"]
    print("What do you want to do? (Add/Delete/Edit) Press Y for agree with the action, or type 'exit' to quit:  ")
    while True:
        for act in lst_of_doing:
            answer = input(f"{act}:  ")
            if answer.upper() == 'Y':
                return act
            elif answer.lower() == 'exit':
                return None
            elif answer == "":
                continue
            else:
                print("Invalid input. Please try again.")
