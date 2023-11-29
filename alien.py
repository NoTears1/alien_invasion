from typing import Any
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''单个外星人的类'''

    def __init__(self, ai_settings, screen):
        '''初始化外星人并设置起始位置'''
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像，并设置rect属性
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        '''在指定位置绘制外星人'''
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        '''如果外星人位于屏幕边缘，就返回True'''   
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >=  screen_rect.bottom:
            return True
        elif self.rect.top <= 0:
            return True

    def update(self):
        '''向上或向下移动外星人'''
        self.y += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.y = self.y


