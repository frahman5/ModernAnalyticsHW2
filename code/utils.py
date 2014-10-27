import numpy,math,datetime,logging
from sklearn import linear_model
from distance import get_distance
# logging.basicConfig(filename='logs/utils.log',level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def calcAndLogStats(y, yhat, output):
    """
    numpy.array numpy.array string -> (float, float, float)

    Given two length n lists and an output file, logs the values for the 
    following statistics to file:
        Root Mean Squared Error (RMSE)
        Correlation Coefficient
        Mean Absolute Error
    """
    print "calculating deltas"
    deltas = y - yhat

    print "calculating length of input"
    dimension = len(y)

    print "calculating ols error"
    ols_error = sum(numpy.square((deltas)))

    print "calculating rmse"
    rmse = (ols_error/dimension)**0.5

    print "calculating correlation coefficient"
    corr = numpy.corrcoef(y,yhat)

    print "Calculating mean absolute error"
    mean_absolute_error = (sum(numpy.absolute((deltas))))/dimension

    logStatsToFile({'Root Mean Squared Error': rmse, 
                    'Correlation Coefficient Matrix': corr, 
                    'Mean Absolute Error': mean_absolute_error}, 
                    output)

def logStatsToFile(statsDict, output):
    """
    dictionary string -> None

    Outputs the stats in statsDict to file. statsDict has key, value pairs:
        statName, statValue
    e.g: "Root Mean Squared Error, 0.45"
    """
    with open(output, "a+") as outputFile:
        outputFile.write('\n')
        for key, value in statsDict.iteritems():
            outputFile.write("-->{}: {}\n".format(key, statsDict[key]))

    print "Logged Stats to: {}".format(output)
def transformPickupDatetime(pickup_datetime):
    """
    string -> float

    pickup_datetime is a string of format:
        yyyy-mm-dd hh:mm:ss

    Function converts pickup_datetime to a float indicating how many 
    minutes have passed since Midnight.
    """
    # Extract the pickup datetime
    assert type(pickup_datetime) == str

    # Convert it to minutes that have elapsed in the day
    dateInfo, timeInfo = pickup_datetime.split(' ')
    num_hours_string, num_minutes_string, num_seconds_string = timeInfo.split(':')
    time_of_day_in_minutes = (int(num_hours_string) * 60) + int(num_minutes_string)

    return time_of_day_in_minutes
    
def metrics(model,x,y):
    """
    compute ols and rmse
    :param y:
    :param yhat:
    :return ols and rmse:
    """
    yhat = model.predict(x)
    ols = sum(numpy.square((y-yhat)))
    rmse = (ols/len(y))**0.5
    corr = numpy.corrcoef(y,yhat)
    return ols,rmse,corr

def evaluate(model_list,x,y):
    for description,model in model_list:
        print "\t",description,"OLS, RMSE and Correlation coefficient",metrics(model,x,y),"Model",model.coef_,model.intercept_


def split(target, features, row, x, y, x_test=None, y_test=None, i= None, nth = None):
    """
    :param target: index of expected
    :param features: list of indexes
    :param row:
    :param x:
    :param y:
    :param x_test:
    :param y_test:
    :param i:
    :param nth:
    """

    if nth and i % nth == 0:
        x_test.append([row[feature] for feature in features])
        y_test.append(row[target])
    else:
        x.append([row[feature] for feature in features])
        y.append(row[target])


def tls(model,x,y):
    pass


def linear_regression(x,y):
    """
    :param x:
    :param y:
    :return linear regression model object:
    """
    model = linear_model.LinearRegression()
    model.fit(x, y)
    return model


def itransformer(row):
    """
    identity transformer returns same
    :param row:
    :return True:
    """
    return row

def ifilter(row):
    """
    identity filter always returns True
    :param row:
    :return True:
    """
    return True


def load_csv_lazy(fname,str_fields,float_fields,exclude_first=True,row_filter=ifilter,row_tranforme=itransformer):
    """
    np.genfromtxt is a good alternative, not sure if it can act as a generator. pandas frames are also a good alternative.
    :param fname:
    :param exclude_first:
    :return:
    """
    error_count = 0
    excluded_count = 0
    for count, line in enumerate(file(fname)):
        if not exclude_first:
            try:
                if count and count % 10**6 == 0:
                    logging.debug("Loaded "+str(count))
                    logging.debug("error_count : "+str(error_count))
                    logging.debug("excluded_count : "+str(excluded_count))
                entries = line.strip().split(',')
                row = [entries[f] for f in str_fields] + [float(entries[f]) for f in float_fields]

                if row_filter(row):
                    row = row_tranformer(row)
                    yield row
                else:
                    excluded_count += 1
            except:
                error_count += 1
        else:
            exclude_first = False
    logging.debug("count : "+str(count))
    logging.debug("error_count : "+str(error_count))
    logging.debug("excluded_count : "+str(excluded_count))

if __name__ == '__main__':
    # Short test for logStatsToFile(statsDict, output)
    RESULTSTEST = "/Users/faiyamrahman/Documents/CTech/ModernAnalytics/Homework2" +\
                  "/output/resultsTEST.txt"
    logStatsToFile({'test value': 89, 'test worked!': True}, RESULTSTEST)