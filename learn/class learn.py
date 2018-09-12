import pygame, sys
import numpy as np


# class Screen(object):
#     size = width, height = 800, 600
#     scr = None
#
#     def __init__(self):
#         pygame.init()
#         self.scr = pygame.display.set_mode(self.size)
#         pygame.display.set_caption("雷达")
#
#     def control(self):
#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     sys.exit()


class Radar(object):
    xx=[]
    yy=[]
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        pygame.key.set_repeat(100,10)

    def draw(self, item):
        for k in np.arange(0, 360, 10):
            pos_xx = self.r * np.cos(k * np.pi / 180)
            pos_yy = self.r * np.sin(k * np.pi / 180)
            self.xx.append(pos_xx)
            self.yy.append(pos_yy)
            pos_x = pos_xx + self.x
            pos_y = pos_yy + self.y
            pygame.draw.line(item, (255, 0, 0), [self.x, self.y], [pos_x, pos_y])

    def control(self):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x -= 10
                if event.key == pygame.K_RIGHT:
                    self.x += 10
                if event.key == pygame.K_UP:
                    self.y -= 10
                if event.key == pygame.K_DOWN:
                    self.y += 10
            # elif event.type in (pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN):
            #     self.x = self.x
            #     self.y = self.y

    def calculate(self):
        print(self.xx)

# class Ball(object):
#     def __init__(self, width, heigth, x, y, r):
#         self.x = np.arange(0, width)
#         self.y = np.arange(0, heigth)
#
#
# class Red_Ball(Ball):
#     pass
#
# class Green_Ball(Ball):
#     pass


# screen = Screen()
# screen.size = width, heigth = 800, 600
# screen.control()
# radar = Radar(200, 200, 200)
# radar.draw(Screen.scr)
# pygame.display.update()
# pygame.init()
# ball = Ball()

pygame.init()
size = width, heigth = 800, 600
screen = pygame.display.set_mode(size)
radar = Radar(200, 200, 200)
while True:
    pygame.init()
    radar.draw(screen)
    radar.control()
    radar.calculate()
    pygame.display.update()