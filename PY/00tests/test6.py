import tkinter as tk

def move():
    global x1, y1, dx, dy, flag
    x1, y1 = x1 + dx, y1 + dy

    if x1 > 210:
        x1, dx, dy = 210, 0, 15

    if y1 > 210:
        y1, dx, dy = 210, -15, 0

    if x1 < 10:
        x1, dx, dy = 10, 0, -15

    if y1 < 10:
        y1, dx, dy = 10, 15, 0

    can1.coords(oval1, x1, y1, x1+30, y1+30)

    if flag:
        fen1.after(50, move)

def stop_it():
    global flag
    flag = 0

def start_it():
    global flag
    if not flag:
        flag = 1
        move()

x1, y1 = 10, 10
dx, dy = 15, 0
flag   = 0

fen1 = tk.Tk()
fen1.title("Exercice d'animation avec Tkinter")

can1 = tk.Canvas(fen1, bg='dark grey', height=250, width=250)
can1.pack(side='left', padx=5, pady=5)

oval1 = can1.create_oval(x1, y1, x1+30, y1+30, width=2, fill='red')

bou1 = tk.Button(fen1, text='Quitter', width=8, command=fen1.quit)
bou1.pack(side='bottom')

bou2 = tk.Button(fen1, text='Démarrer', width=8, command=start_it)
bou2.pack()

bou3 = tk.Button(fen1, text='Arrêter', width=8, command=stop_it)
bou3.pack()


fen1.mainloop()