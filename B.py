__author__ = 'Faiyam Rahman, Rachel Mayer'

import numpy
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from config import TRAIN_DATA, TRIP_DATA_1, RESULTS1B
from code.utils import calcAndLogStats

def main(output=RESULTS1B):
    """
    Using 1 nearest neighbor, predicts NYC Taxi trip times based on feature 
    vectors (pickup latitude, pickup longitude, dropoff latitude, dropoff latitude). 

    Tests on a subset of trip_data_1.csv

    Uses sklearn to implement nearest neighbors
    """
    features = ['pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 
               'dropoff_longitude', 'trip_time_in_secs']

    ## Extract necessary data into pandas dataframes
    numrows = 10000
    df_train_read = pd.read_csv(TRAIN_DATA)
    df_test_read = pd.read_csv(TRIP_DATA_1, nrows = numrows)    # first 100k rows, for speed
    df_test = df_test_read[features].dropna()
    df_train = df_train_read[features].dropna() 

    print df_test.head()
    print df_train.head()


    ## Use sklearn to run nearest neighbors
    k = 1 
    clf = KNeighborsClassifier(n_neighbors=k)                   # default distance metric: euclidean
    clf.fit(df_train[features[0:4]], df_train[features[-1]])
    preds = clf.predict(df_test[features[0:4]])

    # # Calculate statistics (Root Mean Squared Error, Correlation Coefficient, Mean Absolute Error)
    print "Calculating statistics"
    with open(output, "a+") as outputFile:
        outputFile.write("Ran knn with k={}".format(k) + \
            " Trained on {}. Tested on first".format(TRAIN_DATA) + \
            " {} rows of {}. Stats:".format(numrows, TRIP_DATA_1))
    calcAndLogStats( numpy.array(preds), 
                     numpy.array(df_test[features[-1]]), 
                     output=output)
    
# Usage: python B.py
if __name__ == '__main__':
    main()
