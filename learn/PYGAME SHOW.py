import pygame, sys
import numpy as np

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("雷达")

x0 = 400
y0 = 300
r0 = 50

x = 200
y = 200
r = 200

speed = [1, 1]

# pos_xy = []
# pos_xy1 = []
L = np.sqrt((x0 - x) ** 2 + (y0 - y) ** 2)

# for k in np.arange(0, 360, 10):
#     pos_x = r * np.cos(k * np.pi / 180)
#     pos_y = r * np.sin(k * np.pi / 180)
#     # print(pos_x)
#     pos_xy1.append((pos_x + x, pos_y + y))
#     pos_xy.append((pos_x, pos_y))
# for i in range(0, 72):
#     if i % 2 == 1:
#         pos_xy1.insert(i, (x, y))
# line = pygame.draw.lines(screen, (255, 0, 0), False, pos_xy1)
# circle = pygame.draw.circle(screen, (0, 255, 0), (x0, y0), r0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x = x + 100
            elif event.key == pygame.K_LEFT:
                x = x - 100
            elif event.key == pygame.K_UP:
                y = y - 100
            elif event.key == pygame.K_DOWN:
                y = y + 100
            pos_xy = []
            pos_xy1 = []
            L_pp = np.sqrt((x0 - x) ** 2 + (y0 - y) ** 2)
            theta0 = np.arctan(y0 - y / x0 - x)
            for k in np.arange(0, 360, 10):
                theta = k * np.pi / 180
                pos_x = r * np.cos(theta)
                pos_y = r * np.sin(theta)
                # print(pos_x)
                pos_xy1.append((pos_x + x, pos_y + y))
                pos_xy.append((pos_x, pos_y))
            # print(len(pos_xy))
            for i in range(0, 72):
                if i % 2 == 1:
                    pos_xy1.insert(i, (x, y))
            # print(len(pos_xy1))
            for q in range(0, 36):
                theta1 = pos_xy[q][1] / pos_xy[q][0]
                # print(theta1)
                L_pl = np.abs((x0 - x) * theta1 - (y0 - y)) / np.sqrt(theta1 ** 2 + 1)
                # print(L_pl)
                if L_pp <= r0 + r and L_pl <= r0:
                    x_x = (2 * (x0 - x) + 2 * (y0 - y) * theta1 - np.sqrt(
                        (-2 * (x0 - x) - 2 * (y0 - y) * theta1) ** 2 - 4 * (
                                    -r0 ** 2 + (x0 - x) ** 2 + (y0 - y) ** 2) * (
                                1 + theta1 ** 2))) / (2 * (1 + theta1 ** 2))
                    y_y = theta1 * x_x
                    print("x_x:", x_x, "y_y:", y_y)

            line = pygame.draw.lines(screen, (255, 0, 0), False, pos_xy1)
            circle = pygame.draw.circle(screen, (0, 255, 0), (x0, y0), r0)

    pygame.display.update()
