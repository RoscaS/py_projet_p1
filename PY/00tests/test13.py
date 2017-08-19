from sklearn.neighbors import NearestNeighbors
from time import sleep

import cv2
import processImg as pi
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import tkinter as tk

pika = pi.ProcessImg("07Pika.jpg")
points = np.array(pika.coords)

x = points[:, 0]
y = points[:, 1]

clf = NearestNeighbors(2).fit(points)
G   = clf.kneighbors_graph()
T   = nx.from_scipy_sparse_matrix(G)

order = list(nx.dfs_preorder_nodes(T, 0))

mindist = np.inf
minidx  = 0

paths = [list(nx.dfs_preorder_nodes(T, i)) for i in range(len(points))]

for i in range(len(points)):
    p = paths[i]
    ordered = points[p]

    cost = (((ordered[:-1] - ordered[1:]) ** 2).sum(1)).sum()

    if cost < mindist:
        mindist = cost
        minidx  = 1

opt_order = paths[minidx]

xx = x[opt_order]
yy = y[opt_order]


plt.plot(xx, yy)
plt.show()

x1, y1 = xx[0] - 1, yy[0] - 1
x2, y2 = xx[0] + 1, yy[0] + 1

i = 1

fen = tk.Tk()
can = tk.Canvas(fen, bg='dark grey', width=pika.width, height=pika.height)
can.pack(side='left', padx=5, pady=5)
oval = can.create_oval(x1, y1, x2, y2, width=2, fill='red')


def move():
    global i
    x1 = xx[i] - 1
    y1 = yy[i] - 1
    x2 = xx[i] + 1
    y2 = yy[i] + 1

    can.create_oval(x1, y1, x2, y2, width=2, fill='red')

    if i < len(x) - 1:
        i += 1
        fen.after(50, move)

move()

fen.mainloop()