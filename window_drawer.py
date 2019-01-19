


# -*- coding: utf-8 -*-

import pygame
import datetime
import speech_engine
#%% иницилизация

text = [""]
a = 0
window = pygame.display.set_mode((610,1080),0,0)
#window = pygame.display.set_mode((900,1600),pygame.FULLSCREEN ,0)
pygame.display.set_caption("mirror v1")
screen = pygame.Surface((610,1080))

#%%
def unit():
     pygame.init() 
#%%
def main_loop(mainScreen):
    if mainScreen: 
        
        bgColor = (0,0,0) 
        screen.fill(bgColor) 
        screen.blit( pygame.image.load('image/weather.png'),(0,950))
        
        
        time_H = datetime.datetime.today().strftime("%H:%M") 
        #datetime.datetime.now().time()
        (x,y,fontSize) = (450,1000,200)
        myFont = pygame.font.SysFont("none", fontSize)
        fontColor = (255,255,255)
        
        fontImage = myFont.render(time_H, 0, (fontColor))     
        screen.blit(fontImage,(x,y)) 
        
        time_s = datetime.datetime.today().strftime("%S") 
    
        (x,y,fontSize) = (810,1010,100)
        myFont = pygame.font.SysFont("none", fontSize)
        
        fontImage = myFont.render(time_s, 0, (fontColor))     
        
        screen.blit(fontImage,(x,y)) 
        
        
        
    
        window.blit(screen,(0,0))
        pygame.display.update() 
        return 1
#        pygame.mouse.set_visible(0)
    else:
        bgColor = (0,0,0) 
        screen.fill(bgColor) 
        
        t = speech_engine.listen()
#        if (t.lower().find('//////') != -1 ):
#            a+=1
#            if a>3:
#                mainScreen = True
#        else:
#            a= 0
           
        
        
        say = speech_engine.main(t)
#        if (say.lower().find("Вот прогноз на сегодня") != -1 ):
#            text = [""]
#            screen.blit( pygame.image.load('image/forecast_plot.png'),(0,170))
            
        text.insert(0,"__________________________________________")        
        
        text.insert(0,say)
        text.insert(0,t)    
        i = 20
        
        
        for z in text[:3]:
            
                (x,y,fontSize) = (50,i,50)
                myFont = pygame.font.SysFont("none", fontSize)
                fontColor = (255,255,255)
            
                fontImage = myFont.render(str(z), 0, (fontColor))     
                screen.blit(fontImage,(x,y)) 
                i+=50
        
        if len(text)>3:
            for z in text [3:18]:
                (x,y,fontSize) = (50,i,50)
                myFont = pygame.font.SysFont("none", fontSize)
                fontColor = (150,150,150)
            
                fontImage = myFont.render(str(z), 0, (fontColor))     
                screen.blit(fontImage,(x,y)) 
                i+=50
        window.blit(screen,(0,0))
        pygame.display.update()

        
         
        speech_engine.Say (say)
        if (say.lower().find("......") != -1 ):
            return 1
        
        else:
            return 0
     
#        pygame.mouse.set_visible(0)
        
        





    
     














