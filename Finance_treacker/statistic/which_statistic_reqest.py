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
            print("It must be a number!")
    if ask_s == 1:
        return None, None, None, 1
    elif ask_s == 2:
        des = input("If you want to input a start date press Y, if no, press Enter: ")
        while True:
            if des.lower().strip() == "y":
                start = datemark()
                break
            elif des.lower().lower() == "":    
                start = None
                break
            else:
                print("Try again, wrong input!")
        des1 = input("If you want to input a end date press Y, if no, press Enter: ")  
        while True:
            if des1.lower().strip() == "y":
                end = datemark()
                break
            elif des1.lower().lower() == "":    
                end = None
                break
            else:
                print("Try again, wrong input!")
        return start, end, None, 2
    else:
        design = input("If you want to input a start date press Y, if no, press the Enter: ")
        while True:
            if design.lower().strip() == "y":
                start = datemark()
                break
            elif design.lower().lower() == "":    
                start = None
                break
            else:
                print("Try again, wrong input!")
        design1 = input("If you want to input a end date press Y, if no, press the Enter: ")  
        while True:
            if design1.lower().strip() == "y":
                end = datemark()
                break
            elif design1.lower().lower() == "":    
                end = None
                break
            else:
                print("Try again, wrong input!")       
    print("Please, choice the category what do you want. Make your choice with button - Y,  " \
        "if you want not press the Enter")
    while True:   
        for one in categories: 
            while True:   
                choice = input(f"{one}:  ")
                if choice.lower().strip() == "y":
                    return start, end, one, 3
                elif choice.strip() == "":
                    break
                else:
                    print("Try again please.")       
                    print("You must choose at least one category!")        

                    

