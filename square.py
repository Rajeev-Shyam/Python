from rectangle import Rectangle
from study import Point

class Square(Rectangle):
    def __init__(self, point1, point2):
        if type(point1) is not Point or type(point2) is not Point:
            raise(TypeError(" the points shoulde be of type point"))
        len=abs(point2.x-point1.y)
        breadth=abs(point2.y-point1.x)
        if len!=breadth:
            raise(ValueError("These points does not form a square"))

        super().__init__(point1, point2)
    
    @Rectangle.point1.setter
    def point1(self,newpoint1):
        if type(newpoint1) is not Point:
            raise(TypeError(" new point is not of the type Point"))
        len=abs(self._point2.x-newpoint1.y)
        breadth=abs(self._point2.y-newpoint1.x)
        if len!=breadth:
            raise(ValueError("These points does not form a square"))
        
        self._point1=newpoint1
    
    @Rectangle.point2.setter
    def point1(self,newpoint2):
        if type(newpoint2) is not Point:
            raise(TypeError(" new point is not of the type Point"))
        len=abs(newpoint2.x-self._point2.y)
        breadth=abs(newpoint2.y-self._point2.x)
        if len!=breadth:
            raise(ValueError("These points does not form a square"))
        
        self._point2=newpoint2

    
