from tkinter import Tk, Canvas

def mouseClicked(event):
    
    myCanvas.create_oval(event.x, event.y, event.x+20, event.y+20, fill="red")


root= Tk()

myCanvas= Canvas(root, bg="white", width=300, height=300)
myCanvas.bind("<Button-1>", mouseClicked)
myCanvas.pack()

root.mainloop()