
__author__ = 'Faiyam Rahman, Rachel Mayer'

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
    pass

# Usage: python B.py
if __name__ == '__main__':
    main()

