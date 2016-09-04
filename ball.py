import random

class Ball:
    def __init__(self, canvas, color, paddle1, paddle2, P1Goal, P2Goal, P1Score, P2Score):
        self.canvas = canvas
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.P1Goal = P1Goal
        self.P2Goal = P2Goal
        self.P1Score = P1Score
        self.score1 = 0 #Stores player 1's score
        self.P2Score = P2Score
        self.score2 = 0 #Stores player 2's score
        self.randomize_movement() #The balls starting position is random
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
        if pos[3] == centre:
            #if the ball hits the centre of the paddle
            self.y = 0
        elif pos[3] > centre:
            #if the ball hits the top half of the paddle
            self.y = 1
        elif pos[3] < centre:
            #if the ball hits the bottom half of the paddle
            self.y = -1

    def goal(self, pos):
        P1Goal_pos = self.canvas.coords(self.P1Goal.id)
        P2Goal_pos = self.canvas.coords(self.P2Goal.id)
        if pos[2] <= P1Goal_pos[2]:
            #Player 2 scores a goal

            #Stop the ball
            self.x = 0
            self.y = 0

            #Get the positive difference from the current position's coordinates to the centre
            xToCen = abs(250-pos[0])
            yToCen = abs(250-pos[1])

            #Move the ball to the centre
            if pos[1] > 250:
                #print("www " + str(pos[1]))
                self.canvas.move(self.id, xToCen, -yToCen)
            else:
                #print("wwwwwwww " + str(pos[1]))
                self.canvas.move(self.id, xToCen, yToCen)

            #Increment score
            self.score2 += 1
            print("p2 scores")
            self.canvas.itemconfig(self.P2Score.id, text=str(self.score2))

            #Get the ball's new speed
            self.randomize_movement()

        elif pos[0] >= P2Goal_pos[0]:
            #Player 1 scores a goal

            #Stop the ball
            self.x = 0
            self.y = 0

            #Get the positive difference from the current position's coordinates to the centre
            xToCen = abs(250-pos[0])
            yToCen = abs(250-pos[1])

            #Move the ball to the centre
            if pos[1] > 250:
                #print("sss " + str(pos[1]))
                self.canvas.move(self.id, -xToCen, -yToCen)
            else:
                #print("ssssss " + str(pos[1]))
                self.canvas.move(self.id, -xToCen, yToCen)

            #Increment score
            self.score1 += 1
            print("p1 scores")
            self.canvas.itemconfig(self.P1Score.id, text=str(self.score1))

            #Get the ball's new speed
            self.randomize_movement()

    def randomize_movement(self):
        startx = [-3,-2, 2, 3]
        random.shuffle(startx)
        self.x = startx[0]
        startY = [-2, -1, 0, 1, 2]
        random.shuffle(startY)
        self.y = startY[0]