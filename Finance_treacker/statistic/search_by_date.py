def search_date(lst,start=None,end=None):
    on_date_operations = []
    for item in lst:
        if start is not None and end is not None:
            if start <= item["day"] <= end:
                on_date_operations.append(item)
        elif start is not None:
            if start <= item["day"]:
                on_date_operations.append(item)                      
        elif end is not None:
            if item["day"] <= end:
                on_date_operations.append(item)            
        else:
            on_date_operations.append(item)
    return on_date_operations    