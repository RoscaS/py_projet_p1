import processImg as pi
import tkinter as tk

class Grid(object):
    def __init__(self, img):
        self.img    = pi.ProcessImg(img)
        self.canny  = self.img.auto()
        self.width  = self.canny.shape[1] # x
        self.height = self.canny.shape[0] # y
        self.len    = self.canny.size     # l

    @property
    def bin_list(self):
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

        self.w    = tk.Tk()
        self.can  = tk.Canvas(
            self.w, width=self.grid.width, height=self.grid.height)

        self.can.pack(side='left', padx=5, pady=5)

        self.current = None # idx
        self.next    = None # idx
        self.x       = None # x
        self.y       = None # y

        self.i = 1

    def launche(self, speed=5):
        self.speed = speed
        self.first_move()
        self.w.mainloop()

    def start_point(self):
        print('start_point')
        for c, i in enumerate(self.lst):
            if i:
                # return self.idx_xy(c)
                return c
        return None

    def idx_xy(self, idx):
        x = idx - ((idx // self.grid.width) * self.grid.width)
        y = idx // self.grid.width
        return (x, y)

    def set_xy(self):
        self.x = self.idx_xy(self.current)[0]
        self.y = self.idx_xy(self.current)[1]

    def first_move(self):
        print('first_move')
        self.current = self.start_point()
        self.set_xy()
        self.lst[self.current] = 0
        self.move()

    def move(self):
        self.i += 1
        print('i: {}/{}\tcurrent idx: {:6}\t({:3},{:3})'.format(
            self.i, self.dots, self.current, self.x, self.y))

        x1, y1 = self.x - 1, self.y - 1
        x2, y2 = self.x + 1, self.y + 1

        oval = self.can.create_oval(x1, y1, x2, y2, width=1, fill='black')

        self.find_next()

        if self.i < self.dots:
            self.w.after(self.speed, self.move)

    def set_current(self, idx):
        self.current = idx
        self.set_xy()
        self.lst[self.current] = 0

    def find_next(self):
        # Gauche
        if self.lst[self.current - 1]:
            self.set_current(self.current - 1)
        # Bas gauche
        elif self.lst[self.current + self.grid.width - 1]:
            self.set_current(self.current + self.grid.width - 1)
        # Bas
        elif self.lst[self.current + self.grid.width]:
            self.set_current(self.current + self.grid.width)
        # Bas Droite
        elif self.lst[self.current + self.grid.width + 1]:
            self.set_current(self.current + self.grid.width + 1)
        # Droite
        elif self.lst[self.current + 1]:
            self.set_current(self.current + 1)
        # Haut droite
        elif self.lst[self.current - self.grid.width + 1]:
            self.set_current(self.current - self.grid.width + 1)
        # Haut
        elif self.lst[self.current - self.grid.width]:
            self.set_current(self.current - self.grid.width)
        # Haut gauche
        elif self.lst[self.current - self.grid.width - 1]:
            self.set_current(self.current - self.grid.width - 1)

        else:
            self.set_current(self.start_point())







if __name__ == '__main__':

    # d = Draw('07Pika.jpg')
    # d = Draw('08face.jpg')
    # d = Draw('06logo2.png')
    # d = Draw('05logo1.png')
    # d = Draw('04carlage.jpg')
    d = Draw('01atat.jpg')
    d.launche(1)