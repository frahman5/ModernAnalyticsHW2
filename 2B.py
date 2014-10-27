__author__ = 'Faiyam Rahman, Rachel Mayer'

from config import FINEFOODS
from problem2Framework.utils import get_unigram

def main():
    from problem2Framework import scan

    # Extract list of unigrams from finefoods.txt
    binary_label = True
    data = scan.scan(FINEFOODS, binary_label= binary_label) #[(review, score)...(review, score)]
    
    masterDict = {} #{'word': [negative_review_count, positive_review_count], ...}
    for review, score in data:
        unigram, num_words = get_unigram(review) # ({'word1': num_occurences, ..., 'wordn': num_occurences}, total_occurences)
        for word in unigram:
            if word in masterDict.keys():
                masterDict[word] = [0, 0]
            masterDict[word][score] += unigram[word]

    # Extract relevant data
    mostFrequentUnigrams = [('', 0) for i in range(30)] 
    mostFrequenctNegativeUnigrams = [('', 0) for i in range(30)]
    mostFrequentPositiveUnigrams = [('', 0) for i in range(30)]
    for unigram, reviewCount in masterDict.iteritems():
        badReviewCount, positiveReviewCount = reviewCount
        totalCount = sum(reviewCount)

        if totalCount > mostFrequentUnigrams[0][0]:
            mostFrequentUnigrams[0] = (unigram, totalCount)

        if badReviewCount > mostFrequenctNegativeUnigrams[0][0]:
            mostFrequenctNegativeUnigrams[0] = (unigram, badReviewCount)

        if positiveReviewCount > mostFrequentPositiveUnigrams[0][0]:
            mostFrequentPositiveUnigrams[0] = (unigram, positiveReviewCount)

        mostFrequentUnigrams.sort()
        mostFrequenctNegativeUnigrams.sort()
        mostFrequentPositiveUnigrams.sort()



if __name__ == '__main__':
    main()