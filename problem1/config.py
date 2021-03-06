__author__ = 'aub3'
"""
All constants should go here.
"""

# EXAMPLE_DATA = "data/example_data.csv" # small data files (ideally < 5 MB) should be stored in data folder
# TRIP_DATA_1 = "/Users/aub3/code/taxidata/trip_data_1.csv" # Large data files can be outside your directory structure
# TRIP_DATA_2 = "/Users/aub3/code/taxidata/trip_data_2.csv" # Large data files can be outside your directory structure
# TRAIN_DATA = "/Users/aub3/code/taxidata/train_data.csv" # contains every 20th trip from trip_data_2.csv


ROOT = "/Users/rachel/CS5785/ModernAnalyticsHW2"
#ROOT = "/Users/faiyamrahman/Documents/CTech/ModernAnalytics/Homework2"
# ROOT = "/Users/faiyamrahman/Documents/CTech/ModernAnalytics/Homework2"
# ROOT = "/home/faiyamrahman/ModernAnalyticsHW2"

## Problem 1 data locations
EXAMPLE_DATA = ROOT + "/data/example_data.csv"
TRAIN_DATA = ROOT + "/data/train_data.csv"
TRIP_DATA_2 = ROOT + "/data/trip_data_2.csv"
TRIP_DATA_1 = ROOT + "/data/trip_data_1.csv"

## Problem 2 data locations
FINEFOODS = ROOT + "/data/finefoods.txt"

FILE_FORMAT ={
    '0':'medallion',
    '1':'hack_license',
    '2':'vendor_id',
    '3':'rate_code',
    '4':'store_and_fwd_flag',
    '5':'pickup_datetime',
    '6':'dropoff_datetime',
    '7':'passenger_count',
    '8':'trip_time_in_secs',
    '9':'trip_distance',
    '10':'pickup_longitude',
    '11':'pickup_latitude',
    '12':'dropoff_longitude',
    '13':'dropoff_latitude'
}


# FILE_FORMAT_REVERSE = {value:key for key, value in FILE_FORMAT.iteritems()}

F_FIELDS  = [8,9,10,11,12,13] # Float fields
S_FIELDS = [5,] # String fields

## Where results go`
RESULTS1B = ROOT + "/output/results1B.txt"
RESULTS1C = ROOT + "/output/results1C.txt"
RESULTS1D = ROOT + "/output/results1D.txt"
RESULTS1E = ROOT + "/output/results1E.txt"
RESULTS1ETEST = ROOT + "/output/results1Etest.txt"

RESULTS2B = ROOT + "/output/results2B.txt"
RESULTS2C = ROOT + "/output/results2C.txt"
RESULTS2E = ROOT + "/output/results2E.txt"
RESULTS2F = ROOT + "/output/results2F.txt"
