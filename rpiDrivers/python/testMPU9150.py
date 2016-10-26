

import SensorMPU9150
import time
import wiringpi as wp

i2cHandle = wp.wiringPiI2CSetup( 0x68 ) 
imu = SensorMPU9150.MPU9150( i2cHandle )

for i in range( 50 ) :
    imu.takeAccSample()
    imu.takeGyroSample()

    print 'ax: ' , imu.ax()
    print 'ay: ' , imu.ay()
    print 'az: ' , imu.az()
    print 'gx: ' , imu.gx()
    print 'gy: ' , imu.gy()
    print 'gz: ' , imu.gz()

    time.sleep( 0.1 )
