__author__ = 'Faiyam Rahman, Rachel Mayer'

from config import FINEFOODS

def main():
    from problem2Framework import scan

    # Extract list of unigrams from finefoods.txt
    binary_label = True
    data = scan.scan(FINEFOODS, binary_label= binary_label)
    import pdb
    pdb.set_trace()

if __name__ == '__main__':
    main()