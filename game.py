from tkinter import *
from ball import *
from paddle import *
from configure import Config
import time

def main():
    tk = Tk()
    tk.title = "2 Player Pong"
    canvas = Canvas(tk, height=500, width = 500)
    canvas.pack()
    tk.update()

    ball = Ball(canvas,"red")
    paddle1 = Paddle(canvas, 0, 0, "blue")
    paddle2 = Paddle(canvas, 490, 0, "green")

    #config = Config()
    mainloop(tk,ball)


def mainloop(tk, ball):
    while 1:
        ball.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

if __name__ == '__main__':
    main()