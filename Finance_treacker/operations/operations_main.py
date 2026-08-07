from operations.addoperation import user_request
from operations.deleteoperation import delete_operations
from operations.editoperations import edit_operations
from requests.request_doing import request_operations


def operations_main(operations):
    action = request_operations()
    if action == "Add":
        user_request(operations)
    elif action == "Delete":    
        delete_operations(operations)
    else:
        edit_operations(operations)    
    return operations    
        
    



