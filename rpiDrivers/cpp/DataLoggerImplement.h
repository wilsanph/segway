
#pragma once

#include "DataLogger.h"

using namespace logOptions;

template<int BuffSize, int NumAxis, typename DataType>
DataLogger<BuffSize,NumAxis,DataType>::DataLogger()
{
    for ( int q = 0; q < NumAxis; q++ )
    {
        m_currentPos[q] = -1;
    }
    m_delimiter = delimiter::DELIMITER_SEMICOLON;
}

template<int BuffSize, int NumAxis, typename DataType>
DataLogger<BuffSize,NumAxis,DataType>::~DataLogger()
{
}

template<int BuffSize, int NumAxis, typename DataType>
void DataLogger<BuffSize,NumAxis,DataType>::addDataPoint( int pAxis, DataType pPoint )
{
    if ( pAxis < 0 || pAxis >= NumAxis )
    {
        return;
    }

    if ( m_currentPos[pAxis] >= BuffSize - 1 )
    {
        // The buffer in this axis is full :(
        return;
    }
    m_currentPos[pAxis]++;
    m_buffer[pAxis][m_currentPos[pAxis]] = pPoint;
}

template<int BuffSize, int NumAxis, typename DataType>
DataType DataLogger<BuffSize,NumAxis,DataType>::getDataPoint( int pAxis, int pIndex )
{
    if ( pAxis < 0 || pAxis >= NumAxis )
    {
        return;
    }
    
    if ( pIndex < 0 || pIndex > m_currentPos[pAxis] )
    {
        return;
    }
    
    return m_buffer[pAxis][pIndex];
}

template<int BuffSize, int NumAxis, typename DataType>
int DataLogger<BuffSize,NumAxis,DataType>::length( int pAxis )
{
    if ( pAxis < 0 || pAxis >= NumAxis )
    {
        return;
    }
    return m_currentPos[pAxis];
}

template<int BuffSize, int NumAxis, typename DataType> 
void DataLogger<BuffSize,NumAxis,DataType>::dumpAxisToConsole( int pAxis )
{
    if ( pAxis < 0 || pAxis >= NumAxis ) 
    {
        return;
    }
    
    std::cout << "*********" << std::endl;
    std::cout << "axis: " << pAxis << std::endl;
    std::cout << "len: " << m_currentPos[pAxis] << std::endl << std::endl;

    for ( int q = 0; q <= m_currentPos[pAxis]; q++ ) 
    {
        std::cout << m_buffer[pAxis][q] << std::endl;
    }
    
    std::cout << "*********" << std::endl;
}

template<int BuffSize, int NumAxis, typename DataType>
void DataLogger<BuffSize,NumAxis,DataType>::dumpWholeDataToConsole()
{    
    std::cout << "*********" << std::endl << std::endl;

    for ( int k = 0; k < BuffSize; k++ )
    {
        bool hasData = false;
        for ( int axis = 0; axis < NumAxis; axis++ )
        {
            if ( k <= m_currentPos[axis] )
            {
                hasData = true;
            }
        }
        if ( hasData == false )
        {
            break;
        }
        for ( int axis = 0; axis < NumAxis; axis++ )
        {
            if ( k <= m_currentPos[axis] )
            {
                std::cout << m_buffer[axis][k];
            }
            else
            {
                std::cout << "-";
            }

            if ( axis == NumAxis - 1 )
            {
                std::cout << std::endl;
                break;
            }
            switch ( m_delimiter )
            {
                case delimiter::DELIMITER_SEMICOLON:
                    std::cout << ";";
                break;
                case delimiter::DELIMITER_COLON:
                    std::cout << ":";
                break;
                case delimiter::DELIMITER_SPACE:
                    std::cout << " ";
                break;
                default:
                    std::cout << ",";
                break;
            }
        }

    }
    

    std::cout << "*********" << std::endl;


}

template<int BuffSize, int NumAxis, typename DataType>
void DataLogger<BuffSize,NumAxis,DataType>::saveAxisToFile( int pAxis )
{
    std::ofstream file( "axis.txt" );
    if ( !file.is_open() )
    {
        return;
    }

    if ( pAxis < 0 || pAxis >= NumAxis ) 
    {
        return;
    }

    for ( int q = 0; q <= m_currentPos[pAxis]; q++ ) 
    {
        file << m_buffer[pAxis][q] << "\n";
    }

    file.close();
}

template<int BuffSize, int NumAxis, typename DataType>
void DataLogger<BuffSize,NumAxis,DataType>::saveWholeDataToFile()
{
    std::ofstream file( "data.txt" );

    if ( !file.is_open() )
    {
        return;
    }

    for ( int k = 0; k < BuffSize; k++ )
    {
        bool hasData = false;
        for ( int axis = 0; axis < NumAxis; axis++ )
        {
            if ( k <= m_currentPos[axis] )
            {
                hasData = true;
            }
        }
        if ( hasData == false )
        {
            break;
        }
        for ( int axis = 0; axis < NumAxis; axis++ )
        {
            if ( k <= m_currentPos[axis] )
            {
                file << m_buffer[axis][k];
            }
            else
            {
                file << "-";
            }

            if ( axis == NumAxis - 1 )
            {
                file << "\n";
                break;
            }
            switch ( m_delimiter )
            {
                case delimiter::DELIMITER_SEMICOLON:
                    file << ";";
                break;
                case delimiter::DELIMITER_COLON:
                    file << ":";
                break;
                case delimiter::DELIMITER_SPACE:
                    file << " ";
                break;
                default:
                    file << ",";
                break;
            }
        }

    }
    
    file.close();
}

template<int BuffSize, int NumAxis, typename DataType>
void DataLogger<BuffSize,NumAxis,DataType>::setDelimiter( delimiter::_delimiter pDl )
{
    m_delimiter = pDl;
}
