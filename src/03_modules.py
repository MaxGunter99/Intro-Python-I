"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
# print( "This is the name of the script: " , sys.argv[0] )
# print( "Number of arguments: " , len(sys.argv) )
# print( "The arguments are: " , str(sys.argv) )

# Print out the OS platform you're using:
# YOUR CODE HERE
# print( sys.platform )
# RETURNS darwin

# Print out the version of Python you're using:
# YOUR CODE HERE
# print( "Python version: " , sys.version )
# RETURNS 2.7.10 (default, Feb 22 2019, 21:55:15) \n[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)]

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
# print( os.getpid() )
# RETURNS 4351

# Print the current working directory (cwd):
# YOUR CODE HERE
# print( os.getcwd() )
# RETURNS /Users/voidchaser/Lambda/Intro-Python-I/src

# Print out your machine's login name
# YOUR CODE HERE
# print( os.getlogin() )
# RETURNS voidchaser


# RUN IN TERMINAL | python3 03_modules.py |
