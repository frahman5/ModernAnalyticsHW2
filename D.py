__author__ = 'Faiyam Rahman, Rachel mayer'

import numpy
import pandas as pd
from config import TRAIN_DATA, TRIP_DATA_1, RESULTS1D
from code.utils import calcAndLogStats, transformPickupDatetime
from sklearn.neighbors import KNeighborsClassifier

def main(k=1, output=RESULTS1D, weights='uniform'):
    """
    int -> None

    Using 1 nearest neighbor, predicts NYC Taxi trip times based on feature 
    vectors (pickup latitude, pickup longitude, dropoff latitude, dropoff latitude). 

    Tests on a subset of trip_data_1.csv

    K indicates how how many nearest neighbors to use in the nearest neighbors
    algorithm. 
    """
    features = ['pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 
               'dropoff_longitude', 'trip_distance', 'pickup_datetime', 
               'trip_time_in_secs']

    ## Extract necessary data into pandas dataframes
        # Read them in
    numrows = 100000 # ten thousand 
    df_train_read = pd.read_csv(TRAIN_DATA)
    df_test_read = pd.read_csv(TRIP_DATA_1, nrows = numrows)    # first 100k rows, for speed
        # Extract desired features and drop null values
    df_test = df_test_read[features].dropna()
    df_train = df_train_read[features].dropna() 
        # Transform pickup_datetime
    df_test['pickup_datetime'] = df_test['pickup_datetime'].apply(transformPickupDatetime)
    df_train['pickup_datetime'] = df_train['pickup_datetime'].apply(transformPickupDatetime)
        # Seperate out features
    df_test_features = df_test[features[0:6]]
    df_train_features = df_train[features[0:6]]
        # Normalize
    df_train_features_norm = (df_train_features - df_train_features.mean())/df_train_features.std()
    df_test_features_norm = (df_test_features - df_train_features.mean())/df_train_features.std()
    print "finished normzalizing data sets"

    ## Use sklearn to run nearest neighbors
    clf = KNeighborsClassifier(n_neighbors=k, weights=weights)                   # default distance metric: euclidean
    clf.fit(df_train_features_norm, df_train[features[-1]])
    preds = clf.predict(df_test_features_norm)

    # Calculate statistics (Root Mean Squared Error, Correlation Coefficient, Mean Absolute Error)
    with open(output, "a+") as outputFile:
        outputFile.write("Ran knn with k={}, using {}".format(k, weights) + \
            " weighting (voting). Trained on {}. Tested on first".format(TRAIN_DATA) + \
            " {} rows of {}. Stats:".format(numrows, TRIP_DATA_1))
    calcAndLogStats( numpy.array(preds), 
                     numpy.array(df_test[features[-1]]), 
                     output=output)


if __name__ == '__main__':
    main()