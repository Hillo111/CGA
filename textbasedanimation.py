from PIL import Image
from time import sleep
from os import system, name


def getFrames(gifloc):
    frames = []
    frame = Image.open(gifloc)
    i = 0
    while True:
        frames.append(frame.copy())
        i += 1
        try:
            frame.seek(i)
        except EOFError:
            return frames


print("Welcome to the animation-to-text tool!")

loc = input("Enter file location: ")

img = Image.open(loc)
# frames = getFrames(loc)

scale = int(input("Enter how scaled down you want it to be (I suggest 4 for a 400 x 400px image): "))

frameRate = int(input("Frame rate (fps): "))

loopcount = int(input("How many times do you want to loop the animation? "))


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def surfaceToText(surf, squish):

    width, height = surf.size
    # create empty grid
    grid = []
    for y in range(0, height, squish):
        grid.append([])
        for x in range(0, width, squish):
            grid[y // squish].append(' ')

    # do conversion
    rgb_surf = surf.convert("RGB")

    colortable = [  # x=r y=g z=b coordinates represented by where the color values are in the range;
        # 0-85: 0, 86-170: 1, 171-255: 2
        [
            ['&', '>', '+'],
            ['T', ';', 'O'],
            ['/', '?', 'o'],
        ],
        [
            ['#', 'a', 'n'],
            ['`', '|', '*'],
            ['^', '\'', '-'],
        ],
        [
            ['@', '=', 'e'],
            ['(', ')', '}'],
            ['"', '`', ' '],
        ],
    ]

    for y in range(0, height, squish):
        for x in range(0, width, squish):

            # get color value
            # col = surf.get_at((x, y))
            col = rgb_surf.getpixel((x, y))
            # col_val = col[0] + col[1] + col[2]

            # assign char based on vale (might want to tinker around with this later)

            char = colortable[col[2] // 85 - (1 if col[2] == 255 else 0)][col[1] // 85 - (1 if col[1] == 255 else 0)][col[0] // 85 - (1 if col[0] == 255 else 0)]

            '''
            if col_val <= 100:
                char = "&"
            elif 100 <= col_val <= 600:
                char = '*'
            else:
                char = ' '
            '''

            grid[y // squish][x // squish] = char

    return grid


def getTextedFrame(g):
    s = ''
    for row in g:
        for c in row:
            s += c * 2
        s += '\n'
    return s


print("Getting frames...")
frames = getFrames(loc)

print("Converting frames to text...")

textedFrames = []
for frame in frames:
    textedFrames.append(surfaceToText(frame, scale))

print("Getting display frames...")
displayFrames = []
for i in range(len(textedFrames)):
    displayFrames.append(getTextedFrame(textedFrames[i]))


for i in range(len(displayFrames) * loopcount):
    clear()
    print(displayFrames[i % len(displayFrames)])
    sleep(1 / frameRate)
