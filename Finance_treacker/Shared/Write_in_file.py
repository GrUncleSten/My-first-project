import json
def write_in_file(filename,inf):
    with open(filename,"w") as f:
        json.dump(inf,f)
    return filename    


