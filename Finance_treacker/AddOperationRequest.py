from Start.Identificator import identificator
from Shared.Date import datemark
from Shared.Read_file import read_file
from Reqests.Type_operation import type_operations
from Reqests.Action_request import action_request





def user_reqeust(filename):
    spend = {"food":0, "car":0, "education":0, "wear":0, "homehold":0, "fan":0, "other":0}
    top_up = {"refill":0, "salary":0, "side_job":0}
    lst = read_file(filename)
    id = identificator(lst) + 1
    day_date = datemark()
    type = type_operations()
    if type == "out":
        action = action_request(spend) 
    else:    
        action = action_request(top_up)
    action["comment"] = input("Enter a comment: ")
    return action,id,day_date


user_reqeust(r"C:\Users\tomas\OneDrive\Desktop\Мои проекты\Finance treacker\data.json")
