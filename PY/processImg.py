import numpy as np
import cv2

class ProcessImg(object):
    def __init__(self, img):
        self.original  = cv2.imread(img)
        self.height    = self.original.shape[0]
        self.width     = self.original.shape[1]
        self.processed = self.__process()

    @property
    def coords(self):
        '''Retourne une liste de tuples contenant les coordonnées
        de l'image traitée avec `self.auto`(Canny)'''
        canny = self.auto()
        return [(x, y) for y in range(self.height) for x in range(self.width)
                if canny[y, x] != 0]

    def __process(self):
        img    = cv2.cvtColor(self.original, cv2.COLOR_BGR2GRAY)
        img    = cv2.GaussianBlur(img, (3, 3), 0)
        # img  = cv2.Canny(img, 50, 220)
        img    = cv2.Canny(img, 100, 200)
        # kernel = np.ones((2, 2), np.uint8)
        # img  = cv2.dilate(img, kernel, iterations = 1)
        # img  = cv2.erode(img, kernel, iterations  = 1)
        # img  = self.resize(img)

        return self.padding(img)

    def resize(self, img, width=640):
        if self.width > 640:
            img_scale = width / self.width
            xx = int(self.original.shape[1] * img_scale)
            yy = int(self.original.shape[0] * img_scale)
            self.height, self.width = yy, xx
            resized = cv2.resize(img, (xx, yy))
            return resized

    def auto(self, img, sigma=0.33):
        '''Resoud le probleme des bornes de la fonction
        canny originale. En principe le sigma est universel'''
        # medianne de l'intensité de tous les pixels de l'image
        v = np.median(img)
        # lower and upper tresholds de l'hysterisis
        lower = int(max(0, (1.0 - sigma) * v))
        upper = int(min(255, (1.0 + sigma) * v))
        canny = cv2.Canny(img, lower, upper)

        return canny

    def padding(self, canny):
        '''Ajoute du padding pour eviter l'overflow lors du draw'''
        return cv2.copyMakeBorder(
            canny, 100, 100, 100, 100, cv2.BORDER_CONSTANT, value=0000)

    def coords_file(self, file='coords'):
        '''Retourne un fichier dont chaque ligne est une coordonnée
        de l'image traitée avec `self.auto`(Canny)'''
        with open(file, 'w') as f:
            for point in self.coords:
                f.write('{} {}\n'.format(point[0], point[1]))

    def display(self):
        cv2.imshow('img', self.processed)

        k = cv2.waitKey(0)

        if k == 27: # (escape)
            cv2.destroyAllWindows()

        elif k == ord('s') and canny != 'all':
            cv2.imwrite("atat-canny.jpg", img)
            cv2.destroyAllWindows()


class Grid(object):
    def __init__(self, img):
        self.img = ProcessImg(img)
        self.canny = self.img.processed
        self.len = self.canny.size
        self.height, self.width = self.canny.shape  # y, x

    @property
    def bin_list(self):
        '''transforme la liste 2d numpy en liste traditionnelle 1d'''
        l = []
        for i in self.canny:
            for j in i:
                l.append(1) if j else l.append(0)
        return bytearray(l)

    def __str__(self):
        return 'width(x):\t{}\nheight(y):\t{}\nlen:\t\t{}'.format(
            self.width, self.height, self.len)

    def bin_to_file(self, name):
        with open(name, 'w') as f:
            for c, i in enumerate(self.bin_list):
                if c % self.width == 0 and c != 0:
                    f.write('\n')

                f.write(str(i))


if __name__ == '__main__':
    # a = ProcessImg("01atat.jpg")
    # a = ProcessImg("02recur.png")
    # a = ProcessImg("03steph.jpg")
    # a = ProcessImg("04carlage.jpg")
    # a = ProcessImg("05logo1.png")
    # a = ProcessImg("06logo2.png")
    # a = ProcessImg("07Pika.jpg")
    # a = ProcessImg("08face.jpg")
    # a = ProcessImg("11circle.jpg")
    a = ProcessImg("12lena.png")

    # print(type(a.processed))
    # print(a.processed.shape)
    # a.display('original')
    # a.display('processed')
    # a.display('all')
    a.display()

