class ScoreZone:
    def __init__(self, canvas, color, startX, startY):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(0, 0, 20, 500, fill=color)
        self.canvas.move(self.id, startX, startY)
