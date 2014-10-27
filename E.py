__author__ = 'Faiyam Rahman, Rachel mayer'

from config import RESULTS1E

def medianVote(start_array):
    """
    ArrayOfFloats -> ArrayOfFloats

    Given a start_array of k distances, returns a length k end_array where 
        end_array[i] = { 0 if start_array[i] != median(start_array)
                         1/w if start_array[i] = median(start_array)
                        }
            where w < k is the number of entries in start_array equal to
            the median of start_array

    Essentially, implements a uniform weighting over the medians in the array
    """
    # Calculate median
    import numpy as np
    median = np.median(start_array)
    assert median in start_array                        # safety yo

    # Construct weight array
    maybe_end_array = [1 if elem == median else 0 for elem in start_array]
    num_medians = sum(maybe_end_array)
    end_array = maybe_end_array                         # if num_medians == 1
    if num_medians != 1:
        uniform_weight = float(1)/num_medians
        end_array = [uniform_weight if elem == 1 else 0 for elem in maybe_end_array]

    return tuple(end_array)

def main(output=RESULTS1E):
    """
    Runs kNN with k going from 5 to 20, and reports results to
    output/results1E.txt
    """
    import D              # runs k nearest algorithm with static k

    # print a header on the output file
    with open(output, "a+") as outputFile:
        output.write("*** RUNNING kNN with k ranging from 5 to 21 ***\n")

    # Run knn hella times!
    for k in range(5, 21):
        print "Running Knn with K={}\n".format(k)
        D.main(k=k, output=output, weights=medianVote)

if __name__ == '__main__':
    ## Short unit test for medianVote
    start_array_1 = [1, 2, 3, 4, 5, 3]                    # median  = 3
    assert medianVote(start_array_1) == (0, 0, 0.5, 0, 0, 0.5)

    start_array_2 = [1, 3, 2, 4, 5]
    assert (medianVote(start_array_2) == (0, 1, 0, 0, 0))
    print "all tests passed yo!"
    
    main()

