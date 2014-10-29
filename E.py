__author__ = 'Faiyam Rahman, Rachel mayer'

from config import RESULTS1E

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
        for w in ['uniform', 'distance', lambda x: np.median(x)]: ## testing to see which metric is more accurate
            D.main(k=k, output = output, weights = w)


if __name__ == '__main__':
    import numpy as np
    ## Short unit test for medianVote
    # start_array_1 = np.array([1.223452345, 2.23452345, 3.12345, 4.23452345, 5.23452345, 3.12345])
    # assert np.array_equal(medianVote(start_array_1), np.array((0, 0, 0.5, 0, 0, 0.5)))

    # start_array_2 = np.array([1, 3, 2, 4, 5])
    # assert np.array_equal(medianVote(start_array_2), np.array((0, 1, 0, 0, 0)))
    # print "all tests passed yo!"
    
    main()

