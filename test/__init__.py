import pygame                # importujemy biblioteki pygame
from pygame.locals import *  # importujemy nazwy [QUIT, KEYDOWN,K_ESCAPE] itp.
from sys import exit         # importujemy funkcje systemowa exit
 
screen_size = (800,600)      # ustalamy rozmiar ekranu
 
class IsoGame(object):
    def __init__(self):
        pygame.init()       # incjalizujemy biblioteke pygame
        flag = DOUBLEBUF    # wlaczamy tryb podwojnego buforowania
 
        # tworzymy bufor na  grafike
        self.surface = pygame.display.set_mode(screen_size,flag)
 
        # zmienna stanu gry
        self.gamestate = 1  # 1 - run, 0 - exit
 
#        self.player_image = pygame.image.load('spaceship.png')
        self.player_image = pygame.image.load('sammy.png')
        self.police_image = pygame.image.load('policja.png')
        self.fire_image = pygame.image.load('straz.png')
        self.bus_image = pygame.image.load('autobus.png')
        self.speed = 1.2     # szybkosc poruszania duszka
        self.player_x = 50   # pozycja x duszka na ekranise
        self.player_y = 30   # pozycja y duszka na ekranie
        self.radius_player = self.player_image.get_width()/2
        self.radius_police = self.police_image.get_width()/2
        self.opponets_x = 1  # pozycja x duszka
        self.police_x = 400
        self.fire_x = 500
        self.bus_x = 300
        self.police_y = 200
        self.fire_y = 100
        self.bus_y = 300
 
        self.tree_image = pygame.image.load('tree.png') # ladujemy obrazek do pamieci
        self.loop() 
        
    def collision(self,x1,y1,w1,h1,x2,y2,w2,h2):
        if x1 >= x2+w2:
            return True
        if x1+w1 <= x2:
            return True
        if y1 >= y2+h2:
            return True
        if y1+h1 <= y2:
            return True
 
        return False
     
#    def collision(self):
#        return pygame.sprite.collide_rect(pygame.Rect(self.player_image), pygame.Rect(self.police_image))

    def move(self,dirx,diry):
       """ poruszanie duszkiem """
       dx = self.player_x + (dirx * self.speed)
       dy = self.player_y + (diry * self.speed)
#       if self.collision():
#           return
       if not self.collision(dx,dy,self.player_image.get_width(),self.player_image.get_height(),self.police_x% 800,self.police_y % 800,self.police_image.get_width(),self.police_image.get_height()):
           return
       if not self.collision(dx,dy,self.player_image.get_width(),self.player_image.get_height(),self.fire_x% 800,self.fire_y % 800,self.fire_image.get_width(),self.fire_image.get_height()):
           return
       if not self.collision(dx,dy,self.player_image.get_width(),self.player_image.get_height(),self.bus_x% 800,self.bus_y % 800,self.bus_image.get_width(),self.bus_image.get_height()):
           return
       self.player_x = dx
       self.player_y = dy
      
    def game_exit(self):
        """ funkcja przerywa dzialanie gry i wychodzi do systemu"""
        exit()
        
    def loop(self):
        """ glowna petla gry """
        while self.gamestate==1:
           for event in pygame.event.get():
               if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                   self.gamestate=0
 
           keys = pygame.key.get_pressed() # odczytujemy stan klawiszy
 
           if keys[K_s]:
              self.move(0,1)  # ruch w dol
              if self.player_y > 600: #+ self.player_image.get_height() > 600:
                self.player_y = 0;
 
           if keys[K_w]:
              self.move(0,-1)   # ruch w gore
              if self.player_y < 0:
                self.player_y = 600;
 
           if keys[K_d]:
              self.move(1,0)  # ruch w prawo
              if self.player_x >800: # + self.player_image.get_width() > 800:
                self.player_x =0 ;
 
           if keys[K_a]:
              self.move(-1,0)   # ruch w lewo
              if self.player_x < 0: #     - self.player_image.get_width() < 0:    
                 self.player_x = 800;
 
           self.surface.fill((0,0,0))  # czyscimy ekran, malo wydajne ale wystarczy
           self.surface.blit(self.tree_image, (10,20))  # gracz zaslania obrazek
 
           # umieszczamy gracza
           self.surface.blit(self.player_image,(self.player_x,self.player_y))
           if  self.collision(self.police_x% 800,self.police_y % 800,self.police_image.get_width(),self.police_image.get_height(),self.player_x,self.player_y,self.player_image.get_width(),self.player_image.get_height()):
               self.police_x += self.opponets_x;
           else:
            self.police_x -= self.opponets_x;
            
           if  self.collision(self.fire_x % 800,self.fire_y % 800,self.fire_image.get_width(),self.fire_image.get_height(),self.player_x,self.player_y,self.player_image.get_width(),self.player_image.get_height()):
               self.fire_x -= self.opponets_x;
           else:
               self.fire_x += self.opponets_x;
           if  self.collision(self.bus_x% 800,self.bus_y % 800,self.bus_image.get_width(),self.bus_image.get_height(),self.player_x,self.player_y,self.player_image.get_width(),self.player_image.get_height()):
               self.bus_x += self.opponets_x
           else:
                self.bus_x -= self.opponets_x
           
           self.surface.blit(self.police_image, (self.police_x % 800,self.police_y ))
           self.surface.blit(self.fire_image, (self.fire_x % 800,self.fire_y ))
           self.surface.blit(self.bus_image, (self.bus_x % 800,self.bus_y ))
           
#            self.surface.blit(self.police_image, (self.police_x-self.opponets_x,200))
           self.surface.blit(self.tree_image, (220 ,20))  # obrazek zaslania gracza
           
           
           pygame.display.flip()   # przenosimy bufor na ekran
 
        self.game_exit()
 
if __name__ == '__main__':
   IsoGame()