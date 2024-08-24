import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外形人的类"""

    def __init__(self,ai_game):
        """初始化外星人的类"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 加载外星人图像并设置器rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人都在最初的左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精准水平位置
        self.x = float(self.rect.x)

    def check_edges(self):
        """如果外外星人位于屏幕的边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """向右移动外星人"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x