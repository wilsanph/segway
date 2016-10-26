
import wiringpi as wp
import time


i2cHandle = wp.wiringPiI2CSetup( 0x68 )
#g = 9.81
g = 1
roll = 0
pitch = 0
yaw = 0

def configureIMU( devHandle ) :
    
    wp.wiringPiI2CWriteReg8( devHandle, 0x6b, 0x01 ) 
    wp.wiringPiI2CWriteReg8( devHandle, 0x1b, 0x00 )
    wp.wiringPiI2CWriteReg8( devHandle, 0x1c, 0x18 )

def get2sComplement( val ) :
    if ( val & ( 1 << ( 16 - 1 ) ) ) != 0 :
        val = val - ( 1 << 16 )
    return val

if i2cHandle is None :
    print 'there was anerror initializing the i2c interface'
else :
    configureIMU( i2cHandle )

    res = wp.wiringPiI2CReadReg8( i2cHandle, 0x75 )
    print 'whoami: ', res
    
    while( True ) :
        
        ax_low  = wp.wiringPiI2CReadReg8( i2cHandle, 0x3c )
        ax_high = wp.wiringPiI2CReadReg8( i2cHandle, 0x3b )
        
        ay_low  = wp.wiringPiI2CReadReg8( i2cHandle, 0x3e )
        ay_high = wp.wiringPiI2CReadReg8( i2cHandle, 0x3d )

        az_low  = wp.wiringPiI2CReadReg8( i2cHandle, 0x40 )
        az_high = wp.wiringPiI2CReadReg8( i2cHandle, 0x3f )

        ax = ax_high << 8 | ax_low
        ay = ay_high << 8 | ay_low
        az = az_high << 8 | az_low
        
        gx_low  = wp.wiringPiI2CReadReg8( i2cHandle, 0x44 )
        gx_high = wp.wiringPiI2CReadReg8( i2cHandle, 0x43 )
        
        gy_low  = wp.wiringPiI2CReadReg8( i2cHandle, 0x46 )
        gy_high = wp.wiringPiI2CReadReg8( i2cHandle, 0x45 )

        gz_low  = wp.wiringPiI2CReadReg8( i2cHandle, 0x48 )
        gz_high = wp.wiringPiI2CReadReg8( i2cHandle, 0x47 )

        gx = gx_high << 8 | gx_low
        gy = gy_high << 8 | gy_low
        gz = gz_high << 8 | gz_low

        ax = 8 * g * get2sComplement( ax ) / 32768.
        print 'ax: ' , ax
        ay = 8 * g * get2sComplement( ay ) / 32768.
        print 'ay: ' , ay
        az = 8 * g * get2sComplement( az ) / 32768.
        print 'az: ' , az


        gx =  250 * get2sComplement( gx ) / 32768.
        print 'gx: ' , gx 
        gy = 250 * get2sComplement( gy ) / 32768.
        print 'gy: ' , gy 
        gz = 250 * get2sComplement( gz ) / 32768.
        print 'gz: ' , gz 


        roll += gx * 0.01
        pitch += gy * 0.01
        yaw += gz * 0.01
        
        print 'roll: ' , roll
        print 'pitch: ' , pitch
        print 'yaw: ' , yaw

        time.sleep( 0.01 )
        
     
