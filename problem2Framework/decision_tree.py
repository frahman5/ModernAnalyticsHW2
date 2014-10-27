import scan
import util

class DecisionTree(object):
    node_label = None  # takes the values 0, 1, None. If has the values 0 or 1, then this is a leaf
    left = None
    right = None

    def decision(self, data):
        raise 'not defined'

    def go(self, data):
        if node_label != None:
            return node_label
        return go(decision(data))

# http://en.wikipedia.org/wiki/ID3_algorithm
def train(P, N, training_reviews):
    """
    ListOfStrings ListOfStrings ListOfTuples -> DecisionTree
        P: 500 Most frequent unigrams in positive reviews
        N: 500 Most frequent unigrams in negative reviews
        training_reviews: (review, score) duples where
            - review is a set of unigrams (strings)
            - score is either 1 or 0. 1 means positive, 0 if negative

    Returns a decision Tree based on the ID3 algorithm to determine whether a 
    review is positive or negative
    """
    tree = DecisionTree()

    ## Base Case
    If all reviews are same class (e.g all positive):
        tree.node_label = that class (e.g positive)
        return tree

    ## Recursive Case
    set_of_unigrams_and_frequencies = {(word, count)| words in (P union N), 
                                        and count is total number of occurences
                                        of the word in all the reviews}
        # Calculate maximum information gain
    maxGain = 0
    decisionWord = None
    for word in (N union P):
        x = informationGain(word, set_of_unigrams_and_frequencies)
        if x > maxGain:
            maxGain = x
            decisionWord = word

        # make appropriate decision 
    nowTree.left = train(P, N, all reviews without decisionWord)
    nowTree.right = train(P, N, all reviews with decisionWord)

def test(data):
    raise 'not implemented'

