from sklearn.neighbors import NearestNeighbors
from time import sleep

import cv2
import processImg as pi
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import tkinter as tk

pika   = pi.ProcessImg("07Pika.jpg")
points = np.array(pika.coords)

x = points[:,0]
y = points[:,1]



def find_groups(borne):
    # global points

    clf = NearestNeighbors(2).fit(points[borne:])
    G = clf.kneighbors_graph()  # len(G) => 11202
    T = nx.from_scipy_sparse_matrix(G)

    nouvelle_borne = len(list(nx.dfs_preorder_nodes(T, 0)))
    
    return nouvelle_borne


i     = 0
borne = 0

ensembles = []


while borne < 11201:
    nouvelle_borne = find_groups(borne)
    borne += nouvelle_borne
    print('i: {}\t borne: {}\t delta: {}'.format(i, borne, nouvelle_borne))
    i += 1



