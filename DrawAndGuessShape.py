import tkinter as tk
import random
import threading
import pyttsx3
import math

SHAPES = {
    0: "circle",
    3: "triangle",
    4: "square",
    5: "pentagon",
    6: "hexagon",
    7: "heptagon",
    8: "octagon",
}
COLORS = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
MAX_ROUNDS = 5

def speak(text):
    threading.Thread(target=lambda: pyttsx3.init().say(text) or pyttsx3.init().runAndWait()).start()

class ShapeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Shape Game")
        self.correct = 0
        self.total_clicks = 0
        self.shapes = []
        self.target = None

        self.label = tk.Label(root, text="", font=("Helvetica", 14))
        self.label.pack()

        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)

        self.start_round()

    def start_round(self):
        self.canvas.delete("all")
        self.shapes = []

        for _ in range(random.randint(3, 7)):
            x, y = random.randint(100, 700), random.randint(100, 500)
            sides = random.choice(list(SHAPES.keys()))
            shape = SHAPES[sides]
            color = random.choice(COLORS)
            id = self.draw_shape(x, y, sides, color)
            self.shapes.append({
                "id": id,
                "shape": shape,
                "color": color,
            })

        self.target = random.choice(self.shapes)
        self.update_label()
        speak(f"Which one is the {self.target['color']} {self.target['shape']}?")

    def draw_shape(self, x, y, sides, color):
        size = 40
        if sides == 0:
            return self.canvas.create_oval(x - size, y - size, x + size, y + size, fill=color, outline="black")
        else:
            points = []
            angle = 2 * math.pi / sides
            for i in range(sides):
                px = x + size * math.cos(i * angle - math.pi / 2)
                py = y + size * math.sin(i * angle - math.pi / 2)
                points.extend((px, py))
            return self.canvas.create_polygon(points, fill=color, outline="black")

    def update_label(self):
        self.label.config(text=f"Correct: {self.correct}/{MAX_ROUNDS} | Total Clicks: {self.total_clicks}")

    def on_click(self, event):
        items = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
        if not items:
            return

        self.total_clicks += 1
        clicked_id = items[-1]
        clicked = next((s for s in self.shapes if s["id"] == clicked_id), None)

        if not clicked:
            return

        if clicked == self.target:
            self.correct += 1
            speak("Correct!")
            if self.correct >= MAX_ROUNDS:
                self.canvas.delete("all")
                self.canvas.create_text(400, 300, text="🎉 You Won! 🎉", font=("Helvetica", 32))
                speak("You finished the game!")
                return
            else:
                self.update_label()
                self.root.after(1000, self.start_round)
        else:
            speak("Nope!")
            self.canvas.delete(clicked_id)
            self.shapes.remove(clicked)
            self.update_label()

if __name__ == "__main__":
    root = tk.Tk()
    game = ShapeGame(root)
    root.mainloop()
