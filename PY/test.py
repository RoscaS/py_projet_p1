import numpy as np
import cv2

def auto(img, sigma=0.33):
    v = np.median(img)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    return cv2.Canny(img, lower, upper)

image = cv2.imread('07Pika.jpg')
g = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
b = cv2.GaussianBlur(g, (3, 3), 0)

img = auto(b)

nez = img[254:310, 259:309]

# print(np.count_nonzero(img))
print(np.nonzero(img[254:310, 259:309]))





# cv2.imshow("img", img)
# cv2.imshow("img", nez)

k = cv2.waitKey(0)
if k == 27: # (escape)
    cv2.destroyAllWindows()




# 200, 300