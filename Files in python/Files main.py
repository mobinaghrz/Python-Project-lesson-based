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
# opens gfg text file of the current directory
f = open("file.txt")

# specifying the full path
f = open("C:\Users\Mobina\Desktop\Self-Study\GitHub\Python-Project-lesson-based\Files in python\Text.txt")