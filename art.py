import pygame as pg
import random
import numpy as np


def generate_colours(base_colours, offsets, amounts):
    colours = []
    for i in range(len(base_colours)):
        min_colour = base_colours[i] - offsets[i]
        max_colour = base_colours[i] + offsets[i]

        if sum(max_colour) <= sum(min_colour):
            raise ValueError('Colour offset must be positive')

        for k in range(3):
            if min_colour[k] < 0:
                min_colour[k] = 0

            if max_colour[k] > 255:
                max_colour[k] = 255

        for k in range(amounts[i]):
            colour = np.array([0, 0, 0])
            for j in range(3):
                colour[j] = random.randint(min_colour[j], max_colour[j])

            colours.append(colour)

    return colours


base_colours = (
    np.array([235, 0, 0]),
    np.array([241, 245, 17]),
    np.array([10, 10, 10])
)

offsets = (
    np.array([20] * 3),
    np.array([10] * 3),
    np.array([10] * 3)
)

amounts = (
    10,
    10,
    1
)

colours = generate_colours(base_colours, offsets, amounts)
print(colours)

cell_x_count = 50
cell_y_count = 40

cellSize = 10

colour_grid = []
for i in range(cell_y_count):
    colour_grid.append([])
    for j in range(cell_x_count):
        colour_grid[i].append(None)

window = pg.display.set_mode((cell_x_count * cellSize, cell_y_count * cellSize))

for y in range(cell_y_count):
    for x in range(cell_x_count):
        colour_grid[y][x] = random.choice(colours)

print(colour_grid)


def average_colours(colour_grid, directions, steps):
    for i in range(steps):
        new_colour_grid = colour_grid.copy()

        for y in range(len(colour_grid)):
            for x in range(len(colour_grid[y])):
                for d in directions:
                    x1, y1 = x + d[0], y + d[1]

                    avg = np.array([0, 0, 0])
                    valid_dirs = 0
                    if 0 <= x1 < len(colour_grid[y]) and 0 <= y1 < len(colour_grid):
                        avg += colour_grid[y1][x1]
                        valid_dirs += 1

                    print(x, y)

                    new_colour_grid[y][x] = avg // valid_dirs

        colour_grid = new_colour_grid

    return colour_grid


colour_grid = average_colours(colour_grid, [[-1, 0], [0, -1], [0, 1], [1, 0], [0, 0]], 5)

for y in range(cell_y_count):
    for x in range(cell_x_count):
        pg.draw.rect(window, colour_grid[y][x], [x * cellSize, y * cellSize, cellSize, cellSize])


pg.image.save(window, "art.png")

