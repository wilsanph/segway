

import matplotlib.pyplot as plt
import random

xx1 = [ ( 2 * ( q + 1 ) ) for q in range( 5 ) ]
yy1 = [ ( 5 * random.random() + 5 ) for q in range( len( xx1 ) ) ]

xx2 = [ ( 2 * q + 1 ) for q in range( 5 ) ]
yy2 = [ ( 10 * random.random() + 10 ) for q in range( len( xx2 ) ) ]


plt.bar( xx1, yy1, label='First bar chart xD', color='red' )
plt.bar( xx2, yy2, label='Second bar chart :D', color='blue' )

plt.xlabel( 'x' )
plt.ylabel( 'y' )

plt.title( 'Interesting graph :o)' )
plt.legend()
plt.show()
