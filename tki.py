from tkinter import Tk, Label, Button
# from square import Square

# def draw_square(Square, canvas):
#     canvas.create_rectangle()


class Interface(object):
    def __init__(self):
        
        self._root=Tk()
        
        self._l1=Label(self._root, text="Hello")
        self._l1.pack()
        
        self._btn1=Button(self._root,text="Press Me!", command= self.onClickButton)
        self._btn1.pack()
        
        self._root.mainloop()
        
    def onClickButton(self):
        self._l1.config(text="Button was pressed")
        
if __name__ == "__main__":
    
    mi=Interface()
    