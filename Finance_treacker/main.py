from operations.operations_main import operations_main
from prepare import prepare
from questions.request_to_do import reqest_to_user
from shared.write_in_file import write_in_file
from start.start_main import start_main
from statistic.balance import balance
from statistic.statisticmain import main_statistic


def main():
    print("Welcome to the budget manager!")
    while True:
        filiname = prepare()
        operations = start_main(filiname)
        answ = reqest_to_user()
        if answ.strip().lower() == "o":
            operations = operations_main(operations)
            write_in_file(filiname, operations)
        elif answ.strip().lower() == "s":
            my_statistic = main_statistic(operations)
            for operation in my_statistic[0]:
                print("")
                print(operation, end="\n")
            print(f"Spend on curent category, on curent period - {my_statistic[1]}")
            print("")
            print(f"Your balance is: {balance(operations)}")
        elif answ.strip().lower() == "b":
            print(f"Your balance is: {balance(operations)}")
        elif answ.strip().lower() == "e":
            write_in_file(filiname, operations)
            print("Goodbye!")
            return    
if __name__ == "__main__":
    main()