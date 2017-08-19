import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('atat.jpg', 0)
edges = cv2.Canny(img, 100, 200)

plt.subplots(figsize=(12, 6), dpi=300)
# plt.subplot(121), plt.imshow(img, cmap='gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# plt.show()
f = open("temp.txt", 'w')

for i in img:
    f.write('{}\n'.format(i))

f.close()

# print(type(img))