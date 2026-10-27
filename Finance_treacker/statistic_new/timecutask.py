from shared.translation import translate
from shared.date import datemark


def time_cut_ask(lang):
    while True:
        design_start = input(translate("want_start_date", lang))
        if design_start.strip().lower() == "y":
            start = datemark(lang)
            break
        elif design_start.strip() == "":
            start = None
            break
        else:
            print(translate("again",lang))
    while True:
            design_end = input(translate("want_end_date", lang))
            if design_end.strip().lower() == "y":
                end = datemark(lang)
                break
            elif design_end.strip() == "":
                end = None
                break
            else:
                print(translate("again",lang))
    return start,end
                