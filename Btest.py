
__author__ = 'Faiyam Rahman, Rachel Mayer'

import numpy
from config import TRAIN_DATA, TRIP_DATA_2, TRIP_DATA_1, FILE_FORMAT_REVERSE
from code.utils import load_csv_lazy
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
 
 
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
    deltas = y - yhat
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
    # The features we want to operate on
     
    #### Uses sklearn for NN algo
    df_train_read = pd.read_csv(TRAIN_DATA)
    df_test_read = pd.read_csv(TRIP_DATA_1, nrows = 1000000)



    features = ['pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 
               'dropoff_longitude', 'trip_time_in_secs']

    df_test = df_test_read[features].dropna()
    df_train = df_train_read[features].dropna() ##takes first 10000 rows for test data set

    print len(df_train[features[0:4]])
    print len(df_train[features[-1]])

    results = []
    k = 1 
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(df_train[features[0:4]], df_train[features[-1]])
    print "making predictions"
    preds = clf.predict(df_test[features[0:4]])
    print "done with predictions"
    print preds


    # # Load test data
    # test_data = load_csv_lazy( TRIP_DATA_2, str_fields=[], 
    #     float_fields=[int(FILE_FORMAT_REVERSE[feature]) for feature in features] )

    # predictions, true_values = [], []                   # these will hold our results
    # for index_test, values_test in enumerate(test_data):
    #     if index_test % 100 == 0:
    #         if index_test == 100000:
    #             break                                   # only do the first 100 k trips
    #         print "Index Test: {}".format(index_test)

    #     if index_test % 10 == 0:
    #         if index_test == 100000:
    #             break                                   # only do the first 100 k trips
    #         print "Index Test: {}. Percentage Done: {}".format(index_test, float(index_test)/100000 * 100)

        
    #     # extract data
    #     plat_test, plong_test, dlat_test, dlong_test, trip_time_test = values_test

        
    #     # load train dating
    #     train_data = load_csv_lazy( TRAIN_DATA, str_fields=[], 
    #         float_fields=[int(FILE_FORMAT_REVERSE[feature]) for feature in features] )

    #     best_distance = float('inf')                    # keeps track of distance
    #     best_prediction = None                          # tracks best prediction
    #     for index_train, values_train in enumerate(train_data):

    #         # Extract the data
    #         plat_train, plong_train, dlat_train, dlong_train, trip_time_train = values_train

    #         # Calculate the new distance
    #         new_distance = euclideanDistance((plat_test, plong_test, dlat_test, dlong_test), 
    #                                            (plat_train, plong_train, dlat_train, dlong_train))

    #         # Update the best prediction and distance if necessary
    #         if new_distance < best_distance:
    #             best_distance = new_distance
    #             best_prediction = trip_time_train

    #     assert best_prediction                          # Should never be None
    #     predictions.append(best_prediction)
    #     true_values.append(trip_time_test)

    # # Calculate statistics (Root Mean Squared Error, Correlation Coefficient, Mean Absolute Error)
    # rmse, corr, mae = calcStats(numpy.array(predictions), numpy.array(true_values))
    # print "Statistics yo:"
    # print "-->Root Mean Squared Error: {}".format(rmse)
    # print "-->Correlation Coefficient: {}".format(corr)
    # print "-->Mean Absolute Error: {}".format(mae)
    
# Usage: python B.py
if __name__ == '__main__':
    main()
