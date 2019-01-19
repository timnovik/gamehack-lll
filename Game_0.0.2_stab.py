import random
from tkinter import *
from PIL import Image, ImageTk
from menu_t import menu

tk = Tk()
c = Canvas(tk, width=1000, height=1080, bg='white')
c.pack()
size = 13
show_border = [80, 80]
hero_place = [size // 2, size // 2]
images = []
field_width = 200
map_ = [[2] * field_width]
wall_img = ImageTk.PhotoImage(Image.open('images/wall.jpg').resize((50, 50)))
field_img = ImageTk.PhotoImage(Image.open('images/field.jpg').resize((50, 50)))
rock_img = ImageTk.PhotoImage(Image.open('images/rock.jpg').resize((50, 50)))
hero1_img = ImageTk.PhotoImage(Image.open('images/Рыцарь.png').resize((50, 50)))
hero2_img = ImageTk.PhotoImage(Image.open('images/Gamer.jpg').resize((30, 30)))
hero3_img = ImageTk.PhotoImage(Image.open('images/Gamer.jpg').resize((40, 40)))
heroes_img = [hero1_img, hero2_img, hero3_img]
textures = [field_img, wall_img, rock_img]

hero_img = heroes_img[menu()]
for i in range(field_width - 2):
    map_.append([2] + [1.1] * (field_width - 2) + [2])
map_.append([2] * field_width)
for i in range(show_border[0] + hero_place[0] - 1, show_border[0] + hero_place[0] + 2):
    for j in range(show_border[0] + hero_place[0] - 1, show_border[0] + hero_place[0] + 2):
        map_[i][j] = 0


def buttons(key):
    global show_border
    if key.keycode == 38:
        if map_[show_border[1] + hero_place[1] - 1][show_border[0] + hero_place[0]] == 0:
            if show_border[1] > 0 and hero_place[1] == size // 2:
                show_border[1] -= 1
            else:
                hero_place[1] -= 1
    if key.keycode == 37:
        if map_[show_border[1] + hero_place[1]][show_border[0] + hero_place[0] - 1] == 0:
            if show_border[0] > 0 and hero_place[0] == size // 2:
                show_border[0] -= 1
            else:
                hero_place[0] -= 1
    if key.keycode == 40:
        if map_[show_border[1] + hero_place[1] + 1][show_border[0] + hero_place[0]] == 0:
            if show_border[1] < field_width - size and hero_place[1] == size // 2:
                show_border[1] += 1
            else:
                hero_place[1] += 1
    if key.keycode == 39:
        if map_[show_border[1] + hero_place[1]][show_border[0] + hero_place[0] + 1] == 0:
            if show_border[0] < field_width - size and hero_place[0] == size // 2:
                show_border[0] += 1
            else:
                hero_place[0] += 1


def loop():
    for img in images:
        c.delete(img)
    for t in range(show_border[1], show_border[1] + size):
        for g in range(show_border[0], show_border[0] + size):
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
                if map_[t - 1][g] == map_[t][g - 1]:
                    res = map_[t - 1][g]
            except:
                continue
            img = textures[map_[t][g]]
            images.append(c.create_image((g - show_border[0]) * 50, (t - show_border[1]) * 50, image=img, anchor=NW))
    images.append(c.create_image(hero_place[0] * 50, hero_place[1] * 50, image=hero_img, anchor=NW))
    c.after(30, loop)


loop()
tk.bind("<KeyPress>", buttons)
mainloop()
