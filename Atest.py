# __author__ = 'Faiyam Rahman, Rachel Mayer'
import pandas as pd
import numpy as np
import csv
from config import TRAIN_DATA, FILE_FORMAT
from distance import get_distance
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def main():
    """
    Based on 10,000 rows from TRAIN_DATA.csv, produces
    plots of heat maps of the probabilities for using scaled 
    GPS locations
        P(passenger count=1|dropoff longitude, dropoff latitude)
        P(passenger count=3|dropoff longitude, dropoff latitude)
    """

    dic = {}
    longs = []
    lats = []
    final_counts= []
    tripcounts_1 = []
    tripcounts_3 = []
    total_tripcounts = []
    prob_1 = []
    prob_3 = []
    colors1 = []
    colors3 = []
    
    f = open('info.csv', 'rw')  ## saved cvs with excel manipulation of lat and longs
    try:
        reader = csv.reader(f)
        for row in reader:
            key = row[3] + "," + row[4]
            longs.append(int(row[3]))
            lats.append(int(row[4]))
            if (not dic.has_key(key)):
                dic[key] = []
            dic[key].append(int(row[0]))                                   
        for key in dic.keys():
            countOne = 0
            counntThree = 0
            for el in dic[key]:
                if el == 1:
                    countOne +=1
                elif el == 3:
                    counntThree += 1
            #print key + "," + str(len(dic[key])) + "," + str(countOne) + "," + str(counntThree)
                final = [key, str(len(dic[key])), str(countOne), str(counntThree)]
                final_counts.append(final)
                tripcounts_1.append(countOne)
                tripcounts_3.append(counntThree)
                total_tripcounts.append((len(dic[key])))
        ## generating probabilities
        for n in range(len(total_tripcounts)):
            prob_1.append(float(tripcounts_1[n])/float(total_tripcounts[n]))
            prob_3.append(float(tripcounts_3[n])/float(total_tripcounts[n]))

        ## generating list of colors for heat map
        for c in prob_1:
            if c >= 0.85:
                colors1.append('#990000')
            elif c >= 0.60 and c < 0.85:
                colors1.append('#AD3333')
            elif c >= 0.50 and c < 0.60:
                colors1.append('#FF8330')
            elif c >= 0.3 and c < 0.50:
                colors1.append('#FFCC00')
            else: 
                colors1.append('#FFDB4D')
        
        for c in prob_3:
            if c >= 0.85:
                colors3.append('#990000')
            elif c >= 0.60 and c < 0.85:
                colors3.append('#AD3333')
            elif c >= 0.50 and c < 0.60:
                colors3.append('#FF8330')
            elif c >= 0.3 and c < 0.50:
                colors3.append('#FFCC00')
            else: 
                colors3.append('#FFDB4D')
        
        ##plots
        plt.scatter(longs, lats, c = colors1)
        plt.title('Heat Map for Prob P Count = 1')
        plt.xlabel("longs")
        plt.ylabel("lats")
        plt.savefig("graph1.jpg")
        plt.clf()
        plt.cla()

        ##plots
        plt.scatter(longs, lats, c = colors3)
        plt.title('Heat Map for Prob P Count = 3')
        plt.xlabel("longs")
        plt.ylabel("lats")
        plt.savefig("graph2.jpg")
        plt.clf()
        plt.cla()
        
        # prob_1 = []
        # for i in final_counts:
        #     p = 
        # # tripcounts = open('tripcounts.csv', 'wb')
        # writer = csv.writer(tripcounts, dialect = 'excel')
        # for i in final_counts:
        #     writer.writerow(i)
    finally:
        f.close()


 



## Usage: python A.py
if __name__ == '__main__':
    main()


