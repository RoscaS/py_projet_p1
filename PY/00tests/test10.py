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


def find_groups(borne):

    clf = NearestNeighbors(2).fit(points[borne:])
    G = clf.kneighbors_graph()  # len(G) => 11202
    T = nx.from_scipy_sparse_matrix(G)

    order = list(nx.dfs_preorder_nodes(T, 0))
    nouvelle_borne = len(order)
    xx = x[order]
    yy = y[order]

    return [nouvelle_borne, xx, yy]


def move():
    global i
    x1 = data[1][i] - 1
    y1 = data[2][i] - 1
    x2 = data[1][i] + 1
    y2 = data[2][i] + 1

    can.create_oval(x1, y1, x2, y2, width=2, fill='red')

    if i < data[0] - 1:
        i += 1
        fen.after(1, move)


i = 0
borne = 0

data = find_groups(borne)
borne += data[0]
i += 1

x1, y1 = data[1][0] - 1, data[2][0] - 1
x2, y2 = data[1][0] + 1, data[2][0] + 1

fen = tk.Tk()
can = tk.Canvas(fen, bg='dark grey', width=pika.width, height=pika.height)
can.pack(side='left', padx=5, pady=5)
oval = can.create_oval(x1, y1, x2, y2, width=2, fill='red')


move()

while borne < 11201:
    data = find_groups(borne)
    borne += data[0] # += nouvelle borne

    i += 1

    move()
