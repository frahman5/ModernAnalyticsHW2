__author__ = 'Faiyam Rahman, Rachel Mayer'

import numpy
import pandas as pd
from config import TRAIN_DATA, TRIP_DATA_2

def euclideanDistance(vector1, vector2):
    """
    TupleOfFloats TupleOfFloats -> float

    Given two length-n vectors, returns the euclidean distance between them
    """
    assert len(vector1) == len(vector2)                 # defense yo
    import math

    distance = 0
    for x in range(len(vector1)):
        distance += pow((vector1[x] - vector2[x]), 2)
    return math.sqrt(distance)

def calcStats(y, yhat):
    """
    numpy.array numpy.array -> (float, float, float)

    Given two length n lists, returns values for the following statistics:
        Root Mean Squared Error (RMSE)
        Correlation Coefficient
        Mean Absolute Error
    """
    deltas = y-yhat
    dimension = len(y)

    ols_error = sum(numpy.square((deltas)))
    rmse = (ols_error/dimension)**0.5
    corr = numpy.corrcoef(y,yhat)
    mean_absolute_error = (sum(numpy.absolute((deltas))))/dimension

    return rmse, corr, mean_absolute_error

def main():
    """
    Using 1 nearest neighbor, predicts NYC Taxi trip times based on feature 
    vectors (pickup latitude, pickup longitude, dropoff latitude, dropoff latitude). 

    Tests on a subset of trip_data_1.csv
    """
    features = ['pickup latitude', 'pickup longitude', 'dropoff_latitude', 
               'dropoff_longitude', 'trip_time_in_secs']
    # Train
    train_data = pd.read_csv( TRAIN_DATA )[features]

    # Test
    limit = 100000
    test_data = pd.read_csv( TRIP_DATA_2 , nrows=limit)[features]
    predictions, true_values = [], []
    for plat_test, plong_test, dlat_test, dlong_test, trip_time_test in test_data.itertuples():
        distances = []
        for plat_train, plong_train, dlat_train, dlong_train, trip_time_train in train_data.itertuples():
            distances.append(euclideanDistance((plat_test, plong_test, dlat_test, d_long_test), 
                                               (plat_train, plong_train, dlat_train, dlong_train)))
            nearest_neighbor_index = distances.index(min(distances))
            predictions.append(train_data['trip_time_in_secs'][nearest_neighbor_index])
            true_values.append(trip_time_test)

    # Calculate statistics (Root Mean Squared Error, Correlation Coefficient, Mean Absolute Error)
    rmse, corr, mae = calcStats(numpy.array(predictions), numpy.array(true_values))
    print "Statistics yo:"
    print "-->Root Mean Squared Error: {}".format(rmse)
    print "-->Correlation Coefficient: {}".format(corr)
    print "-->Mean Absolute Error: {}".format(mae)
    
# Usage: python B.py
if __name__ == '__main__':
    main()

