from pathlib import Path

from shared.translation import translate
from questions.choice import choice
from shared.read_file import read_file
from shared.write_in_file import write_in_file
from start.first_start import first_start
from start.start import start


def start_main(filename,lang):
    isfile = start(filename)

    if isfile == "Ok":
        lst = read_file(filename)
        return lst

    elif isfile == "First start":
        lst = first_start(lang)
        write_in_file(filename, lst)
        return lst

    else:
        next_step = choice(lang)
        if next_step == 2:
            lst = first_start(lang)
            write_in_file(filename, lst)
            return lst
        else:
            while True:
                source_path =  Path(input(translate("path", lang)))
                source_file = start(source_path)
                if source_file == "Ok":
                    lst = read_file(source_path)
                    write_in_file(filename, lst)
                    return lst
                else:
                    print(translate("wrong_pass", lang))




                


    
