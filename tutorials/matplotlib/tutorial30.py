
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import math
import random


fig = plt.figure()
ax = fig.gca( projection='3d' )

r = 10
N = 100
tt = [ 2 * math.pi * random.random() for q in range( N ) ]
pp = [ 2 * math.pi * random.random() for q in range( N ) ]


xx = [ r * math.cos( tt[q] ) * math.sin( pp[q] ) for q in range( N ) ]
yy = [ r * math.cos( tt[q] ) * math.cos( pp[q] ) for q in range( N ) ]
zz = [ r * math.sin( tt[q] ) for q in range( N ) ]

ax.scatter( xx, yy, zz )

plt.show()
