

import matplotlib.pyplot as plt
import random

populationAges = [ int( random.random() * 100 ) for q in range( 100 ) ]

## ids = [ q for q in range( len( populationAges ) ) ]
## plt.bar( ids, populationAges )

bins = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist( populationAges, bins, histtype='bar', rwidth=0.8 )

plt.xlabel( 'age' )
plt.ylabel( 'dist' )

plt.title( 'Interesting graph :o)' )
plt.show()
