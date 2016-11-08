

import math 

class Vector3 :

    def __init__( self, x=0, y=0, z=0 ) :

        self.x = x
        self.y = y
        self.z = z

    def dot( self, v3 ) :
        return self.x * v3.x + self.y * v3.y + self.z * v3.z

    def cross( self, v3 ) :
        vResult = Vector3()
        vResult.x = self.y * v3.z - self.z * v3.y
        vResult.y = self.z * v3.x - self.x * v3.z
        vResult.z = self.x * v3.y - self.y * v3.x
        return vResult

    def norm( self ) :
        return math.sqrt( self.x ** 2 + 
                          self.y ** 2 + 
                          self.z ** 2 )
    
    def plus( self, v3 ) :
        return Vector3( self.x + v3.x,
                        self.y + v3.y,
                        self.z + v3.z )

    def minus( self, v3 ) :
        return Vector3( self.x - v3.x,  
                        self.y - v3.y,
                        self.z - v3.z )
    
    def scaled( self, scale ) :
        return Vector3( self.x * scale, 
                        self.y * scale,
                        self.z * scale )

    def uDir( self ) :
        norm = self.norm()
        return self.scaled( 1 / norm ) 

    def toString( self ) :
        return "x: " + str( self.x ) + " - y: " + str( self.y ) + " - z: " + str( self.z )


class Line3 :

    def __init__( self ) :
        self.p1 = Vector3( 0, 0, 0 )
        self.p2 = Vector3( 1, 0, 0 )
        self.uDir = Vector3( 1, 0, 0 )

    @staticmethod
    def fromPoints( p1, p2 ) :
        line = Line3()
        line.p1 = p1
        line.p2 = p2
        line.uDir = ( line.p1.minus( line.p2 ) ).uDir()
        
        return line

    @staticmethod
    def fromPointAndDir( p1, uDir ) :
        line = Line3()
        line.p1 = p1
        line.p2 = p1.plus( uDir )
        line.uDir = uDir
        
        return line

    def getIntersect( self, otherLine ) :
        ## if the lines intersect, then the vector
        ## ( self.uDir ).cros( otherLine.uDir ) must 
        ## be perpendicular to any vector formed by 2
        ## points, one in each line 
        
        vectorCandidate = ( self.p1 ).minus( otherLine.p1 )
        normalCandidate = ( self.uDir ).cross( otherLine.uDir )
        result = vectorCandidate.dot( normalCandidate )
        print 'res: ', result 
        if ( abs( vectorCandidate.dot( normalCandidate ) ) > 0.00000001  ) :
            print 'Intersection not found for: '
            print 'vc: ' , vectorCandidate.toString()
            print 'nc: ' , normalCandidate.toString()
            return None
        
        ## the intersection exists, so calculate it using this:
        ## Ps = P0 + s * self.uDir = Q0 + t * otherLine.uDir
        ## ( Q0 - P0 ) = s * self.uDir - t * otherLine.uDir
        ## ( Q0 - P0 ) x  otherLine.uDir = s * self.uDir x otherLine.uDir
        ## s = || ( Q0 - P0 ) x  otherLine.uDir || / || self.uDir x otherLine.uDir ||
        ## s = || vect1 || / || vect2 ||
        q0p0 = ( otherLine.p1 ).minus( self.p1 )
        vect1 = q0p0.cross( otherLine.uDir )
        vect2 = self.uDir.cross( otherLine.uDir )
        s = ( ( vect1.uDir() ).dot( vect2.uDir() ) ) *  vect1.norm() / vect2.norm()
           
        return ( self.p1 ).plus( ( self.uDir ).scaled( s ) )
        
class Sphere :

    def __init__( self, radius, center ) :
        self.radius = radius
        self.center = center

    def toString( self ) :
        return 'r: ' + str( self.radius ) + ' - ' + self.center.toString()

"""

Calculates the circumcenter of a triangle
given its three vertices

@param Vector3 vA A vertex of the triangle
@param Vector3 vB B vertex of the triangle
@param Vector3 vC C vertex of the triangle
@return Vector3 circumcenter of the triangle 
"""
def calcCircumcenter( vA, vB, vC ) :
    b = vA.minus( vC )
    a = vB.minus( vC )

    cCenter = ( a.scaled( b.norm() ** 2 ) ).minus( b.scaled( a.norm() ** 2 ) )
    cCenter = cCenter.cross( b.cross( a ) )
    cCenter = cCenter.scaled( 1 / ( 2 * ( ( b.cross( a ) ).norm() ** 2 ) ) )
    cCenter = cCenter.plus( vC )

    return cCenter 


"""

Calculates the normal to the plane defined by the 3
given points

@param Vector3 vA first point
@param Vector3 vB second point
@param Vector3 vC third point
@return Vector3 normal to the plane defined by the 3 points
""" 
def calcNormalToPlane( vA, vB, vC ) :
    ## Just cross product
    b = vA.minus( vC )
    a = vB.minus( vC )
    return a.cross( b )

def calcCircumsphere( v1, v2, v3, v4 ) :
    ## pick face1 and find the rect that is normal to it and 
    ## goes through the circumcenter of the face
    p1 = calcCircumcenter( v1, v2, v3 )
    udir1 = calcNormalToPlane( v1, v2, v3 )
    line1 = Line3.fromPointAndDir( p1, udir1 ) 
    ## pick face2 and do the same as before 
    p2 = calcCircumcenter( v2, v3, v4 )
    udir2 = calcNormalToPlane( v2, v3, v4 )
    line2 = Line3.fromPointAndDir( p2, udir2 )

    cSphereCenter = line1.getIntersect( line2 )
    cSphereRadius = ( v1.minus( cSphereCenter ) ).norm()

    return Sphere( cSphereRadius, cSphereCenter )


def _test1() :
    vA = Vector3( 2, 2, 0 )
    vB = Vector3( 4, 4, 0 )
    vC = Vector3( 6, 2, 0 )

    print 'vA ', vA.toString()
    print 'vB ', vB.toString()
    print 'vC ', vC.toString()

    cCenter = calcCircumcenter( vA, vB, vC )
    print 'cCenter: ' , cCenter.toString()



def _test2() :

    p1 = Vector3( 0, 0, 0 )
    p2 = Vector3( 5, 5, 5 )
    
    q1 = Vector3( 0, 5, 5 )
    q2 = Vector3( 5, 0, 0 )

    lineP = Line3.fromPoints( p1, p2 )
    lineQ = Line3.fromPoints( q1, q2 )

    intersect = lineP.getIntersect( lineQ )
    print 'test Intersection'
    print 'intersect of lineP and lineQ: ' , intersect.toString()
    

def _test3() :

    p1 = Vector3( 0, -1, 0 )
    p2 = Vector3( 0, 1, 0 )
    p3 = Vector3( -1, 0, 0 )
    p4 = Vector3( 0, 0, 1 )

    csphere = calcCircumsphere( p1, p2, p3, p4 )
    print 'test circumsphere'
    print 'csphere', csphere.toString()


