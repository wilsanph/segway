
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
        this->accFactor = 1;
        this->gx = 0;
        this->gy = 0;
        this->gz = 0;
        this->gyroFactor = 1;
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
        wiringPiI2CWriteReg8( this->m_i2cHandle,
                              regMap::REG_GYRO_CONFIG,
                              config::GYRO_RANGE_250 );
    }

    void MPU9150::takeAccSample()
    {

    }

    void MPU9150::takeGyroSample()
    {

    }

    int MPU9150::get2sComplement( u16 val )
    {

    }
}
