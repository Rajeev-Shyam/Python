from study import Point

class Rectangle(object):
    def __init__(self,point1,point2):
        if type(point1) is not Point or type(point2) is not Point:
            raise(TypeError(" both given points should be in a point format x and y "))
        
        self._point1=point1
        self._point2=point2

    @property
    def point1(self):
        return self._point1
    
    @property
    def point2(self):
        return self._point2
    
    @point1.setter
    def point1(self,newpoint1):
        if type(newpoint1) is not Point:
            raise(TypeError("point 1 is not a point type"))
        else:
            self._point1=newpoint1
    
    @point2.setter
    def point1(self,newpoint2):
        if type(newpoint2) is not Point:
            raise(TypeError("point 2 is not a point type"))
        else:
            self._point2=newpoint2
    
    @property
    def area(self):
        len= self._point2.x-self._point1.x
        breadth= self._point2.y-self._point1.y
        return len*breadth

