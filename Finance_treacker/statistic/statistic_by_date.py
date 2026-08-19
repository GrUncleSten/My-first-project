from statistic.search_by_date import search_date
from statistic.sort_by_type import sort_operations
from statistic.summing_up import summing


def statistic_by_date(lst, start = None, end = None):
    time_cut = search_date(lst,start,end)
    come_in, come_out = sort_operations(time_cut)
    sum_in = summing(come_in)
    sum_out = summing(come_out) * (-1)
    return time_cut, come_in, come_out, sum_in, sum_out