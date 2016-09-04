from tkinter import *
from ball import *
from paddle import *
from score_zone import *
from text_display import *
from configure import Config
import time

def main():
    tk = Tk()
    tk.title = "2 Player Pong"
    canvas = Canvas(tk, height=500, width = 500)
    canvas.create_line(250, 0, 250, 500)
    canvas.pack()
    tk.update()

    paddle1 = Paddle(canvas, "blue",20, 200,"<KeyPress-w>", "<KeyPress-s>", "<KeyPress-a>")
    paddle2 = Paddle(canvas, "green", 475, 200, "<KeyPress-Up>", "<KeyPress-Down>", "<KeyPress-Right>")
    P1Goal = ScoreZone(canvas, "yellow", 0, 0)
    P2Goal = ScoreZone(canvas, "yellow", 485, 0)
    P1Score = TextDisplay(canvas, 200, 20, "0")
    P2Score = TextDisplay(canvas, 300, 20, "0")
    ball = Ball(canvas, "red", paddle1, paddle2, P1Goal, P2Goal, P1Score, P2Score)
    #config = Config()
    mainloop(tk,ball,paddle1,paddle2)

def mainloop(tk, ball, paddle1, paddle2):
    while 1:
        ball.draw()
        paddle1.draw()
        paddle2.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

if __name__ == '__main__':
    main()