
#include <iostream>
#include <errno.h>
#include <wiringPiI2C.h>

using namespace std;

typedef unsigned char u8;

void configure( int devHandle );

int main()
{
    int i2cHandle = wiringPiI2CSetup( 0x68 );
    configure( i2cHandle );

    u8 whoAmI = wiringPiI2CReadReg8( i2cHandle, 0x75 );
    
    cout << "Who am i: " << (u8) whoAmI << endl;

    return 0;
}


void configure( int devHandle ) 
{
    wiringPiI2CWriteReg8( devHandle, 0x6b, 0x01 );
    wiringPiI2CWriteReg8( devHandle, 0x1b, 0x00 );
    wiringPiI2CWriteReg8( devHandle, 0x1c, 0x18 );
}
