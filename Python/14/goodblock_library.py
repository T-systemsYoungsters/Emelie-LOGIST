import pygame
import block_library
import random

class GoodBlock(block_library.Block):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)
    def update(self):
        self.change_x = random.randrange(-3,4)
        self.change_y = random.randrange(-3,4)
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.change_x < 0:
            self.change_x = 0
        if self.change_x > 685:
            self.change_x = 685
        if self.change_y < 0:
            self.change_y = 0
        if self.change_y > 385:
            self.change_y = 285
        
