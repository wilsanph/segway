
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
axs = fig.gca( projection='3d' )

accX, accY, accZ = np.loadtxt( 'data.txt', delimiter=';', unpack=True )

axs.scatter( accX, accY, accZ, label='accelerometer data', marker='o', color='b' )


axs.set_xlabel( 'acceleration X' )
axs.set_ylabel( 'acceleration Y' )
axs.set_zlabel( 'acceleration Z' )


## for an initial guess, try using the 





axs.legend()

plt.show()
