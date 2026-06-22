def summing(lst, category = None):
    total = 0 
    for element in lst:
        for key,value in element.items():
            if category is None:
                if key in ("id","day","type","comment"):
                    continue
                else:
                    total += value
            else:
                if key != category:
                    continue
                else:
                    total += value
    return total                        