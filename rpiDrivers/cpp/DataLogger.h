
#pragma once

#include <iostream>
#include <fstream>

namespace logOptions
{
    namespace delimiter
    {
        enum _delimiter
        {
            DELIMITER_SEMICOLON,
            DELIMITER_COLON,
            DELIMITER_SPACE
        };
    }


}


template<int BuffSize,int NumAxis,typename DataType>
class DataLogger
{


    public :
    
    DataLogger();
    ~DataLogger();

    void addDataPoint( int pAxis, DataType pPoint );
    DataType getDataPoint( int pAxis, int pIndex );
    int length( int pAxis );
    
    void dumpAxisToConsole( int pAxis );
    void dumpWholeDataToConsole();

    void saveAxisToFile( int pAxis );
    void saveWholeDataToFile();

    void setDelimiter( logOptions::delimiter::_delimiter pDelimiter );
    
    private :
    
    DataType m_buffer[NumAxis][BuffSize];
    int m_currentPos[NumAxis];
    int m_delimiter;
    
};



#include "DataLoggerImplement.h"
