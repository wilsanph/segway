



import wiringpi as wp

class RegMap:
    REG_GYRO_CONFIG = 0x1b
    REG_ACC_CONFIG  = 0x1c
    REG_PWR1 = 0x6b

    REG_ACC_X_HIGH = 0x3b
    REG_ACC_X_LOW  = 0x3c
    REG_ACC_Y_HIGH = 0x3d
    REG_ACC_Y_LOW  = 0x3e
    REG_ACC_Z_HIGH = 0x3f
    REG_ACC_Z_LOW  = 0x40

    REG_GYRO_X_HIGH = 0x43
    REG_GYRO_X_LOW  = 0x44
    REG_GYRO_Y_HIGH = 0x45
    REG_GYRO_Y_LOW  = 0x46
    REG_GYRO_Z_HIGH = 0x47
    REG_GYRO_Z_LOW  = 0x48
    
    pass

class Config:
    GYRO_RANGE_250  = 0x00
    GYRO_RANGE_500  = 0x08
    GYRO_RANGE_1000 = 0x10
    GYRO_RANGE_2000 = 0x18

    ACC_RANGE_2G  = 0x00
    ACC_RANGE_4G  = 0x08
    ACC_RANGE_8G  = 0x10
    ACC_RANGE_16G = 0x18

    PWR_CLK_INTERNAL    = 0x0
    PWR_CLK_PLL_GYRO_X  = 0x1
    PWR_CLK_PLL_GYRO_Y  = 0x2
    PWR_CLK_PLL_GYRO_Z  = 0x3
    PWR_CLK_PLL_32K_EXT = 0x4
    PWR_CLK_PLL_16K_EXT = 0x5 

    pass

    


class MPU9150:
    
    def __init__( self, i2cHandle ) :
        self.m_i2cHandle = i2cHandle

        self.m_ax = 0
        self.m_ay = 0
        self.m_az = 0
        self.m_accFactor = 1

        self.m_gx = 0
        self.m_gy = 0
        self.m_gz = 0
        self.m_gyroFactor = 1

    def configure( self ) :

        #enable the module 
        wp.wiringPiI2CWriteReg8( self.m_i2cHandle, 
                                 RegMap.REG_PWR1,
                                 Config.PWR_CLK_PLL_GYRO_X )

        wp.wiringPiI2CWriteReg8( self.m_i2cHandle,
                                 RegMap.REG_ACC_CONFIG,
                                 Config.ACC_RANGE_2G )
        self.m_accFactor = 2.

        wp.wiringPiI2CWriteReg8( self.m_i2cHandle,
                                 RegMap.REG_GYRO_CONFIG,
                                 Config.GYRO_RANGE_500 )
        self.m_gyroFactor = 500.



    def _get2sComplement( self, val ) :
        if ( val & ( 1 << 15 ) ) != 0 :
            val = val - ( 1 << 16 )
        return val

    def takeAccSample( self ) :

        ax_low = wp.wiringPiI2CReadReg8( self.m_i2cHandle,
                                         RegMap.REG_ACC_X_LOW )
        ax_high = wp.wiringPiI2CReadReg8( self.m_i2cHandle,
                                          RegMap.REG_ACC_X_HIGH )

        ay_low = wp.wiringPiI2CReadReg8( self.m_i2cHandle,
                                         RegMap.REG_ACC_Y_LOW )
        ay_high = wp.wiringPiI2CReadReg8( self.m_i2cHandle,
                                          RegMap.REG_ACC_Y_HIGH )

        az_low = wp.wiringPiI2CReadReg8( self.m_i2cHandle,
                                         RegMap.REG_ACC_Z_LOW )
        az_high = wp.wiringPiI2CReadReg8( self.m_i2cHandle,
                                          RegMap.REG_ACC_Z_HIGH )
        
        self.m_ax = ( ax_high << 8 ) | ax_low
        self.m_ay = ( ay_high << 8 ) | ay_low
        self.m_az = ( az_high << 8 ) | az_low 

        self.m_ax = self.m_accFactor * self._get2sComplement( self.m_ax ) / 32768.
        self.m_ay = self.m_accFactor * self._get2sComplement( self.m_ay ) / 32768.
        self.m_az = self.m_accFactor * self._get2sComplement( self.m_az ) / 32768.

    def takeGyroSample( self ) :
 
        gx_low = wp.wiringPiI2CReadReg8( self.m_i2cHandle,
                                         RegMap.REG_GYRO_X_LOW )
        gx_high = wp.wiringPiI2CReadReg8( self.m_i2cHandle,
                                          RegMap.REG_GYRO_X_HIGH )

        gy_low = wp.wiringPiI2CReadReg8( self.m_i2cHandle,
                                         RegMap.REG_GYRO_Y_LOW )
        gy_high = wp.wiringPiI2CReadReg8( self.m_i2cHandle,
                                          RegMap.REG_GYRO_Y_HIGH )

        gz_low = wp.wiringPiI2CReadReg8( self.m_i2cHandle,
                                         RegMap.REG_GYRO_Z_LOW )
        gz_high = wp.wiringPiI2CReadReg8( self.m_i2cHandle,
                                          RegMap.REG_GYRO_Z_HIGH )
        
        self.m_gx = ( gx_high << 8 ) | gx_low
        self.m_gy = ( gy_high << 8 ) | gy_low
        self.m_gz = ( gz_high << 8 ) | gz_low 

        self.m_gx = self.m_gyroFactor * self._get2sComplement( self.m_gx ) / 32768.
        self.m_gy = self.m_gyroFactor * self._get2sComplement( self.m_gy ) / 32768.
        self.m_gz = self.m_gyroFactor * self._get2sComplement( self.m_gz ) / 32768.
        

    def ax( self ) :
        return self.m_ax

    def ay( self ) :
        return self.m_ay

    def az( self ) :
        return self.m_az

    def gx( self ) :
        return self.m_gx

    def gy( self ) :
        return self.m_gy
    
    def gz( self ) :
        return self.m_gz 

    
