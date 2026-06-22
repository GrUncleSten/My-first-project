import os
def start(filename):
    answer = os.path.isfile(filename)
    name, ext = os.path.splitext(filename)
    if answer:
        if ext.lower() == ".json":
            if  os.path.getsize(filename) != 0:
                return "Ok"
            else:
                return "First start"
        else:
            return "Unknown File"
    else:
        return "File not found"        
    
 
