import random
from tkinter import *
from PIL import Image, ImageTk

tk = Tk()
c = Canvas(tk, width=600, height=1080, bg='white')
c.pack()
show_border = [20, 20]
images = []
field_width = 200


def buttons(key):
    global show_border
    if key.keycode == 38:
        show_border[1] = max(0, show_border[1] - 1)
    if key.keycode == 37:
        show_border[0] = max(0, show_border[0] - 1)
    if key.keycode == 40:
        show_border[1] = min(field_width - 21, show_border[1] + 1)
    if key.keycode == 39:
        show_border[0] = min(field_width - 21, show_border[0] + 1)


wall_img = ImageTk.PhotoImage(Image.open('images/wall.jpg'))
field_img = ImageTk.PhotoImage(Image.open('images/field.jpg'))
rock_img = ImageTk.PhotoImage(Image.open('images/rock.jpg'))
textures = [field_img, wall_img, rock_img]
map_ = [[2] * field_width]
for i in range(field_width - 2):
    map_.append([2] + [1.1] * (field_width - 2) + [2])
map_.append([2] * field_width)


def loop():
    for img in images:
        c.delete(img)
    for t in range(show_border[1], show_border[1] + 21):
        for g in range(show_border[0], show_border[0] + 21):
            if map_[t][g] == 1.1:
                prob = (map_[t + 1][g] + map_[t][g + 1] + map_[t - 1][g] + map_[t][g - 1]) * 12.5
                a = random.randint(1, 100)
                if prob >= 2.5 * a:
                    res = 2
                elif prob >= 1.1 * a:
                    res = 1
                else:
                    res = 0
                map_[t][g] = res
            try:
                if map_[t + 1][g] == map_[t][g + 1] == map_[t - 1][g] == map_[t][g - 1]:
                    res = map_[t + 1][g]
            except:
                continue
            img = textures[map_[t][g]]
            images.append(c.create_image((g - show_border[0]) * 30, (t - show_border[1]) * 30, image=img, anchor=NW))
    c.after(15, loop)


loop()
tk.bind("<KeyPress>", buttons)
mainloop()
