'''
Linux Commands:

g++ decode.cpp -o decode
./decode output.dat


'''

# Import Pandas Library to create a data frame and seaborn library for visualization tools
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Reads a text file, returns a data frame without header and footer
def dataImport(textfile):
    df = pd.read_csv(textfile, sep=",", header=None, names=list(range(8)), engine="python")
    return df

def main():
    # ask for type of input
    choice = input("Would you like to plot decoded packets or data? (packets/data): ")
    if (choice == "packets"):
        # define text file
        if (not Path("decodedpackets").exists()):
            print("Folder \"decodedpackets\" not found.")
            return

        GPS_Data = pd.DataFrame() # unused for now
        RMC_Data = pd.DataFrame() # unused for now
        ACC_Data = pd.DataFrame()
        IMU_Data = pd.DataFrame()
        TC_Data = pd.DataFrame()
        PRES_Data = pd.DataFrame()
        Spectrometer_Data = pd.DataFrame() # unused for now

        # Take input for number of packets to be graphed
        fileCount = 0
        files = Path("decodedpackets").glob('*')
        for file in files:
            fileCount += 1
        
        graphCount = input("How many packets should be graphed? (There are " + str(fileCount) + " total packets): ")
        
        try:
            graphCount = int(graphCount)
        except ValueError:
            print("That was not acceptable input.")
            return
        if (graphCount > fileCount) or (graphCount < 1):
            print("That was not acceptable input.")
            return

        # import the data from each file in directory
        files = Path("decodedpackets").glob('*')
        for file in files:
            x = str(file)
            x = x.strip("decodedpackets/\.txt")
            x = int(x)
    
            if (x < graphCount):
                print("Adding " + str(file) + " to the graph.")
                data = dataImport(file)

                #new_GPS_Data = data[data[0] == 1].drop([0], axis=1) # unused for now
                #GPS_Data = pd.concat([GPS_Data, new_GPS_Data]) # unused for now

                #new_RMC_Data = data[data[0] == 2].drop([0], axis=1) # unused for now
                #RMC_Data = pd.concat([RMC_Data, RMC_GPS_Data]) # unused for now

                new_ACC_Data = data[data[0] == 3].drop([0, 5, 6, 7], axis=1)
                ACC_Data = pd.concat([ACC_Data, new_ACC_Data])

                new_IMU_Data = data[data[0] == 4].drop([0], axis=1)
                IMU_Data = pd.concat([IMU_Data, new_IMU_Data])
                
                new_TC_Data = data[data[0] == 5].drop([0], axis=1)
                TC_Data = pd.concat([TC_Data, new_TC_Data])

                new_PRES_Data = data[data[0] == 6].drop([0, 7], axis=1)
                PRES_Data = pd.concat([PRES_Data, new_PRES_Data])

                #new_Spectrometer_Data = data[data[0] == 7].drop([0], axis=1) # unused for now
                #Spectrometer_Data = pd.concat([Spectrometer_Data, new_Spectrometer_Data]) # unused for now
    elif(choice == "data"):
        # define text file
        if (not Path("decodeddata").exists()):
            print("Folder \"decodeddata\" not found.")
            return

        GPS_Data = pd.DataFrame() # unused for now
        RMC_Data = pd.DataFrame() # unused for now
        ACC_Data = pd.DataFrame()
        IMU_Data = pd.DataFrame()
        TC_Data = pd.DataFrame()
        PRES_Data = pd.DataFrame()
        Spectrometer_Data = pd.DataFrame() # unused for now

        # Take input for number of packets to be graphed
        print("Here are the available files:")
    
        files = Path("decodeddata").glob('*')
        for file in files:
            print(str(file))

        fileChoice = input("Would you like all files graphed or one in particular? (all/\"name_of_file\"): ")
        
        if (fileChoice == "all"):
            # import the data from each file in directory
            files = Path("decodeddata").glob('*')
            for file in files:
                print("Adding " + str(file) + " to the graph...")
                data = dataImport(file)

                #new_GPS_Data = data[data[0] == 1].drop([0], axis=1) # unused for now
                #GPS_Data = pd.concat([GPS_Data, new_GPS_Data]) # unused for now

                #new_RMC_Data = data[data[0] == 2].drop([0], axis=1) # unused for now
                #RMC_Data = pd.concat([RMC_Data, RMC_GPS_Data]) # unused for now

                new_ACC_Data = data[data[0] == 3].drop([0], axis=1)
                ACC_Data = pd.concat([ACC_Data, new_ACC_Data])

                new_IMU_Data = data[data[0] == 4].drop([0], axis=1)
                IMU_Data = pd.concat([IMU_Data, new_IMU_Data])
                
                new_TC_Data = data[data[0] == 5].drop([0], axis=1)
                TC_Data = pd.concat([TC_Data, new_TC_Data])

                new_PRES_Data = data[data[0] == 6].drop([0], axis=1)
                PRES_Data = pd.concat([PRES_Data, new_PRES_Data])

                #new_Spectrometer_Data = data[data[0] == 7].drop([0], axis=1) # unused for now
                #Spectrometer_Data = pd.concat([Spectrometer_Data, new_Spectrometer_Data]) # unused for now

        elif (Path(fileChoice).exists()):
            # import the data from each file in directory
            files = Path("decodeddata").glob('*')
            for file in files:
                if (str(file) == fileChoice):
                    print("Adding " + str(file) + " to the graph...")
                    data = dataImport(file)

                    #new_GPS_Data = data[data[0] == 1].drop([0], axis=1) # unused for now
                    #GPS_Data = pd.concat([GPS_Data, new_GPS_Data]) # unused for now

                    #new_RMC_Data = data[data[0] == 2].drop([0], axis=1) # unused for now
                    #RMC_Data = pd.concat([RMC_Data, RMC_GPS_Data]) # unused for now

                    new_ACC_Data = data[data[0] == 3].drop([0], axis=1)
                    ACC_Data = pd.concat([ACC_Data, new_ACC_Data])

                    new_IMU_Data = data[data[0] == 4].drop([0], axis=1)
                    IMU_Data = pd.concat([IMU_Data, new_IMU_Data])
                    
                    new_TC_Data = data[data[0] == 5].drop([0], axis=1)
                    TC_Data = pd.concat([TC_Data, new_TC_Data])

                    new_PRES_Data = data[data[0] == 6].drop([0], axis=1)
                    PRES_Data = pd.concat([PRES_Data, new_PRES_Data])

                    #new_Spectrometer_Data = data[data[0] == 7].drop([0], axis=1) # unused for now
                    #Spectrometer_Data = pd.concat([Spectrometer_Data, new_Spectrometer_Data]) # unused for now

                    ACC_Data_M = ACC_Data.melt(1, var_name='Sensor_number', value_name='val')
                    IMU_Data_M = IMU_Data.melt(1, var_name='Sensor_number', value_name='val')
                    TC_Data_M = TC_Data.melt(1, var_name='Sensor_number', value_name='val')
                    PRES_Data_M = PRES_Data.melt(1, var_name='Sensor_number', value_name='val')

                    if (len(ACC_Data) != 0):
                        ACC_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=ACC_Data_M, marker='d')
                        ACC_graph.set(title = "Acceleration Data", xlabel='time',ylabel='acceleration',
                            facecolor="#e0e0e0")
                        ACC_graph.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
                    if (len(IMU_Data) != 0):
                        # IMU Graph settings
                        IMU_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=IMU_Data_M, marker='d')
                        IMU_graph.set(title = "IMU Data", xlabel='time',ylabel='IMU',
                            facecolor="#e0e0e0")
                        IMU_graph.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
                    if (len(TC_Data) != 0):
                        # TC Graph settings
                        TC_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=TC_Data_M, marker='d')
                        TC_graph.set(title = "TC Data", xlabel='time',ylabel='TC',
                            facecolor="#e0e0e0")
                        TC_graph.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
                    if (len(PRES_Data) != 0):
                        # PRES Graph settings
                        PRES_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=PRES_Data_M, marker='d')
                        PRES_graph.set(title = "PRES Data", xlabel='time',ylabel='PRES',
                            facecolor="#e0e0e0")
                        PRES_graph.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

                    # Show plots
                    plt.subplots_adjust(hspace=0.3, wspace=0.42)
                    plt.show()
                    return

        else:
            print("That was not acceptable input.")
            return

    else:
        print("That was not acceptable input.")
        return

    # Melt/Format data correctly for graphs
    #GPS_Data_M = GPS_Data.melt(1, var_name='Sensor_number', value_name='val') # unused for now
    #RMC_Data_M = RMC_Data.melt(1, var_name='Sensor_number', value_name='val') # unused for now

    ACC_Data_M = ACC_Data.melt(1, var_name='Sensor_number', value_name='val')
    IMU_Data_M = IMU_Data.melt(1, var_name='Sensor_number', value_name='val')
    TC_Data_M = TC_Data.melt(1, var_name='Sensor_number', value_name='val')
    PRES_Data_M = PRES_Data.melt(1, var_name='Sensor_number', value_name='val')

    #Spectrometer_Data_M = Spectrometer_Data.melt(1, var_name='Sensor_number', value_name='val') # unused for now

    # Graph setup
    fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(12,7), facecolor='#adadad')

    #GPS Graph settings # unused for now and needs additional changing
    '''
    GPS_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=GPS_Data_M, 
        ax=axs[], marker='d')
    GPS_graph.set(title = "GPS Data", xlabel='time',ylabel='',
        facecolor="#e0e0e0")
    GPS_graph.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
    '''

    #RMC Graph settings # unused for now and needs additional changing
    '''
    RMC_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=RMC_Data_M, 
        ax=axs[], marker='d')
    RMC_graph.set(title = "RMC Data", xlabel='time',ylabel='',
        facecolor="#e0e0e0")
    RMC_graph.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
    '''

    # ACC Graph settings
    ACC_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=ACC_Data_M, 
        ax=axs[0,0], marker='d')
    ACC_graph.set(title = "Acceleration Data", xlabel='time',ylabel='acceleration',
        facecolor="#e0e0e0")
    ACC_graph.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

    # IMU Graph settings
    IMU_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=IMU_Data_M, 
        ax=axs[1,0], marker='d')
    IMU_graph.set(title = "IMU Data", xlabel='time',ylabel='IMU',
        facecolor="#e0e0e0")
    IMU_graph.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

    # TC Graph settings
    TC_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=TC_Data_M, 
        ax=axs[0,1], marker='d')
    TC_graph.set(title = "TC Data", xlabel='time',ylabel='TC',
        facecolor="#e0e0e0")
    TC_graph.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

    # PRES Graph settings
    PRES_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=PRES_Data_M, 
        ax=axs[1,1], marker='d')
    PRES_graph.set(title = "PRES Data", xlabel='time',ylabel='PRES',
        facecolor="#e0e0e0")
    PRES_graph.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

    #Spectrometer Graph settings # unused for now and needs additional changing
    '''
    Spectrometer_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=Spectrometer_Data_M, 
        ax=axs[], marker='d')
    Spectrometer_graph.set(title = "Spectrometer Data", xlabel='time',ylabel='',
        facecolor="#e0e0e0")
    Spectrometer_graph.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
    '''

    # Show plots
    plt.subplots_adjust(hspace=0.3, wspace=0.42)
    plt.show()
    
main()