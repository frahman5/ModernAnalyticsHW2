import re, string
import nltk
from nltk.corpus import stopwords

# constants
LINES_PER_REVIEW = 8
BINARY = True
NONWORDS = re.compile('[\W_]+')
STOPWORDS = stopwords.words('english')
LENGTH_OF_STANDARD_INPUT_FILE = 5116086

# read in a file
def scan(filename, exclude_stopwords = False, binary_label = False):
    """
    string bool bool -> ListOfTuples
        filename: pathname of input file
        exclude_stopwords: if True, ignores all words that indicate stops in english, I think
        binary_label: if True, reports scores as 1|0 depending on criteria in score_to_binary

    OutputTuples are of the form (string, float|int) interpreted as (review, review_score)
    """
    data = []
    line_number = 0
    with open(filename, 'r') as f:
        keep_going = True
        while keep_going:
            # read in LINES_PER_REVIEW lines from finefoods.txt
            elements = []
            for i in range(LINES_PER_REVIEW):
                line = f.readline()
                # print("line: {}".format(line))
                # print("i: {}".format(i))
                elements.append(line.split(':', 1)[1])
            line_number += LINES_PER_REVIEW

            # strip out the review
            review = (elements[6] + ' ' + elements[7])
            review = ' '.join(re.split(NONWORDS, review))
            review = review.strip().lower()

            # Remove stopwords
            if exclude_stopwords:
                review = ' '.join([w for w in review.split() if w not in STOPWORDS])

            # Extract the score
            score = float(elements[4].strip())
            if binary_label:
                score = score_to_binary(score)
            
            # Update data
            datum = [review, score]
            data.append(datum)

            # Read the next empty line
            f.readline()
            line_number += 1

            # Determine whether or not to continue
            if line_number >= LENGTH_OF_STANDARD_INPUT_FILE:
                keep_going = False

    return data

def score_to_binary(score):
    if score >= 4:
        return 1
    else:
        return 0
