def cost_request(dct):
    for key in dct:
        while True:
            answer = input(f"for {key}:  ")
            if answer.strip() == "":
                dct[key] = 0
                break
            try:
                value = float(answer)
                dct[key] = value
                if dct[key] >= 0:
                    break
                else:
                    print("It must be a non-negative number!")
            except ValueError:
                print("It must be a number!")
    return dct            
