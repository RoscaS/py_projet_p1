import processImg as pi

import numpy as np
import cv2


def auto(img, sigma=0.33):
    v = np.median(img)

    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))

    return cv2.Canny(img, lower, upper)


def bin_to_file():
    with open('data.txt', 'w') as f:
        for c, i in enumerate(l):
            if c % 710 == 0 and c != 0:
                f.write('\n')

            f.write(str(i))


def canny_to_bin_lst(canny):
    l = []
    for i in canny:
        for j in i:
            if j == 255:
                l.append(1)
            else:
                l.append(0)
    return l


def get_start_point(bin_lst):
    for c, i in enumerate(bin_lst):
        if i == 1:
            return c


img = cv2.imread("08face.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = auto(img)