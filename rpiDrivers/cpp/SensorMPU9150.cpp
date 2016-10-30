
#include <wiringPiI2C.h>
#include "SensorMPU9150.h"



namespace mpu9150
{


    MPU9150::MPU9150( int pI2cHandle )
    {
        this->m_i2cHandle = pI2cHandle;
        this->ax = 0;
        this->ay = 0;
        this->az = 0;
        this->m_accFactor = 1;
        this->gx = 0;
        this->gy = 0;
        this->gz = 0;
        this->m_gyroFactor = 1;
    }

    MPU9150::~MPU9150()
    {

    }

    void MPU9150::configure()
    {
        wiringPiI2CWriteReg8( this->m_i2cHandle, 
                              regMap::REG_PWR1, 
                              config::PWR_CLK_PLL_GYRO_X );
        
        wiringPiI2CWriteReg8( this->m_i2cHandle,
                              regMap::REG_ACC_CONFIG,
                              config::ACC_RANGE_2G );
        this->m_accFactor = 2.;

        wiringPiI2CWriteReg8( this->m_i2cHandle,
                              regMap::REG_GYRO_CONFIG,
                              config::GYRO_RANGE_500 );
        this->m_gyroFactor = 500.;
    }

    void MPU9150::takeAccSample()
    {
        u8 ax_low = wiringPiI2CReadReg8( this->m_i2cHandle,
                                         regMap::REG_ACC_X_LOW );
        u8 ax_high = wiringPiI2CReadReg8( this->m_i2cHandle,
                                          regMap::REG_ACC_X_HIGH );

        u8 ay_low = wiringPiI2CReadReg8( this->m_i2cHandle,
                                         regMap::REG_ACC_Y_LOW );
        u8 ay_high = wiringPiI2CReadReg8( this->m_i2cHandle,
                                          regMap::REG_ACC_Y_HIGH );

        u8 az_low = wiringPiI2CReadReg8( this->m_i2cHandle,
                                         regMap::REG_ACC_Z_LOW );
        u8 az_high = wiringPiI2CReadReg8( this->m_i2cHandle,
                                          regMap::REG_ACC_Z_HIGH );

        int axReg = this->get2sComplement( ( ax_high << 8 ) | ax_low );
        this->ax = this->m_accFactor * ( ( float ) axReg ) / 32768.;

        int ayReg = this->get2sComplement( ( ay_high << 8 ) | ay_low );
        this->ay = this->m_accFactor * ( ( float ) ayReg ) / 32768.;

        int azReg = this->get2sComplement( ( az_high << 8 ) | az_low );
        this->az = this->m_accFactor * ( ( float ) azReg ) / 32768.;

    }

    void MPU9150::takeGyroSample()
    {
        u8 gx_low = wiringPiI2CReadReg8( this->m_i2cHandle,
                                         regMap::REG_GYRO_X_LOW );
        u8 gx_high = wiringPiI2CReadReg8( this->m_i2cHandle,
                                          regMap::REG_GYRO_X_HIGH );

        u8 gy_low = wiringPiI2CReadReg8( this->m_i2cHandle,
                                         regMap::REG_GYRO_Y_LOW );
        u8 gy_high = wiringPiI2CReadReg8( this->m_i2cHandle,
                                          regMap::REG_GYRO_Y_HIGH );

        u8 gz_low = wiringPiI2CReadReg8( this->m_i2cHandle,
                                         regMap::REG_GYRO_Z_LOW );
        u8 gz_high = wiringPiI2CReadReg8( this->m_i2cHandle,
                                          regMap::REG_GYRO_Z_HIGH );

        int gxReg = this->get2sComplement( ( gx_high << 8 ) | gx_low );
        this->gx = this->m_gyroFactor * ( ( float ) gxReg ) / 32768.;

        int gyReg = this->get2sComplement( ( gy_high << 8 ) | gy_low );
        this->gy = this->m_gyroFactor * ( ( float ) gyReg ) / 32768.;

        int gzReg = this->get2sComplement( ( gz_high << 8 ) | gz_low );
        this->gz = this->m_gyroFactor * ( ( float ) gzReg ) / 32768.;
    }

    int MPU9150::get2sComplement( u16 val )
    {
        int res = 0; 
        if ( ( val & ( 1 << ( 16 - 1 ) ) ) != 0 )
        {
            res = val - ( 1 << 16 );
        }
        else
        {
            res = ( int ) val;
        }
      
        return res;
    }
}
