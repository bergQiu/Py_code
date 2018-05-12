import sys,pygame
from Settings import Settings
from ship import  Ship
import game_functioin as gf
from pygame.sprite import Group
from game_stats import  GameStats
#from alien import  Alien


def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    stats =GameStats(ai_settings)
    ship =Ship(ai_settings,screen)
    bulltes = Group()
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)

    while True:

        #监视键盘和鼠标事件
        gf.check_event(ai_settings,screen,ship,bulltes)
        #ship.update()
        gf.update_buttles(ai_settings,screen,ship,bulltes,aliens)
        gf.aliens_update(ai_settings,stats,screen,ship,aliens,bulltes)
        #每次循环时都重绘屏幕
        gf.update_screen(ai_settings,stats,screen,ship,bulltes,aliens)
run_game()











