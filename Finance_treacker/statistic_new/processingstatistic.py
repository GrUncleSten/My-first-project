from shared.translation import translate


def processing(data,lang,category=None):
    if len(data) == 0:
        print(translate("empty_lst",lang))
        return
    sorted_data = sorted(data, key=lambda item: item["day"])
    statistic = {}
    count = len(data)
    start = sorted_data[0]["day"]
    end = sorted_data[count - 1]["day"]
    if category is None:
        op = translate('op_many', lang)
        for item in sorted_data:
            for key in item:
                if key not in ("day","type","id","comment"):
                    statistic[translate(f"category_{key}: ",lang)] = statistic.get(translate(f"category_{key}: ",lang), 0) + item[key]
        param = {"start":start, "end":end, "statistic":statistic,"count":count,"op":op }  
    else:
        op = translate('op_1st',lang)
        for item in sorted_data:
            for key in item:
                if key == category:
                    statistic[translate(f"category_{key}: ",lang)] = statistic.get(translate(f"category_{key}: ",lang), 0) + item[key]
        param = {"start":start, "end":end, "statistic":statistic,"count":count,"op":op }            
    output = translate("output_st",lang,**param)
    return output            