"""Constants in the game"""
import pygame
import os
pygame.init()

file_dir = os.path.dirname(__file__)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 675

<<<<<<< HEAD
BOARD_SIZE = 14
TILE_SIZE = 20


=======
BOARD_SIZE = 28
TILE_SIZE = 20

>>>>>>> refs/remotes/origin/main
gFonts = {
    "smallFont": pygame.font.Font(file_dir + "/../fonts/ARCADECLASSIC.TTF", 16),
    "mediumFont": pygame.font.Font(file_dir + "/../fonts/ARCADECLASSIC.TTF", 32),
    "largeFont": pygame.font.Font(file_dir + "/../fonts/ARCADECLASSIC.TTF", 64),
    "veryLargeFont": pygame.font.Font(file_dir + "/../fonts/ARCADECLASSIC.TTF", 128)
}

gColors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "orange": (255, 165, 0),
    "gray": (128,128,128),
    "red": (255, 0, 0)
}
