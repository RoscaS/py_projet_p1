import processImg as pi
import tkinter as tk
from time import sleep


class Grid(object):
    def __init__(self, img):
        self.img = pi.ProcessImg(img)
        self.canny = self.img.auto()
        self.len = self.canny.size
        self.height, self.width = self.canny.shape  # y, x

    @property
    def bin_list(self):
        '''transforme la liste 2d numpy en liste traditionnelle 1d'''
        l = []
        for i in self.canny:
            for j in i:
                l.append(1) if j else l.append(0)
        return l

    def __str__(self):
        return 'width(x):\t{}\nheight(y):\t{}\nlen:\t\t{}'.format(
            self.width, self.height, self.len)

    def bin_to_file(self, name):
        with open(name, 'w') as f:
            for c, i in enumerate(self.bin_list):
                if c % self.width == 0 and c != 0:
                    f.write('\n')

                f.write(str(i))


class Draw(object):

    def __init__(self, img):
        self.grid  = Grid(img)
        self.lst   = self.grid.bin_list
        self.dots  = self.lst.count(1)
        self.speed = None

        self.window = tk.Tk()
        self.can    = tk.Canvas(
            self.window, width=self.grid.width, height=self.grid.height)
        self.can.pack(side='left', padx=5, pady=5)

        self.pen  = 0

        self.up   = self.can.create_oval(0, 0, 0, 0, width=1, fill='blue')
        self.down = self.can.create_oval(0, 0, 0, 0, width=1, fill='red')

        self.idx  = 0    # idx
        # self.next = None # idx
        self.next = self.find_dot()
        self.x    = 0 # x
        self.y    = 0 # y

        self.i, self.j = 0, 0


    def start(self, speed=5):
        self.speed = speed
        # self.next  = self.find_dot()
        self.move()
        self.window.mainloop()


    def idx_to_xy(self, idx):
        x = idx - ((idx // self.grid.width) * self.grid.width)
        y = idx // self.grid.width
        return (x, y)


    def move(self):
        width  = self.grid.width
        x1, y1 = self.x - 1, self.y -1
        x2, y2 = self.x + 1, self.y +1

        if self.pen == 0: # up
            dy = -((self.idx // width) - (self.next // width))
            dx = -((self.idx % width) - (self.next % width))

            if self.i != dx:
                print('self.i != dx')
                if dx > 0 :
                    self.x  += 1
                    self.i  += 1
                else:
                    self.x  -= 1
                    self. i -= 1

            if self.j != dy:
                print('self.j != dy')
                if dy > 0:
                    self.y  += 1
                    self.j  += 1
                else:
                    self.y  -= 1
                    self.j  -= 1

            if self.i == dx and self.j == dy:
                print('\n\n\nICI\n\n\n\n')
                self.pen = 1
                self.i, self.j = 0, 0
                self.can.coords(self.up, 0, 0, 0, 0)

            self.can.coords(self.up, x1-4, y1-4, x2+4, y2+4)
            self.window.after(self.speed, self.move)


        elif self.pen == 1: # down
            mark = self.can.create_oval(x1, y1, x2, y2, width=1, fill='black')
            self.can.coords(self.down, x1-4, y1-4, x2+4, y2+4)

            self.next = self.find_dot()

            self.x, self.y = self.idx_to_xy(self.next)
            self.lst[self.idx] = 0
            self.idx = self.next


            self.window.after(self.speed, self.move)

        print('pen:', self.pen)



    def find_dot(self, radius=3):
        '''Recherche et retourne l'idx du prochain `1` dans 
        `self.lst`. `radius` représente le rayon qui a pour 
        centre l'idx du dernier pixel traité. Si aucun 1 n'existe 
        scan `self.lst` à partir du début pour en trouver un. 
        Si il n'en trouve pas, le dessin est finit. '''

        a = - radius
        b = - radius

        for i in range((radius * 2) + 1):
            for j in range((radius * 2) + 1):
                n = self.idx + a * self.grid.width + b
                # print('j: {} \ta: {}\tb: {}\tidx: {}\t value:{}'.
                # format(j, a, b, n, self.lst[n]))

                if self.lst[n] == 1:
                    print('\t[Pixel found @ idx: {}]'.format(n))
                    return n

                b += 1

            a += 1
            b = - radius

        print('\t[No pixel found. Search from start]') # debug
        self.pen = 0
        for c, i in enumerate(self.lst):
            if i :
                return c

        return None


d = Draw('01atat.jpg')
d.start(10)
# print(d.find_dot(50))
# print(d.grid.len)