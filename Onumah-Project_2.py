# John Mensah Onumah
# Python 3.7
# A simple script that takes a file path or name as input from the command line and then reads the entire file and print out files ending with 
# the extension exe.

import sys

# read from command line the file name or full file path.
try:
        file_path = sys.argv[1]
except IndexError:
        print('Kindly pass the filename or full path of the file as a command line argument')
        print('Kindly try again.')
        sys.exit()

# opening file and storing it in the variable file_opened.
try:
        file_opened = open(file_path)
except FileNotFoundError:
        print('Kindly ensure that this file exist and that the file path specified is correct')
        print('Kindly try again.')
        sys.exit()

#looping through the file to get the filnames listed within it
#if filenames end in exe, it gets printed to the screen.
for line in file_opened:
    if line.strip().lower().endswith('.exe'):
            print(line.strip())
    
file_opened.close()



