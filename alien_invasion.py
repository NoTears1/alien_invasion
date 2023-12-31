import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from alien import Alien
from button import Button
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个用于存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人编组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 开始游戏循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:# 初始状态为False，不会绘制屏幕，但是仍然可以监测到鼠标事件（图像与动作分离）
            # 更新飞船位置
            ship.update_location()
            # 更新子弹
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # 更新外星人
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # 更新屏幕图像
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button) 

run_game()