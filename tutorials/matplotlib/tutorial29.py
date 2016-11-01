

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import math

fig = plt.figure()
ax = fig.gca( projection='3d' )

tt = [ 2 * math.pi * q / 100 for q in range( 100 ) ]



xx = [ math.cos( tt[q] ) for q in range( len( tt ) ) ]
yy = [ math.sin( tt[q] ) for q in range( len( tt ) ) ]
zz = [ tt[q] / ( 2 * math.pi ) for q in range( len( tt ) ) ]

ax.plot( xx, yy, zz, color='cyan' )

plt.show()




