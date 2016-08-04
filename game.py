from tkinter import *
from configure import Config
import time

def main():
    tk = Tk()
    tk.title = "2 Player Pong"
    canvas = Canvas(tk, height=500, width = 500)
    canvas.pack()
    tk.update()

    while 1:
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

if __name__ == '__main__':
    main()