from pygame import *
from menu_t import menu
from map_ import make_map
screen = display.set_mode((1025, 768))
init()
display.update()
size = [26, 13]
show_border = [80, 80]
hero_place = [size[0] // 2, size[1] // 2]
images = []
field_width = 200
map_ = make_map(field_width, show_border, hero_place)
border_speed = [0, 0]
hero_speed = [0, 0]


while 1:
    for i in event.get():
        if i.TYPE == QUIT:
            exit()
        elif i.TYPE == KEYDOWN:
            if i.key == K_w:
                if map_[show_border[1] + hero_place[1] - 1][show_border[0] + hero_place[0]] <= 0:
                    if show_border[1] > 0 and hero_place[1] == size[1] // 2:
                        border_speed[1] -= 1
                    else:
                        hero_speed[1] -= 1
            if i.key == K_a:
                if map_[show_border[1] + hero_place[1]][show_border[0] + hero_place[0] - 1] <= 0:
                    if show_border[0] > 0 and hero_place[0] == size[0] // 2:
                        border_speed[0] -= 1
                    else:
                        hero_speed[0] -= 1
            if i.key == K_s:
                if map_[show_border[1] + hero_place[1] + 1][show_border[0] + hero_place[0]] <= 0:
                    if show_border[1] < field_width - size[1] and hero_place[1] == size[1] // 2:
                        border_speed[1] += 1
                    else:
                        hero_speed[1] += 1
            if i.key == K_d:
                if map_[show_border[1] + hero_place[1]][show_border[0] + hero_place[0] + 1] <= 0:
                    if show_border[0] < field_width - size[0] and hero_place[0] == size[0] // 2:
                        border_speed[0] += 1
                    else:
                        hero_speed[0] += 1
        elif i.TYPE == K_UP:
            if i.key == K_w:
                if map_[show_border[1] + hero_place[1] - 1][show_border[0] + hero_place[0]] <= 0:
                    if show_border[1] > 0 and hero_place[1] == size[1] // 2:
                        border_speed[1] = 0
                    else:
                        hero_speed[1] = 0
            if i.key == K_a:
                if map_[show_border[1] + hero_place[1]][show_border[0] + hero_place[0] - 1] <= 0:
                    if show_border[0] > 0 and hero_place[0] == size[0] // 2:
                        border_speed[0] = 0
                    else:
                        hero_speed[0] = 0
            if i.key == K_s:
                if map_[show_border[1] + hero_place[1] + 1][show_border[0] + hero_place[0]] <= 0:
                    if show_border[1] < field_width - size[1] and hero_place[1] == size[1] // 2:
                        border_speed[1] = 0
                    else:
                        hero_speed[1] = 0
            if i.key == K_d:
                if map_[show_border[1] + hero_place[1]][show_border[0] + hero_place[0] + 1] <= 0:
                    if show_border[0] < field_width - size[0] and hero_place[0] == size[0] // 2:
                        border_speed[0] = 0
                    else:
                        hero_speed[0] = 0
    show_border[0], show_border[1] = border_speed[0] + show_border[0], border_speed[1] + show_border[1]
    hero_place[0], hero_place[1] = hero_speed[0] + hero_place[0], hero_speed[1] + hero_place[1]
    
