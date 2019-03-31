#! /usr/bin/env python3
# John Mensah Onumah ITS 5900
# A script that implements a calibration function and returns a calibrated values.
# The script reads a data file with sensor readings.

#importing python module with function needed to produce calibrated function.
import calibration

#reading data file.
with open('SensorData.dat','r') as fh:
    for line in fh:
        #condition that handles empty lines and new lines.
        if line not in ['','\n']:
            # A little data cleaning and formatting.
            data_type,data_value = line.strip().split(',')
            try:
                # calling function from imported module.
                calibration.calibration_function(data_type,float(data_value))
            except:
                pass