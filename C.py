__author__ = 'Faiyam Rahman, Rachel Mayer'

import numpy
from B import euclideanDistance, calcStats

def transformPickupDatetime(row):
    """
    ListOfStringsAndFloats -> ListOfStringsAndFloats

    Operates on rows of 
        [pickup_datetime, pickup_latitude, pickup_longitude, dropoff_latitude, 
         dropoff_longitude, trip_time_in_secs, trip_distance]

    pickup_datetime is a string of format:
        yyyy-mm-dd hh:mm:ss

    Function converts pickup_datetime to a float indicating how many 
    minutes have passed since Midnight.
    """
    # Extract the pickup datetime
    pickup_datetime = row[0]
    assert type(pickup_datetime) == str

    # Convert it to minutes that have elapsed in the day
    dateInfo, timeInfo = pickup_datetime.split(' ')
    num_hours_string, num_minutes_string, num_seconds_string = timeInfo.split(':')
    time_of_day_in_minutes = (int(num_hours_string) * 60) + int(num_minutes_string)

    # Update and return the row
    row[0] = time_of_day_in_minutes
    return row

def main():
    """
    Using 1 nearest neighbor, predicts NYC Taxi trip times based on feature 
    vectors (pickup latitude, pickup longitude, dropoff latitude, dropoff latitude). 

    Tests on a subset of trip_data_1.csv
    """
    # The features we want to operate on
    str_features = ['pickup_datetime']
    float_features = ['pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 
               'dropoff_longitude', 'trip_time_in_secs', 'trip_distance']

    # Load test data
    test_data = load_csv_lazy( TRIP_DATA_2, 
        str_fields=[FILE_FORMAT_REVERSE[feature] for feature in str_features], 
        float_fields=[int(FILE_FORMAT_REVERSE[feature]) for feature in float_features],
        row_tranformer=transformPickupDatetime)

    predictions, true_values = [], []                   # these will hold our results
    for index_test, values_test in enumerate(test_data):
        if index_test % 10 == 0:
            if index_test == 100000:
                break                                   # only do the first 100 k trips
            print "Index Test: {}. Percentage Done: {}".format(index_test, float(index_test)/100000 * 100)
        
        # extract data
        timeofday_test, plat_test, plong_test, dlat_test, dlong_test, trip_time_test, trip_distance_test = values_test
        # load train data
        train_data = load_csv_lazy( TRAIN_DATA, 
            str_fields=[FILE_FORMAT_REVERSE[feature] for feature in str_features], 
            float_fields=[int(FILE_FORMAT_REVERSE[feature]) for feature in float_features],
            row_tranformer=transformPickupDatetime)

        best_distance = float('inf')                    # keeps track of distance
        best_prediction = None                          # tracks best prediction
        for index_train, values_train in enumerate(train_data):

            # Extract the data
            timeofday_train, plat_train, plong_train, dlat_train, dlong_train, trip_time_train, trip_distance_train = values_train

            # Calculate the new distance
            new_distance = euclideanDistance(
                (timeofday_test, plat_test, plong_test, dlat_test, 
                    dlong_test, trip_time_test, trip_distance_test), 
                (timeofday_train, plat_train, plong_train, dlat_train,
                    dlong_train, trip_time_train, trip_distance_train))

            # Update the best prediction and distance if necessary
            if new_distance < best_distance:
                best_distance = new_distance
                best_prediction = trip_time_train

        assert best_prediction                          # Should never be None
        predictions.append(best_prediction)
        true_values.append(trip_time_test)

    # Calculate statistics (Root Mean Squared Error, Correlation Coefficient, Mean Absolute Error)
    rmse, corr, mae = calcStats(numpy.array(predictions), numpy.array(true_values))
    print "Statistics yo:"
    print "-->Root Mean Squared Error: {}".format(rmse)
    print "-->Correlation Coefficient: {}".format(corr)
    print "-->Mean Absolute Error: {}".format(mae)

if __name__ == '__main__':

    # Short test for row transformer
    row_test = [2013-01-01 15:11:48,382,1.00,-73.978165,40.757977,-73.989838,40.751171]
    assert([911.8,382,1.00,-73.978165,40.757977,-73.989838,40.751171] == transformPickupDatetime(row_test))
