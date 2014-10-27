# __author__ = 'Faiyam Rahman, Rachel Mayer'
import pandas as pd
import numpy as np
from config import TRAIN_DATA, DEBUG_DATA, FILE_FORMAT
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



# def main():
#     """
#     Based on train_data.csv, produces
#     plots of the pdfs (approximated as histograms) of 
#         P(passenger count=1|dropoff longitude, dropoff latitude)
#         P(passenger count=3|dropoff longitude, dropoff latitude)
#     """
#     # # read relevant data into pandas dataframe
#     # num_data_points = 10000                       # limit data size to increase speed
#     # data = pd.read_csv( DEBUG_DATA, nrows = 10000)
#     # data = data[['passenger_count', 'dropoff_longitude', 'dropoff_latitude']] 
#     # import pdb
#     # pdb.set_trace()
#     # for pc_count in (1, 3):
#     #     filteredData = data[data['passenger_count'] == pc_count]
#     #     make3DHist(dlongbinsize, dlatbinsize, filteredData)

from distance import get_distance
from config import TRAIN_DATA, DEBUG_DATA, FILE_FORMAT

def make3DHist(dlongbinsize, dlatbinsize, data, pc_count):
    """
    float float pandas.DataFrame int -> None

    Given the parameters for binsize, a 2xN matrix of dropoff
    longitudes and latitudes, and the (constant) passenger count for all of 
    those dropoff points, produces (saves to file) a labeled 3DHistogram
    """
    pass

def calcBinSize(num_miles, axis):
    """
    float string(lat|long) -> float

    Given the number of miles along an axis, returns how many units on that
    axis the binsize should be
    """
    assert axis in ("lat", "long")

    increment = 0.000001                # step size for axis unit
    epsilon = 0.001                   # acceptable error
    start_val = 1.0                     # arbitrary starting point for calculation
    lat1, lat2, long1, long2 = (start_val, start_val, start_val, start_val)
    while ((num_miles - get_distance(lat1, long1, lat2, long2)) > epsilon):
        if axis == "lat":
            lat2 += increment
        else:
            long2 += increment

    return max(lat1, lat2, long1, long2) - start_val

def main():
    """
    Based on train_data.csv, produces
    plots of the pdfs (approximated as histograms) of 
        P(passenger count=1|dropoff longitude, dropoff latitude)
        P(passenger count=3|dropoff longitude, dropoff latitude)
    """
    # Calculate bin sizes. We want dlongbinsize to be ~ 1/20 mile, and 
    # dlatbinsize to be ~1/7 of a mile, as this corresponds roughly to a NYC block
    dlongbinsize = calcBinSize(float(1)/20, "long")
    dlatbinsize = calcBinSize(float(1)/7, "lat")
    print "dlongbinsize, dlatbinsize: {}, {}".format(dlongbinsize, dlatbinsize)

    # read relevant data into pandas dataframe
    num_data_points = 10000                       # limit data size to increase speed
    data = pd.read_csv( DEBUG_DATA, nrows = 10000)
    data = data[['passenger_count', 'dropoff_longitude', 'dropoff_latitude']] 
    for pc_count in (1, 3):
        filteredData = data[data['passenger_count'] == pc_count]
    
        #make3DHist(dlongbinsize, dlatbinsize, filteredData)

    # ##### good example
    # fig = plt.figure()
    # ax1 = fig.add_subplot(111, projection='3d')

    # xpos = [1,2,3,4,5,6,7,8,9,10]
    # ypos = [2,3,4,5,1,6,2,1,7,2]
    # zpos = [0,0,0,0,0,0,0,0,0,0]
    # dx = np.ones(10)
    # dy = np.ones(10)
    # dz = [1,2,3,4,5,6,7,8,9,10]

    # ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#00ceaa')
    # ax1.bar3d()

    # plt.show()
    # ####### working example
    # fig = plt.figure()
    # ax1 = fig.add_subplot(111, projection='3d')
    # xpos = filteredData['dropoff_latitude'].tolist()
    # ypos = filteredData['dropoff_longitude'].tolist()
    # zpos = np.zeros(len(dlat))

    # dx = np.ones(10)
    # dy = np.ones(10)
    # dz = [1,2,3,4,5,6,7,8,9,10]

    # ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#00ceaa')
    # ax1.bar3d()

    # plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y = np.random.rand(2, 100) * 4
    hist, xedges, yedges = np.histogram2d(x, y, bins=4)

    elements = (len(xedges) - 1) * (len(yedges) - 1)
    xpos, ypos = np.meshgrid(xedges[:-1]+0.25, yedges[:-1]+0.25)

    xpos = xpos.flatten()
    ypos = ypos.flatten()
    zpos = np.zeros(elements)
    print zpos
    dx = 0.5 * np.ones_like(zpos)
    dy = dx.copy()
    dz = hist.flatten()
    print dz

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')

    plt.show()

## Usage: python A.py
if __name__ == '__main__':
    main()


