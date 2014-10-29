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

    # Gaurd against corner case
    if total == 0:
        frequencies = tuple(np.array(column_sums)[0])
    else:
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

# @profile
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
    import numpy as np

    ## Calculate Entropy(S)
    entropy_s = calc_entropy_of_matrix(training_data)

    ## Calculate p(t1), Entropy(t1), p(t2), Entropy(t2)
    col_word = training_data.getcol(j)
    total_num_reviews, total_num_cols = training_data.get_shape()
    num_reviews_with_nonzero_val = col_word.nnz
    num_reviews_with_zero_val = total_num_reviews - num_reviews_with_nonzero_val

    # Make t1 and t2
    t1_exists = num_reviews_with_zero_val > 0           # gaurd against height 0 matrices 
    t2_exists = num_reviews_with_nonzero_val > 0        # throwing errors
    t1, t2 = None, None                                 # placeholder values
    col_word_generator = (elem[0] for elem in col_word.toarray())
    t1_numpy_array, t2_numpy_array = None, None
    for master_row_index, word_count in enumerate(col_word_generator):
        next_row = training_data[master_row_index, :].toarray()
        if word_count == 0:
            assert t1_exists, "if word count is 0, we should have a left tree!"
            if t1_numpy_array is None:
                t1_numpy_array = next_row
            else:
                t1_numpy_array = np.append(t1_numpy_array, next_row, 0)
        elif word_count != 0:
            assert t2_exists, "if word count is nonzero, we should have a right tree!"
            if t2_numpy_array is None:
                t2_numpy_array = next_row
            else:
                t2_numpy_array = np.append(t1_numpy_array, next_row, 0)
        else:
            raise "should not happen!"
    if t1_exists:
        t1 = ss.csr_matrix(t1_numpy_array)
    if t2_exists:
        t2 = ss.csr_matrix(t2_numpy_array)
    
    # Calculate p(t1), p(t2)
    p_t1 = float(num_reviews_with_zero_val)/total_num_reviews
    p_t2 = float(num_reviews_with_nonzero_val)/total_num_reviews

    # Calculate entropy(t1), entropy(t2), and transform matrices if needbe
    entropy_t1 = 0.0                                    # placeholder value
    preserved_columns_1 = None                          # placeholder value
    if t1_exists:   
        entropy_t1 = calc_entropy_of_matrix(t1)
        t1, preserved_columns_1 = removeZeroColumnsOfMatrix(t1, nonremovable=total_num_cols-1)
                                        
    entropy_t2 = 0.0                                    # placeholder value
    preserved_columns_2 = None                          # placeholder value
    if t2_exists:
        entropy_t2 = calc_entropy_of_matrix(t2)
        t2, preserved_columns_2 = removeZeroColumnsOfMatrix(t2, nonremovable=total_num_cols-1)              

    ## Calculate information gain, prune t1 and t2,  and return them
    information_gain = entropy_s - (p_t1 * entropy_t1) - (p_t2 * entropy_t2)
    
    return information_gain, t1, t2, preserved_columns_1, preserved_columns_2

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

