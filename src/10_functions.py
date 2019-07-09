# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
even_or_odd = num % 2
if even_or_odd > 0:
    print("Odd!")
else:
    print("Even!")

# RUN IN TERMINAL | python3 10_functions.py |