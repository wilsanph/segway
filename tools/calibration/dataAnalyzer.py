
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import fit3

fig = plt.figure()
axs = fig.gca( projection='3d' )

accX, accY, accZ = np.loadtxt( 'data.txt', delimiter=';', unpack=True )


## axs.set_aspect( 'equal' )

axs.scatter( accX, accY, accZ, 
             label='accelerometer data', 
             marker='o', 
             color='b' )

r = 0.964241415992
xc = -0.0421070
yc = 0.1402106    
zc = 0.351609

u, v = np.mgrid[0 : 2 * np.pi : 20j, 0 : np.pi : 10j]
xx = r * np.cos( u ) * np.sin( v ) + xc
yy = r * np.sin( u ) * np.sin( v ) + yc
zz = r * np.cos( v ) + zc
##axs.plot_wireframe( xx, yy, zz, color='b' )

fitter = fit3.SphereFitter( accX, accY, accZ )
fitter.fitSimpleGradientDescend( xc, yc, zc, r )

print 'xc: ' , fitter.x0
print 'yc: ' , fitter.y0
print 'zc: ' , fitter.z0
print 'r0: ' , fitter.r0

u, v = np.mgrid[0 : 2 * np.pi : 20j, 0 : np.pi : 10j]
xx = fitter.r0 * np.cos( u ) * np.sin( v ) + fitter.x0
yy = fitter.r0 * np.sin( u ) * np.sin( v ) + fitter.y0
zz = fitter.r0 * np.cos( v ) + fitter.z0
axs.plot_wireframe( xx, yy, zz, color='r' )

axs.set_xlabel( 'acceleration X' )
axs.set_ylabel( 'acceleration Y' )
axs.set_zlabel( 'acceleration Z' )


## for an initial guess, try using the 





axs.legend()

plt.show()
