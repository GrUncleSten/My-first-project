import json


def write_in_file(filename,inf):
    with open(filename,"w", encoding="utf-8") as f:
        json.dump(inf,f, indent=4)
    return filename    


