


#include <iostream>
#include <wiringPiI2C.h>
#include <thread>
#include <chrono>

#include "SensorMPU9150.h"
#include "SensorFilters.h"

#define NUM_SAMPLES 2000 // 2000 samples
#define SAMPLE_RATE 10  // 10ms sample rate

#define CALIBRATION_ACC_X -0.017857
#define CALIBRATION_ACC_Y -0.003134
#define CALIBRATION_ACC_Z  0.335875

int main()
{
    int i2cHandle = wiringPiI2CSetup( 0x68 );
    
    mpu9150::MPU9150 sensor( i2cHandle );
    sensor.configure();

    sensorFilters::ComplementaryFilter cFilter;
   
    std::cout << "beggining sampling" << std::endl;

    for ( int q = 0; q < NUM_SAMPLES; q++ )
    {   
        sensor.takeGyroSample();
        sensor.takeAccSample();
        
        cFilter.update( sensor.gx, sensor.gy, sensor.gz, 
                        sensor.ax - CALIBRATION_ACC_X, 
                        sensor.ay - CALIBRATION_ACC_Y, 
                        sensor.az - CALIBRATION_ACC_Z,
                        SAMPLE_RATE / 1000. );

        std::cout << "gx: " << sensor.gx << " - gy: " << sensor.gy << " - gz: " << sensor.gz << std::endl;
        std::cout << "ax: " << sensor.ax << " - ay: " << sensor.ay << " - az: " << sensor.az << std::endl;
        
        std::cout << "roll: " << cFilter.roll() << std::endl;
        std::cout << "pitch: " << cFilter.pitch() << std::endl;
        std::this_thread::sleep_for( std::chrono::milliseconds( SAMPLE_RATE ) );
    }
   
    std::cout << "finished sampling" << std::endl;    

    return 0;
}
