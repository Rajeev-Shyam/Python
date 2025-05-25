import tkinter as tk
import random
import time
from datetime import datetime
import math


class ReactionGame:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, bg="white", height=300, width=300)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.check_click)

        self.oval_coords = None
        self.start_time = None
        self.oval_visible = False

        # Start the game
        self.game()

    def game(self):
        # Sleep for a random time between 5 and 10 seconds
        delay = random.randint(5, 10)
        self.root.after(delay * 1000, self.show_oval)

    def show_oval(self):
        # Generate random position within the canvas
        rand_x = random.randint(0, 200)
        rand_y = random.randint(0, 200)
        radius = 50

        # Draw the oval
        self.oval_coords = (rand_x, rand_y, rand_x + 2 * radius, rand_y + 2 * radius)
        self.canvas.create_oval(*self.oval_coords, fill="red")
        self.oval_visible = True

        # Record the time the oval is shown
        self.start_time = datetime.now()

    def check_click(self, event):
        if not self.oval_visible:
            print("Miss - No oval visible.")
            return

        # Check if the click is inside the oval
        x0, y0, x1, y1 = self.oval_coords
        center_x = x0 + (x1 - x0) / 2
        center_y = y0 + (y1 - y0) / 2
        radius = (x1 - x0) / 2

        distance = math.sqrt((event.x - center_x) ** 2 + (event.y - center_y) ** 2)
        if distance <= radius:
            print("Hit!")
            end_time = datetime.now()
            print(f"Reaction time: {(end_time - self.start_time).total_seconds()} seconds")
        else:
            print("Miss!")

        # Reset game state
        self.reset_game()

    def reset_game(self):
        self.canvas.delete("all")
        self.oval_visible = False
        self.oval_coords = None
        self.start_game()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Reaction Game")
    game = ReactionGame(root)
    root.mainloop()
