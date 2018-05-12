import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        '''初始化飞船并设置位置'''
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('image/ship.png')
        self.rect =self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx =self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_rigth = False
        self.moving_left = False

    def blitme(self):
        '''绘制飞船'''
        self.screen.blit(self.image,self.rect)

    def update(self):
        '''更新飞船的位置'''
        if self.moving_rigth:
            self.center += self.ai_settings.ship_speed_factor
            #self.rect.centerx += 1
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
            #self.rect.centerx -= 1
        if (self.screen_rect.left < self.center < self.screen_rect.right):
            self.rect.centerx = self.center