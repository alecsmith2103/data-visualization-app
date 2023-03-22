import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def dataImport(textfile):
    df = pd.read_csv(textfile, sep=" ", header=None)
    #df = df.iloc[1:]
    return df
    
    
def main():
    #fileName = input('Enter filename: ')
    fileName = 'packet1.txt'
    data = dataImport(fileName)
    print(data)

main()
