from operations.operations_main import operations_main
from prepare import prepare
from questions.request_to_do import reqest_to_user
from shared.write_in_file import write_in_file
from start.start_main import start_main
from statistic.balance import balance
from statistic.statisticmain import main_statistic
from shared.ask_language import choice_lang
from shared.translation import translate


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
            my_statistic = main_statistic(operations,lang)
            for operation in my_statistic[0]:
                print("")
                print(operation, end="\n")
            #print(translate("spend_on_category",lang, my_statistic = balance(my_statistic[1])))
            print("")
            print(translate("balance",lang,balance = curent_balance))
        elif answ.strip().lower() == "b":
            print(translate("balance",lang,balance = curent_balance))
        elif answ.strip().lower() == "e":
            write_in_file(filiname, operations)
            print(translate("Goodbye",lang))
            return    
if __name__ == "__main__":
    main()


   