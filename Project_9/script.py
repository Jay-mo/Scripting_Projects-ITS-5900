import calibration

with open('SensorData.dat','r') as fh:
    for line in fh:
        if line not in ['','\n']:
            data_type,data_value = line.strip().split(',')
            try:
                calibration.calibration_function(data_type,float(data_value))
            except:
                pass