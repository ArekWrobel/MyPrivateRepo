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
        self.player = Sprite('spaceship.png',125,47)
        self.player.x = 50
        self.player.y = 30
        self.asteroids = []
        self.loop()                             # glowna petla gry

    def game_exit(self):
        """ funkcja przerywa dzialanie gry i wychodzi do systemu"""
        exit()

    def collision(self,x,y,w,h,cx,cy,r):
        tx = cx
        ty = cy
        if cx < x: tx = x
        if cx >(x+w): tx = (x+w)
        if cy < y: ty = y
        if cy >(y+h): ty = (y+h)
        if (cx-tx)**2+(cy-ty)**2<r**2:
            return True
        return False

    def loop(self):
        time2 = 0
        timeasteroid = 0
        """ glowna petla gry """
        while self.gamestate==1:
           time = pygame.time.get_ticks()/1000

           self.player.anim = 0

           if len(self.asteroids)<10 and timeasteroid<time-0.01:
              h = random.randrange(50,550)
              self.asteroids.append(Sprite('straz.png'))
              self.asteroids[-1].x = 850
              self.asteroids[-1].y = h
              speed = random.uniform(0.4,3.0)
              self.asteroids[-1].speed = speed
              timeasteroid = pygame.time.get_ticks()/1000
       
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
	   
           if self.player.x<10: self.player.x = 10
           if self.player.x>600: self.player.x=600
           if self.player.y<10: self.player.y = 10
           if self.player.y>540: self.player.y = 540
           self.surface.fill((0,0,0))  # czyscimy ekran, malo wydajne ale wystarczy
           #self.surface.blit(self.tree_image, (10,20))     # umieszczamy obrazek a graczem


           for n in range(len(self.asteroids)-1):
                self.asteroids[n].move(-1,0)
                if self.collision(self.player.x+40,self.player.y,self.player.width-40,self.player.height,self.asteroids[n].x+32,self.asteroids[n].y+32,32):
                     self.player.curframe = 3
                self.asteroids[n].draw()
                if self.asteroids[n].x < -50:
                     del self.asteroids[n]

           # umieszczamy gracza
           #self.surface.blit(self.player_image[int(self.player_frame)],(self.player_x,self.player_y))
#           if self.player.curframe==3:
#                if not time2: time2 = pygame.time.get_ticks()/1000
#                if time2<time-2:
#                    self.gamestate=0
               
           self.player.draw()
           #self.surface.blit(self.tree_image, (220,20))     # umieszczamy obrazek przed graczem
           pygame.display.flip()   # przenosimy bufor na ekran

        self.game_exit()

if __name__ == '__main__':
   IsoGame()
