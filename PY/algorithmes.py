from sklearn.neighbors import NearestNeighbors

import processImg as pi

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

import tkinter as tk


x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

points = np.c_[x, y]

clf = NearestNeighbors(2).fit(points)
G = clf.kneighbors_graph()

T = nx.from_scipy_sparse_matrix(G)

order = list(nx.dfs_preorder_nodes(T, 0))

xx = x[order]
yy = y[order]

plt.plot(xx, yy)
plt.show()

