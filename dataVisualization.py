# Import Pandas Library to create a data frame and seaborn library for visualization tools
import seaborn as sb
import pandas as pd

# Reads a text file, returns a data frame without header and footer
def dataImport(textfile):
    df = pd.read_csv(textfile, sep=",", skiprows=1, skipfooter=1, header=None, names=list(range(8)))
    return df

def main():
    
    #define text file
    fileName = 'packet2.txt'
    data = dataImport(fileName)
    
    # Sort data into separate dataframes based on class label
    GPS_Data = data[data[0] == 1].drop([7], axis=1)
    RMC_Data = data[data[0] == 2].drop([7], axis=1)
    ACC_Data = data[data[0] == 3].drop([0, 5, 6, 7], axis=1)
    print(ACC_Data)
    ACC_Data_M = ACC_Data.melt(1, var_name='Sensor_number', value_name='val')
    print(ACC_Data_M)
    IMU_Data = data[data[0] == 4]
    TC_Data = data[data[0] == 5]
    PRES_Data = data[data[0] == 6].drop([7], axis=1)
    Spectrometer_Data = data[data[0] == 7].drop([7], axis=1)
    
    # graph stuff
    graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=ACC_Data_M)
    #Graph1 = sb.lineplot(x=1, y= [2,3,4], data=ACC_Data)
    #graph = sb.relplot(data=ACC_Data, kind="line",x=1, y=2)
   # graph = sb.relplot(data=ACC_Data, kind="line",x=1, y=3)
    #graph = sb.relplot(data=ACC_Data, kind="line",x=1, y=4)
    #graph.set(title = "Temperature Data", xlabel='time',ylabel='temp')
main()
