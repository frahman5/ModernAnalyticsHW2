__author__ = 'Faiyam Rahman, Rachel Mayer'

from config import FINEFOODS, RESULTS2B
from problem2Framework.utils import get_unigram

def updateUnigramList(unigramList, unigram, count):
    """
    listOfTuples string int -> listOfTuples

    UnigramList: Each tuple is of form (string, int). e.g ('hello', 5)
    unigram: a word we want to consider adding to the list
    reviewCount: number of time the unigram occurs 

    If the given unigram is more frequent than the least frequent unigram in 
    unigramList, inserts it and sorts the list

    ** HAS SIDE EFFECTS ON UNIGRAMLIST **
    """
    if count > unigramList[0][1]:
        unigramList[0] = (unigram, count)
    unigramList.sort(key=lambda t: t[1])            # sort based on count

# @profile
def main(results_file=RESULTS2B, exclude_stopwords=False, num_top_unigrams=30):
    from problem2Framework import scan

    # Extract list of unigrams from finefoods.txt
    binary_label = True
    data = scan.scan( FINEFOODS, exclude_stopwords=exclude_stopwords, 
                      binary_label= binary_label) #[(review, score)...(review, score)]
    print "finished scanning in data"
    
    masterDict = {} #{'word': [negative_review_count, positive_review_count], ...}
    keys = set([])
    for index, datum in enumerate(data):
        if index % 1000 == 0:
            print index
        review, score = datum
        unigram, num_words = get_unigram(review) # ({'word1': num_occurences, ..., 'wordn': num_occurences}, total_occurences)
        for word in unigram:
            if word not in keys:
                keys.add(word)
            # if word not in masterDict.keys():
                masterDict[word] = [0, 0]
            masterDict[word][score] += unigram[word]
    print "finished creating master dictionary"

    # Extract relevant data
    mostFrequentUnigrams = [('', 0) for i in range(num_top_unigrams)] 
    mostFrequentNegativeUnigrams = [('', 0) for i in range(num_top_unigrams)]
    mostFrequentPositiveUnigrams = [('', 0) for i in range(num_top_unigrams)]
    for unigram, reviewCount in masterDict.iteritems():
        badReviewCount, positiveReviewCount = reviewCount
        totalCount = sum(reviewCount)

        updateUnigramList(mostFrequentUnigrams, unigram, totalCount)
        updateUnigramList(mostFrequentNegativeUnigrams, unigram, badReviewCount)
        updateUnigramList(mostFrequentPositiveUnigrams, unigram, positiveReviewCount)

    with open(results_file, "a+") as outputFile:
        outputFile.write("\n")
        outputFile.write("{} Most Frequent Unigrams\n".format(num_top_unigrams))
        outputFile.write(str(mostFrequentUnigrams) + "\n")
        outputFile.write("{} Most Frequent Negative Unigrams\n".format(num_top_unigrams))
        outputFile.write(str(mostFrequentNegativeUnigrams) + "\n")
        outputFile.write("{} Most Frequent Positive Unigrams\n".format(num_top_unigrams))
        outputFile.write(str(mostFrequentPositiveUnigrams) + "\n")
        print "Logged output to {}".format(results_file)

if __name__ == '__main__':
    main()