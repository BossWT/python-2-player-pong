class Ball:
    def __init__(self, canvas, color, paddle1, paddle2, P1Goal, P2Goal, P1Score, P2Score):
        self.canvas = canvas
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.P1Goal = P1Goal
        self.P2Goal = P2Goal
        self.P1Score = P1Score
        self.P2Score = P2Score
        self.x = -3
        self.y = 0
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 250, 250)
        self.canvas_height = self.canvas.winfo_height();

    def draw(self):
        pos = self.canvas.coords(self.id)
        if self.hit_paddle(self.paddle1, pos) == True:
            self.x = 3
            self.hit_location(self.paddle1, pos)
        if self.hit_paddle(self.paddle2, pos) == True:
            self.x = -3
            self.hit_location(self.paddle2, pos)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.y = -1
        self.goal(pos)
        self.canvas.move(self.id, self.x, self.y)

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

    def goal(self, pos):
        P1Goal_pos = self.canvas.coords(self.P1Goal.id)
        P2Goal_pos = self.canvas.coords(self.P2Goal.id)
        if pos[2] <= P1Goal_pos[2]:
            self.x = 0
            self.y = 0

            xToCen = abs(250-pos[0])
            yToCen = abs(250-pos[1])

            if pos[1] > 250:
                print(pos[1])
                self.canvas.move(self.id, -xToCen, -yToCen)
            else:
                print(pos[1])
                self.canvas.move(self.id, xToCen, yToCen)

            self.x = 2
            #self.y = 1

        if pos[0] >= P2Goal_pos[0]:
            self.x = 0
            self.y = 0

            xToCen = abs(250-pos[0])
            yToCen = abs(250-pos[1])

            if pos[1] >= 250:
                print("s" + str(pos[1]))
                self.canvas.move(self.id, -xToCen, -yToCen)
            else:
                print(pos[1])
                self.canvas.move(self.id, xToCen, yToCen)

            self.x = 2

