from shared.date import datemark
from shared.translation import translate 


def first_start(lang):
    while True:
        try:
            balance = float(input(translate("enter_balance", lang)))
            break
        except ValueError:
            print(translate("integer_error", lang))
    date = datemark(lang)        
    first_operation = [{"id":0,"day": date,"type":"in","refill":balance}]
    return first_operation

