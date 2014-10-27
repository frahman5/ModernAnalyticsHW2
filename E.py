__author__ = 'Faiyam Rahman, Rachel mayer'

from config import RESULTS1E

def medianVote(distance_array):
    """
    np.ArrayOfFloats -> np.ArrayOfFloats

    Given a distance_array of k distances, returns a length k end_array where 
        end_array[i] = { 0 if distance_array[i] != median(distance_array)
                         1/w if distance_array[i] = median(distance_array)
                        }
            where w < k is the number of entries in distance_array equal to
            the median of distance_array

    Essentially, implements a uniform weighting over the medians in the array
    """
    import numpy as np

    # Calculate median
    distance_array = distance_array.round(decimals=4)         # round to handle float comparison issues
    median = np.median(distance_array)
    assert median in distance_array                        # safety yo

    # Construct weight array
    np.place(distance_array, distance_array!=median, [0])
    np.place(distance_array, distance_array==median, [1])
    num_medians = distance_array.sum()
    print "Number of medians in distance_array: {}".format(num_medians)
    if num_medians != 1:
        np.place(distance_array, distance_array==1, [float(1)/num_medians])

    return distance_array

def main(output=RESULTS1E):
    """
    Runs kNN with k going from 5 to 20, and reports results to
    output/results1E.txt
    """
    import D              # runs k nearest algorithm with static k

    # print a header on the output file
    with open(output, "a+") as outputFile:
        outputFile.write("*** RUNNING kNN with k ranging from 5 to 21 ***\n")

    # Run knn hella times!
    for k in range(5, 21):
        print "Running Knn with K={}\n".format(k)
        D.main(k=k, output=output, weights=medianVote)

if __name__ == '__main__':
    import numpy as np
    ## Short unit test for medianVote
    start_array_1 = np.array([1.223452345, 2.23452345, 3.12345, 4.23452345, 5.23452345, 3.12345])
    assert np.array_equal(medianVote(start_array_1), np.array((0, 0, 0.5, 0, 0, 0.5)))

    start_array_2 = np.array([1, 3, 2, 4, 5])
    assert np.array_equal(medianVote(start_array_2), np.array((0, 1, 0, 0, 0)))
    print "all tests passed yo!"
    
    main()

