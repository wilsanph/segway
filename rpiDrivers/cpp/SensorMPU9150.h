


typedef unsigned char u8;
typedef unsigned short u16;

namespace mpu9150
{

    namespace regMap
    {
        enum _regMap
        {                        
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
        };
    }

    namespace config
    {
        enum _config
        {
            GYRO_RANGE_250  = 0x00,
            GYRO_RANGE_500  = 0x08,
            GYRO_RANGE_1000 = 0x10,
            GYRO_RANGE_2000 = 0x18,

            ACC_RANGE_2G  = 0x00,
            ACC_RANGE_4G  = 0x08,
            ACC_RANGE_8G  = 0x10,
            ACC_RANGE_16G = 0x18,

            PWR_CLK_INTERNAL    = 0x0,
            PWR_CLK_PLL_GYRO_X  = 0x1,
            PWR_CLK_PLL_GYRO_Y  = 0x2,
            PWR_CLK_PLL_GYRO_Z  = 0x3,
            PWR_CLK_PLL_32K_EXT = 0x4,
            PWR_CLK_PLL_16K_EXT = 0x5
        };
    }

    class MPU9150
    {
        public :

        MPU9150( int pI2cHandle );
        ~MPU9150();

        void configure();
        void takeAccSample();
        void takeGyroSample();

        
        float ax;
        float ay;
        float az;
        
        float gx;
        float gy;
        float gz;

        private :
        int get2sComplement( u16 val );
        
        int m_i2cHandle;
        float m_accFactor;
        float m_gyroFactor;
    };
}




