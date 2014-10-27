# decision tree stuff
def entropy():
    raise 'not implemented'

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
