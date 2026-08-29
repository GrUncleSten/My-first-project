from operations.addoperation import user_request
from operations.deleteoperation import delete_operations
from operations.editoperations import edit_operations
from questions.requestoperationsdoing import request_operations


def operations_main(operations,lang):
    action = request_operations(lang)
    if action == "Add":
        user_request(operations,lang) 
    elif action == "Delete":    
        delete_operations(operations,lang)
    elif action == "Edit":
        edit_operations(operations,lang)
    elif action is None:
        return operations 
    return operations      
       
        
    



