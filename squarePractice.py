from point import Point
from rectanglePractice import Rectangle


class Square(Rectangle):
    def __init__(self,point1,point2):
        if point1 is not Point or point2 is not Point:
            raise(TypeError("both the points has to be the type Point"))
        len=abs(point2.x-point1.y)
        breadth=abs(point2.y-point1.x)
        if len!=breadth:
            raise(ValueError("These points are not of a square"))
        
        super().__init__(point1,point2)
        
        
    @Rectangle.point1.setter
    def point1(self,newpoint1):
        if type(newpoint1) is not Point:
            raise(TypeError("The new point must be of type Point"))
        len=abs(self.point2.x-newpoint1.y)
        breadth=abs(self._point2.y-newpoint1.x)
        if len!=breadth:
            raise(ValueError("The new point is not of a square"))
        self._point1=newpoint1
        
    @Rectangle.point2.setter
    def point1(self,newpoint2):
        if type(newpoint2) is not Point:
            raise(TypeError("The new point must be of type Point"))
        len=abs(newpoint2.x-self._point1.y)
        breadth=abs(newpoint2.y-self._point1.x)
        if len!=breadth:
            raise(ValueError("The new point is not of a square"))
        self._point2=newpoint2