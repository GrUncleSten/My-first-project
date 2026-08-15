from start.start import start
from start.first_start import first_start
from shared.read_file import read_file
from requests.choice import choice

                  

def start_main():
    while True:
        filename = input("Please enter the path to the file:  ")
        is_file = start(filename)
        if is_file == "Ok":
            lst = read_file(filename)
            return lst
        elif is_file == "First start":
            lst = first_start()
            return lst
        else:
            next_step = choice()
            if next_step == 2:
                lst = first_start()
                return lst
            else:
                print("Try again enter a new path to the file")
print(start_main())                

    
