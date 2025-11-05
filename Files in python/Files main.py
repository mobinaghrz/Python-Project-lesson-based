##File Handling in Python##
# File handling refers to the process of performing operations on a file,
#  such as creating, opening, reading, writing and closing it through a programming interface.
#  It involves managing the data flow between the program and the file system on the storage device,
#  ensuring that data is handled safely and efficiently.

# Why do we need File Handling
# To store data permanently, even after the program ends.
# To access external files like .txt, .csv, .json, etc.
# To process large files efficiently without using much memory.
# To automate tasks like reading configs or saving outputs.
# To handle input/output in real-world applications and tools.

#Opening a File
# opens Text text file of the current directory
f = open("Text.txt")

#Because "r" for read, and "t" for text are the default values, you do not need to specify them.
f = open("Text.txt", "rt")

# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

# f = open("Text.txt")
# print(f.read())

# # Now you can safely perform operations within or on this path

# # If the file is located in a different location, you will have to specify the file path, like this:

# f = open("C:/Users/Mobina/Desktop/Self-Study/GitHub/Python-Project-lesson-based/Files in python/anotherPath/Test2.txt")
# print(f.read())

# # You can also use the with statement when opening a file:
# with open("Text.txt") as f:
#   print(f.read())
  
# close file and readline
# f = open("Text.txt")
# print(f.readline(10))
# print(f.readline())
# print(f.readline())
# f.close()
# # f.read()

# # Read Only Parts of the File
# # By default the read() method returns the whole text, but you can also specify how many characters you want to return:
# with open("Text.txt") as f:
#   print(f.read(5))

# # By looping through the lines of the file, you can read the whole file, line by line:
# with open("Text.txt") as f:
#   for x in f:
#     print(x)

# # Write to an Existing File
# # To write to an existing file, you must add a parameter to the open() function:

# # "a" - Append - will append to the end of the file

# # "w" - Write - will overwrite any existing content

# with open("Text.txt", "w") as f:
#   f.write("Woops! I have deleted the content!")

# #open and read the file after the overwriting:
# with open("Text.txt") as f:
#   print(f.read())


# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exists

# "a" - Append - will create a file if the specified file does not exists

# "w" - Write - will create a file if the specified file does not exists

# f = open("myfile.txt", "x")
# f = open("myfile.txt")
# # f = open("Text.txt", "x")
# # f.write("oh hello")
# # print(f.read())
# f.close()

# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:
# import os
# os.remove("myfile.txt")

# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:

# Example
# Check if file exists, then delete it:

import os

if os.path.exists("myfile.txt"):
  os.remove("myfile.txt")
else:
  print("The file does not exist")

# create / delete file
import os
# os.mkdir("myfolder")
os.rmdir("myfolder")



# Open the file in append mode ('a')
# f = open('example.txt','x')
# with open('example.txt', 'a') as f:
#     f.write('This is new appended content.\n')
#     f.write('Another line.\n')
# f = open('example.txt','r')
# print(f.read())

# The file is automatically closed after exiting the 'with' block.
# The new content is added to the end of the file.
# Working with csv files in Python
# Last Updated : 05 Aug, 2025
# A CSV (Comma Separated Values) file is a plain text file where each line represents a data record, and fields within each record are separated by commas. It's commonly used for spreadsheets and databases due to its simplicity and readability.

# Below are some operations that we perform while working with Python CSV files in Python

# Reading a CSV file
# Reading from a CSV file is done using the reader object. The CSV file is opened as a text file with Python’s built-in open() function, which returns a file object. In this example, we first open the CSV file in READ mode, file object is converted to csv.reader object and further operation takes place. Code and detailed explanation is given below.


# import csv

# filename = "aapl.csv"  # File name
# fields = []  # Column names
# rows = []    # Data rows

# with open(filename, 'r') as csvfile:
#     csvreader = csv.reader(csvfile)  # Reader object

#     fields = next(csvreader)  # Read header
#     for row in csvreader:     # Read rows
#         rows.append(row)

#     print("Total no. of rows: %d" % csvreader.line_num)  # Row count

# print('Field names are: ' + ', '.join(fields))

# print('\nFirst 5 rows are:\n')
# for row in rows[:5]:
#     for col in row:
#         print("%10s" % col, end=" ")
#     print('\n')