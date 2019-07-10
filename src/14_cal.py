"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# user_input = []
# date = input( "Please Enter A Date! 🗓\n" )

# # NO INPUT
# if len(date) == 0:
#   i = datetime.now()
#   print( "The current month is:" , i.strftime("%B"), "!" , "Please try again." )

# # MONTH AND YEAR
# else:
#   i = datetime.now()
#   user_input.append( date )
#   for i in user_input:
#     you = i.split(" ")
#     selected_month = you[0]
#     if you[0] == "january":
#       you[0] = 1
#     elif you[0] == "february":
#       you[0] = 2
#     elif you[0] == "march":
#       you[0] = 3
#     elif you[0] == "april":
#       you[0] = 4
#     elif you[0] == "may":
#       you[0] = 5
#     elif you[0] == "june":
#       you[0] = 6
#     elif you[0] == "july":
#       you[0] = 7
#     elif you[0] == "august":
#       you[0] = 8
#     elif you[0] == "september":
#       you[0] = 9
#     elif you[0] == "october":
#       you[0] = 10
#     elif you[0] == "november":
#       you[0] = 11
#     elif you[0] == "december":
#       you[0] = 12

#     # JUST MONTH
#     if len(you) >= 3:
#       print( "Please use format ( month year )" )
#       break

#     if len(you) == 1:
#       i = datetime.now()
#       year = i.strftime("%j")
#       days_until_end_of_year = 365 - int(year)
#       print( "Days of", selected_month , calendar.monthcalendar(int(i.strftime("%Y")), you[0]))
#       print( "Days until the end of this year:", days_until_end_of_year )

#     else:
#       i = datetime.now()
#       year = i.strftime("%j")
#       days_until_end_of_year = 365 - int(year)
#       print( "Days of", selected_month , calendar.monthcalendar(int(you[1]), you[0]))
#       print( "Days until the end of this year:", days_until_end_of_year )

# TYPE IN A MONTH AND THE YEAR
# RUN IN TERMINAL | python3 14_cal.py |