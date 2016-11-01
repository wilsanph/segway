
import matplotlib.pyplot as plt
import csv
import numpy as np

"""
## csv way of parsing
xx = []
yy = []
fileHandler = open( 'data.txt', 'r' )
points = csv.reader( fileHandler, delimiter=';' )

for q in points :
    xx.append( float( q[0] ) )
    yy.append( float( q[1] ) )
"""


## numpy way
xx, yy = np.loadtxt( 'data.txt', delimiter=';', unpack=True )

plt.plot( xx, yy )

plt.show()
