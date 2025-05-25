from math import sqrt

class Point(object):
    def __init__(self,x,y):
        self._x=x
        self._y=y
    
    def getx(self):
        return self._x
    
    def setx(self,x):
        self._x=x
    
    x=property(getx,setx)
    
    def gety(self):
        return self._y
    
    def sety(self,y):
        self._y=y
    
    y=property(gety,sety)
    
    def __str__(self):
        return "the value of x is %d and the value of y is %d"%(self._x,self._y)
    
    def DistanceBetweenPoints(self,secondPoint):
        if secondPoint is not Point:
            raise(TypeError("The second point must be of type point"))
        
        else:
            distance= sqrt((secondPoint.x-self._x)**2+(secondPoint.y-self._y)**2)
            return distance
        
if __name__ == "__main__":
        point1=Point(10,10)
        print (point1.x)
        print(point1.y)
        point1.x=20
        point1.y=20
        print("%d and %d"%(point1.x,point1.y))