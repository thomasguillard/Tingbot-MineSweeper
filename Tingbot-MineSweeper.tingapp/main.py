import tingbot
from tingbot import *

import cell
from cell import *

# setup code here

'''
Only accepts RGB...

color_pallete = {
    'Medium Sky Blue': '#65DEF1',
    'Pale Robin Egg Blue': '#A8DCD1',
    'Bone': '#DCE2C8',
    'Safety Orange': '#F96900',
    'Princeton Orange': '#F17F29',
    }'''
    
color_palette = {
    'Medium Sky Blue': (101, 222, 241),
    'Pale Robin Egg Blue': (168, 220, 209),
    'Bone': (220, 226, 200),
    'Safety Orange': (249, 105, 0),
    'Princeton Orange': (241, 127, 41),
    }

cell = Cell(0, 0, 20)
grid_size = 6
cell_size = screen.height/grid_size
grid = [[] for i in xrange(grid_size)]

gameOver = False

mode = 0 # 0: Discover, 1: Mark

for col in xrange(grid_size):
    for row in xrange(grid_size):
            grid[col].append(Cell(col, row, cell_size))
            
for col in xrange(grid_size):
    for row in xrange(grid_size):
            grid[col][row].countNeighbours(grid)

@touch(xy=(0,0), size=(screen.height,screen.height), align='topleft')
def on_touch(xy, action):
    global touch_Pos, pos_Col, pos_Row, grid, gameOver, mode
    if action == 'up' and gameOver == False:
        col = xy[0] / cell_size
        row = xy[1] / cell_size
        if mode == 0:
            gameOver = grid[col][row].discover()
        elif mode == 1:
            grid[col][row].ismarked = not(grid[col][row].ismarked)
        else:
            pass

@touch(xy=(screen.width - 5, 50), size=(screen.width-screen.height-10,50), align='topright')
def toggle_Mode(xy, action):
    if action == 'up':
        global mode
        if mode == 0:
            mode = 1
        else:
            mode = 0

@every(seconds=1.0/30)
def loop():
    # drawing code here
    screen.fill(color='black')
    #screen.text('Hello world!')
    
    screen.rectangle(
        xy = (screen.width - 5, 50),
        size = (screen.width-screen.height-10,50),
        color = color_palette.get('Bone'),
        align = 'topright',
    )
    
    screen.text(
        'Mode: ' + str(mode),
        xy = (screen.height + (screen.width-screen.height)/2, 75),
        color = color_palette.get('Medium Sky Blue'),
        align = 'center',
        font_size = 15,
    )
    
    for col in xrange(grid_size):
        for row in xrange(grid_size):
            grid[col][row].plot()
    
    if gameOver:
        for col in xrange(grid_size):
            for row in xrange(grid_size):
                grid[col][row].isdiscovered = True
        screen.text(
            'Game Over!',
            xy = (screen.height/2, screen.height/2),
            align = 'center',
            font_size = 70,
            color = 'black',
            max_width = screen.height,
        )
        

tingbot.run()
