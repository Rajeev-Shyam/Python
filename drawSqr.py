from tkinter import Tk, Label, Button, Canvas, Frame
from point import Point
from square import Square

def draw_sqr(sqr,canvas):
    canvas.create_rectangle(sqr.topLeft.x,sqr.topLeft.y,sqr.bottomRight.x,sqr.bottomRight.y,fill=sqr.color)

def main():
    root=Tk()
    root.title("Square-Drawing")

    canvas=Canvas(root, width=400, height=400, bg="white")
    canvas.pack()

    topLeft=Point(50,50)
    bottomRight=Point(200,200)
    sqr=Square(topLeft,bottomRight,color="blue")

    draw_sqr(sqr,canvas)

    root.mainloop()

if __name__=="__main__":
    main()