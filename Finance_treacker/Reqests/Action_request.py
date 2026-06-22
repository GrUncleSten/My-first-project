def action_request(dct):
    for key in dct:
        while True:
            try:
                dct[key] = float(input(f"For{key}: "))
                break
            except ValueError:
                print("It ust be an integr!")
    return dct            
