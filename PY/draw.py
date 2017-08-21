import processImg as pi
import sys
import numpy as np
import tkinter as tk
from time import sleep

class Draw(object):
    '''Pour empecher les pointillés, réduire le radius '''
    def __init__(self, img):
        self.grid  = pi.Grid(img)
        self.lst   = self.grid.bin_list
        self.dots  = self.lst.count(1)
        self.speed = None

        self.window = tk.Tk()
        self.can = tk.Canvas(
            self.window, width=self.grid.width, height=self.grid.height)
        self.can.pack(side='left', padx=5, pady=5)

        self.pen = 0

        self.up = self.can.create_oval(0, 0, 0, 0, width=1, fill='blue')
        self.down = self.can.create_oval(0, 0, 0, 0, width=1, fill='red')

        self.idx = 0  # idx
        self.next = self.find_dot()
        self.x = 0  # x
        self.y = 0  # y

        self.i, self.j = 0, 0

        self.alarm = 100

    def start(self, speed=5):
        self.speed = speed
        self.move()
        self.window.mainloop()

    def idx_to_xy(self, idx):
        x = idx - ((idx // self.grid.width) * self.grid.width)
        y = idx // self.grid.width
        return (x, y)

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

            if self.i == dx and self.j == dy:
                sleep(0.1)
                self.pen = 1
                self.i, self.j = 0, 0
                self.idx = self.next
                self.x, self.y = self.idx_to_xy(self.next)

            self.can.coords(self.up, x1 - 6, y1 - 6, x2 + 6, y2 + 6)
            self.can.coords(self.down, 0, 0, 0, 0)

        # PROBLEME DE RECURSSION QUI INDUIT LA LENTEUR PROGRESSIVE.
        # SEPARER CETTE FONCTION EN DEUX PEUT PEUT-ETRE RESOUDRE
        # LE PROBLEME !
        # https://www.daniweb.com/programming/software-development/threads/322107/python-after-method-causing-slowdown

        elif self.pen == 1:  # down

            self.can.coords(self.down, x1 - 6, y1 - 6, x2 + 6, y2 + 6)
            self.can.coords(self.up, 0, 0, 0, 0)

            if self.find_dot():
                mark = self.can.create_oval(x1, y1, x2, y2, width=1, fill='black')
                self.x, self.y = self.idx_to_xy(self.next)
                self.lst[self.idx] = 0
                self.idx = self.next
                self.dots -= 1
            else:
                sleep(0.1)
                self.pen = 0

                if self.lst.count(1) == 0:
                    return 0

        self.window.after(self.speed, self.move)

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




# d = Draw('01atat.jpg')
# d = Draw('07Pika.jpg')
# d = Draw('12lena.png')
# d = Draw('02recur.png')
d = Draw('06logo2.png')
# d = Draw('05logo1.png')
# d = Draw('11circle.jpg')
d.start(1)
# print(d.find_dot(50))
# print(d.grid.len)