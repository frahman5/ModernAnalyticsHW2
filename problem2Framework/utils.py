import numpy as np

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

def calc_entropy_of_matrix(sparse_matrix):
    """
    Helper function for informationGain
    """
    column_sums = sparse_matrix.sum(axis=0)[0, :-1]
    total = column_sums.sum(axis=1)[0, 0]
    frequencies = tuple(np.array(column_sums/total)[0])

    return entropy(frequencies)

def removeZeroColumnsOfMatrix(sparse_matrix, nonremovable):
    """
    scipy.sparse.sparsematrix int -> scipy.sparse.sparsematrix ListOfInts

    Helper function for informationGain
    """
    nonzero_indices = np.nonzero(sparse_matrix)
    non_zero_column_indices = list(nonzero_indices[1])       
    unique_nonzero_columns = sorted(set(non_zero_column_indices))
    if nonremovable not in unique_nonzero_columns:                 # to gaurd against removing last column
        unique_nonzero_columns.append(nonremovable) 

    return sparse_matrix[:, unique_nonzero_columns], unique_nonzero_columns

def informationGain(j, training_data):
    """
    int scipy.sparse.csr_matrix -> float scipy.sparse.csr_matrix scipy.sparse.csr_matrix tuple tuple

    Calculates the information gain of word j with respect to the set represented
    by training_data. See decision_tree.train for the structure of the matrix. 
    Returns the gain, the "t1" matrix, the "t2" matrix, and tuples of ints
    indicating which columns were removed from t1 and t2 respectively. 

    IG(word, training_data) = Entropy(S) - p(t1)Entropy(t1) - p(t2)Entropy(t2)
    where S is the training data and
    where t1 is only the rows in training_data with 0 in column word
          and t2 is the only the rows in training_data with 1 in column word
    """
    import scipy.sparse as ss

    ## Calculate Entropy(S)
    entropy_s = calc_entropy_of_matrix(training_data)

    ## Calculate p(t1), Entropy(t1), p(t2), Entropy(t2)
    col_word = training_data.getcol(j)
    total_num_reviews, total_num_cols = training_data.get_shape()
    num_reviews_with_nonzero_val = col_word.nnz
    num_reviews_with_zero_val = total_num_reviews - num_reviews_with_nonzero_val

    # Make t1 and t2
    t1 = ss.lil_matrix((num_reviews_with_zero_val, total_num_cols), dtype='float')
    t2 = ss.lil_matrix((num_reviews_with_nonzero_val, total_num_cols), dtype='float')
    col_word_generator = (elem[0] for elem in col_word.toarray())
    t1_row_index, t2_row_index = 0, 0
    for master_row_index, word_count in enumerate(col_word_generator):
        if word_count == 0:
            t1[t1_row_index, :] = training_data[master_row_index, :]
            t1_row_index += 1
        elif word_count != 0:
            t2[t2_row_index, :] = training_data[master_row_index, :]
            t2_row_index += 1
        else:
            raise "should not happen!"
    
    # Calculate p(t1), p(t2)
    p_t1 = float(num_reviews_with_zero_val)/total_num_reviews
    p_t2 = float(num_reviews_with_nonzero_val)/total_num_reviews

    # Calculate entropy(t1), entropy(t2)
    entropy_t1 = calc_entropy_of_matrix(t1)
    entropy_t2 = calc_entropy_of_matrix(t2)

    ## Calculate information gain, prune t1 and t2,  and return them
    information_gain = entropy_s - (p_t1 * entropy_t1) - (p_t2 * entropy_t2)
    # import pdb
    # pdb.set_trace()
    t1, preserved_columns_1 = removeZeroColumnsOfMatrix(t1, nonremovable=total_num_cols-1)
    t2, preserved_columns_2 = removeZeroColumnsOfMatrix(t2, nonremovable=total_num_cols-1)
    return information_gain, t1.tocsr(), t2.tocsr(), preserved_columns_1, preserved_columns_2

# natural language processing stuff
def freq(reviewAsListOfStrings):
    """
    ListOfStrings -> (Dictionary, int)
        reviewAsListOfStrings: e.g ['this', 'product', 'stinks', 'this', 'sucks!']

    Given a review as a list of strings, outputs a tuple with entries:
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
