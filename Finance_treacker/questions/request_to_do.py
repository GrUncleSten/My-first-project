from shared.translation import translate

def reqest_to_user(lang):
    while True:
        ask = input(translate("ask_to_do",lang))
        if ask.strip().lower() in ("s", "o", "b", "e"):
            return ask
        else:
            print(translate("wrong_input",lang))
