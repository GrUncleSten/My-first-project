from shared.translation import translate

def cost_request(dct,lang):
    for key in dct:
        while True:
            answer = input(translate(f"category_{key}", lang))
            if answer.strip() == "":
                dct[key] = 0
                break
            try:
                value = float(answer)
                dct[key] = value
                if dct[key] >= 0:
                    break
                else:
                    print(translate("number_error", lang))
            except ValueError:
                print(translate("integer_error", lang))
    return dct            
