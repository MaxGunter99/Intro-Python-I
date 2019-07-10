# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE 
# x.append(4)
# print(x)
# RETURNS [1, 2, 3, 4]

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE 
# print(x + y)
# RETURNS [1, 2, 3, 4, 8, 9, 10]

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE 
y.remove(8)
# print(x + y)
# RETURNS [1, 2, 3, 4, 9, 10]

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE 
x.append(4)
y.remove(8)
y.insert( 2 , 99 )
# print(x + y)
# RETURNS [1, 2, 3, 4, 9, 10, 99]

# Print the length of list x
# YOUR CODE HERE 
# print( len(x) )
# RETURNS 3

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
# for i in range( 0, len(x) ):
#     print( x[i] * 1000 )
# TRUNCATING! RETURNS 1000 2000 3000

# RUN IN TERMINAL | python3 05_lists.py |