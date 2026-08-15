from statistic.which_statistic_reqest import which_statistic
from statistic.statistic_by_date import statistic_by_date


def main_statistic(lst):
    wich_st_answ = which_statistic()
    if wich_st_answ[3] == 1:
       my_satat = statistic_by_date(lst,None,None)
       return my_satat
    else:
        return None
        
    


