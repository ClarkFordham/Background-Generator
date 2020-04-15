from tkinter import *
from array_gen import Array_gen
from PIL import Image

class Background_engine(Frame):
    width = 1920
    height = 1080
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets(master)

    def draw_background(self, frame, root, canvas):
        canvas.delete("all")
        gen = Array_gen(self.colors, self.width//2, self.height//2)
        array = gen.create_array()
        for x in range (0, self.width//2):
            for y in range (0, self.height//2):
                canvas.create_rectangle(x*2,y*2,x*2+2,y*2+2,outline=array[x][y], fill=array[x][y])
        root.update()

    def create_widgets(self, root):
        frame = Frame(root)
        frame.pack()
        canvas = Canvas(width=self.width, height=self.height)
        canvas.pack()
        self.generate = Button(frame, text="Generate", command= lambda: self.draw_background(frame, root, canvas))
        self.save = Button(frame, text="Save", command= lambda: self.save_image(canvas))
        self.save.pack(side="bottom")
        self.generate.pack(side="bottom")

    def save_image(self, canvas):
        canvas.postscript(file = 'C:/Users/Clark/Desktop/background.eps')
        image = Image.open('C:/Users/Clark/Desktop/background.eps')
        image.save('C:/Users/Clark/Desktop/background.tif')

def main():
    root = Tk()
    root.geometry("1200x800")
    app = Background_engine(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()