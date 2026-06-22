from Start import start
from First_start import first_start
from Shared.Read_file import read_file
from Reqests.Choice import choice

                  

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

    
