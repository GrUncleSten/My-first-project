from shared.translation import translate


def wich_period(lang):
    while True:
            ask_s = input(translate("wich_statistic", lang))
            if ask_s  not in ("1","2","3"):
                print(translate("integer_error",lang))
                while True:
                    to_exit = input(translate("ask_to_return", lang))
                    if to_exit.strip().lower() == "y":
                        return "exit"
                    elif to_exit.strip().lower() == "n":
                        break              
            else:
                return int(ask_s)        
          