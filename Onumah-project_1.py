# A script that asks a user for file size(in Megabytes) and transfer speed(in Megabits per second)
# Performs computation and returns the amount of time needed for transfer to occur in seconds and minutes.


#A loop with if else statement to ensure that user input is an integer
valid_file_size = False
while not valid_file_size:
    
    #ask user for file size
    file_size = input("What is the size of your file in Megabytes. Kindly enter the figure below.\n>>>")
    
    #check if user string input is all decimals
    if file_size.isdecimal():
        valid_file_size = True
    else:
        print ("kindly ensure your input is an integer")

valid_transfer_speed = False
while not valid_transfer_speed:
    
    #ask user for for transfer speed
    transfer_speed = input("What is your estimated transfer speed in Megabits per second. Kindly enter value at the prompt below.\n>>>")
    
    #check if user input is all decimals
    if transfer_speed.isdecimal():
        valid_transfer_speed = True
    else:
        print ("kindly ensure your input is an integer")


#converts user input from string to integers
file_size = int(file_size)

transfer_speed = int(transfer_speed)

# converts user input from Megabytes to Megabits
file_size_Mb = file_size * 8

# calculates time of transfer in seconds
time_of_transfer = file_size_Mb / transfer_speed

# if clause to ensure that any time duration above 60 seconds is converted into minutes and seconds
if time_of_transfer >= 60:

    #use floor division to get whole number
    minutes = int(time_of_transfer // 60)
    
    #use modulo to get remainder
    seconds = round(time_of_transfer % 60,2)
    
    if minutes == 1:
        print ("it will take " + str(minutes) + " minute and " + str(seconds) + " seconds to transfer your files")
    else:
        print ("it will take " + str(minutes) + " minutes and " + str(seconds) + " seconds to transfer your files")
else: 
    print ("it will take " + str(time_of_transfer) + " seconds to transfer your files")

