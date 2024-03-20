#1.引入模块
import time #控制刷新频率
import pygame
from pygame.locals import *   #检测事件，如监控键盘按键
import sys #用来退出游戏
import random #控制子弹随机发射

#2.创建分类
#2.1玩家类
class Player():
    def __init__(self,screen):
        self.screen = screen
        self.x = 150
        self.y = 500
        self.img = pygame.image.load(r"feiji/hero1.png") #玩家图片
        self.bulletList = []
        self.moveLeftstate = 0
        self.moveRightstate = 0
    def display(self):
        pass
    def move(self):
        pass
    def fire(self):
        pass

#2.2玩家子弹类
class PlayerBullet():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x + 40
        self.y = y - 20
        self.img = pygame.image.load(r"feiji/bullet.png")

    def display(self):
        pass

    def move(self):
        pass

#2.3敌机类
class Enemy():
    def __init__(self, screen):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.img = pygame.image.load(r"feiji/enemy0.png")
        self.bulletList = []
        self.movestate = 1

    def display(self):
        pass

    def move(self):
        pass

    def fire(self):
        pass

#2.4敌机子弹类
class EnemyBullet():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x + 20
        self.y = y + 30
        self.img = pygame.image.load(r"feiji/bullet2.png")

#2.5控制方法
def Key_control(player):
    for event in pygame.event.get():
        if event.type == QUIT:
            print("正在退出....")
            sys.exit(0)

#3.main()方法
class main():
    screen = pygame.display.set_mode((300, 600))  # 创建窗口
    background = pygame.image.load(r"feiji/background.png")  # 创建背景
    player = Player(screen)  # 创建玩家，并将screen属性传入玩家
    enemy = Enemy(screen)  # 创建敌军，并将screen属性传入敌军

    while 1 == 1:
        screen.blit(background, (0, 0))
        player.display()
        enemy.display()
        player.move()
        enemy.move()

        r = random.randint(1,10)
        if r == 1:
            enemy.fire()

        Key_control(player)

        pygame.display.update()
        time.sleep(0.05)

#4.运行
if __name__ == '__main__':
    pass

