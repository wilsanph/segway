import wiringpi
import time

GPIO_BCM_PIN = 25

wiringpi.wiringPiSetupGpio()

class Led:

    def __init__( self, bcmGpioPinNumber ):
        self.m_pinNumber = bcmGpioPinNumber
    	wiringpi.pinMode( self.m_pinNumber, 1 )

    def toggle( self ):
        print 'toggle'
        if self.isHigh():
            self.setLow()
        else:
            self.setHigh()

    def setHigh( self ):
        print 'high'
        wiringpi.digitalWrite( self.m_pinNumber, 1 )

    def setLow( self ):
        print 'low' 
        wiringpi.digitalWrite( self.m_pinNumber, 0 )

    def isHigh( self ):
        _res = wiringpi.digitalRead( self.m_pinNumber )
        return _res == 1

    def free( self ):
        self.setLow()
        wiringpi.pinMode( self.m_pinNumber, 0 )

class DimLed:

    def __init__( self ):
        wiringpi.pinMode( 18, 2 )
        self.m_percent = 0

    def setDimPercent( self, percent ):
        self.m_percent = percent
        wiringpi.pwmWrite( 18, int ( 1024 * self.m_percent ) )

    def addDimPercent( self, amount ):
        self.m_percent += amount
        if self.m_percent > 1 :
            self.m_percent = 1
        elif self.m_percent < 0 :
            self.m_percent = 0
        self.setDimPercent( self.m_percent )

    def free( self ):
        wiringpi.pinMode( 18, 0 )
led = Led( 25 )

for i in range( 4 ):
    led.toggle()
    time.sleep( 0.5 )
    led.toggle()
    time.sleep( 0.5 )


led.free()


dimLed = DimLed()


DT = 10
N = 10
dt = 0.05

numTotalSteps = int( DT / dt )
numSteps = int( numTotalSteps / N )

dimLed.setDimPercent( 0 )



for q in range( N ):
    for k in range( numSteps ):
        dimLed.addDimPercent( dt )
        time.sleep( dt )
    for k in range( numSteps ):
        dimLed.addDimPercent( -dt )
        time.sleep( dt )

dimLed.free()
