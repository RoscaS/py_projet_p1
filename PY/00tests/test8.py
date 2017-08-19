from sklearn.neighbors import NearestNeighbors
from time import sleep

import cv2
import processImg as pi
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import tkinter as tk

pika = pi.ProcessImg("07Pika.jpg")
p = np.array(pika.coords)

x = p[:, 0]
y = p[:, 1]

points = np.c_[x, y]

clf = NearestNeighbors(2).fit(points)
G = clf.kneighbors_graph()  # len(G) => 11202
T = nx.from_scipy_sparse_matrix(G)

order = list(nx.dfs_preorder_nodes(T, 0))

print(len(order))

xx = x[order]
yy = y[order]

x1, y1 = xx[0] - 1, yy[0] - 1
x2, y2 = xx[0] + 1, yy[0] + 1

i = 1

fen = tk.Tk()
can = tk.Canvas(fen, bg='dark grey', width=pika.width, height=pika.height)
can.pack(side='left', padx=5, pady=5)
oval = can.create_oval(x1, y1, x2, y2, width=2, fill='red')

# f = open("data.py", 'w')
# f.close()


def move():
    global i
    x1 = x[i] - 1
    y1 = y[i] - 1
    x2 = x[i] + 1
    y2 = y[i] + 1

    # x1 = xx[i] - 1
    # y1 = yy[i] - 1
    # x2 = xx[i] + 1
    # y2 = yy[i] + 1

    # with open("data.py", 'a') as f:
    #     f.write('i: {:3}\t\ta: ({:3}, {:3})\t\tb: ({:3}, {:3})\t\tcoord: ({:3}, {:3})\n'.format(
    #         # i, x1, y1, x2, y2, xx[i], yy[i]))
    #         i, x1, y1, x2, y2, x[i], y[i]))

    can.create_oval(x1, y1, x2, y2, width=2, fill='red')

    # if i < len(xx)-1:
    if i < len(x) - 1:
        i += 1
        fen.after(1, move)


print(
    'clf:\n{}\n\nwidth:\t\t{}\nheight:\t\t{}\nlen(coords):\t{}\nlen(x):\t\t{}\n\
len(y):\t\t{}\nlen(points):\t{}\nG.shape:\t{}\nlen(T):\t{}\n'
    .format(clf, pika.width, pika.height,
            len(pika.coords), len(x), len(y), len(points), G.shape, len(T)))

# move()

# print(np.size(xx))
# print(np.size(yy))
#
# print(np.size(x))
# print(np.size(y))

# cv2.imshow('img', pika.processed)
# k = cv2.waitKey(0)
# cv2.destroyAllWindows()

# fen.mainloop()
