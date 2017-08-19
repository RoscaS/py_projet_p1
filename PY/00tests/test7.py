from sklearn.neighbors import NearestNeighbors
from time import sleep
import processImg as pi
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import tkinter as tk


# x = np.linspace(0, 2 * np.pi, 100)
# y = np.sin(x)


p = pi.ProcessImg("07Pika.jpg").coords

points = []
x = []
y = []
for i in p:
    points.append([i[0], i[1]])
    x.append(i[0])
    y.append(i[1])

x = np.array(x)
y = np.array(y)
points = np.array(points)



# points = np.c_[x, y]
# print(points)

clf = NearestNeighbors(2).fit(points)
G = clf.kneighbors_graph()

T = nx.from_scipy_sparse_matrix(G)

order = list(nx.dfs_preorder_nodes(T, 0))

# xx = x[order]
# yy = y[order]

ordered_points = list(zip(x[order]+50, y[order]+50))

# plt.plot(xx, yy)
# plt.show()


# l = []
# for i in ordered_points:
#     l.append((int(i[0]*10), int(i[1]*10)))


l = ordered_points
i = 1


fen1 = tk.Tk()

x1, y1 = l[i][0] - 1, l[i][1] - 1
x2, y2 = l[i][0] + 1, l[i][1] + 1


can1 = tk.Canvas(fen1, bg='dark grey', height=1000, width=1000)
can1.pack(side='left', padx=5, pady=5)
oval1 = can1.create_oval(x1,y1,x2,y2,width=2,fill='red')

def move():
    global i
    x1, y1 = l[i][0] - 1, l[i][1] - 1
    x2, y2 = l[i][0] + 1, l[i][1] + 1
    # can1.coords(oval1,x1,y1,x2,y2)
    can1.create_oval(x1,y1,x2,y2, width=2, fill='red')
    if i >= len(l):
        i = 0
        fen1.after(10,move)
    else:
        i += 1
        fen1.after(10, move)


move()

fen1.mainloop()