from statistic_new.search_by_date import search_date
from statistic_new.sort_by_type import sort_operations
from statistic_new.sort_by_category import sort_operations_by_categories


def prepare_st(lst,type,start=None,end=None,category=None):
    time_cut = search_date(lst,start=start,end=end)
    if type == "exit":
        return "exit"
    elif type == "incoming":
        tmp = sort_operations(time_cut)["pr"]
    elif type == "out":
        tmp = sort_operations(time_cut)["ds"]
    elif type == "both":
        tmp = time_cut     
    final_st = sort_operations_by_categories(tmp,category=category)
    return final_st     