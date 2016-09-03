class Ball:
    def __init__(self, canvas, color, paddle1, paddle2):
        self.canvas = canvas
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.x = -3
        self.y = 0
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 250, 250)
        self.canvas_height = self.canvas.winfo_height();

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if self.hit_paddle(self.paddle1, pos) == True:
            self.x = 3
            self.hit_location(self.paddle1, pos)
        if self.hit_paddle(self.paddle2, pos) == True:
            self.x = -3
            self.hit_location(self.paddle2, pos)
        if pos[1] <=0:
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.y = -1

    def hit_paddle(self, paddle, pos):
        paddle_pos = self.canvas.coords(paddle.id)
        if pos[2] >= paddle_pos[2] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def hit_location(self, paddle, pos):
        paddle_pos = self.canvas.coords(paddle.id)
        centre = (paddle_pos[1] + paddle_pos[3]) / 2
        if pos[3] > centre:
            self.y = 1
        elif pos[3] < centre:
            self.y = -1

    def hit_paddle2(self, pos):
        paddle_pos = self.canvas.coords(self.paddle2.id)
        if pos[2] >= paddle_pos[2] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

