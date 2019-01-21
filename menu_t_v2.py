import pygame
from pygame import time, draw, init, display, event, QUIT, KEYDOWN, K_d, K_a, KEYUP, K_w, K_s, K_SPACE, quit
from time import sleep
screen = display.set_mode((1024, 768))

def text_get(txt = "", color = (0,0,0), x = 0, y = 0, size = 50):
    global screen
    myFont = pygame.font.SysFont("none", size)
    fontImage = myFont.render(txt, 0, (color)) 
    place = fontImage.get_rect(center=(x, y))
    screen.blit(fontImage, place)   
    # display.update() 
def keyPressed(inputKey):
    keysPressed = pygame.key.get_pressed()
    if keysPressed[inputKey]:
        return True
    else:
        return False

def menu():
    init()
    FPS = 15
    clock = pygame.time.Clock()    
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (255, 255, 100)
    
    screen.fill((0, 0, 0))
    display.update()
    play_is_pressed = False
    chosen_pers = None
    chosen_btn = 0
    first_screen_chosen_btn = 0
    
    
    #music
    pygame.mixer.music.load('2.mp3')
    pygame.mixer.music.play(-1)
    
    bg = pygame.image.load('images/bg1.png')
    bg1 = pygame.image.load('images/bg2.png')
    x = 250
    y = 250
    r = 20
    dx = 0
    dy = 0
    btn_play = [512 - 100, 368 - 50, 200, 90]
    btn_exit = [5, 690, 80, 50]
    first_screen_btns_r = [btn_play, btn_exit]
    
    btn_play = [512 - 100, 368 - 50,pygame.image.load('images/play.png')]
    btn_exit = [18, 700, pygame.image.load('images/exit.png')]
    first_screen_btns = [btn_play, btn_exit]    
    
    btn1 = [512 - 100 - 250, 368 - 100]
    btn2 = [512 - 100, 368 - 100]
    btn3 = [512 - 100 + 250, 368 - 100] 
    btn_back = [18, 700]
    btn_rating = [900, 700]
    
    r_btn1 = [512 - 100 - 250, 368 - 100, 200, 200]
    r_btn2 = [512 - 100, 368 - 100, 200, 200]
    r_btn3 = [512 - 100 + 250, 368 - 100, 200, 200] 
    r_btn_back = [18, 700, 60, 50]
    r_rating = [900, 700, 100, 60]
    buttons_r = [r_btn1, r_btn2, r_btn3, r_btn_back, r_rating]  
    
    btn1 += [pygame.image.load('images/Nps/Рыцарь/2(Стоит).png')]  
    btn2 += [pygame.image.load('images/Nps/Принцесса/Стоит.png')]
    btn3 += [pygame.image.load('images/Nps/Маг/2(Стоит).png')]
    btn_back += [pygame.image.load('images/back.png')]
    btn_rating += [pygame.image.load('images/rating.png')]
    buttons_ = [btn1, btn2, btn3, btn_back, btn_rating]     
    
    display.update()
    loop = 1
    rating_screen = 0
    st = 0
    check = 0
    while loop:
        pygame.mouse.set_visible(0)
        clock.tick(FPS)
        screen.fill((0, 0, 0))
        if st == 0:
            screen.blit(bg, (0,0))
            for btn in first_screen_btns:
                screen.blit(btn[2], btn[:2])
                
            draw.rect(screen, blue, first_screen_btns_r[first_screen_chosen_btn], 5)
            display.update()
            for i in event.get():
                if i.type == QUIT:
                    loop = 0
                elif i.type == KEYDOWN:
                    if i.key == K_SPACE:
                        if first_screen_chosen_btn == 0:
                            st = 1
                        else:
                            loop = 0
                    if i.key == K_s:
                        first_screen_chosen_btn = 1
                    if i.key == K_w:
                        first_screen_chosen_btn = 0
        elif st == 2:
            
            text_get("Last 5 player results", (255 ,255,255), 512, 100, 100)
            
            with open("history.txt", "r") as file: 
                text = list(map(str, [line[:-1] for line in file]))[-5:]
                for i in range(5):
                    text_get(text[i], (255,255,255), 512, 250 + i * 100, 79)
                for i in event.get():
                    if i.type == QUIT:
                        loop = 0
                    elif i.type == KEYDOWN:
                        if i.key == K_a:
                            check = 1
                        elif i.key == K_d:
                            check = 1
                        elif i.key == K_w:
                            check = 1
                        elif i.key == K_s:
                            check = 1
                        elif i.key == K_SPACE:
                            st = 1
                screen.blit(buttons_[3][2], buttons_[3][:2])
                draw.rect(screen, blue, buttons_r[3], 5)
                
                
                if keyPressed(pygame.K_SPACE) and check:
                    st = 1
                sleep(0.5)
                display.update()  
                    
        elif chosen_pers == None and st == 1:
            screen.blit(bg1, (0,0))
            text_get("Choose one of sprites:", (255, 255, 255), 512, 100, 50)
            for button in buttons_:
                screen.blit(button[2], button[:2])
               # draw.rect(screen, (255, 255, 255), button)
            draw.rect(screen, blue, buttons_r[chosen_btn], 5)
            display.update()
            for i in event.get():
                if i.type == QUIT:
                    loop = 0
                elif i.type == KEYDOWN:
                    if i.key == K_a:
                        chosen_btn = max(0, chosen_btn - 1)
                    elif i.key == K_d:
                        chosen_btn = min(4, chosen_btn + 1)
                    elif i.key == K_w:
                        if chosen_btn == 3 or chosen_btn == 4:
                            chosen_btn = 0
                    elif i.key == K_s:
                        chosen_btn = 3
                    elif i.key == K_SPACE:
                        if chosen_btn < 3:
                            chosen_pers = chosen_btn
                        elif chosen_btn == 4:
                            st  = 2
                        else:
                            st = 0
        
                    # sleep(0.5)            
        else:
            loop = 0
            # quit()  
            return chosen_pers
    quit()  
    time.delay(30)
      
# menu()

