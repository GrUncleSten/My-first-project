from operations.operations_main import operations_main
from prepare import prepare
from questions.request_to_do import reqest_to_user
from shared.write_in_file import write_in_file
from start.start_main import start_main
from statistic_new.balance import balance
#from statistic.statisticmain import main_statistic
from shared.ask_language import choice_lang
from shared.translation import translate
from statistic_new.statisticmain import statistic_main
from shared.goback import go_back


def main():
    lang = choice_lang()
    print(translate("welcome", lang))
    filiname = prepare()
    operations = start_main(filiname,lang)
    while True:
        answ = reqest_to_user(lang)
        curent_balance = balance(operations) 
        if answ.strip().lower() == "o":
            operations = operations_main(operations,lang)
            write_in_file(filiname, operations)
        elif answ.strip().lower() == "s":
            my_statistic = statistic_main(operations,lang)
            if my_statistic == "exit":
                if go_back(lang) == "exit":
                    print(translate("Goodbye",lang))
                    return 
            print(my_statistic)
            print(translate("balance",lang,balance = curent_balance))
        elif answ.strip().lower() == "b":
            print(translate("balance",lang,balance = curent_balance))
        elif answ.strip().lower() == "e":
            write_in_file(filiname, operations)
            print(translate("Goodbye",lang))
            return    
if __name__ == "__main__":
    main()


   