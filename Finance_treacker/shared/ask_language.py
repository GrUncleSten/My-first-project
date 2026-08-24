def choice_lang():
    choice_lang = input("Please choice your language, if you want English, press E./Выберите язык, если вы хотите выбрать Русский, нажмите R:  ")
    while True:
            if choice_lang.lower().strip() == "e":
                return "English"
            elif choice_lang.lower().strip() == "r":
                return "Russian"
            else:
                 print("Wrong input, try again /Неправильный ввод, попробуйте снова")
                 