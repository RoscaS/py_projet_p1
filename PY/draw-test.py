import processImg as pi
import sys
import numpy as np
import tkinter as tk
from time import sleep
from math import sqrt

class Draw(object):
    def __init__(self, img):
        self.grid  = pi.Grid(img)
        self.lst   = self.grid.bin_list
        self.dots  = self.lst.count(1)
        self.speed = None
        self.pen   = 0

        # Tkinter
        self.window = tk.Tk()
        self.can = tk.Canvas(self.window, width=1150, height=800)
        self.can.pack(side='left', padx=5, pady=5)

        # bras
        self.arm_b = self.can.create_line(
            0, 768, 618, 768, width=10, fill='green')
        self.arm_a = self.can.create_line(
            618, 768, 1122, 768, width=10, fill='blue')

        # A4
        self.sheet = self.can.create_rectangle(100, 98, 1016, 730, width=2)

        # pen up, down
        self.up = self.can.create_oval(0, 0, 0, 0, width=1, fill='blue')
        self.down = self.can.create_oval(0, 0, 0, 0, width=1, fill='red')

        # var dessin
        self.x = 0
        self.y = 0
        self.dx_i = 0
        self.dy_i = 0
        self.idx  = 0
        self.next = 0

        
    
    def start(self, speed=5):
        self.speed = speed
        self.move()
        self.window.mainloop()

    def idx_to_xy(self, idx):
        return( idx - ((idx // self.grid.width) * self.grid.width),
            idx // self.grid.width)

    def xy_to_idx(self, x, y):
        return (y * self.grid.width) + x

    def circles_intersection(self):
        '''Intersection de deux cercles pour trouver
        le point de jonction du bras'''
        cx_a, cy_a = self.x, self.y
        cx_b, cy_b = 1122, 768
        r_a, r_b = 504, 618
        dx, dy = cx_a - cx_b, cy_a - cy_b
        dist = sqrt(dx**2 + dy**2)

        # segment `a` et hauteur
        a = (r_a**2 - r_b**2 + dist**2) / (2 * dist)
        h = sqrt(abs(r_a**2 - a**2))

        # p2
        x_centre = cx_a + a * (cx_b - cx_a) / dist
        y_centre = cy_a + a * (cy_b - cy_a) / dist

        # p3
        x_intersect = x_centre + h * (cy_b - cy_a) / dist
        y_intersect = y_centre - h * (cx_b - cx_a) / dist

        return (x_intersect, y_intersect, h, a)

    def draw_arms(self):
        c_int_x, c_int_y, h, a = self.circles_intersection()
        self.can.coords(self.arm_b, c_int_x, c_int_y, 1122, 778)
        self.can.coords(self.arm_a, self.x, self.y, c_int_x, c_int_y)
        # pass

    def move(self):
        width = self.grid.width
        x1, y1 = self.x - 1, self.y - 1
        x2, y2 = self.x + 1, self.y + 1
        self.draw_arms()

        if self.pen == 0:
            self.pend_down(x1, y1, x2, y2)

        elif self.pen == 1:
            self.pen_up(x1, y1, x2, y2)

        self.window.after(self.speed, self.move)


    def pen_up(self, x1, y1, x2, y2):
        self.can.coords(self.down, x1 - 6, y1 - 6, x2 + 6, y2 + 6)
        self.can.coords(self.up, 0, 0, 0, 0)

        if self.find_dot(2):
            self.mark(x1, y1, x2, y2)
        else:
            sleep(0.2)
            self.pen = 0

    def pen_down(x1, y1, x2, y2):
        dy = -((self.idx // width) - (self.next // width))
        dx = -((self.idx % width) - (self.next % width))

        if self.dx_i != dx:
            if dx_i > 0:
                self.x += 1
                self.dx_i += 1
            else:
                self.x -= 1
                self.dx_i += 1

        if self.dy_i != dy:
            if dy_i > 0:
                self.y += 1
                self.dy_i += 1
            else:
                self.y -= 1
                self.dy_i -= 1

        if self.dx_i == dx and self.j == dy_i:
            sleep(0.2)
            self.pen = 1
            self.i, self.j = 0, 0
            self.idx = self.next
            self.idx = self.next

        self.can.coords(self.up, x1 - 6, y1 - 6, x2 + 6, y2 + 6)
        self.can.coords(self.down, 0, 0, 0, 0)

    def mark(self, x1, y1, x2, y2):
        self.can.create_oval(x1, y1, x2, y2, width=1, fill='black')
        self.draw_arms()
        self.x, self.y     = self.idx_to_xy(self.next)
        self.idx           = self.next
        self.lst[self.idx] = 0
        self.dots         -= 1

    def finr_dot(self, radius=50):
        for i in range(radius):
            radius = i + 1

            for j in range(-radius, radius + 1):
                n = self.idx - (self.grid.width * radius) + j
                if self.lst[n]:
                    print(1)
                    self.next = n
                    # return 1 if flag else 0
                    return 1

                n = self.idx + (self.grid.width * radius) + j
                if self.lst[n]:
                    print(2)
                    self.next = n
                    # return 1 if flag else 0
                    return 1

            for j in range(-radius + 1, radius):
                n = self.lst[self.idx - radius + (j * self.grid.width)]
                if self.lst[n]:
                    print(3)
                    self.next = n
                    # return 1 if flag else 0
                    return 1

                n = self.lst[self.idx + radius + (j * self.grid.width)]
                if self.lst[n]:
                    print(4)
                    self.next = n
                    # return 1 if flag else 0
                    return 1

        for c, i in enumerate(self.lst):
            if i:
                print(5)
                self.next = c
                self.lst[self.idx] = 0
                return 0

if __name__ == '__main__':
    # d = Draw('01atat.jpg')
    # d = Draw('07Pika.jpg')
    d = Draw('12lena.png')
    # d = Draw('02recur.png')
    # d = Draw('06logo2.png')
    # d = Draw('05logo1.png')
    # d = Draw('11circle.jpg')
    d.start(5)