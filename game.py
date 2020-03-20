from tkinter import Tk, Canvas
from ball import Ball
from paddle import Paddle
from score_zone import ScoreZone
from text_display import TextDisplay
import time


def main():
    tk = Tk()
    tk.title = "2 Player Pong"
    canvas = Canvas(tk, height=500, width=500)
    canvas.create_line(250, 0, 250, 500, dash=(20, 20), width=4)
    canvas.pack()
    tk.update()

    paddle1 = Paddle(canvas, "white", 20, 200, "<KeyPress-w>", "<KeyPress-s>", "<KeyPress-a>")
    paddle2 = Paddle(canvas, "white", 475, 200, "<KeyPress-Up>", "<KeyPress-Down>", "<KeyPress-Right>")
    P1Goal = ScoreZone(canvas, "black", 0, 0)
    P2Goal = ScoreZone(canvas, "black", 485, 0)
    P1Score = TextDisplay(canvas, 200, 20, "0")
    P2Score = TextDisplay(canvas, 300, 20, "0")
    ball = Ball(canvas, "white", paddle1, paddle2, P1Goal, P2Goal, P1Score, P2Score)
    mainloop(tk, ball, paddle1, paddle2)


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
