from shared.translation import translate


def wich_statistic(lang):
    lst_choice = ["incoming","out","both","exit"]
    print(translate("choice_op",lang))
    while True:
        for ch in lst_choice:
            while True:
                op_choice = input(translate(f"oper_{ch}",lang))
                if op_choice.strip().lower() == "y":
                    return ch
                elif op_choice.strip() == "":
                    break
                else:
                    print(translate("again",lang))
        print(translate("wrong_input1",lang))