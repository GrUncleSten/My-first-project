from Shared.Date import datemark

def first_start():
    while True:
        try:
            balance = float(input("Enter your balance: "))
            break
        except ValueError:
            print("It must be an integer!")
    date = datemark()        
    first_operation = [{"id":0,"day": date,"type":"in","refill":balance}]
    return first_operation

