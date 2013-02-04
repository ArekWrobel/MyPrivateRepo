import pygame

class Sprite:
    x = 0
    y = 0
    speed = 1.2
    anim = 0
    frames = 0

    def __init__(self,image,width=0,height=0):

        image_object = pygame.image.load(image)
        
        if width==0:
                 width=image_object.get_width()-1
        if height==0:
                 height=image_object.get_height()-1
        self.width = width
        self.height = height
        #self.rect(0,0,width,height)
        frames_x = int(image_object.get_width()/width)
        frames_y = int(image_object.get_height()/height)
        #self.frames= frames_x + frames_y-1
        self.frames= 1

        self.surface = pygame.display.get_surface()
        frame_rect = pygame.Rect(1,0,width,height)
        #if speed > -1: self.speed = speed
        self.curframe = 0
        self.images = []
        self.images.append(image_object)
        for imx in range(0,frames_x):
            for imy in range(0,frames_y):
                frame_rect.top = imy* (height+1)
                frame_rect.left = imx* (width)+1
                self.images.append(image_object.subsurface(frame_rect))

    def setSpeed(self,speed):
        self.speed = speed

    def move(self,dx,dy):
        self.x+=dx*self.speed
        self.y+=dy*self.speed
        #self.rect.left = self.x
        #self.rect.top = self.y
        #if self.frames > 1:
        self.anim = 1


    def draw(self):
        if self.curframe <> 3:
           if self.anim == 1:
               self.curframe += 0.5
               if self.curframe > 2:
                  self.curframe = 1
           else:
                self.curframe = 0
#        self.surface.blit(self.images[int(self.curframe)],(self.x,self.y))
        self.surface.blit(self.images[0],(self.x,self.y))
        

