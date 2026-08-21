from statistic.search_by_date import search_date
from statistic.sort_by_category import sort_operations_by_categories
from statistic.summing_up import summing


def statistic_by_category(lst,start = None, end = None, category = None):
    time_cut = search_date(lst,start=start,end=end)
    operatons_by_category = sort_operations_by_categories(time_cut,category = category)
    sum_category = summing(operatons_by_category, category = category)
    return  operatons_by_category, sum_category


