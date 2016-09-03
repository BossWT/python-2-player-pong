class Ball:
    def __init__(self, canvas, color, paddle1, paddle2, scoreZone1, scoreZone2):
        self.canvas = canvas
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.scoreZone1 = scoreZone1
        self.scoreZone2 = scoreZone2
        self.count1 = 0
        self.count2 = 0
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
        zone1_pos = self.canvas.coords(self.scoreZone1.id)
        zone2_pos = self.canvas.coords(self.scoreZone2.id)
        if pos[2] <= zone1_pos[2]:
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

            #self.x = 1
            #self.y = 1

        if pos[0] >= zone2_pos[0]:
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

            #self.x = 1
            #self.y = 1

