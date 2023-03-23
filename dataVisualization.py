'''
Linux Commands:

g++ log_parser.cpp -o log_parser

./log_parser output.dat
'''

# Import Pandas Library to create a data frame and seaborn library for visualization tools
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Reads a text file, returns a data frame without header and footer
def dataImport(textfile):
    df = pd.read_csv(textfile, sep=",", skiprows=1, skipfooter=1, header=None, names=list(range(8)), engine="python")
    return df

def main():
    
    #define text file
    directory = input('Enter name of directory containing the packets: ')
    files = Path(directory).glob('*')
    

    for file in files:
        data = dataImport(file)

        # Sort data into separate dataframes based on class label
        GPS_Data = data[data[0] == 1].drop([7], axis=1) # unused for now

        RMC_Data = data[data[0] == 2].drop([7], axis=1) # unused for now

        ACC_Data = data[data[0] == 3].drop([0, 5, 6, 7], axis=1)
        ACC_Data_M = ACC_Data.melt(1, var_name='Sensor_number', value_name='val')

        IMU_Data = data[data[0] == 4].drop([0], axis=1)
        IMU_Data_M = IMU_Data.melt(1, var_name='Sensor_number', value_name='val')
        
        TC_Data = data[data[0] == 5].drop([0], axis=1)
        TC_Data_M = TC_Data.melt(1, var_name='Sensor_number', value_name='val')

        PRES_Data = data[data[0] == 6].drop([0, 7], axis=1)
        PRES_Data_M = PRES_Data.melt(1, var_name='Sensor_number', value_name='val')

        Spectrometer_Data = data[data[0] == 7].drop([7], axis=1) #unused for now
        
        # Graph stuff
        fig, axs = plt.subplots(ncols=2, nrows=2)
        ACC_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=ACC_Data_M, ax=axs[0,0])
        IMU_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=IMU_Data_M, ax=axs[1,0])
        TC_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=TC_Data_M, ax=axs[0,1])
        PRES_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=PRES_Data_M, ax=axs[1,1])

        ACC_graph.set(title = "Acceleration Data", xlabel='time',ylabel='acceleration')
        IMU_graph.set(title = "IMU Data", xlabel='time',ylabel='IMU')
        TC_graph.set(title = "TC Data", xlabel='time',ylabel='TC')
        PRES_graph.set(title = "PRES Data", xlabel='time',ylabel='PRES')
        plt.show()

    # The update is compiling and close to working, but there is a bug after the melt where equivalent sensor numbers from each
    # packet are treated differently. ie once a second packet is added, there are now two sensor_number = 2, two sensor_number = 3, etc.
    # Graph is also only currently being updated for ACC, and data is only being updated for ACC, IMU, TC, and PRES.

    '''
    newFile = input('Enter name of new file path: ')
    
    while newFile != '':
    
        data = dataImport(newFile)
        
        new_GPS_Data = data[data[0] == 1].drop([0, 7], axis=1) # unused for now
        
        new_RMC_Data = data[data[0] == 2].drop([0, 7], axis=1) # unused for now
        
        new_ACC_Data = data[data[0] == 3].drop([0, 5, 6, 7], axis=1)
        ACC_Data = pd.concat([ACC_Data, new_ACC_Data])
        ACC_Data_M = ACC_Data.melt(1, var_name='Sensor_number', value_name='val')
        
        IMU_Data = data[data[0] == 4].drop([0], axis=1)
        IMU_Data_M = IMU_Data.melt(1, var_name='Sensor_number', value_name='val')
            
        TC_Data = data[data[0] == 5].drop([0], axis=1)
        TC_Data_M = TC_Data.melt(1, var_name='Sensor_number', value_name='val')
        
        PRES_Data = data[data[0] == 6].drop([0, 7], axis=1)
        PRES_Data_M = PRES_Data.melt(1, var_name='Sensor_number', value_name='val')
        
        Spectrometer_Data = data[data[0] == 7].drop([7], axis=1) #unused for now 
        
        ACC_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=ACC_Data_M)
        ACC_graph.set(title = "Acceleration Data", xlabel='time',ylabel='acceleration')
        plt.show()
        
        newFile = input('Enter name of new file path: ')
    '''
    
main()