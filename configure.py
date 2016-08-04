from tkinter import *

class Config:
    def __init__(self):
        self.file = open('p1_config.txt')
        self.text = self.file.read().split()
        self.p1_up = self.text[0]
        self.p1_down = self.text[1]

        self.file = open('p2_config.txt')
        self.text = self.file.read().split()
        self.p2_up = self.text[0]
        self.p2_down = self.text[1]

        self.tk = Tk()
        self.tk.title = "Config"
        self.canvas = Canvas(self.tk, height=150, width=250)
        self.canvas.pack()
        self.tk.update()

        self.txt_p1 = self.canvas.create_text(100, 25, text="Player 1")
        self.txt_p2 = self.canvas.create_text(200, 25, text="Player 2")

        self.txt_p1_up = self.canvas.create_text(40, 50, text="Up")
        self.txt_p1_down = self.canvas.create_text(35, 100, text="Down")

        self.display_p1_up = self.canvas.create_text(100, 50, text= self.p1_up)
        self.display_p1_down = self.canvas.create_text(100, 100, text= self.p1_down)

        self.txt_p2_up = self.canvas.create_text(150, 50, text="Up")
        self.txt_p2_down = self.canvas.create_text(145, 100, text="Down")

        self.display_p1_up = self.canvas.create_text(200, 50, text=self.p2_up)
        self.display_p1_down = self.canvas.create_text(200, 100, text=self.p2_down)


