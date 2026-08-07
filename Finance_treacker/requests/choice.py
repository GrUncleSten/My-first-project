def choice():
    while True:
        try:
            user_choice = int(input("Please make your choice: 1 - import file; 2 - new file. Your choice:"))          
            if user_choice not in (1,2):
                print("It must be 1 or 2!") 
                continue
            return user_choice
        except ValueError:
            print("It must be an integer!")

           

            