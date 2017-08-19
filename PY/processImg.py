import numpy as np
import cv2

class ProcessImg(object):
    def __init__(self, img):
        self.original  = img
        self.processed = self.__process()
        self.width     = np.size(self.processed, 0)
        self.height    = np.size(self.processed, 1)

    def __process(self):
        img = cv2.imread(self.original)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        return cv2.GaussianBlur(gray, (3, 3), 0)

    @property
    def coords(self):
        '''Retourne une liste de tuples contenant les coordonnées
        de l'image traitée avec `self.auto`(Canny)'''
        canny = self.auto()
        return [(x, y) for y in range(self.height) for x in range(self.width)
                if canny[y, x] != 0]

    @property
    def wide(self):
        return cv2.Canny(self.processed, 10, 200)

    @property
    def tight(self):
        return cv2.Canny(self.processed, 225, 250)

    def auto(self, sigma=0.33):
        '''Resoud le probleme des bornes de la fonction
        canny originale. En principe le sigma est universel'''
        # medianne de l'intensité de tous les pixels de l'image
        v = np.median(self.processed)

        # lower and upper tresholds de l'hysterisis
        lower = int(max(0, (1.0 - sigma) * v))
        upper = int(min(255, (1.0 + sigma) * v))
        canny = cv2.Canny(self.processed, lower, upper)
        # ajoute du padding pour eviter l'overflow lors du draw
        paddi = cv2.copyMakeBorder(
            canny, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=0000)
        return paddi

    def coords_file(self, file='coords'):
        '''Retourne un fichier dont chaque ligne est une coordonnée
        de l'image traitée avec `self.auto`(Canny)'''
        with open(file, 'w') as f:
            for point in self.coords:
                f.write('{} {}\n'.format(point[0], point[1]))

    def display(self, debug='auto'):
        '''Options de la detection de bords: `wide` = bornes de 
        l'hysteris large. `tight` = bornes de l'hysteresis proches. 
        Auto est préférable dans la majorité des cas. `all` affiche 
        les 3'''
        # cv2.namedWindow('wide',  cv2.WINDOW_NORMAL)

        if debug == 'wide':
            cv2.imshow('wide', self.wide)

        elif debug == 'tight':
            cv2.imshow('tight', self.tight)

        elif debug == 'auto':
            cv2.imshow('auto', self.auto())

        elif debug == 'processed':
            cv2.imshow('processed', self.processed)

        elif debug == 'all':
            cv2.imshow('wide', self.wide)
            cv2.imshow('tight', self.tight)
            cv2.imshow('auto', self.auto())

        k = cv2.waitKey(0)

        if k == 27: # (escape)
            cv2.destroyAllWindows()

        elif k == ord('s') and canny != 'all':
            cv2.imwrite("atat-canny.jpg", img)
            cv2.destroyAllWindows()

    # def padding(self):
    # self.processed = cv2.resize(
    # self.processed, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
    # pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
    # M = cv2.getPerspectiveTransform(pts1,pts2)
    # self.processed = cv2.warpPerspective(self.processed,M,(300,300))

    # self.processed = cv2.copyMakeBorder(self.processed, 10, 10, 10, 10,
    #                                     cv2.BORDER_CONSTANT, value=0000)


if __name__ == '__main__':
    # a = ProcessImg("01atat.jpg")
    # a = ProcessImg("02recur.png")
    # a = ProcessImg("03steph.jpg")
    # a = ProcessImg("04carlage.jpg")
    # a = ProcessImg("05logo1.png")
    # a = ProcessImg("06logo2.png")
    # a = ProcessImg("07Pika.jpg")
    # a = ProcessImg("08face.jpg")

    a.display()
