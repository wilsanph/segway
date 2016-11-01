


#include <iostream>
#include <wiringPiI2C.h>
#include "SensorMPU9150.h"
#include "DataLogger.h"
#include <thread>
#include <chrono>

#define NUM_SAMPLES 2000 // 2000 samples
#define SAMPLE_RATE 10  // 10ms sample rate


int main()
{
    int i2cHandle = wiringPiI2CSetup( 0x68 );
    
    mpu9150::MPU9150 sensor( i2cHandle );
    sensor.configure();

    DataLogger<NUM_SAMPLES,3,float> sensorLogger;
    
    std::cout << "beggining sampling" << std::endl;

    for ( int q = 0; q < NUM_SAMPLES; q++ )
    {
        sensor.takeAccSample();
        

        sensorLogger.addDataPoint( 0, sensor.ax );
        sensorLogger.addDataPoint( 1, sensor.ay );
        sensorLogger.addDataPoint( 2, sensor.az );


        std::this_thread::sleep_for( std::chrono::milliseconds( SAMPLE_RATE ) );
    }
   
    std::cout << "finished sampling" << std::endl;    
    
    sensorLogger.dumpWholeDataToConsole();
    sensorLogger.saveWholeDataToFile();

    return 0;
}
