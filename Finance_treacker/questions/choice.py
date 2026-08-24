from shared.translation import translate

def choice(lang):
    while True:
        try:
            user_choice = int(input(translate("choice_file",lang)))          
            if user_choice not in (1,2):
                print(translate("error_choice",lang)) 
                continue
            return user_choice
        except ValueError:
            print(translate("integer_error",lang))

           

            