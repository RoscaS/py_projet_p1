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


def groupes():
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


temp = groupes()
tot  = 0

f = open('data.txt', 'w')
f.close()

for c, i in enumerate(temp):
    tot += len(i[0])
    with open('data.txt', 'a') as f:
        f.write('GROUPE {}\tlen x: {}\tlen y: {}\t tot: {}\n\nx:\n\n{}\n\ny:\n\n{}\n\n'.
            format(c, len(i[0]), len(i[1]), tot, i[0], i[1]))


print(type(temp))
print(type(temp[0]))