from shared.translation import translate
from shared.date import datemark


def edit_operations(lst, lang):
    edited_date = datemark(lang)
    candidates = []
    for operation in lst:
        if operation["day"] == edited_date:
            candidates.append(operation)
    if not candidates:
        print(translate("operations_on_date", lang))
        return lst        
    print(translate("wich_operation_edit", lang))
    for item in candidates:
        for key in item:
            if key in("id","comment","type","day"):
                continue
            else:
                while True:
                    answer = input(f"{key}: ")
                    if answer.strip().lower() == "y":
                        try:
                            item[key] = float(input(translate("new_value", lang)))
                            return lst
                        except ValueError:
                            print(translate("integer_error", lang)) 
                    elif answer.strip() == "":
                        break   
                    else:
                        print(translate("wrong_input", lang))    
    return lst                           
                    