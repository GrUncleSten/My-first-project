
def start(filename): 
    if filename.is_file():
        if filename.suffix.lower() == ".json":
            if filename.stat().st_size != 0:
                return "Ok"
            else:
                return "First start"
        else:
            return "Unknown File"
    else:
        return "File not found"         
    
 
