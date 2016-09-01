class Paddle:
    def __init__(self, canvas, color, startX, startY, upKey, downKey):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 10, 100, fill=color)
        self.canvas.move(self.id, startX, startY)
        self.y = 0
        self.canvas.bind_all(upKey, self.go_up)
        self.canvas.bind_all(downKey, self.go_down)
        self.canvas_height = self.canvas.winfo_height()

    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        self.pos = self.canvas.coords(self.id)
        if self.pos[1] <=0 or self.pos[3] >= self.canvas_height:
            self.y = 0

    def go_up(self, evt):
        if self.pos[1] <=0:
            self.y = 0
        else:
            self.y = -2

    def go_down(self, evt):
        if self.pos[3] >= self.canvas_height:
            self.y = 0
        else:
            self.y = 2
