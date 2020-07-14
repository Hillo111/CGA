import numpy as np
import pygame as pg


def average_colours(colour_grid, directions, steps):
    for i in range(steps):
        new_colour_grid = colour_grid.copy()

        for y in range(len(colour_grid)):
            for x in range(len(colour_grid[y])):
                valid_dirs = 0
                avg = np.array([.0, .0, .0])
                for d in directions:
                    x1, y1 = x + d[0], y + d[1]
 
                    if 0 <= x1 < len(colour_grid[y]) and 0 <= y1 < len(colour_grid):
                        avg += colour_grid[y1][x1]
                        valid_dirs += 1

                if valid_dirs > 0:
                    new_colour_grid[y][x] = avg / valid_dirs

        colour_grid = new_colour_grid

    return colour_grid


xCount = 50
yCount = 40

cellSize = 10
screen = pg.display.set_mode((xCount * cellSize, yCount * cellSize))

brush = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
]

brushCenter = np.floor(len(brush) / 2)

pixelGrid = []
for i in range(yCount):
    pixelGrid.append([])
    for j in range(xCount):
        pixelGrid[i].append(np.array([255, 255, 255]))

run = True
clock = pg.time.Clock()

drawing = False
while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
        if e.type == pg.MOUSEBUTTONDOWN:
            drawing = True
        if e.type == pg.MOUSEBUTTONUP:
            drawing = False
        if e.type == pg.KEYDOWN:
            pixelGrid = average_colours(pixelGrid, [[1, 0], [0, 1], [-1, 0], [0, -1]], 1)

    if drawing:
        xm, ym = map(int, pg.mouse.get_pos())
        x_center, y_center = xm // cellSize, ym // cellSize
        x_add, y_add = x_center - len(brush[0]) // 2, y_center - len(brush) // 2
        for y in range(len(brush)):
            for x in range(len(brush[y])):
                nx, ny = x + x_add, y + y_add
                if 0 <= nx < len(pixelGrid[0]) and 0 <= ny < len(pixelGrid):
                    if brush[y][x]:
                        col = (0, 0, 0)
                        p = pg.mouse.get_pressed()
                        if p[0]:
                            col = (255, 0, 0)
                        if p[1]:
                            col = (0, 255, 0)
                        if p[2]:
                            col = (0, 0, 255)
                        pixelGrid[ny][nx] = col

    screen.fill((255, 255, 255))
    for y in range(yCount):
        for x in range(xCount):
            pg.draw.rect(screen, pixelGrid[y][x], [x * cellSize, y * cellSize, cellSize, cellSize])

    pg.display.flip()
    clock.tick(60)

pg.quit()