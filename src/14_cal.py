import os
os.system( 'clear' )
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

def date():
  spec = input( 'Please Choose Month & Year ( ex: 9, 2019 ) ' ).split( ',' )
  print( spec )

  if ( spec == '' ):
    os.system( 'clear' )
    x = datetime.now()
    c = calendar.TextCalendar( calendar.SUNDAY )
    str = c.formatmonth( x.year , x.month )
    print( str )
    print( '--------------------' )
    print( 'Please try again' )

  elif ( len( spec ) == 1 ):
    os.system( 'clear' )
    c = calendar.TextCalendar( calendar.SUNDAY )
    str = c.formatmonth( 2019 , int(spec[0]) )
    print( str )
    print( '--------------------' )

  elif ( len( spec ) == 2 ):
    os.system( 'clear' )
    c = calendar.TextCalendar( calendar.SUNDAY )
    str = c.formatmonth( int( spec[1] ) , int( spec[0]) )
    print( str )
    print( '--------------------' )

  else:
    os.system( 'clear' )
    print( 'Please try again using a valid input ( ex: 9, 2019 )' )


date()