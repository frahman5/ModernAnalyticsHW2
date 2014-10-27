import re, string
import nltk
from nltk.corpus import stopwords

# constants
LINES_PER_REVIEW = 8
BINARY = True
NONWORDS = re.compile('[\W_]+')
STOPWORDS = stopwords.words('english')

# read in a file
def scan(filename, exclude_stopwords = False, binary_label = False):
<<<<<<< HEAD
    """
    string bool bool -> ListOfTuples
        filename: pathname of input file
        exclude_stopwords: if True, ignores all words that indicate stops in english, I think
        binary_label: if True, reports scores as 1|0 depending on criteria in score_to_binary

    OutputTuples are of the form (string, float|int) interpreted as (review, review_score)
    """

=======
>>>>>>> 5694e8c56611e34ea464bc051153154560b974b6
    data = []
    with open(filename, 'r') as f:
        elements = []
        for i in range(LINES_PER_REVIEW):
            elements.append(f.readline().split(':', 1)[1])

        review = (elements[6] + ' ' + elements[7])
        review = ' '.join(re.split(NONWORDS, review))
        review = review.strip().lower()

        if exclude_stopwords:
            review = ' '.join([w for w in review.split() if w not in STOPWORDS])

        score = float(elements[4].strip())

        if binary_label:
            score = score_to_binary(score)

        datum = [review, score]
        data.append(datum)
    return data

def score_to_binary(score):
    if score >= 4:
        return 1
    else:
        return 0
