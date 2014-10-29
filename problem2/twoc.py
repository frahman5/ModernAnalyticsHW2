from twob import main

if __name__ == '__main__':
    from config import RESULTS2C
    main(results_file=RESULTS2C, exclude_stopwords=True, num_top_unigrams=30)