import os
os.system( 'clear' )
"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
def openFile():
    x = open( 'foo.txt' , 'rt' )
    print( x.read() )
    x.close()

openFile()


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
def writeFile():
    x = open( 'bar.txt' , 'w' )
    x = open( 'bar.txt' , 'a' )
    x.write( ' Hey there.' )
    x.write( ' This is a file now.' )
    x.write( ' Bye.' )
    x = open( 'bar.txt' , 'rt' )
    print( x.read() )
    x.close()


writeFile()