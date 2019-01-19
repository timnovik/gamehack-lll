import pygame
from pygame import time, draw, init, display, event, QUIT, KEYDOWN, K_d, K_a, KEYUP, K_w, K_s, K_SPACE


def menu():
    init()
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    screen = display.set_mode((500, 500))
    screen.fill((255, 255, 255))
    display.update()
    play_is_pressed = False
    chosen_pers = None
    chosen_btn = 0
    first_screen_chosen_btn = 0
    x = 250
    y = 250
    r = 20
    dx = 0
    dy = 0
    btn_play = [150, 100, 200, 100]
    btn_exit = [220, 440, 60, 50]
    first_screen_btns = [btn_play, btn_exit]
    btn1 = [20, 200, 100, 100]
    btn2 = [160, 200, 100, 100]
    btn3 = [300, 200, 100, 100]
    btn_back = [20, 400, 60, 50]
    buttons_ = [btn1, btn2, btn3, btn_back]

    display.update()
    while 1:
        screen.fill((255, 255, 255))
        if not play_is_pressed:
            for btn in first_screen_btns:
                draw.rect(screen, (0, 0, 0), btn)
            draw.rect(screen, blue, first_screen_btns[first_screen_chosen_btn], 10)
            display.update()
            for i in event.get():
                if i.type == QUIT:
                    exit()
                elif i.type == KEYDOWN:
                    if i.key == K_SPACE:
                        if first_screen_chosen_btn == 0:
                            play_is_pressed = True
                        else:
                            quit()
                    if i.key == K_s:
                        first_screen_chosen_btn = 1
                    if i.key == K_w:
                        first_screen_chosen_btn = 0
        elif chosen_pers == None:
            for button in buttons_:
                draw.rect(screen, (0, 0, 0), button)
            draw.rect(screen, blue, buttons_[chosen_btn], 10)
            display.update()
            for i in event.get():
                if i.type == QUIT:
                    exit()
                elif i.type == KEYDOWN:
                    if i.key == K_a:
                        chosen_btn = max(0, chosen_btn - 1)
                    elif i.key == K_d:
                        chosen_btn = min(2, chosen_btn + 1)
                    elif i.key == K_w:
                        if chosen_btn == 3:
                            chosen_btn = 0
                    elif i.key == K_s:
                        chosen_btn = 3
                    elif i.key == K_SPACE:
                        if chosen_btn != 3:
                            chosen_pers = chosen_btn
                        else:
                            play_is_pressed = False
        else:
            pygame.quit()
            return chosen_pers
        time.delay(30)
        pass
