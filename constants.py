"""Module for font"""
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # hide welcome prompt from pygame
import pygame

RED = (255, 0, 0)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
LIGHT_GREEN = (188, 245, 188)

INSTRUCTIONS = {"up": (-1, 0), "left": (0, -1), "down": (1, 0), "right": (0, 1)}
WIDTH = 720
WIDTH_WINDOW = 1450
HEIGHT_WINDOW = 780
WAIT_VARIABLE_FOR_10_X_10 = 70
WAIT_VARIABLE_FOR_20_X_20 = 20
WAIT_VARIABLE_FOR_30_X_30 = 5
WAIT_VARIABLE_FOR_40_X_40 = 2
DEFAULT_ROWS = 30
DEFAULT_COLS = 30
WIN = pygame.display.set_mode((WIDTH_WINDOW, HEIGHT_WINDOW), pygame.RESIZABLE)

pygame.init()
GUI_FONT = pygame.font.Font(None, 26)
