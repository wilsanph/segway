
#pragma once

namespace sensorFilters
{

    class ComplementaryFilter
    {
        public :
        
        ComplementaryFilter();
        ~ComplementaryFilter();
        
        void update( float gyroX, float gyroY, float gyroZ, 
                     float accX, float accY, float accZ, 
                     float dt );
        void updateWithGyro( float gyroX, float gyroY, float gyroZ,
                             float dt );
        void correctWithAccel( float accX, float accY, float accZ, 
                               float dt );
        float roll();
        float pitch();
        
        private :

        float m_pitch;
        float m_roll;
        float m_kGyro;
        float m_kAcc;

    };





}
