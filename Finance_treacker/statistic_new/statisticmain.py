from statistic_new.wichperiod import wich_period
from statistic_new.wichstatisticask import wich_statistic
from statistic_new.preparestatistic import prepare_st
from statistic_new.processingstatistic import processing
from statistic_new.timecutask import time_cut_ask
from statistic_new.wichcategory import wich_category
from shared.translation import translate
from shared.goback import go_back



def statistic_main(lst,lang):
    while True:
        kind_st = wich_period(lang)
        if kind_st == "exit":
            if go_back(lang) == "exit":
                return "exit"
        elif kind_st == 1:
            while True:
                type = wich_statistic(lang)
                if type == "exit":
                    if go_back(lang) == "exit":
                        return "exit"
                else:        
                    my_st = prepare_st(lst,type,start=None,end=None,category=None)
                    statistic = processing(my_st,lang,category=None)
                    return statistic
        elif kind_st == 2:
            while True:
                type = wich_statistic(lang)
                if type == "exit":
                    if go_back(lang) == "exit":
                        return "exit"
                else:        
                    start,end = time_cut_ask(lang)
                    my_st = prepare_st(lst,type,start=start,end=end,category=None)
                    statistic = processing(my_st,lang,category=None)
                    return statistic
        elif kind_st == 3:
            while True:
                type = wich_statistic(lang)
                if type == "exit":
                    if go_back(lang) == "exit":
                        return "exit"
                elif type == "both":
                    print(translate("wrong_type",lang))
                    continue
                else:
                    start,end = time_cut_ask(lang)
                    while True:
                        category = wich_category(type,lang)
                        if category == "exit":
                            if go_back(lang) == "exit":
                                return "exit"
                        else:                 
                            my_st = prepare_st(lst,type,start=start,end=end,category=category)
                            statistic = processing(my_st,lang,category=category)
                            return statistic                     
