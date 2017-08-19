import numpy as np
import tkinter as tk
import cv2

def auto_canny(image, sigma=0.33):
    v = np.median(image)

    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    return edged

image   = cv2.imread("atat.jpg")
gray    = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)

canny   = auto_canny(blurred)

height = np.size(canny, 0)
width  = np.size(canny, 1)

coords = []

cv2.imshow('image', canny)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):  
    cv2.imwrite("atat-canny.jpg", img)
    cv2.destroyAllWindows()

for x in range(width):
    for y in range(height):
        if canny[y, x] != 0:
            coords.append((x, y))

# master = tk.Tk()

# w = tk.Canvas(master, width=width, height=height)
# w.pack()

# for i in coords:
#     x1, y1 = i[0] - 1, i[1] - 1
#     x2, y2 = i[0] + 1, i[1] + 1
#     w.create_oval(x1, y1, x2, y2, fill="black")

# tk.mainloop()
