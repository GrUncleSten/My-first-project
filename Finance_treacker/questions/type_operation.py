from shared.translation import translate 


def type_operations(lang):
    while True:
        try:
            type = input(translate("type_operations", lang))
            if type not in ("in","out"):
                print(translate("type_of_operation_error", lang))
            else:
                return type
        except ValueError:
            print(translate("type_of_operation_error", lang))
    