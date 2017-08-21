import processImg as pi
import sys
import numpy as np
import tkinter as tk
from time import sleep


class Draw(object):
    def __init__(self, img):
        self.grid = pi.Grid(img)
        self.lst = self.grid.bin_list
        self.dots = self.lst.count(True)
        self.speed = None
        self.pen = 0
        self.up = self.can.create_oval(0,0,0,0, width=1, fill='blue')
        self.down = self.can.create_oval(0,0,0,0, width=1, fill='red')

        self.idx, self.next = 0, self.find_dot()
        self.i, self.j = 0, 0

        self.window = tk.Tk()
        self.can = tk.Canvas(
            self.window, width=self.grid.width, height=self.grid.height)
        self.can.pack(side='left', padx=5, pady=5)

    def idx_to_xy(self, idx):
        x = idx - ((idx // self.grid.width) * self.grid.width)
        y = idx // self.grid.width
        return (x, y)

    def move_up(self):
        width = self.grid.width
        x1, y1 = self.x - 1, self.y - 1
        x2, y2 = self.x + 1, self.y + 1

        if self.i > 0:
            self.x += 1
            self.i += 1
        else:
            self.x -= 1
            self.i -= 1
        
        if self.j != dy:
            pass
