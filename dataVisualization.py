'''
Linux commands:

g++ log_parser.cpp -o log_parser
/log_parser output.dat
'''

import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def dataImport(textfile):
    df = pd.read_csv(textfile, sep=",", skiprows=1, skipfooter=1, header=None, names=list(range(8)))
    return df

def main():
    fileName = 'packet2.txt'
    data = dataImport(fileName)
    tempData = data[data[0] == 3].drop([5, 6, 7], axis=1)

    
    graph = sb.relplot(data=tempData, kind="line",x=1, y=3)
    graph.set(title = "GRAPH", xlabel='time',ylabel='temp')

main()
