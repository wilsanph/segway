
#include <iostream>
#include <wiringPiI2C.h>
#include "SensorMPU9150.h"
#include <thread>
#include <chrono>

using namespace std;



int main()
{
    int i2cHandle = wiringPiI2CSetup( 0x68 );

    mpu9150::MPU9150 sensor( i2cHandle );
    sensor.configure();

    for ( int q = 0; q < 500; q++ )
    {
        sensor.takeAccSample();
        sensor.takeGyroSample();

        std::cout << " ax: " << sensor.ax << std::endl;
        std::cout << " ay: " << sensor.ay << std::endl;
        std::cout << " az: " << sensor.az << std::endl;
        
        std::cout << " gx: " << sensor.gx << std::endl;
        std::cout << " gy: " << sensor.gy << std::endl;
        std::cout << " gz: " << sensor.gz << std::endl;

        std::this_thread::sleep_for( std::chrono::milliseconds( 10 ) );
    }

    return 0;
}
