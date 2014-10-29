from twob import main

if __name__ == '__main__':
    from config import RESULTS2E
    main(results_file=RESULTS2E, exclude_stopwords=True, num_top_unigrams=500)