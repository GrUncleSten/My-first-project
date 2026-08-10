from shared.date import datemark

            
def which_statistic():
    categories = ["food","car", "education", "wear", "fun","homehold", "other", "salary", "refill", "side_job"]
    while True:
        try:
            ask_s = int(input("Which statistic do you want to see? "
              "1 -> for all time  "
              "2 -> for some time  "
              "3 -> for category on some time.  Your choice:  "))
            if ask_s in (1,2,3):
                break
            else:
                print("Try again please")
        except ValueError:
            print("It must be an integer!")
    if ask_s == 1:
        return None, None, None
    elif ask_s == 2:
        print("Enter a start date.")
        start = datemark()
        print("Enter a end date.")
        end = datemark()
        return start, end, None 
    else:
        print("Enter a start date.")
        start = datemark()
        print("Enter a end date.")
        end = datemark()
        print("Please, choice the category what do you want. Make your choice with button - Y,  " \
            "if you want not press the Enter")
        while True:   
            for one in categories: 
                while True:   
                    choice = input(f"{one}:  ")
                    if choice.lower().strip() == "y":
                        return start, end, one
                    elif choice.strip() == "":
                        break
                    else:
                        print("Try again please")       
            print("You must choose at least one category!")        

                    

