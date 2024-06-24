import pygame
from cell import Cell
import math
from random import randrange

pygame.init()
CELL_SIZE = 50
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
cells = [[Cell(y, x, CELL_SIZE) for x in range(math.floor(SCREEN_WIDTH/CELL_SIZE))]
         for y in range(math.floor(SCREEN_HEIGHT/CELL_SIZE))]


def dfs(cells):
    for i in range(len(cells)):
        if not cells[i][-1].blocked:
            path = _dfs(cells, i, len(cells[i])-1, [])
            if path:
                return path

def _dfs(cells, i, j, path):
    if i < 0 or j < 0 or i >= len(cells) or j >= len(cells[i]) or cells[i][j].visited or cells[i][j].blocked:
        return None
    cells[i][j].set_visited()
    path.append((i, j))
    if j == 0:
        return path
    result = _dfs(cells, i-1, j, path)
    if result:
        return result
    result = _dfs(cells, i+1, j, path)
    if result:
        return result
    result = _dfs(cells, i, j-1, path)
    if result:
        return result
    result = _dfs(cells, i, j+1, path)
    if result:
        return result
    path.pop()
    return None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    path =  dfs(cells)
    if path:
        for i, j in path:
            cells[i][j].set_best_path()
    for row in cells:
        for cell in row:
            cell.display(screen)
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
