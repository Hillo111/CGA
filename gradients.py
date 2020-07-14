import pygame as pg
import numpy as np


width, height = 500, 300
colours = [[255, 175, 189],
           [255, 195, 160]]
gradient_type = 'DIAGONAL'

gradient_type = gradient_type.upper()

if gradient_type not in ('VERTICAL', 'HORIZONTAL'):
    raise TypeError('Non existent gradient type')

if len(colours) < 2:
    raise EOFError('Not enough colours')

for i in range(len(colours)):
    for b in range(len(colours[i])):
        colours[i][b] = float(colours[i][b])
    colours[i] = np.array(colours[i])

locations = [1]
comparison = width if gradient_type == 'HORIZONTAL' else height
spread = comparison // (len(colours) - 1)

for i in range(len(colours) - 2):
    locations.append(locations[-1] + spread)

locations.append(comparison)
print(locations)
print(colours)

image = pg.Surface((width, height))

for i in range(len(colours) - 1):
    colour, next_colour = colours[i], colours[i + 1]
    loc, next_loc = locations[i], locations[i + 1]

    spread = (next_colour - colour) / (next_loc - loc)
    if gradient_type == 'DIAGONAL':
        pass
    else:
        for j in range(loc, next_loc):
            if gradient_type == 'HORIZONTAL':
                pg.draw.line(image, colour, [j, 0], [j, height])
            if gradient_type == 'VERTICAL':
                pg.draw.line(image, colour, [0, j], [width, j])

            colour += spread

pg.image.save(image, 'gradient.png')