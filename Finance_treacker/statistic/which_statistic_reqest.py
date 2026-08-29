from shared.translation import translate
from shared.date import datemark

            
def which_statistic(lang):
    categories = ["food","car", "education", "wear", "fun","homehold", "other", "salary", "refill", "side_job"]
    while True:
        try:
            ask_s = int(input(translate("Wich_statistic", lang)))
            if ask_s in (1,2,3):
                break
            else:
                print(translate("again", lang))
        except ValueError:
            print(translate("integer_error", lang))
    if ask_s == 1:
        return None, None, None, 1
    elif ask_s == 2:
        while True:
            des = input(translate("want_start_date", lang))
            if des.lower().strip() == "y":
                start = datemark(lang)
                break
            elif des.lower().lower() == "":    
                start = None
                break
            else:
                print(translate("wrong_input", lang))  
        while True:
            des1 = input(translate("want_end_date", lang))
            if des1.lower().strip() == "y":
                end = datemark(lang)
                break
            elif des1.lower().strip() == "":    
                end = None
                break
            else:
                print(translate("wrong_input", lang))
        return start, end, None, 2
    else:
        while True:
            design = input(translate("want_start_date", lang))
            if design.lower().strip() == "y":
                start = datemark(lang)
                break
            elif design.lower().lower() == "":    
                start = None
                break
            else:
                print(translate("wrong_input", lang))  
        while True:
            design1 = input(translate("want_end_date", lang))
            if design1.lower().strip() == "y":
                end = datemark(lang)
                break
            elif design1.lower().strip() == "":    
                end = None
                break
            else:
                print(translate("wrong_input", lang))       
    print(translate("choice_category", lang))
    while True:   
        for one in categories: 
            while True:   
                choice = input(f"{one}:  ")
                if choice.lower().strip() == "y":
                    return start, end, one, 3
                elif choice.strip() == "":
                    break
                else:
                    print(translate("again", lang))       
        print(translate("choice_one_category", lang))        

                    

