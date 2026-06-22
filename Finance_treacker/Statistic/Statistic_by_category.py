from Search_by_date import search_date
from Sort_by_category import sort_operations_by_categories
from Summing_up import summing
           


def statistic_by_category(lst,start = None, end = None, category = None):
    time_cut = search_date(lst,start=None,end=None)
    operatons_by_category = sort_operations_by_categories(lst,category)
    sum_category = summing(lst, category = None)
    return time_cut, operatons_by_category, sum_category


