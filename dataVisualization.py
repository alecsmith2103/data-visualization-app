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

# Reads a text file, returns a data frame
def dataImport(textfile):
    df = pd.read_csv(textfile, sep=",", header=None, names=list(range(10)), engine="python")
    return df

def main():
    # ask for type of input
    choice = input("Would you like to plot decoded packets or data? (packets/data): ")

    # Packet input
    if (choice == "packets"):
        # See if path exists
        if (not Path("decodedpackets").exists()):
            print("Folder \"decodedpackets\" not found.")
            return

        # Create blank dataframes
        GPS_Data = pd.DataFrame() 
        RMC_Data = pd.DataFrame()
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

        # import the data from each packet file in directory
        files = Path("decodedpackets").glob('*')
        for file in files:
            x = str(file)
            x = x.strip("decodedpackets/\.txt")
            x = int(x)
    
            if (x < graphCount):
                print("Adding " + str(file) + " to the graph.")
                data = dataImport(file)

                new_GPS_Data = data[data[0] == 1].drop([0, 2, 3, 4, 5, 8, 9], axis=1) 
                GPS_Data = pd.concat([GPS_Data, new_GPS_Data])

                new_RMC_Data = data[data[0] == 2].drop([0, 2, 3, 4, 5, 8, 9], axis=1)
                RMC_Data = pd.concat([RMC_Data, new_RMC_Data])

                new_ACC_Data = data[data[0] == 3].drop([0, 5, 6, 7, 8, 9], axis=1)
                ACC_Data = pd.concat([ACC_Data, new_ACC_Data])
                ACC_IMU_Data = data[data[0] == 4].drop([0, 5, 6, 7, 8, 9], axis=1)
                ACC_IMU_Data = ACC_IMU_Data.rename(columns={2:5, 3:6, 4:7})
                ACC_Data = pd.concat([ACC_Data, ACC_IMU_Data])

                new_IMU_Data = data[data[0] == 4].drop([0, 2, 3, 4, 8, 9], axis=1)
                IMU_Data = pd.concat([IMU_Data, new_IMU_Data])
                
                new_TC_Data = data[data[0] == 5].drop([0, 8, 9], axis=1)
                TC_Data = pd.concat([TC_Data, new_TC_Data])

                new_PRES_Data = data[data[0] == 6].drop([0, 7, 8, 9], axis=1)
                PRES_Data = pd.concat([PRES_Data, new_PRES_Data])

                #new_Spectrometer_Data = data[data[0] == 7].drop([0], axis=1) # unused for now
                #Spectrometer_Data = pd.concat([Spectrometer_Data, new_Spectrometer_Data]) # unused for now

    # Data input
    elif(choice == "data"):
        # See if path exists
        if (not Path("decodeddata").exists()):
            print("Folder \"decodeddata\" not found.")
            return

        # Create blank dataframes
        GPS_Data = pd.DataFrame()
        RMC_Data = pd.DataFrame()
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
        
        # All types of data to be plotted
        if (fileChoice == "all"):
            # import the data from each data file in directory
            files = Path("decodeddata").glob('*')
            for file in files:
                print("Adding " + str(file) + " to the graph...")
                data = dataImport(file)

                new_GPS_Data = data[data[0] == 1].drop([0, 2, 3, 4, 5, 8, 9], axis=1) 
                GPS_Data = pd.concat([GPS_Data, new_GPS_Data])

                new_RMC_Data = data[data[0] == 2].drop([0, 2, 3, 4, 5, 8, 9], axis=1)
                RMC_Data = pd.concat([RMC_Data, new_RMC_Data])

                new_ACC_Data = data[data[0] == 3].drop([0, 5, 6, 7, 8, 9], axis=1)
                ACC_Data = pd.concat([ACC_Data, new_ACC_Data])
                ACC_IMU_Data = data[data[0] == 4].drop([0, 5, 6, 7, 8, 9], axis=1)
                ACC_IMU_Data = ACC_IMU_Data.rename(columns={2:5, 3:6, 4:7})
                ACC_Data = pd.concat([ACC_Data, ACC_IMU_Data])

                new_IMU_Data = data[data[0] == 4].drop([0, 2, 3, 4, 8, 9], axis=1)
                IMU_Data = pd.concat([IMU_Data, new_IMU_Data])
                
                new_TC_Data = data[data[0] == 5].drop([0, 8, 9], axis=1)
                TC_Data = pd.concat([TC_Data, new_TC_Data])

                new_PRES_Data = data[data[0] == 6].drop([0, 7, 8, 9], axis=1)
                PRES_Data = pd.concat([PRES_Data, new_PRES_Data])

                #new_Spectrometer_Data = data[data[0] == 7].drop([0], axis=1) # unused for now
                #Spectrometer_Data = pd.concat([Spectrometer_Data, new_Spectrometer_Data]) # unused for now

        # Specific type of data to get plotted alone
        elif (Path(fileChoice).exists()):
            # import the data from each data file in directory
            if fileChoice != 'decodeddata\\decodeddata3.txt' and fileChoice != 'decodeddata/decodeddata3.txt':
                files = Path("decodeddata").glob('*')
                ACC_flag = False
            else:
                files = Path("decodeddata").glob('./decodeddata[3-4].txt')
                ACC_flag = True
            
            for file in files:
                if (str(file) == fileChoice or ACC_flag == True):
                    print("Adding " + str(file) + " to the graph...")
                    data = dataImport(file)

                    new_GPS_Data = data[data[0] == 1].drop([0, 2, 3, 4, 5, 8, 9], axis=1) 
                    GPS_Data = pd.concat([GPS_Data, new_GPS_Data])

                    new_RMC_Data = data[data[0] == 2].drop([0, 2, 3, 4, 5, 8, 9], axis=1)
                    RMC_Data = pd.concat([RMC_Data, new_RMC_Data])

                    new_ACC_Data = data[data[0] == 3].drop([0, 5, 6, 7, 8, 9], axis=1)
                    ACC_Data = pd.concat([ACC_Data, new_ACC_Data])
                    if ACC_flag == True:
                        ACC_IMU_Data = data[data[0] == 4].drop([0, 5, 6, 7, 8, 9], axis=1)
                        ACC_IMU_Data = ACC_IMU_Data.rename(columns={2:5, 3:6, 4:7})
                        ACC_Data = pd.concat([ACC_Data, ACC_IMU_Data])

                    new_IMU_Data = data[data[0] == 4].drop([0, 2, 3, 4, 8, 9], axis=1)
                    IMU_Data = pd.concat([IMU_Data, new_IMU_Data])
                    
                    new_TC_Data = data[data[0] == 5].drop([0, 8, 9], axis=1)
                    TC_Data = pd.concat([TC_Data, new_TC_Data])

                    new_PRES_Data = data[data[0] == 6].drop([0, 7, 8, 9], axis=1)
                    PRES_Data = pd.concat([PRES_Data, new_PRES_Data])

                    #new_Spectrometer_Data = data[data[0] == 7].drop([0], axis=1) # unused for now
                    #Spectrometer_Data = pd.concat([Spectrometer_Data, new_Spectrometer_Data]) # unused for now

            ACC_Data_M = ACC_Data.melt(1, var_name='Sensor_number', value_name='val')
            IMU_Data_M = IMU_Data.melt(1, var_name='Sensor_number', value_name='val')
            TC_Data_M = TC_Data.melt(1, var_name='Sensor_number', value_name='val')
            PRES_Data_M = PRES_Data.melt(1, var_name='Sensor_number', value_name='val')

            #if sensor has data, set the graph settings to plot - only for "data" option
            if (GPS_Data.empty == False):
                # GPS Graph settings
                GPS_graph = sb.scatterplot(x=6,y=7, hue=1, data=GPS_Data, palette="blend:gold,dodgerblue") #gradient color for gps location over time
                GPS_graph.set(title = "GPS Data", xlabel='latitude',ylabel='longitude', facecolor="#e0e0e0")
                GPS_graph.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, title="time (sec)")
            if (RMC_Data.empty == False):
                # RMC Graph settings
                RMC_graph = sb.scatterplot(x=6,y=7, hue=1, data=RMC_Data, palette="blend:gold,dodgerblue") #gradient color for gps location over time
                RMC_graph.set(title = "RMC Data", xlabel='latitude',ylabel='longitude', facecolor="#e0e0e0")
                RMC_graph.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, title="time (sec)")
            if (ACC_Data.empty == False):
                # ACC Graph settings
                ACC_graph = sb.lineplot(x=1, y='val', hue='Sensor_number', data=ACC_Data_M,
                    palette=sb.color_palette('pastel', n_colors=6), marker='d')
                #have to declare labels and handles to merge legends since ACC and IMU data is combined, format allows for distinction of ACC vs. IMU sensors
                labels = ['{}{}'.format(l if i < 3 else l-3, 'ACC' if i < 3 else 'IMU') for i, l in enumerate(ACC_Data_M['Sensor_number'].unique())]
                handles, _ = ACC_graph.get_legend_handles_labels() 
                ACC_graph.legend(handles=handles, labels=labels, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, title="Sensor #")
                ACC_graph.set(title="Acceleration Data", xlabel='time', ylabel='acceleration', facecolor="#e0e0e0")
            if (IMU_Data.empty == False and ACC_flag == False):
                # IMU Graph settings
                IMU_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=IMU_Data_M, marker='d', palette = sb.color_palette('pastel', n_colors=3))
                IMU_graph.set(title = "IMU Data", xlabel='time',ylabel='IMU',
                    facecolor="#e0e0e0")
                IMU_graph.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, title="sensor #")
            if (TC_Data.empty == False):
                # TC Graph settings
                TC_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=TC_Data_M, marker='d', palette = sb.color_palette('pastel', n_colors=6))
                TC_graph.set(title = "TC Data", xlabel='time',ylabel='TC',
                    facecolor="#e0e0e0")
                TC_graph.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, title="sensor #")
            if (PRES_Data.empty == False):
                # PRES Graph settings
                PRES_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=PRES_Data_M, marker='d', palette = sb.color_palette('pastel', n_colors=5))
                PRES_graph.set(title = "PRES Data", xlabel='time',ylabel='PRES',
                    facecolor="#e0e0e0")
                PRES_graph.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, title="sensor #")

            # Show plots
            plt.tight_layout()
            plt.show()
            return
        
        # Bad input, error handling
        else:
            print("That was not acceptable input.")
            return

    # Bad input, error handling
    else:
        print("That was not acceptable input.")
        return

    # Melt/Format data correctly for graphs
    ACC_Data_M = ACC_Data.melt(1, var_name='Sensor_number', value_name='val')
    IMU_Data_M = IMU_Data.melt(1, var_name='Sensor_number', value_name='val')
    TC_Data_M = TC_Data.melt(1, var_name='Sensor_number', value_name='val')
    PRES_Data_M = PRES_Data.melt(1, var_name='Sensor_number', value_name='val')
    #Spectrometer_Data_M = Spectrometer_Data.melt(1, var_name='Sensor_number', value_name='val') # unused for now and needs additonal changing

    # Graph setup, change here if spectrometer data gets added in future implementation - graph settings below only for "packet" option
    fig, axs = plt.subplots(ncols=3, nrows=2, figsize=(12,7), facecolor='#adadad')

    # GPS Graph settings
    GPS_graph = sb.scatterplot(x=6,y=7, hue=1, data=GPS_Data, ax=axs[0,2], palette="blend:gold,dodgerblue") #gradient color for gps location over time
    GPS_graph.set(title = "GPS Data", xlabel='latitude',ylabel='longitude', facecolor="#e0e0e0")
    GPS_graph.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, title="time (sec)")

    # RMC Graph settings
    RMC_graph = sb.scatterplot(x=6,y=7, hue=1, data=RMC_Data, ax=axs[1,2], palette="blend:gold,dodgerblue") #gradient color for gps location over time
    RMC_graph.set(title = "RMC Data", xlabel='latitude',ylabel='longitude', facecolor="#e0e0e0")
    RMC_graph.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, title="time (sec)")

    # ACC Graph settings
    ACC_graph = sb.lineplot(x=1, y='val', hue='Sensor_number', data=ACC_Data_M,
            palette=sb.color_palette('pastel', n_colors=6), marker='d', ax=axs[0, 0])
    #have to declare labels and handles to merge legends since ACC and IMU data is combined, format allows for distinction of ACC vs. IMU sensors
    labels = ['{}{}'.format(l if i < 3 else l-3, 'ACC' if i < 3 else 'IMU') for i, l in enumerate(ACC_Data_M['Sensor_number'].unique())]
    handles, _ = ACC_graph.get_legend_handles_labels() 
    axs[0, 0].legend(handles=handles, labels=labels, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, title="Sensor #")
    axs[0, 0].set(title="Acceleration Data", xlabel='time', ylabel='acceleration', facecolor="#e0e0e0")
    
    # IMU Graph settings
    IMU_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=IMU_Data_M, 
        ax=axs[1,0], marker='d', palette = sb.color_palette('pastel', n_colors=3))
    IMU_graph.set(title = "IMU Data", xlabel='time',ylabel='IMU',
        facecolor="#e0e0e0")
    IMU_graph.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, title="sensor #")

    # TC Graph settings
    TC_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=TC_Data_M, 
        ax=axs[0,1], marker='d', palette = sb.color_palette('pastel', n_colors=6))
    TC_graph.set(title = "TC Data", xlabel='time',ylabel='TC',
        facecolor="#e0e0e0")
    TC_graph.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, title="sensor #")

    # PRES Graph settings
    PRES_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=PRES_Data_M, 
        ax=axs[1,1], marker='d', palette = sb.color_palette('pastel', n_colors=5))
    PRES_graph.set(title = "PRES Data", xlabel='time',ylabel='PRES',
        facecolor="#e0e0e0")
    PRES_graph.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, title="sensor #")

    #Spectrometer Graph settings # unused for now and needs additional changing
    '''
    Spectrometer_graph = sb.lineplot(x=1,y='val',hue='Sensor_number', data=Spectrometer_Data_M, 
        ax=axs[], marker='d')
    Spectrometer_graph.set(title = "Spectrometer Data", xlabel='time',ylabel='',
        facecolor="#e0e0e0")
    Spectrometer_graph.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
    '''

    # Show plots
    plt.subplots_adjust(hspace=0.4, wspace=0.72)
    plt.show()
    return
    
main()