'''
Score class
Handles score tracking and display
'''
import pygame
class Score:
    def __init__(self):
        """Initialize score counter"""
        self.value = 0
    def increase(self):
        """Increase score by 1"""
        self.value += 1
    def draw(self, screen, color, screen_width):
        """Draw current score on the screen"""
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"得分: {self.value}", True, color)
        screen.blit(score_text, (10, 10))
        # Draw instructions
        instructions = font.render("使用方向键控制蛇的移动", True, color)
        screen.blit(instructions, (screen_width - 300, 10))