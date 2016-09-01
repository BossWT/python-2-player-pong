class Paddle:
    def __init__(self, canvas, startX, startY, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 10, 100, fill=color)
        self.canvas.move(self.id, startX, startY)
