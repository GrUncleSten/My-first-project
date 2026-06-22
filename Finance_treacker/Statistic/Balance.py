from Statistic_by_date import statistic_by_date

def balance(lst):
    inf = statistic_by_date(lst, start = None, end = None)
    in_operations = inf[3] 
    out_operations = inf[4]
    now_balance = in_operations + out_operations
    return now_balance