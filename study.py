# class light(object):
#     def __init__(self, isOnOff, watt):
#         self._isOnOff= isOnOff
#         self._watt= watt
    
#     def getisOnOff(self):
#         return self._isOnOff
    
#     def setisOnOff(self, isOnOff):
#         if type(isOnOff) is not bool:
#             print("Error")
#         else:
#             self._isOnOff=isOnOff
#     def getwatt(self):
#         return self._watt
    
#     def setwatt(self, watt):
#         if watt<0 or watt>120:
#             print("Error")
#         else:
#             self._watt=watt
#     isOnOff=property(getisOnOff,setisOnOff)
#     def __str__(self):
#         if self._isOnOff==True:
#             return "Light is on"
#         else:
#             return "Light is off"
#     watt=property(getwatt,setwatt)


# light1= light(False,80)
# light1.isOnOff=True
# print(light1.isOnOff)
from math import sqrt

class Point(object):
    def __init__(self,x,y):
        self._x=x
        self._y=y
    
    def getx(self):
        return self._x
    
    def setx(self,x):
        if type(x) is not int:
            raise(TypeError("x has to be an integer"))
        else:
            self._x=x

    x=property(getx,setx)

    def gety(self):
        return self._y
    
    def sety(self,y):
        if type(y) is not int:
            raise(TypeError("y has to be an integer"))
        else:
            self._y=y
    
    y=property(gety,sety)
    
    def __str__(self):
        return "x is %d and y is %d" % (self._x,self._y)
    
    def distance_between_points(self,secondPoint):
        if type(secondPoint) is not Point:
            raise(TypeError("second point must be a point"))
        
        distance= sqrt((secondPoint.x - self._x)**2 +(secondPoint.y- self._y)**2)
        return distance

    
if __name__ =="__main__":
    point1=Point(10,10)

    print (point1.x)
    print(point1.y)

    point1.x=20
    point1.y=20

    print("%d %d"%(point1.x,point1.y))

    