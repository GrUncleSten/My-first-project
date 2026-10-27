from shared.translation import translate


def go_back(lang):
    while True:
        to_exit = input(translate("ask_to_return", lang))
        if to_exit.strip().lower() == "y":
            return "exit"
        elif to_exit.strip().lower() == "n":
            return "go_on"       
        else:
            print(translate("again",lang)) 