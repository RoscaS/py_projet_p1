import processImg as pi
import sys
import numpy as np
import tkinter as tk
from time import sleep
from math import sqrt

class Draw(object):
    '''Pour empecher les pointillés, réduire le radius '''
    def __init__(self, img):
        self.grid  = pi.Grid(img)
        self.lst   = self.grid.bin_list
        self.dots  = self.lst.count(1)
        self.speed = None
        self.pen   = 0

        self.window = tk.Tk()
        self.can = tk.Canvas(
            self.window, width=1150, height=800)
        self.can.pack(side='left', padx=5, pady=5)


        self.arm_b = self.can.create_line(0,768,618,768, width=10,fill='green')
        self.arm_a = self.can.create_line(618,768,1122,768, width=10,fill='blue')

        self.sheet = self.can.create_rectangle(100,98,1016,730, width=2)



        # Variables dessin
        self.x    = 0
        self.y    = 768
        self.idx  = self.xy_to_idx(0, 768)
        self.next = self.find_dot()

        self.up   = self.can.create_oval(0, 0, 0, 0, width = 1, fill = 'blue')
        self.down = self.can.create_oval(0, 0, 0, 0, width = 1, fill = 'red')


        self.first = True
        self.i, self.j = 0, 0

    def start(self, speed=5):
        self.speed = speed
        self.move()

        if self.dots > 0:
            self.move()

        self.window.mainloop()

    def idx_to_xy(self, idx):
        x = idx - ((idx // self.grid.width) * self.grid.width)
        y = idx // self.grid.width
        return (x, y)

    def xy_to_idx(self, x, y):
        return (y * self.grid.width) + x

    def circles_intersection(self):
        '''Intersection de deux cercles pour trouver
        le point de jonction du bras'''
        cx_a, cy_a = self.x, self.y
        cx_b, cy_b = 1122, 768
        r_a, r_b   = 504, 618
        dx, dy     = cx_a - cx_b, cy_a - cy_b
        dist       = sqrt(dx ** 2 + dy ** 2)

        # segment `a` et hauteur
        a = (r_a ** 2 - r_b ** 2 + dist ** 2) / (2 * dist)
        h = sqrt(abs(r_a ** 2 - a ** 2))

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

    def move(self):
        width  = self.grid.width
        x1, y1 = self.x - 1, self.y - 1
        x2, y2 = self.x + 1, self.y + 1

        if self.pen == 0:  # up
            dy = -((self.idx // width) - (self.next // width))
            dx = -((self.idx % width) - (self.next % width))

            if self.i != dx:
                if dx > 0:
                    self.x += 1
                    self.i += 1
                else:
                    self.x -= 1
                    self.i -= 1

            if self.j != dy:
                if dy > 0:
                    self.y += 1
                    self.j += 1
                else:
                    self.y -= 1
                    self.j -= 1
            
            self.draw_arms()

            if self.i == dx and self.j == dy:
                sleep(0.2)
                self.pen = 1
                self.i, self.j = 0, 0
                self.idx = self.next
                self.x, self.y = self.idx_to_xy(self.next)

            self.can.coords(self.up, x1 - 6, y1 - 6, x2 + 6, y2 + 6)
            self.can.coords(self.down, 0, 0, 0, 0)

        elif self.pen == 1:  # down

            self.can.coords(self.down, x1 - 6, y1 - 6, x2 + 6, y2 + 6)
            self.can.coords(self.up, 0, 0, 0, 0)

            if self.find_dot():
                self.mark(x1, y1, x2, y2)
            else:
                sleep(0.2)
                self.pen = 0

                # Ici pour réduire le nombre d'itérations de count
                if self.lst.count(1) == 0:
                    return 0

        self.window.after(self.speed, self.move)

    def mark(self, x1, y1, x2, y2):
        self.can.create_oval(x1, y1, x2, y2, width=1, fill='black')
        self.draw_arms()
        self.x, self.y = self.idx_to_xy(self.next)
        self.lst[self.idx] = 0
        self.idx = self.next
        self.dots -= 1


    def find_dot(self, radius=1):
        '''Recherche et retourne l'idx du prochain `1` dans 
        `self.lst`. `radius` représente le rayon qui a pour 
        centre l'idx du dernier pixel traité. Si aucun 1 n'existe 
        scan `self.lst` à partir du début pour en trouver un. 
        Si il n'en trouve pas, le dessin est finit. '''
        a = -radius
        b = -radius
        # Cherche dans un rayon de `radius` un pixel noir suivant
        # pour continuer le trait.
        for i in range((radius * 2) + 1):
            for j in range((radius * 2) + 1):
                n = self.idx + a * self.grid.width + b

                if self.lst[n] == 1:
                    self.next = n
                    return 1
                b += 1
            a += 1
            b = -radius

        # Pas de pixel noir dans un rayon de radius. => Cherche
        # un pixel noir proche pour reprendre de là.
        radius += 2
        a = -radius
        b = -radius
        for i in range((radius * 2) + 1):
            for j in range((radius * 2) + 1):
                n = self.idx + a * self.grid.width + b

                if self.lst[n] == 1:
                    self.next = n
                    return 0 # return 0 => pen up !!
                b += 1
            a += 1
            b = -radius
        # si il ne trouve vraiment pas cherche à partir
        # du début de la self.lst
        for c, i in enumerate(self.lst):
            if i == 1:
                self.next = c
                return 0



if __name__ == '__main__':
    # d = Draw('01atat.jpg')
    d = Draw('07Pika.jpg')
    # d = Draw('12lena.png')
    # d = Draw('02recur.png')
    # d = Draw('06logo2.png')
    # d = Draw('05logo1.png')
    # d = Draw('11circle.jpg')
    d.start(20)
