import pygame

class Ship():
    def __init__(self, screen):
        """初始化飞船并设置初始位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕右边中央
        self.rect.centery = self.screen_rect.centery  # 飞船中心的y坐标设置为屏幕矩形的属性centery
        self.rect.right = self.screen_rect.right  # 飞船下边缘的y坐标设置为屏幕矩形的属性bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
