from shared.translation import translate
from shared.date import datemark


def delete_operations(lst,lang):
    day_delete = datemark(lang)
    candidates = []
    for operation in lst:
        if operation["day"] == day_delete:
            candidates.append(operation)
    if not candidates:
        print(translate("operations_on_date", lang))
        return lst        
    print(translate("choice_delete_optration", lang))    
    for item in candidates:
        while True:
            deleted = input(translate("this_one", lang, item = item))
            if deleted.strip().lower() == "y":
                lst.remove(item)
                return lst
            elif deleted.strip() == "":
                break
            else:
                print(translate("wrong_input", lang))
                