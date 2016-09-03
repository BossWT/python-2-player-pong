from tkinter import *
from ball import *
from paddle import *
from score_zone import *
from configure import Config
import time

def main():
    tk = Tk()
    tk.title = "2 Player Pong"
    canvas = Canvas(tk, height=500, width = 500)
    canvas.pack()
    tk.update()

    paddle1 = Paddle(canvas, "blue", 20, 200,"<KeyPress-w>", "<KeyPress-s>", "<KeyPress-a>")
    paddle2 = Paddle(canvas, "green", 475, 200, "<KeyPress-Up>", "<KeyPress-Down>", "<KeyPress-Right>")
    ball = Ball(canvas, "red", paddle1, paddle2)
    scorezone1 = ScoreZone(canvas, "yellow", 0, 0)
    scorezone2 = ScoreZone(canvas, "yellow", 485, 0)

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