import random
from menu_t_v2 import menu
from map_ import make_map
import pygame
def keyPressed(inputKey):
    keysPressed = pygame.key.get_pressed()
    if keysPressed[inputKey]:
        return True
    else:
        return False
import time
size = [25, 13]
show_border = [88, 94]
hero_place = [size[0] // 2, size[1] // 2] 
images = []
field_width = 200
castle_hp = 10
map_ = make_map(field_width)
wall_img = pygame.image.load('images/wall.png')
field_img = pygame.image.load('images/grass5.jpg')
road_img = pygame.image.load('images/road1.png')
rock_img = pygame.image.load('images/rock.png')
qq = menu()
knight_img1 = pygame.image.load('images/Рыцарь/Стоит.png')
knight_img2 = pygame.image.load('images/Рыцарь/Бежит 1.png')
knight_img3 = pygame.image.load('images/Рыцарь/Бежит 2.png')
knight_img4 = pygame.image.load('images/Рыцарь/Атака.png')
knight_img5 = pygame.image.load('images/Рыцарь/спец атака.png')
knight_img6 = pygame.image.load('images/Рыцарь/2(Стоит).png')
knight_img7 = pygame.image.load('images/Рыцарь/2(Бежит 1).png')
knight_img8 = pygame.image.load('images/Рыцарь/2(Бежит 2).png')
knight_img9 = pygame.image.load('images/Рыцарь/2(Атака).png')
p_img5 = pygame.image.load('images/Принцесса/Стоит.png')
p_img6 = pygame.image.load('images/Принцесса/Идет.png')
p_img7 = pygame.image.load('images/Принцесса/Атака.png')
p_img4 = pygame.image.load('images/Принцесса/Спец атака.png')
p_img1 = pygame.image.load('images/Принцесса/2(Стоит).png')
p_img2 = pygame.image.load('images/Принцесса/2(Идет).png')
p_img3 = pygame.image.load('images/Принцесса/2(Атака).png')
mag_1 = pygame.image.load('images/Маг/Стоит.png')
mag_2 = pygame.image.load('images/Маг/Атака.png')
mag_3 = pygame.image.load('images/Маг/2(Стоит).png')
mag_4 = pygame.image.load('images/Маг/2(Атака).png')
monster1_img = pygame.image.load('images/лучник2.png')
if qq == 0:
    right_ = [knight_img1, knight_img2, knight_img3, knight_img1]
    left_ = [knight_img6, knight_img7, knight_img8, knight_img6]
    attack_right = [knight_img1, knight_img4, knight_img1]
    attack_left = [knight_img6, knight_img9, knight_img6]
    heroes_img = [knight_img1, knight_img6]
elif qq == 1:
    right_ = [p_img1, p_img2, p_img1]
    left_ = [p_img5, p_img6, p_img5]
    attack_right = [p_img1, p_img3, p_img1]
    attack_left = [p_img5, p_img7, p_img5]
elif qq == 2:
    right_ = [mag_1]
    left_ = [mag_2]
    attack_right = [mag_2]
    attack_left = [mag_4]
tower1 = pygame.image.load('images/Хорошие лучники.png')
textures = [field_img, wall_img, rock_img, road_img]
heroes_img = [(knight_img1, knight_img6), (p_img1, p_img5), (mag_1, mag_3)]
hero_img = heroes_img[qq][0]
knight = {'attack': 2, 'special': 4, 'hp': 6, 'hp_left': 6}
pr = {'attack': 3, 'special': 2, 'hp': 4, 'hp_left': 4}
mag = {'attack': 4, 'hp': 3, 'hp_left': 3}
archer_tower = {'attack': 3, 'range': 5, 'hp': 3, 'hp_left': 3, 'cost': 30, 'count' : 0, 'timer':0}
towers = []
heroes = [knight, pr, mag]
hero = heroes[qq]
tower_counter = 0
monster1 = {'attack': 1, 'hp': 1, 'hp_left': 1, 'reward': 10, 'time': 0}
monsters = []
monster1counter = 0
money = 10

window = pygame.display.set_mode((1025, 768))
pygame.display.set_caption("towers and magic")
pygame.init()
FPS = 30
clock = pygame.time.Clock()
dir = [0, 1]


def draw_bullet(xs, ys, xf, yf):
    pygame.draw.line(window, (0, 0, 0), [xs * 40, ys * 40], [xf * 40, yf * 40], 40)
    pygame.time.delay(100)
   

def animation(img_list, x, y):
    for i in range(len(img_list)):
        window.blit(img_list[i], (x * 40, y * 40))
        pygame.display.update()
        pygame.time.delay(40)
        window.blit(textures[map_[y + show_border[1]][x + show_border[0]]], (x * 40, y * 40))


def text_get(txt = "", color = (0,0,0), x = 0, y = 0, size = 50):
    global screen 
    myFont = pygame.font.SysFont("none", size)
    fontImage = myFont.render(txt, 0, (color)) 
    # place = fontImage.get_rect(center=(x, y))
    window.blit(fontImage, (x, y))

info = "press Q to build tower, if you have more then 15 coins..."
loop = 1
m_timer = 0
try:
    while loop:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                loop = 0
            else:
                if i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_q:
                        if  tower_counter >= 120 and money >= 15 and map_[show_border[1] + hero_place[1] + dir[1]][show_border[0] + hero_place[0] + dir[0]] == 0:
                            tower_counter = 0
                            money -= 15
                            tower = archer_tower
                            tower['x'] = show_border[0] + hero_place[0] + dir[0]
                            tower['y'] = show_border[1] + hero_place[1] + dir[1]
                            towers.append(tower)
                            map_[show_border[1] + hero_place[1] + dir[1]][show_border[0] + hero_place[0] + dir[0]] = -len(towers) - 2
                        else:
                            info = "coins required or place choosen incorrectly"
        if keyPressed(pygame.K_w):
            animation(right_, hero_place[0], hero_place[1])
            dir = [0, -1]
            if -1 <= map_[show_border[1] + hero_place[1] - 1][show_border[0] + hero_place[0]] <= 0:
                if hero_place[1] == size[1] // 2:
                    show_border[1] -= 1
                else:
                    hero_place[1] -= 1
    
        if keyPressed(pygame.K_a):
            try:
                animation(left_, hero_place[0], hero_place[1])
                hero_img = heroes_img[qq][1]
                dir = [-1, 0]
            except:
                pass
            if -1 <= map_[show_border[1] + hero_place[1]][show_border[0] + hero_place[0] - 1] <= 0:
                if hero_place[0] == size[0] // 2:
                    show_border[0] -= 1
                else:
                    hero_place[0] -= 1
    
        if keyPressed(pygame.K_s):
            animation(right_, hero_place[0], hero_place[1])
            dir = [0, 1]
            if -1 <= map_[show_border[1] + hero_place[1] + 1][show_border[0] + hero_place[0]] <= 0:
                if show_border[1] < field_width - size[1] and hero_place[1] == size[1] // 2:
                    show_border[1] += 1
                else:
                    hero_place[1] += 1
    
        if keyPressed(pygame.K_d):
            hero_img = heroes_img[qq][0]
            animation(right_, hero_place[0], hero_place[1])
            dir = [1, 0]
            if -1 <= map_[show_border[1] + hero_place[1]][show_border[0] + hero_place[0] + 1] <= 0:
                if show_border[0] < field_width - size[0] and hero_place[0] == size[0] // 2:
                    show_border[0] += 1
                else:
                    hero_place[0] += 1
    
        if keyPressed(pygame.K_SPACE):
            target = map_[show_border[1] + hero_place[1] + dir[1]][show_border[0] + hero_place[0] + dir[0]]
            if target == 1:
                map_[show_border[1] + hero_place[1] + dir[1]][show_border[0] + hero_place[0] + dir[0]] = 0
                if dir[0] == 1 or dir[0] == 0:
                    animation(attack_right, hero_place[0], hero_place[1])
                else:
                    animation(attack_left, hero_place[0], hero_place[1])
            elif target >= 3:
                monsters[target - 3]['hp_left'] -= hero['attack']
                if dir[0] == 1 or dir[0] == 0:
                    animation(attack_right, hero_place[0], hero_place[1])
                else:
                    animation(attack_left, hero_place[0], hero_place[1])
                if monsters[target - 3]['hp_left'] <= 0:
                    money += monsters[target - 3]['reward']
                    map_[show_border[1] + hero_place[1] + dir[1]][show_border[0] + hero_place[0] + dir[0]] = -1
    
        tower_counter += 1
        monster1counter += 1
        try:
            for i in range(show_border[0] + hero_place[0] - 1, show_border[0] + hero_place[0] + 2):
                for j in range(show_border[1] + show_border[1] - 1, show_border[1] + show_border[1] + 2):
                    if map_[j][i] > 2:
                        hero['hp_left'] -= monsters[map_[j][i] - 3]['attack'] * (monsters[map_[j][i] - 3]['time']) // 30
                        monsters[map_[j][i] - 3]['time'] = 0
            if hero['hp_left'] <= 0:
                print('death')
                loop=0
        except:
            pass
        for monster in monsters:
            x, y = monster['x'], monster['y']
            if map_[y][x] == -1:
                pass
            elif monster['x'] == 1:
                map_[y][x] = -1
                castle_hp -= 1
            else:
                monster['time'] += 1
                if monster['time'] >= 60:
                    monster['time'] = 30
                if random.randint(1, 4) and monster['time'] >= 30:
                    monster['time'] -= 30
                    if map_[y][x - 1] == -1:
                        map_[y][x], map_[y][x - 1] = -1, map_[y][x]
                        monster['x'] -= 1
                    elif map_[y - 1][x] == -1:
                        map_[y][x], map_[y - 1][x] = -1, map_[y][x]
                        monster['y'] -= 1
                    else:
                        map_[y][x], map_[y + 1][x] = -1, map_[y][x]
                        monster['y'] += 1
        if monster1counter == 10 and len(monsters) < 1000:
            monster1counter = 0
            monster = monster1
            monster['x'] = random.randint(field_width // 2, field_width - 2)
            monster['y'] = random.randint(field_width // 2, field_width // 2 + 2)
            monsters.append(monster)
            map_[monster['y']][monster['x']] = len(monsters) + 2
    
        # monsters
        window.fill((0, 0, 0))
        for t in range(show_border[1], show_border[1] + size[1]):
            for g in range(show_border[0], show_border[0] + size[0]):
                if map_[t][g] == 1.1:
                    prob = (map_[t + 1][g] + map_[t][g + 1] + map_[t - 1][g] + map_[t][g - 1])
                    a = random.randint(1, 8)
                    res = 0
                    if prob >= 2 * a:
                        res = 2
                    elif prob >= a:
                        res = 1
                    map_[t][g] = res
                if t == show_border[1] + hero_place[1] and g == show_border[0] + hero_place[0]:
                    try:
                        window.blit(textures[map_[t][g]], ((g - show_border[0]) * 40, (t - show_border[1]) * 40))
                        window.blit(hero_img, (hero_place[0] * 40, hero_place[1] * 40))
                    except:
                        hero["hp_left"] -= 1
                elif map_[t][g] > 2:
                    try:
                        window.blit(textures[-1], ((g - show_border[0]) * 40, (t - show_border[1]) * 40))
                        window.blit(monster1_img, ((g - show_border[0]) * 40, (t - show_border[1]) * 40))
                    except:
                        hero["hp_left"] -= 1
                elif map_[t][g] < -2:
                    try:
                        window.blit(textures[0], ((g - show_border[0]) * 40, (t - show_border[1]) * 40))
                        window.blit(tower1, ((g - show_border[0]) * 40, (t - show_border[1] - 1) * 40))
                    except:
                        hero["hp_left"] -= 1
                else:
                    try:
                        window.blit(textures[map_[t][g]], ((g - show_border[0]) * 40, (t - show_border[1]) * 40))
                    except:
                        hero["hp_left"] -= 1
        def tower_killing():
            global money,m_timer
            for tower in towers:
                for c1 in range(tower['x'] - tower['range'], tower['x'] + tower['range'] + 1):
                    for c2 in range(tower['y'] - tower['range'], tower['y'] + tower['range'] + 1):
                        # print(map_[c2][c1], c2, c1, tower['x'], tower['y'])
                        if monsters[map_[c2][c1] - 3]['hp_left'] <= 0 and time.clock() - tower['timer'] >= 3:
                                    towers[towers.index(tower)]['count'] += 1
                                    # print(tower['count'])
                                    if tower['count'] > 10:
                                        map_[tower['y']][tower['x']] = 0
                                    tower['timer'] = time.clock()
                                    money += monsters[map_[c2][c1] - 3]['reward'] // 2
                                    inf0 = "monster is killed"
                                    map_[c2][c1] = -1
                                    return
        tower_killing()
        text_get("Money: " + str(money), (255, 255, 255), 50, 550, 50)
        text_get("Health: " + str(hero["hp_left"]), (255, 255,255), 50, 600, 50)  
        text_get(str(info), (255, 255, 255), 50, 650, 50)
        pygame.display.update()
        clock.tick(FPS)
    ch = 1
    ts = pygame.image.load('images/Game over.png')
    while ch:
        window.blit(ts, (0,0))
        text_get("Exit", (255, 255, 255), 50, 680, 100)
        if keyPressed(pygame.K_SPACE):
            ch = 0
        pygame.display.update()
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                ch = 0    
except:
    ch = 1
    ts = pygame.image.load('images/Game over.png')
    while ch:
        window.blit(ts, (0,0))
        text_get("Exit", (255, 255, 255), 50, 680, 100)
        if keyPressed(pygame.K_SPACE):
            ch = 0
        pygame.display.update()
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                ch = 0        
    
pygame.quit()

