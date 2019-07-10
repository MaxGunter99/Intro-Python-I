"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# # YOUR CODE HERE
# def load_foo():
#     text_file = open( "foo.txt" , "r" )
#     read = text_file.read().split(",")
#     text_file.close()
#     print(read)

# load_foo()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE

# def save_info( info ):
#     text_file = open( "bar.txt" , "w" )
#     text_file.write(info)
#     text_file.close()

# save_info("what a beautiful day, a care free happy day, one that youll want to relive again and again. you can try remembering this day on your own, but for some reason ... you cant piece it all together. You can try drawing it, but lets face it, your hardly an artist. You can try coming back to the same spot, with the same people, only to find that your older, crankier, and the entire area has been bombarded with nucular missiles. In fact these days, theres only one way to save a perfect summer day, its with pictures! Use Kodak cameras to save all your best days, because it will only get worse from here.")

# RUN IN TERMINAL | python3 13_file_io.py |