import pygame
import math

pygame.font.init()

screen = pygame.display.set_mode((500, 500))

#Title and icon
pygame.display.set_caption('Sudoku Solver')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
