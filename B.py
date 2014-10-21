
__author__ = 'Faiyam Rahman, Rachel Mayer'

from config import TRAIN_DATA, TRIP_DATA_2

def euclideanDistance(vector1, vector2):
    """
    TupleOfFloats TupleOfFloats -> float

    Given two length-n vectors, returns the euclidean distance between them
    """
    import math
    distance = 0
    for x in range(length(vector1)):
        distance += pow((vector1[x] - vector2[x]), 2)
    return math.sqrt(distance)

    v1 = [-73.978165,40.757977,-73.989838,40.75117]
    v2 = [-74.006683,40.731781,-73.994499,40.75066]

    print euclideanDistance(v1,v2,4)




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

