class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)

    def draw(self):
        self.canvas.move(self.id, 2, 0)
        pos = self.canvas.coords(self.id)