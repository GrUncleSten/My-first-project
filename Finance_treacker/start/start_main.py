from pathlib import Path

from questions.choice import choice
from shared.read_file import read_file
from shared.write_in_file import write_in_file
from start.first_start import first_start
from start.start import start


def start_main(filename):
    isfile = start(filename)

    if isfile == "Ok":
        lst = read_file(filename)
        return lst

    elif isfile == "First start":
        lst = first_start()
        write_in_file(filename, lst)
        return lst

    else:
        next_step = choice()
        if next_step == 2:
            lst = first_start()
            write_in_file(filename, lst)
            return lst
        else:
            while True:
                source_path =  Path(input("Please enter the path to the file:  "))
                source_file = start(source_path)
                if source_file == "Ok":
                    lst = read_file(source_path)
                    write_in_file(filename, lst)
                    return lst
                else:
                    print("Wrong path to the file. Please try again.")




                


    
