

import math



class SphereFitter :

    def __init__( self, xx, yy, zz ) :

        self.xx = xx
        self.yy = yy
        self.zz = zz

        self.x0 = 0
        self.y0 = 0
        self.z0 = 0
        self.r0 = 1
        
        self.x0Hist = []
        self.y0Hist = []
        self.z0Hist = []
        self.r0Hist = []

        self.m_totalIterations = 500
        self.m_step = 0.001

    def fitSimpleGradientDescend( self, x0, y0, z0, r0 ) :
        
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.r0 = r0
        
        self.x0Hist.append( self.x0 )
        self.y0Hist.append( self.y0 )
        self.z0Hist.append( self.z0 )
        self.r0Hist.append( self.r0 )

        for n in range( self.m_totalIterations ) :

            dJdx0 = 0
            dJdy0 = 0  
            dJdz0 = 0
            for q in range( len( self.xx ) ) :
                dq = math.sqrt( ( self.x0 - self.xx[q] ) ** 2 + 
                                ( self.y0 - self.yy[q] ) ** 2 + 
                                ( self.z0 - self.zz[q] ) ** 2 )
                dJdx0_q = 2 * ( self.x0 - self.xx[q] ) * ( dq - self.r0 ) / dq
                dJdy0_q = 2 * ( self.y0 - self.yy[q] ) * ( dq - self.r0 ) / dq
                dJdz0_q = 2 * ( self.z0 - self.zz[q] ) * ( dq - self.r0 ) / dq

                dJdx0 += dJdx0_q
                dJdy0 += dJdy0_q
                dJdz0 += dJdz0_q
                

            self.x0 += -dJdx0 * self.m_step
            self.y0 += -dJdy0 * self.m_step
            self.z0 += -dJdz0 * self.m_step
            self.r0 = 0
            for q in range( len( self.xx ) ) :
                dq = math.sqrt( ( self.x0 - self.xx[q] ) ** 2 + 
                                ( self.y0 - self.yy[q] ) ** 2 + 
                                ( self.z0 - self.zz[q] ) ** 2 )
                 
                self.r0 += dq
            self.r0 = self.r0 / len( self.xx ) 

            self.x0Hist.append( self.x0 )
            self.y0Hist.append( self.y0 )
            self.z0Hist.append( self.z0 )
            self.r0Hist.append( self.r0 )


















































