'''
Food class
Handles food generation, positioning, and rendering
'''
import pygame
import random
class Food:
    def __init__(self, screen_width, screen_height, grid_size):
        """Initialize food with grid alignment"""
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.grid_size = grid_size
        self.position = [0, 0]
    def generate_food(self, snake_body):
        """Generate food at random position not occupied by snake"""
        while True:
            x = random.randrange(0, self.screen_width, self.grid_size)
            y = random.randrange(0, self.screen_height, self.grid_size)
            self.position = [x, y]
            # Ensure food doesn't spawn on snake
            if self.position not in snake_body:
                break
    def draw(self, screen, color):
        """Draw food on the screen"""
        pygame.draw.rect(screen, color, 
                        (self.position[0], self.position[1], 
                         self.grid_size, self.grid_size))