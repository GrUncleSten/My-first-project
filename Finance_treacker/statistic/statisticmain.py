from statistic.which_statistic_reqest import which_statistic
from statistic.statistic_by_date import statistic_by_date


def main_statistic(lst):
    wich_st_answ = which_statistic()
    if wich_st_answ[3] == 1:
       my_stat = statistic_by_date(lst,None,None)
       return my_stat
    elif wich_st_answ[3] == 2:
       start = wich_st_answ[0]
       end = wich_st_answ[1]
       my_stat = statistic_by_date(lst,start,end)
       return my_stat
    else:
       return None
        
    


