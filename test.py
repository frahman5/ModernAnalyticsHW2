
if __name__ == '__main__':
    from config import TRAIN_DATA
    from code.utils import load_csv_lazy
  
    train_data = load_csv_lazy(TRAIN_DATA, [], [8])
    index = 0
    for row in train_data:
        index += 1
        if index == 10:
            break
        print row
    print "train_data.next: {}".format(train_data.next())
    print "code ran"
