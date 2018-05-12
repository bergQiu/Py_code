import pygame
from pygame.sprite import   Sprite

class bullet(Sprite):
    '''对发射的子弹进行管理'''
    def __init__(self,ai_settings,screen,ship):
        '''在飞船位置创建一个子弹对象'''
        super(bullet,self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #储存用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factory = ai_settings.bullet_speed_factor

    def update(self):
        '''向上移动子弹'''
        self.y -= self.speed_factory
        self.rect.y = self.y

    def draw_bullte(self):
        '''绘制子弹模型'''
        pygame.draw.rect(self.screen,self.color,self.rect)















