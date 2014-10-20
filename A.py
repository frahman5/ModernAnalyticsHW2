__author__ = 'Faiyam Rahman, Rachel Mayer'

def make3DHist(dlongbinsize, dlatbinsize, data):
    """
    float float np.array -> ???

    Given the parameters for binsize and a matrix of data, 
    produces (saves to file) a 3DHistogram
    """
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    import numpy as np

    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')

    xpos = [1,2,3,4,5,6,7,8,9,10]
    ypos = [2,3,4,5,1,6,2,1,7,2]
    num_elements = len(xpos)
    zpos = [0,0,0,0,0,0,0,0,0,0]
    dx = np.ones(10)
    dy = np.ones(10)
    dz = [1,2,3,4,5,6,7,8,9,10]

    ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#00ceaa')
    
    plt.savefig(foo)
    
def main(trainData):
    """
    string -> None

    Given the filepath of training data of taxi trips in NYC, produces
    plots of the pdfs of 
        P(passenger count=1|dropoff longitude, dropoff latitude)
        P(passenger count=3|dropoff longitude, dropoff latitude)
    """
    pass
