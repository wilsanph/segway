
#include <iostream>
#include <wiringPiI2C.h>
#include <thread>
#include <chrono>

using namespace std;

typedef unsigned char u8;
typedef unsigned short u16;

void configure( int devHandle );
int get2sComplement( u16 val );

int main()
{
    int i2cHandle = wiringPiI2CSetup( 0x68 );
    configure( i2cHandle );

    u8 whoAmI = wiringPiI2CReadReg8( i2cHandle, 0x75 );
    
    cout << "Who am i: " << (u8) whoAmI << endl;

    std::cout << "countdown: " << std::endl; 
    for ( int q = 0; q < 10; q++ ) 
    {
        std::cout << q << std::endl;
        std::this_thread::sleep_for( std::chrono::milliseconds( 100 ) );
    }

    for ( int q = 0; q < 1000; q++ )
    {
        u8 az_low  = wiringPiI2CReadReg8( i2cHandle, 0x40 );
        u8 az_high = wiringPiI2CReadReg8( i2cHandle, 0x3f );

        int azReg = get2sComplement( ( az_high << 8 ) | az_low );
        float azVal = 8 * ( ( float ) azReg ) / 32768.;
        
        std::cout << "az: " << azVal << std::endl;

        std::this_thread::sleep_for( std::chrono::milliseconds( 10 ) );
    }

    return 0;
}


void configure( int devHandle ) 
{
    wiringPiI2CWriteReg8( devHandle, 0x6b, 0x01 );
    wiringPiI2CWriteReg8( devHandle, 0x1b, 0x00 );
    wiringPiI2CWriteReg8( devHandle, 0x1c, 0x18 );
}

int get2sComplement( u16 val )
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
