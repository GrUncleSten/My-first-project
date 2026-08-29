from shared.translation import translate 
from questions.cost_request import cost_request
from questions.type_operation import type_operations
from shared.date import datemark
from start.identificator import identificator


def user_request(lst, lang):
    spend = {"food":0, "car":0, "education":0, "wear":0, "homehold":0, "fun":0, "other":0}
    top_up = {"refill":0, "salary":0, "side_job":0}
    ident = identificator(lst) + 1
    day_date = datemark(lang)
    my_type = type_operations(lang)
    if my_type == "out":
        action = cost_request(spend,lang) 
        action["comment"] = input(translate("comment", lang))
        action["id"] = ident
        action["day"] = day_date
        action["type"] = my_type
    else:    
        action = cost_request(top_up,lang)
        action["comment"] = input(translate("comment", lang))
        action["id"] = ident
        action["day"] = day_date
        action["type"] = my_type
    lst.append(action)    
    return lst



