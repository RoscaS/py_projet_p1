from PIL import Image, ImageFilter
import tkinter as tk

image = Image.open('atat.jpg')
image = image.filter(ImageFilter.FIND_EDGES)
image.save('new_name.png')
image = image.convert('1')
image.save('new_name2.png')

pixels = image.load()
width, height = image.size

all_pixels = []
coords = []

for x in range(width):
    for y in range(height):
        cpixel = pixels[x, y]
        # bw_value = int(round(sum(cpixel) / float(len(cpixel))))
        # if bw_value >= 200:
            # (x, y, (r,g,b))
            # coords.append((x, y, cpixel))

        if cpixel == 255:
            coords.append((x, y))


canvas_width  = width
canvas_height = height

master = tk.Tk()

w = tk.Canvas(master, width=canvas_width, height=canvas_height)

w.pack()

for i in coords:
    # print(i)
    x1, y1 = i[0] - 1, i[1] - 1
    x2, y2 = i[0] + 1, i[1] + 1
    w.create_oval(x1, y1, x2, y2, fill="black")

print(width)
print(height)

tk.mainloop()
