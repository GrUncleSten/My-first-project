from operations.operations_main import operations_main
from prepare import prepare
from requests.request_to_do import reqest_to_user
from shared.write_in_file import write_in_file
from start.start_main import start_main
from statistic.balance import balance


def main():
    print("Welcome to the budget manager!")
    filiname = prepare()
    operations = start_main(filiname)
    answ = reqest_to_user()
    if answ.strip().lower() == "o":
        operations_main(operations)
    elif answ.strip().lower() == "s":
        print("Statistic is not implemented yet") 
        print(f"Your operations -\n{chr(10).join(str(op) for op in operations)}")
    elif answ.strip().lower() == "b":
        print(f"Your balance is: {balance(operations)}")
    elif answ.strip().lower() == "e":
        print("Goodbye!")
        return    
    write_in_file(filiname, operations)
    print(f"Your balance is: {balance(operations)}") 
 
if __name__ == "__main__":
    main()