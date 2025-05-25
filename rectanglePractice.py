from point import Point


class Rectangle(object):
    def __init__(self,point1,point2):
        if point1 is not Point or point2 is not Point:
            raise(TypeError("Both points should be of type Point"))
        
        self._point1=point1
        self._point2=point2
        
    @property
    def point1(self):
        return self._point1
    
    @property
    def point2(self):
        return self.point2
    
    @point1.setter
    def point1(self,newpoint1):
        if type(newpoint1) is not Point:
            raise(TypeError("The new point should be of type Point"))
        else:
            self._point1=newpoint1
    
    @point2.setter
    def point2(self,newpoint2):
        if type(newpoint2) is not Point:
            raise(TypeError("The type of the new point should be Point"))
        else:
            self._point2=newpoint2
    
    @property
    def area(self):
        len=self._point2.x-self._point1.x
        breadth=self._point2.y-self._point1.y
        return len*breadth