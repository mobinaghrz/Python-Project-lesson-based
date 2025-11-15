
# A CSV (Comma Separated Values) file is a plain text file where each line represents a data record, and fields within each 
#  are separated by commas. It's commonly used for spreadsheets and databases due to its simplicity and readability.

# Below are some operations that we perform while working with Python CSV files in Python

# Reading a CSV file
# Reading from a CSV file is done using the reader object. The CSV file is opened as a text file with Python’s built-in open() function,
# which returns a file object. In this example, we first open the CSV file in READ mode, file object is converted to csv.reader 
# object and further operation takes place. Code and detailed explanation is given below


# with open(...) opens the CSV file in read mode safely using a context manager.
# csv.reader(csvfile) turns the file into a CSV reader object.
# next(csvreader) extracts the first row as column headers.
# Loop through csvreader to append each row (as a list) to rows.
# Print total rows, headers and first 5 data rows in a formatted view.

import csv

filename = "AAPL.csv"  # File name
fields = []  # Column names
rows = []    # Data rows

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)  # Reader object

    fields = next(csvreader)  # Read header
    for row in csvreader:     # Read rows
        rows.append(row)

    print("Total no. of rows: %d" % csvreader.line_num)  # Row count

print('Field names are: ' + ', '.join(fields))

print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    for col in row:
        print("%10s" % col, end=" ")
    print('\n')


# Reading CSV Files Into a Dictionary With csv
# We can read a CSV file into a dictionary using the csv module in Python and the csv.DictReader class. 

# with open(...) opens the file using a context manager.
# csv.DictReader(file) reads each row as a dictionary using headers as keys.
# data_list.append(row) stores each dictionary in a list.

import csv
with open('employees.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)  # Create DictReader

    data_list = []  # List to store dictionaries
    for row in csv_reader:
        data_list.append(row)

for data in data_list:
    print(data)

# Writing to a CSV file
# To write to a CSV file, we first open the CSV file in WRITE mode. 
# The file object is converted to csv.writer object and further operations takes place. Code and detailed explanation is given below.

# fields defines the column headers and rows contains the data as a list of lists.
# with open(..., 'w') opens the file in write mode using a context manager.
# csv.writer(csvfile) creates a writer object for writing to the CSV.
# writerow(fields) writes the header row to the file.
# writerows(rows) writes all data rows to the CSV at once.

# import csv

# # Define header and data rows
# fields = ['Name', 'Branch', 'Year', 'CGPA']
# rows = [
#     ['Nikhil', 'COE', '2', '9.0'],
#     ['Sanchit', 'COE', '2', '9.1'],
#     ['Aditya', 'IT', '2', '9.3'],
#     ['Sagar', 'SE', '1', '9.5'],
#     ['Prateek', 'MCE', '3', '7.8'],
#     ['Sahil', 'EP', '2', '9.1']
# ]

# filename = "university_records.csv"
# with open(filename, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)        # Create writer object
#     csvwriter.writerow(fields)             # Write header
#     csvwriter.writerows(rows)              # Write multiple rows


# Writing a dictionary to a CSV file
# To write a dictionary to a CSV file, the file object (csvfile) is converted to a DictWriter object. 
# Detailed example with explanation and code is given below.


# with open(...) opens file safely using a context manager.
# csv.DictWriter(...) maps dictionary keys to CSV columns.
# writeheader() writes column headers.
# writerows(mydict) writes all dictionaries as CSV rows.

# importing the csv module
import csv

# my data rows as dictionary objects
mydict = [{'branch': 'COE', 'cgpa': '9.0',
           'name': 'Nikhil', 'year': '2'},
          {'branch': 'COE', 'cgpa': '9.1',
           'name': 'Sanchit', 'year': '2'},
          {'branch': 'IT', 'cgpa': '9.3',
           'name': 'Aditya', 'year': '2'},
          {'branch': 'SE', 'cgpa': '9.5',
           'name': 'Sagar', 'year': '1'},
          {'branch': 'MCE', 'cgpa': '7.8',
           'name': 'Prateek', 'year': '3'},
          {'branch': 'EP', 'cgpa': '9.1',
           'name': 'Sahil', 'year': '2'}]

# field names
fields = ['name', 'branch', 'year', 'cgpa']

# name of csv file
filename = "university_records.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(mydict)