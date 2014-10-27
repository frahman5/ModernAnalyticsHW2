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

def main():
    from problem2Framework import scan

    # Extract list of unigrams from finefoods.txt
    binary_label = True
    data = scan.scan(FINEFOODS, binary_label= binary_label) #[(review, score)...(review, score)]
    print "finished scanning in data"
    
    masterDict = {} #{'word': [negative_review_count, positive_review_count], ...}
    for review, score in data:
        unigram, num_words = get_unigram(review) # ({'word1': num_occurences, ..., 'wordn': num_occurences}, total_occurences)
        for word in unigram:
            if word not in masterDict.keys():
                masterDict[word] = [0, 0]
            masterDict[word][score] += unigram[word]
    print "finished creating master dictionary"

    # Extract relevant data
    mostFrequentUnigrams = [('', 0) for i in range(30)] 
    mostFrequentNegativeUnigrams = [('', 0) for i in range(30)]
    mostFrequentPositiveUnigrams = [('', 0) for i in range(30)]
    for unigram, reviewCount in masterDict.iteritems():
        badReviewCount, positiveReviewCount = reviewCount
        totalCount = sum(reviewCount)

        updateUnigramList(mostFrequentUnigrams, unigram, totalCount)
        updateUnigramList(mostFrequentNegativeUnigrams, unigram, badReviewCount)
        updateUnigramList(mostFrequentPositiveUnigrams, unigram, positiveReviewCount)

    with open(RESULTS2B, "a+") as outputFile:
        outputFile.write("\n")
        outputFile.write("30 Most Frequent Unigrams\n")
        outputFile.write(str(mostFrequentUnigrams) + "\n")
        outputFile.write("30 Most Frequent Negative Unigrams\n")
        outputFile.write(str(mostFrequentNegativeUnigrams) + "\n")
        outputFile.write("30 Most Frequent Positive Unigrams\n")
        outputFile.write(str(mostFrequentPositiveUnigrams) + "\n")
        print "Logged output to {}".format(RESULTS2B)

if __name__ == '__main__':
    main()