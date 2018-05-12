class Settings():
    '''储存游戏的所有设置'''
    def __init__(self):
        '''初始化游戏设置'''
        # 屏幕设置
        self.screen_width = 500
        self.screen_height = 600
        self.bg_color = (230,230,230) # 背景颜色
        self.ship_speed_factor = 1 #飞船速度控制
        self.ships_limit = 3
        self.bullet_speed_factor = 2 # 子弹速度
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bulltes_allowed = 5
        self.alien_speed_factor = 0.3 # 外星人速度
        self.alien_drop_factory = 50
        self.fleet_direction = 1