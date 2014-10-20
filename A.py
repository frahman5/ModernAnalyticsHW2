__author__ = 'Faiyam Rahman, Rachel Mayer'

import pandas as pd
import numpy as np
from config import TRAIN_DATA, DEBUG_DATA, FILE_FORMAT

def make3DHist(dlongbinsize, dlatbinsize, data):
    """
    float float np.array -> ???

    Given the parameters for binsize and a matrix of data, 
    produces (saves to file) a 3DHistogram
    """
    pass

def main():
    """
    Based on train_data.csv, produces
    plots of the pdfs (approximated as histograms) of 
        P(passenger count=1|dropoff longitude, dropoff latitude)
        P(passenger count=3|dropoff longitude, dropoff latitude)
    """
    # read relevant data into pandas dataframe
    num_data_points = 10000                       # limit data size to increase speed
    data = pd.read_csv( DEBUG_DATA, nrows = 10000)
    data = data[['passenger_count', 'dropoff_longitude', 'dropoff_latitude']] 
    import pdb
    pdb.set_trace()
    for pc_count in (1, 3):
        filteredData = data[data['passenger_count'] == pc_count]
        make3DHist(dlongbinsize, dlatbinsize, filteredData)


## Usage: python A.py
if __name__ == '__main__':
    main()

