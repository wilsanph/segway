
#include <iostream>
#include "DataLogger.h"

int main()
{
    std::cout << "DataLogger test" << std::endl << std::endl;

    DataLogger<1000,2,float> logger;

    for ( int q = 0; q < 10; q++ )
    {
        logger.addDataPoint( 0, ( float ) q );
        logger.addDataPoint( 1, ( float ) q * q );
    }
    for ( int q = 0; q < 10; q++ )
    {
        logger.addDataPoint( 0, q + 10 );
    }

    logger.dumpAxisToConsole( 0 );
    logger.dumpAxisToConsole( 1 );

    logger.dumpWholeDataToConsole();

    logger.saveAxisToFile( 0 );
    logger.saveWholeDataToFile();

    return 0;
}
