"""Title screen state class."""
import pygame

class TitleScreenState:
    def __init__(self, game, params: dict):
        """Initialize title screen"""
        self.game = game
    
    def draw_title_screen(self):
        """Draw the title screen."""
        font = pygame.font.Font("../../fonts/ARCADECLASSIC.TTF", 32)
        
