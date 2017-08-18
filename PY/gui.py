import tkinter as tk
import processImg

class Gui(object):
    def __init__(self, Processed_img):
        self.coords = Processed_img.coords
        self.height = Processed_img.height
        self.width  = Processed_img.width

    def display(self):
        master = tk.Tk()
        w = tk.Canvas(master, width=self.width, height=self.height)
        w.pack()

        for i in self.coords:
            x1, y1 = i[0] - 1, i[1] - 1
            x2, y2 = i[0] + 1, i[1] + 1
            w.create_oval(x1, y1, x2, y2, fill="black")

        tk.mainloop()


if __name__ == '__main__':

    gui = Gui(processImg.ProcessImg("07Pika.jpg"))
    gui.display()