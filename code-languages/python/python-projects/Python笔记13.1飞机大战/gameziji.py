import time  # 控制刷新频率
import pygame
from pygame.locals import *  # 检测事件，如监控键盘按键
import sys  # 用来退出游戏
import random  # 控制子弹随机发射


# 玩家类：
# 属性：显示窗口、位置、图片、子弹列表、移动状态
# 方法：显示、移动、开火
class Player():
    def __init__(self, screen):  # 将main()中的screen传入
        self.screen = screen  # 将一个窗口对象作为了属性值，表示玩家对象显示的窗口
        # 等号左侧的screen为类的形参，右侧的为实参，右侧为main()中定义的screen
        self.x = 150  # 玩家初始位置
        self.y = 500
        self.img = pygame.image.load(r"feiji/hero1.png")  # 玩家图片
        self.bulletList = []  # 玩家子弹列表
        self.moveLeftState = 0  # 0不移动  1移动
        self.moveRightState = 0  # 0不移动  1移动

    def display(self):
        # 当前对象所在的screen属性下，调blit函数
        self.screen.blit(self.img, (self.x, self.y))  # 将玩家显示到窗口
        for b in self.bulletList:  # 创建子弹，并在子弹列表中遍历
            b.display()  # 将玩家子弹显示到窗口
            b.move()  # 将玩家子弹移动状态显示到窗口
            if b.y <= 0:
                self.bulletList.remove(b)  # 在子弹列表中移除b

    def move(self):
        if self.moveLeftState == 1 and self.x > -30:
            self.x -= 5
        if self.moveRightState == 1 and self.x < 330:
            self.x += 5

    def fire(self):
        b = PlayerBullet(self.screen, self.x, self.y)
        self.bulletList.append(b)


# 玩家子弹类：
# 属性：显示窗口、位置、图片
# 方法：显示、移动
class PlayerBullet():
    def __init__(self, screen, x, y):  # xy为玩家位置，传入给玩家子弹
        self.screen = screen
        self.x = x + 40  # 玩家子弹初始位置，需要跟随玩家飞机
        self.y = y - 20
        self.img = pygame.image.load(r"feiji/bullet.png")

    def display(self):
        self.screen.blit(self.img, (self.x, self.y))

    def move(self):
        self.y -= 20


# 敌机类
# 属性：显示窗口、位置、图片、子弹列表、移动状态
# 方法：显示、移动、开火
class Enemy():
    def __init__(self, screen):
        self.screen = screen
        self.x = 0  # 敌机初始位置
        self.y = 0
        self.img = pygame.image.load(r"feiji/enemy0.png")
        self.bulletList = []
        self.moveState = 1

    def display(self):
        # 当前对象所在的screen属性下，调blit函数
        self.screen.blit(self.img, (self.x, self.y))
        for b in self.bulletList:
            b.display()
            b.move()
            if b.y >= 600:
                self.bulletList.remove(b)

    def move(self):
        if self.moveState == 1:
            self.x += 5
        elif self.moveState == 0:
            self.x -= 5
        if self.x < -20:
            self.moveState = 1
        if self.x > 280:
            self.moveState = 0

    def fire(self):
        b = EnemyBullet(self.screen, self.x, self.y)
        self.bulletList.append(b)


# 敌机子弹类
# 属性：显示窗口、位置、图片
# 方法：显示、移动
class EnemyBullet():
    def __init__(self, screen, x, y):  # xy为敌机位置，传入给敌机子弹
        self.screen = screen
        self.x = x + 20  # 敌机子弹初始位置，需要跟随敌机飞机
        self.y = y + 30
        self.img = pygame.image.load(r"feiji/bullet2.png")

    def display(self):
        self.screen.blit(self.img, (self.x, self.y))

    def move(self):
        self.y += 20


# 捕捉用户操作
def key_control(player):  # 传入玩家对象，只控制玩家
    for event in pygame.event.get():
        if event.type == QUIT:
            print("正在退出....")
            sys.exit(0)
        elif event.type == KEYDOWN:  # 按下键盘
            if event.key == K_LEFT:
                print("玩家向左！")
                player.moveLeftState = 1
            if event.key == K_RIGHT:
                print("玩家向右！")
                player.moveRightState = 1
            if event.key == K_SPACE:
                print("玩家开火！")
                player.fire()
        elif event.type == KEYUP:  # 松开键盘
            if event.key == K_LEFT:
                player.moveLeftState = 0
            if event.key == K_RIGHT:
                player.moveRightState = 0


# main方法
class main():
    # 创建对象
    screen = pygame.display.set_mode((300, 600))  # 创建窗口
    background = pygame.image.load(r"feiji/background.png")  # 创建背景
    player = Player(screen)  # 创建玩家，并将screen属性传入玩家
    enemy = Enemy(screen)  # 创建敌军，并将screen属性传入敌军

    while 1 == 1:  # 在循环中显示所有对象并刷新，以实现对象的变化
        screen.blit(background, (0, 0))  # 将背景添加到屏幕，即显示背景
        player.display()  # 显示玩家，因为玩家还要显示其它操作。所以玩家的显示写在display中
        enemy.display()  # 显示敌机
        player.move()  # 玩家移动
        enemy.move()  # 敌机移动

        # 敌机随机开火
        r = random.randint(1, 10)
        if r == 1:
            enemy.fire()

        # 捕捉玩家操作
        key_control(player)

        pygame.display.update()  # 刷新窗口
        time.sleep(0.05)  # 休眠0.05秒，减少内存消耗


# ---------------------------
if __name__ == '__main__':
    main()
