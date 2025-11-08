'''
Snake class
Handles snake movement, growth, collision detection, and rendering
'''
import pygame
import random
class Snake:
    def __init__(self, screen_width, screen_height, grid_size):
        """Initialize snake with starting position and direction"""
        self.grid_size = grid_size
        self.direction = "RIGHT"
        # Start snake in the middle of the screen
        start_x = screen_width // 2
        start_y = screen_height // 2
        # Align to grid
        start_x = (start_x // grid_size) * grid_size
        start_y = (start_y // grid_size) * grid_size
        self.body = [
            [start_x, start_y],
            [start_x - grid_size, start_y],
            [start_x - 2 * grid_size, start_y]
        ]
    def move(self):
        """Move the snake in the current direction"""
        head = self.body[0].copy()
        if self.direction == "UP":
            head[1] -= self.grid_size
        elif self.direction == "DOWN":
            head[1] += self.grid_size
        elif self.direction == "LEFT":
            head[0] -= self.grid_size
        elif self.direction == "RIGHT":
            head[0] += self.grid_size
        # Add new head and remove tail
        self.body.insert(0, head)
        self.body.pop()
    def grow(self):
        """Grow the snake by one segment"""
        # Add a new segment at the tail position
        self.body.append(self.body[-1].copy())
    def check_self_collision(self):
        """Check if snake collides with itself"""
        head = self.body[0]
        return head in self.body[1:]
    def check_wall_collision(self, screen_width, screen_height):
        """Check if snake hits the wall"""
        head = self.body[0]
        return (head[0] < 0 or head[0] >= screen_width or 
                head[1] < 0 or head[1] >= screen_height)
    def draw(self, screen, body_color, head_color):
        """Draw the snake on the screen"""
        # Draw body segments
        for segment in self.body[1:]:
            pygame.draw.rect(screen, body_color, 
                           (segment[0], segment[1], self.grid_size, self.grid_size))
        # Draw head with different color
        head = self.body[0]
        pygame.draw.rect(screen, head_color, 
                       (head[0], head[1], self.grid_size, self.grid_size))