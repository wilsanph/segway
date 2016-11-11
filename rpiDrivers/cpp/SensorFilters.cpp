

#include "SensorFilters.h"
#include <math.h>

namespace sensorFilters
{


    ComplementaryFilter::ComplementaryFilter()   
    {
        m_roll = 0;
        m_pitch = 0;
        m_kGyro = 0.98;
        m_kAcc = 0.02;
    }

    ComplementaryFilter::~ComplementaryFilter()
    {
    
    }

    
    void ComplementaryFilter::update( float gyroX, float gyroY, float gyroZ,
                                      float accX, float accY, float accZ,
                                      float dt )
    {
        this->updateWithGyro( gyroX, gyroY, gyroZ, dt );
        this->correctWithAccel( accX, accY, accZ, dt );
    }

    void ComplementaryFilter::updateWithGyro( float gyroX, float gyroY, float gyroZ, float dt )
    {
        m_roll += gyroX * dt;
        m_pitch += gyroY * dt;

    }

    void ComplementaryFilter::correctWithAccel( float accX, float accY, float accZ, float dt )
    {
        float rollAcc = atan2( accY, accZ ) * 180.0 / M_PI;
        float pitchAcc = atan2( -accX, sqrt( accY * accY + accZ * accZ ) ) * 180.0 / M_PI;


        m_roll  = m_kGyro * m_roll + m_kAcc * rollAcc;       
        m_pitch = m_kGyro * m_pitch + m_kAcc * pitchAcc;       

    }

    float ComplementaryFilter::pitch()
    {
        return m_pitch;
    }


    float ComplementaryFilter::roll()
    {
        return m_roll;
    }


}
