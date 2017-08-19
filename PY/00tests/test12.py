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


def groupes_list():
    l = []
    borne = 0

    while borne < 11201:

        clf = NearestNeighbors(2).fit(points[borne:])
        G = clf.kneighbors_graph()  # len(G) => 11202
        T = nx.from_scipy_sparse_matrix(G)

        order = list(nx.dfs_preorder_nodes(T, 0))
        borne += len(order)

        l.append([x[order], y[order]])

    return l

def move():

    global groupes
    global j
    global i

    print('j: {}\t i: {}'.format(j, i))


    x1 = groupes[j][0][i] - 1
    y1 = groupes[j][1][i] - 1

    x2 = groupes[j][0][i] + 1
    y2 = groupes[j][1][i] + 1


    can.create_oval(x1, y1, x2, y2, width=2, fill='red')

    if i < len(groupes[0][0]) - 1:
        i += 1
        fen.after(100, move)
    else:
        j += 1
        i = 0
        fen.after(100, move)
        
        

i = 0
j = 0

groupes = groupes_list()
print('len groupes: ', len(groupes))

x1, y1 = groupes[0][0][0] - 1, groupes[0][0][1] - 1
x2, y2 = groupes[0][0][0] + 1, groupes[0][0][1] + 1

fen = tk.Tk()
can = tk.Canvas(fen, bg='dark grey', height=pika.height, width=pika.width)
can.pack(side='left', padx=5, pady=5)
oval = can.create_oval(x1, y1, x2, y2, width=2, fill='red')

move()

fen.mainloop()