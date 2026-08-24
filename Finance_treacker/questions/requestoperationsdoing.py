from shared.translation import translate 


def request_operations(lang):
    lst_of_doing = ["Add","Delete","Edit"]
    print(translate("operation_to_do", lang))
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
                print(translate("wrong_input", lang))
