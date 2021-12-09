# import functionality from bios.py
from bios import time, os, sys, typingPrint, typingInput, clearScreen 
from datetime import datetime, date
# from datetime import date
    
# start program
def start():
    typingPrint("\nHello, my name is kc. What is your name ?\n")
    print("")
    
    user_input = input(">")

    typingPrint("\nHello " + user_input + " It's nice to meet you.")
    main()

def main():
    typingPrint("\nType 'h' for help menu, or 'exit' to close program.\n")
    print("")

    user_input = input(">")

    if user_input == "h":
        help()
    elif user_input == "exit":
        typingPrint("Goodbye!!!")
        exit
    else:
        print("Im sorry, that is not a valid option.")
        main()
    
def help():
    print("\nHELP MENU")
    print("\ntime - view current time")
    print("\ndate - view todays date")
    print("")

    user_input = input(">")

    if user_input == "time":
        time_function()
    elif user_input == "date":
        date_function()
    else:
        print("Im sorry, I dont seem to understand what your saying.")
        help()

def time_function():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    typingPrint("\nThe time is currently ")
    typingPrint(current_time)
    print("")
    main()

    
def date_function():
    # creating the date object of todays date
    todays_date = date.today()

    # print todays date
    typingPrint("Current date:")
    print(todays_date)

    # fetching the current year, month and day of today
    typingPrint("Current year: ")
    print(todays_date.year)
    typingPrint("Current month: ") 
    print(todays_date.month)
    typingPrint("Current day:")
    print(todays_date.day)
    print("")
    main()


    



start()