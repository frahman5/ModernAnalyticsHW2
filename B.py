__author__ = 'Faiyam Rahman, Rachel Mayer'

from config import TRAIN_DATA, TRIP_DATA_2

def euclideanDistance(vector1, vector2):
    """
    TupleOfFloats TupleOfFloats -> float

    Given two length-n vectors, returns the euclidean distance between them
    """
    pass

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
    test_data = pd.read_csv( TRIP_DATA_2 )[features]
    predictions, true_values = [], []
    for plat_test, plong_test, dlat_test, dlong_test, trip_time_test in test_data.itertuples():
        distances = []
        for plat_train, plong_train, dlat_train, dlong_train, trip_time_train in train_data.itertuples():
            distances.append(euclideanDistance((plat_test, plong_test, dlat_test, d_long_test), 
                                               (plat_train, plong_train, dlat_train, dlong_train)))
            nearest_neighbor_index = distances.index(min(distances))
            predictions.append(train_data['trip_time_in_secs'][nearest_neighbor_index])
            true_values.append(trip_time_test)

    # Calculate statistics
    pass
    
# Usage: python B.py
if __name__ == '__main__':
    main()
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