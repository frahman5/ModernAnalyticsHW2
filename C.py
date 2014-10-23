__author__ = 'Faiyam Rahman, Rachel Mayer'

import numpy
import pandas as pd
from config import TRAIN_DATA, TRIP_DATA_1, FILE_FORMAT_REVERSE
from code.utils import calcStats
from sklearn.neighbors import KNeighborsClassifier

def transformPickupDatetime(pickup_datetime):
    """
    string -> float

    pickup_datetime is a string of format:
        yyyy-mm-dd hh:mm:ss

    Function converts pickup_datetime to a float indicating how many 
    minutes have passed since Midnight.
    """
    # Extract the pickup datetime
    assert type(pickup_datetime) == str

    # Convert it to minutes that have elapsed in the day
    dateInfo, timeInfo = pickup_datetime.split(' ')
    num_hours_string, num_minutes_string, num_seconds_string = timeInfo.split(':')
    time_of_day_in_minutes = (int(num_hours_string) * 60) + int(num_minutes_string)

    return time_of_day_in_minutes

def main():
    """
    Using 1 nearest neighbor, predicts NYC Taxi trip times based on feature 
    vectors (pickup latitude, pickup longitude, dropoff latitude, dropoff latitude). 

    Tests on a subset of trip_data_1.csv
    """
    features = ['pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 
               'dropoff_longitude', 'trip_distance', 'pickup_datetime', 
               'trip_time_in_secs']

    ## Extract necessary data into pandas dataframes
        # Read them in
    df_train_read = pd.read_csv(TRAIN_DATA)
    df_test_read = pd.read_csv(TRIP_DATA_1, nrows = 1000000)    # first 100k rows, for speed
        # Extract desired features and drop null values
    df_test = df_test_read[features].dropna()
    df_train = df_train_read[features].dropna() 
        # Transform pickup_datetime
    df_test['pickup_datetime'] = df_test['pickup_datetime'].apply(transformPickupDatetime)
    df_train['pickup_datetime'] = df_train['pickup_datetime'].apply(transformPickupDatetime)

    ## Use sklearn to run nearest neighbors
    k = 1 
    clf = KNeighborsClassifier(n_neighbors=k)                   # default distance metric: euclidean
    clf.fit(df_train[features[0:6]], df_train[features[-1]])
    preds = clf.predict(df_test[features[0:6]])

    # Calculate statistics (Root Mean Squared Error, Correlation Coefficient, Mean Absolute Error)
    print "Calculating statistics"
    rmse, corr, mae = calcStats(numpy.array(preds), numpy.array(df_test[features[-1]]))
    print "-->Root Mean Squared Error: {}".format(rmse)
    print "-->Correlation Coefficient: {}".format(corr)
    print "-->Mean Absolute Error: {}".format(mae)
    
if __name__ == '__main__':

    main()
