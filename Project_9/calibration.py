# Python module that implements function needed to calibrate data from sensor readings.
#John Mensah Onumah
#ITS 5900


def calibration_function(data_type,data_value):
    calibration_values = {'A':[0.95,0.2],'X':[1.01,-0.3],'R':[1,0]}
    if data_type.upper() == 'A':
        print('calibrated value: {:.2f}'.format(sensor_function(*calibration_values['A'],data_value)),('original value: {:.2f}'.format(data_value)).rjust(25))
    elif data_type.upper() == 'X':
        print ('calibrated value: {:.2f}'.format(sensor_function(*calibration_values['X'],data_value)),('original value: {:.2f}'.format(data_value)).rjust(25))
    elif data_type.upper() == 'R':
        print ('No calibration needed',('original value: {:.2f}'.format(data_value)).rjust(27))
    else:
        pass



def sensor_function(x,y,D):
    return (x*D) + y
