from shared.translation import translate 


def datemark(lang):
    while True:
        try:
            year = int(input(translate("enter_year",lang)))
            month = int(input(translate("enter_month",lang)))
            day = int(input(translate("enter_day",lang)))
            if (0 < month <= 12) and (0 < day <= 31):
                if (month in (4,6,9,11) and day > 30) or (month == 2 and day > 28):
                    print(translate("date_error",lang))
                else:
                    break
            else:
                print(translate("date_error",lang))
        except ValueError:
            print(translate("integer_error", lang))
    return f"{year:04d}-{month:02d}-{day:02d}"                      

