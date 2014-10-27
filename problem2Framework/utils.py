# decision tree stuff
def entropy(frequencies):
    """
    tupleOfFrequencies -> float
        frequencies: A probability distribution (i.e sum(frequencies) = 1)

    Calculates the entropy of the given tupleOfFrequencies. 
    """
    import math

    entropy = 0
    for frequency in frequencies:
        if frequency == 0:
            continue
        entropy -= frequency * math.log(frequency, 10)
    return entropy


def information_gain():
    raise 'not implemented'

# natural language processing stuff
def freq(reviewAsListOfStrings):
    """
    ListOfStrings -> (Dictionary, int)
        reviewAsListOfStrings: e.g ['this', 'product', 'stinks', 'this', 'sucks!']

    Given a review as a list of strings, a tuple with entries:
        1) Dictionary with key, value pairs (string, frequency) e.g ('this', 2)
        2) The number of words in the input list as an int (e.g 5)
    """
    dictOfFreqs = {}
    num_unigrams = len(reviewAsListOfStrings)
    for unigram in reviewAsListOfStrings:
        if unigram not in dictOfFreqs.keys():
            dictOfFreqs[unigram] = 0
        dictOfFreqs[unigram] += 1
        
    return (dictOfFreqs, num_unigrams)

def get_unigram(review):
    return freq(review.split())

def get_unigram_list(review):
    return get_unigram(review).keys()

if __name__ == '__main__':
    print entropy([1.0/2, 1.0/2])
    # x = (5.0/14) * entropy((2.0/5, 3.0/5)) + (4.0/14) * entropy((1, 0)) + (5.0/14) * entropy((3.0/5, 2.0/5))
    # print x
