# John Mensah Onumah
# Python 3.7
# A simple script that takes a two csv file paths or names as input from the command line.
# The script then reads both files,merge and remove duplicates based on a key column
# and write output as a csv file.

# import csv and sys modules
import csv, sys

# a try except clause that checks if files have been passed on the commandline
# will print output to users to guide them to provide the necessary input.
try:
    data_file_1 = open(sys.argv[1])
    data_file_2 = open(sys.argv[2])
except FileNotFoundError:
    print("Kindly check the filename or path and enter again")
    sys.exit()
except IndexError:
    print("Kindly pass data files(at least two of them) as arguments on the command line")
    sys.exit()


# use csv module to create csv reader objects.
file_1_Reader = csv.reader(data_file_1)
file_2_Reader = csv.reader(data_file_2)

#create a list that will store the the lines of rows from both files.
storage=[]

# use reader objects to loop through and read lines in both files.
for row in file_1_Reader: 
    #add the lines to storage
    storage.append(row)
for row in file_2_Reader:
    # ignore the first line in file 2
    if file_2_Reader.line_num == 1:
        continue
    # add the lines to storage.
    storage.append(row)

# sort the rows in storage based on the 3rd colummn
storage.sort(key= lambda row: row[2])

# create an output csv file and write the rows in storage to it.
with open('outputfile.csv','w') as output:
    #create a csv write object to write to output file
    write_output = csv.writer(output)
    column_three_tracker = []
    for row in storage:
        # this is meant to strip elements in each row
        row = list(map(lambda x: str(x).strip(),row))
        #if clause to remove duplicates and empty rows
        if row[2] not in column_three_tracker and row[2] != '':
            column_three_tracker.append(row[2])
            write_output.writerow(row)
    
