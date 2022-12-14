#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)


# =======================================================================================
# Класс для работы с векторами
# =======================================================================================
class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, obj):
        """возвращает сумму двух векторов"""
        return self.x + obj.x, self.y + obj.y

    def __sub__(self, obj):
        """"возвращает разность двух векторов"""
        return self.x - obj.x, self.y - obj.y

    def __mul__(self, k):
        """возвращает произведение вектора на число"""
        return self.x * k, self.y * k

    @staticmethod
    def len(obj):
        """возвращает длину вектора"""
        return math.sqrt(obj.x * obj.x + obj.y * obj.y)

    def int_pair(self):
        """вовращает кортеж из двух целых чисел(текущие координаты)"""
        return self.x, self.y


class Polyline:
    def __init__(self):
        pass

    def add_point(self, point, speed):
        """добавление в ломаную точки (Vec2d) c её скоростью"""
        pass

    def set_points(self):
        """пересчёт координат точек"""
        pass

    def draw_points(self):
        """отрисовка ломаной"""
        pass


class Knot(Polyline):
    def add_point(self):
        """добавление в ломаную точки (Vec2d) c её скоростью"""
        pass

    def set_points(self):
        """пересчёт координат точек"""
        pass

    def get_knot(self):
        """для расчёта точек кривой по добавляемым «опорным» точкам"""
        pass

# def vec(x, y):
#     """возвращает пару координат, определяющих вектор (координаты точки конца вектора),
#     координаты начальной точки вектора совпадают с началом системы координат (0, 0)"""
#     return sub(y, x)


# =======================================================================================
# Функции отрисовки
# =======================================================================================
def draw_points(points, style="points", width=3, color=(255, 255, 255)):
    """функция отрисовки точек на экране"""
    if style == "line":
        for p_n in range(-1, len(points) - 1):
            pygame.draw.line(gameDisplay, color,
                             (int(points[p_n].x), int(points[p_n].y)),
                             (int(points[p_n + 1].x), int(points[p_n + 1].y)), width)

    elif style == "points":
        for p in points:
            pygame.draw.circle(gameDisplay, color,
                               (int(p.x), int(p.y)), width)


def draw_help():
    """функция отрисовки экрана справки программы"""
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# # =======================================================================================
# # Функции, отвечающие за расчет сглаживания ломаной
# # =======================================================================================
# def get_point(points, alpha, deg=None):
#     if deg is None:
#         deg = len(points) - 1
#     if deg == 0:
#         return points[0]
#     return add(mul(points[deg], alpha), mul(get_point(points, alpha, deg - 1), 1 - alpha))
#
#
# def get_points(base_points, count):
#     alpha = 1 / count
#     res = []
#     for i in range(count):
#         res.append(get_point(base_points, i * alpha))
#     return res
#
#
# def get_knot(points, count):
#     if len(points) < 3:
#         return []
#     res = []
#     for i in range(-2, len(points) - 2):
#         ptn = []
#         ptn.append(mul(add(points[i], points[i + 1]), 0.5))
#         ptn.append(points[i + 1])
#         ptn.append(mul(add(points[i + 1], points[i + 2]), 0.5))
#
#         res.extend(get_points(ptn, count))
#     return res
#
#
# def set_points(points, speeds):
#     """функция перерасчета координат опорных точек"""
#     for p in range(len(points)):
#         points[p] = add(points[p], speeds[p])
#         if points[p][0] > SCREEN_DIM[0] or points[p][0] < 0:
#             speeds[p] = (- speeds[p][0], speeds[p][1])
#         if points[p][1] > SCREEN_DIM[1] or points[p][1] < 0:
#             speeds[p] = (speeds[p][0], -speeds[p][1])
#

# =======================================================================================
# Основная программа
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    points = []
    speeds = []
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    points = []
                    speeds = []
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                points.append(Vec2d(*event.pos))
                speeds.append((random.random() * 2, random.random() * 2))
                print(speeds)

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        draw_points(points)
        # draw_points(get_knot(points, steps), "line", 3, color)
        # if not pause:
        #     set_points(points, speeds)
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)

# a = Vec2d(3, 4)
# b = Vec2d(2, 5)
# print(Vec2d.len(a))
# print(a.__mul__(2))

