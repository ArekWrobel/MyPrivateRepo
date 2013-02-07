'''
Created on 04-02-2013

@author: Arek
'''
import random
import pygame                # importujemy biblioteki pygame
from pygame.locals import *  # importujemy nazwy [QUIT, KEYDOWN,K_ESCAPE] itp.
from sys import exit         # importujemy funkcje systemowa exit
from sprite import *
 
screen_size = (800,600)      # ustalamy rozmiar ekranu
 
class IsoGame(object):
    def __init__(self):
        pygame.init()       # incjalizujemy biblioteke pygame
        flag = DOUBLEBUF    # wlaczamy tryb podwojnego buforowania
 
        # tworzymy bufor na  grafike
        self.surface = pygame.display.set_mode(screen_size,flag)
 
        # zmienna stanu gry
        self.gamestate = 1  # 1 - run, 0 - exit
        self.player = Sprite('policja.png',125,47)
        self.player.x = 50
        self.player.y = 30
        self.cars = []
        self.loop()      
 
        
    def collision(self,x1,y1,w1,h1,x2,y2,w2,h2):
        if x1 >= x2+w2:
            return False
        if x1+w1 <= x2:
            return False
        if y1 >= y2+h2:
            return False
        if y1+h1 <= y2:
            return False
 
        return True
      
    def game_exit(self):
        """ funkcja przerywa dzialanie gry i wychodzi do systemu"""
        exit()
        
    def loop(self):
        time2 = 0
        timecars = 0
        """ glowna petla gry """
        while self.gamestate==1:
           time = pygame.time.get_ticks()/1000

           self.player.anim = 0

           if len(self.cars)<10 and timecars<time-0.01:
              h = random.randrange(50,550)
              image_cars = ['straz.png','autobus.png','sammy.png']
              self.cars.append(Sprite(image_cars[random.randint(0, 2)]))
              self.cars[-1].x = 850
              self.cars[-1].y = h
              speed = random.uniform(0.4,3.0)
              self.cars[-1].speed = speed
              timecars = pygame.time.get_ticks()/1000
       
           for event in pygame.event.get():
               if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                   self.gamestate=0


           if self.player.curframe<3:
                keys = pygame.key.get_pressed() # odczytujemy stan klawiszy

           if keys[K_s]:
              self.player.move(0,1)  # ruch w dol
     
           if keys[K_w]:
              self.player.move(0,-1)   # ruch w gore
                 
           if keys[K_d]:
              self.player.move(1,0)  # ruch w prawo
       
           if keys[K_a]:
              self.player.move(-1,0)   # ruch w lewo
       
           if self.player.x<0: self.player.x = 800
           if self.player.x>800: self.player.x=0
           if self.player.y<0: self.player.y = 600
           if self.player.y>600: self.player.y = 0
           self.surface.fill((0,0,0))  # czyscimy ekran, malo wydajne ale wystarczy
           #self.surface.blit(self.tree_image, (10,20))     # umieszczamy obrazek a graczem


           for n in range(len(self.cars)-1):
                self.cars[n].move(-1,0)
                if self.collision(self.player.x,self.player.y,self.player.width,self.player.height,self.cars[n].x,self.cars[n].y,self.cars[n].width,self.cars[n].height):
                     self.player.curframe = 3
                self.cars[n].draw()
                if self.cars[n].x < -50:
                     del self.cars[n]

           # umieszczamy gracza
           #self.surface.blit(self.player_image[int(self.player_frame)],(self.player_x,self.player_y))
           if self.player.curframe==3:
                if not time2: time2 = pygame.time.get_ticks()/1000
                if time2<time-2:
                    self.gamestate=0
            
           self.player.draw()
           #self.surface.blit(self.tree_image, (220,20))     # umieszczamy obrazek przed graczem
           pygame.display.flip()   # przenosimy bufor na ekran

        self.game_exit()


if __name__ == '__main__':
   IsoGame()

