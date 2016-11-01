

import matplotlib.pyplot as plt
import random
import math


tt = [ 2 * math.pi * random.random() for q in range( 100 ) ]

xx = [ math.cos( tt[q] ) for q in range( len( tt ) ) ]
yy = [ math.sin( tt[q] ) for q in range( len( tt ) ) ]

plt.scatter( xx, yy, label='circumference', color='c', s=100, marker='o' )

plt.xlabel( 'x' )
plt.ylabel( 'y' )

plt.title( 'Interesting graph :o)' )
plt.legend()
plt.show()
