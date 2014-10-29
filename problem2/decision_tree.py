import scan
from utils import entropy, informationGain, freq
import scipy.sparse as ss

class DecisionTree(object):

    node_label = None  # takes the values 0, 1, None. If has the values 0 or 1, then this is a leaf
    left = None
    right = None
    decision_word = None

    def decision(self, data):
        assert self.decision_word is not None, "If node is making a decision, should have a decision word"
        if self.decision_word in data:
            return self.right.go(data)
        else:
            return self.left.go(data)

    def go(self, data):
        if self.node_label is not None:
            return self.node_label  
        return self.decision(data)

#http://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.lil_matrix.html#scipy.sparse.lil_matrix
def makeReviewMatrix(PN, training_data):
    """
    ListOfStrings ListOfTuples -> scipy.sparse.csr_matrix
        PN: 500-1000 Most frequent unigrams in positive and negative reviews (
            union of 500 most frequent positive and 500 most frequent negative
            unigrams)        
        training_data: 
            a listOfTuples with (review, score) duples where
            - review is a tuple of unigrams (strings)
            - score is either 1 or 0. 1 means positive, 0 if negative

    returns a scipy.sparse.csr_matrix with structure as defined in "train"
    """
    import numpy as np
    num_reviews = len(training_data)                            # num columns
    num_words = len(PN)                                         # num rows - 1

    ## Construct using a row-based linked list sparse matrix
        # initalize a linked list row-based matrix of size num_reviews x num_words + 1
    lil_matrix = ss.lil_matrix((num_reviews, num_words + 1), dtype=float)
        # add a row at a time
    for index, datum in enumerate(training_data):
        review, score = datum
        frequencyDict, total_words = freq(review)     
            # a_ij is the numbe rof times word j appears in review i, 0 <=j <= n
        counts = [frequencyDict[word] if word in frequencyDict else 0 for word in PN]
            # a_ij is 1 if the review is positive, 0 if negative, j = n+1
        counts.append(score)
            # replace the corresponding index
        lil_matrix[index, :] = np.array([counts])
    
    return lil_matrix.tocsr()

    
# http://en.wikipedia.org/wiki/ID3_algorithm
# http://docs.scipy.org/doc/scipy-0.14.0/reference/sparse.html
depth = 0
MAX_DEPTH = 20
# @profile
def train(PN, training_data):
    """
    ListOfStrings ListOfTuples|scipy.sparse.csr_matrix -> DecisionTree
        PN: 500-1000 Most frequent unigrams in positive and negative reviews (
            union of 500 most frequent positive and 500 most frequent negative
            unigrams)
        training_data: 
            Either a listOfTuples with (review, score) duples where
            - review is a set of unigrams (strings)
            - score is either 1 or 0. 1 means positive, 0 if negative

            Or a m x n+1 scipy.sparse.csc_matrix with:
                Rows 1-m corresponding to reviews.
                Columns 1-n corresponding to words in PN. Column
                n+1 is 1|0 depending on whether or not review n is positive or negative

                a_ij = number of occurences of word j in review i (i<=n, j<=m)
                a_ij = 1 if review i is positive, 0 if review i is negative (i=n+1, j<=m)
                a_ij = 0 otherwise

    Returns a decision Tree based on the ID3 algorithm to determine whether a 
    review is positive or negative
    """
    global depth                                            # to limit tree depth
    global MAX_DEPTH

    tree = DecisionTree()
    depth += 1
    print "depth: {}".format(depth)

    # Construct a sparse matrix if necessary
    if type(training_data) == list:
        training_data = makeReviewMatrix(PN, training_data)
        print "made master training data matrix"

    ## Base Case
    num_positive_reviews = training_data.sum(axis=0)[0,-1]   # sum of entries in far right column
    num_reviews = training_data.get_shape()[0]
    if num_positive_reviews == num_reviews:                  # all reviews positive
        tree.node_label = 1
        return tree
    elif num_positive_reviews == 0:                          # all reviews negative
        tree.node_label = 0
        return tree
    elif training_data.get_shape()[1] == 1:                  # mixed reviews, but no words left to decide on
        tree = makeNonconclusiveLeafNode(tree, num_positive_reviews, num_reviews)
        return tree
    elif depth == MAX_DEPTH:                                 # hit max depth
        print "hit max depth"
        tree = makeNonconclusiveLeafNode(tree, num_positive_reviews, num_reviews)
        return tree

    ## Recursive Case
        # Determine which word offers maximum information gain
    maxGain = -1 * float('inf')                              # in case all igs are zero
    left_tree, right_tree, decision_word = None, None, None
    left_column_indices, right_column_indices = None, None
    for index, review_data in enumerate(PN):
        word, score = review_data
        ig_x, t1, t2, pn1_indices, pn2_indices = informationGain(index, training_data)
        if ig_x > maxGain:
            maxGain = ig_x
            left_tree = t1
            right_tree = t2
            decision_word = word
            left_column_indices = pn1_indices
            right_column_indices = pn2_indices

        ## If the left tree exists (i.e there are training data that dont 
        ## have the word), then recurse. Otherwise label the left tree
        ## with whatever is the majority score of the reviews
        ## in the current training data. Do the same for right_tree
    tree.decision_word = decision_word 
    if left_tree is not None:
        tree.left = train((word for index, word in enumerate(PN) if index in 
                           left_column_indices), left_tree)
    else:
        tree.left = makeNonconclusiveLeafNode(tree.left, num_positive_reviews, num_reviews)
    if right_tree is not None:
        tree.right = train((word for index, word in enumerate(PN) if index in 
                            right_column_indices), right_tree)
    else:
        tree.right = makeNonconclusiveLeafNode(tree.right, num_positive_reviews, num_reviews)

    return tree

def makeNonconclusiveLeafNode(decision_tree_child, num_positive_reviews, num_reviews):
    decision_tree_child = DecisionTree()
    decision_tree_child.node_label = 0
    if float(num_positive_reviews) / num_reviews > 0.5:
        decision_tree_child.node_label = 1
    return decision_tree_child

def test(decision_tree, data):
    from config import RESULTS2F

    total_reviews = len(data)
    num_correct = 0.0
    for review_tuple, score in data:
        test_result = decision_tree.go(review_tuple)
        if test_result == score:
            num_correct += 1.0

    percent_accurate = round((num_correct / total_reviews) * 100, 4)
    with open(RESULTS2F, 'a') as f:
        f.write('\n')
        f.write('{}% correct of {}'.format(percent_accurate, total_reviews))
        print "Wrote test results to: {}".format(RESULTS2F)

    return percent_accurate


if __name__ == '__main__':
    PN = ['good', 'bad', 'heyyo!']
    training_data = [(('this', 'product', 'is', 'good'), 1),
                     (('this', 'product', 'is', 'bad'), 0), 
                     (('this', 'is', 'ok,', 'heyyo!'), 1)]

    decision_tree = train(PN, training_data)
    print decision_tree.go(('this', 'is', 'ok,', 'heyyo!'))
    print decision_tree.go(('this', 'product', 'is', 'bad'))
    print decision_tree.go(('this', 'product', 'is', 'good'))

    # INSERT CODE To RUN makeReviewMatrix