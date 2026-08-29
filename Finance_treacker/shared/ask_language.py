def choice_lang():
    while True:
        choice = input("Please choose your language, if you want English, press E./Выберите язык, если вы хотите выбрать Русский, нажмите R:  ")
        if choice.lower().strip() == "e":
            return "English"
        elif choice.lower().strip() == "r":
            return "Russian"
        else:
            print("Wrong input, try again /Неправильный ввод, попробуйте снова")
                