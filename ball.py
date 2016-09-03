class Ball:
    def __init__(self, canvas, color, paddle1, paddle2):
        self.canvas = canvas
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.x = -3
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if self.hit_paddle2(pos) == True:
            self.x = -3
        if self.hit_paddle1(pos) == True:
            self.x = 3

    def hit_paddle1(self, pos):
        paddle_pos = self.canvas.coords(self.paddle1.id)
        if pos[2] >= paddle_pos[2] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def hit_paddle2(self, pos):
        paddle_pos = self.canvas.coords(self.paddle2.id)
        if pos[2] >= paddle_pos[2] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False