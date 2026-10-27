from statistic_new.sort_by_type import sort_operations
from statistic_new.summing_up import summing




def balance(lst):
    in_ = summing(sort_operations(lst)["pr"])
    out = summing(sort_operations(lst)["ds"]) * (-1)
    balance_now = in_ + out
    return balance_now