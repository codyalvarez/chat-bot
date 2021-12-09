# import calendar 
# import datetime

# current_y = datetime.now().year
# print(current_y)
# print("Calendar of " + current_y + "year")
# print(calendar.month(current_y, 3, 2, 1))


# importing date class from datetime module
from datetime import date
  
# creating the date object of today's date
todays_date = date.today()
  
# printing todays date
print("Current date: ", todays_date)
  
# fetching the current year, month and day of today
print("Current year:", todays_date.year)
print("Current month:", todays_date.month)
print("Current day:", todays_date.day)