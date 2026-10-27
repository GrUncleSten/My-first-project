from shared.translation import translate


def wich_category(type,lang):
    out_category = ["food","car","wear","fun","homehold","other","education"]
    in_category = ["salary","refill","side_job"]
    if type == "incoming":
        my_categories = in_category
    elif type == "out":
        my_categories = out_category
    while True:
        for one in my_categories:
            while True:
                choice = input(translate(f"category_{one}: ",lang))
                if choice.strip().lower() == "y":
                    return one
                elif choice.strip() == "":
                    break
                else:
                    print(translate("again", lang))
        while True:
            to_exit = input(translate("ask_to_return", lang))
            if to_exit.strip().lower() == "y":
                return "exit"
            elif to_exit.strip().lower() == "n":
                break  
            else:
                print(translate("again",lang))
    



    
