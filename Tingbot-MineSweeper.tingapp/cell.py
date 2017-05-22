import tingbot
from tingbot import screen

import random
from random import *

color_palette = {
    'Medium Sky Blue': (101, 222, 241),
    'Pale Robin Egg Blue': (168, 220, 209),
    'Bone': (220, 226, 200),
    'Safety Orange': (249, 105, 0),
    'Princeton Orange': (241, 127, 41),
    }


class Cell(object):
    def __init__(self, col, row, size):
        self.col = col
        self.row = row
        self.size = size
        if random() < 0.3:
            self.ismine = True
        else:
            self.ismine = False
        self.ismarked = False
        self.isdiscovered = False
        self.neighbourCount = 0
    
    def countNeighbours(self, grid):
        for i in range(-1,2,1):
            for j in range(-1,2,1):
                if self.col + i >= 0 and self.col + i  <= 6-1 and self.row + j >= 0 and self.row + j <= 6-1:
                    #print 'Current Cell (' + str(self.col) + ',' + str(self.row) + ')'
                    #print 'Cell to check (' + str(self.col + i) + ',' + str(self.row + j) + ')'
                    if grid[self.col + i][self.row + j].ismine:
                        self.neighbourCount += 1
                    else:
                        pass
                else:
                    pass
                
    def discover(self): #return True if GameOver
        self.isdiscovered = True
        if self.ismine:
            return True
        else:
            return False
    
    def plot(self):
        screen.rectangle(
            xy = (self.col * self.size, self.row * self.size),
            align = 'topleft',
            size = [self.size]*2,
            color = color_palette.get('Medium Sky Blue'),
        )
        
        if self.isdiscovered:
            if self.ismine:
                col = color_palette.get('Safety Orange')
            elif self.neighbourCount == 0:
                col = color_palette.get('Medium Sky Blue')
            else:
                col = color_palette.get('Pale Robin Egg Blue')
        elif self.ismarked:
            col = 'green'
        else:
            col = 'white'
            
        screen.rectangle(
            xy = (self.col * self.size + 1, self.row * self.size + 1),
            align = 'topleft',
            size = [self.size-2]*2,
            color = col,
        )
        
        if self.isdiscovered and not self.ismine and self.neighbourCount <> 0:
            screen.text(
                self.neighbourCount,
                xy = (self.col * self.size + self.size / 2, self.row * self.size + self.size / 2),
                font_size = self.size-2,
                align = 'center',
                color = 'white'
            )
        
    
