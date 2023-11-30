import pygame

class Ship():
    def __init__(self, ai_sittings, screen):
        """初始化飞船并设置初始位置"""
        self.screen = screen
        self.ai_settings = ai_sittings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕右边中央
        self.rect.centery = self.screen_rect.centery  # 飞船中心的y坐标设置为屏幕矩形的属性centery
        self.rect.right = self.screen_rect.right  # 飞船下边缘的y坐标设置为屏幕矩形的属性bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centery)

        # 移动标志
        self.moving_up = False
        self.moving_down = False
    def update_location(self):
        '''根据移动标志调整飞船位置'''
        if self.moving_up and self.rect.top > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centery = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''让飞船在屏幕上居中'''
        self.center = self.screen_rect.centerx