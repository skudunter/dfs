import pygame
from random import random

BLOCKED_PROBABILITY = 0.3


class Cell:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size
        self.visited = False
        self.blocked = random() < BLOCKED_PROBABILITY
        self.color = '#3F2F6F' 
        self.color = '#000000' if self.blocked == True else self.color

    def display(self,screen):
        pygame.draw.rect(screen, self.color, (self.col * self.size, self.row * self.size, self.size, self.size))

    def set_visited(self):
        self.visited = True
        self.color = 'red'
    def set_best_path(self):
        self.color = 'green'    