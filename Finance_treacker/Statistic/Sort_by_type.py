def sort_operations(lst):
    profit = []
    discharge = []
    for item in lst:
        if  item["type"] == "in":
            profit.append(item)
        else:
            discharge.append(item)
    return profit, discharge                