

import matplotlib.pyplot as plt
import math


xx = [ ( q * 2 * math.pi / 100 ) for q in range( 100 ) ]
yy = [ math.sin( xx[q] ) for q in range( len( xx ) ) ]
zz = [ math.cos( xx[q] ) for q in range( len( xx ) ) ]

plt.plot( xx, yy, label='Sine' )
plt.plot( xx, zz, label='Cosine' )

plt.xlabel( 'x' )
plt.ylabel( 'y = sin(x) ' )

plt.title( 'Graph of a sine function' )
plt.legend()
plt.show()
