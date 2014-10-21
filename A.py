# __author__ = 'Faiyam Rahman, Rachel Mayer'

# import pandas as pd
# import numpy as np
# from config import TRAIN_DATA, DEBUG_DATA, FILE_FORMAT

# def make3DHist(dlongbinsize, dlatbinsize, data, pc_count):
#     """
#     float float np.array int(1|3) -> ???

#     Given the parameters for binsize and a matrix of data
#     and the pc count for that data 
#     produces (saves to file) a 3DHistogram
#     """
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

xpos = [1,2,3,4,5,6,7,8,9,10]
ypos = [2,3,4,5,1,6,2,1,7,2]
num_elements = len(xpos)
zpos = [0,0,0,0,0,0,0,0,0,0]
dx = np.ones(10)
dy = np.ones(10)
dz = [1,2,3,4,5,6,7,8,9,10]

ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#00ceaa')

plt.show()
break

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


## Usage: python A.py
if __name__ == '__main__':
    main()


