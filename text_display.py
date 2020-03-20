class TextDisplay:
    def __init__(self, canvas, startX, startY, text):
        self.canvas = canvas
        self.id = self.canvas.create_text(startX, startY, text=text, font=('terminal', 35, 'bold'))
