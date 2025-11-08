'''
Main game controller
Handles game loop, events, and overall game state
'''
import pygame
import sys
from snake import Snake
from food import Food
from score import Score
class Game:
    def __init__(self):
        """Initialize game settings and objects"""
        pygame.init()
        # Game constants
        self.WIDTH = 800
        self.HEIGHT = 600
        self.GRID_SIZE = 20
        self.FPS = 10
        # Colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        # Initialize screen
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("贪吃蛇游戏 - Snake Game")
        self.clock = pygame.time.Clock()
        # Game objects
        self.snake = Snake(self.WIDTH, self.HEIGHT, self.GRID_SIZE)
        self.food = Food(self.WIDTH, self.HEIGHT, self.GRID_SIZE)
        self.score = Score()
        # Generate initial food
        self.food.generate_food(self.snake.body)
        # Game state
        self.game_over = False
    def handle_events(self):
        """Handle keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != "DOWN":
                    self.snake.direction = "UP"
                elif event.key == pygame.K_DOWN and self.snake.direction != "UP":
                    self.snake.direction = "DOWN"
                elif event.key == pygame.K_LEFT and self.snake.direction != "RIGHT":
                    self.snake.direction = "LEFT"
                elif event.key == pygame.K_RIGHT and self.snake.direction != "LEFT":
                    self.snake.direction = "RIGHT"
                elif event.key == pygame.K_r and self.game_over:
                    self.restart_game()
    def update(self):
        """Update game state"""
        if not self.game_over:
            self.snake.move()
            # Check if snake ate food
            if self.snake.body[0] == self.food.position:
                self.snake.grow()
                self.score.increase()
                self.food.generate_food(self.snake.body)
            # Check collisions
            if (self.snake.check_self_collision() or 
                self.snake.check_wall_collision(self.WIDTH, self.HEIGHT)):
                self.game_over = True
    def draw(self):
        """Draw all game elements"""
        self.screen.fill(self.BLACK)
        # Draw grid (optional visual aid)
        for x in range(0, self.WIDTH, self.GRID_SIZE):
            pygame.draw.line(self.screen, (50, 50, 50), (x, 0), (x, self.HEIGHT))
        for y in range(0, self.HEIGHT, self.GRID_SIZE):
            pygame.draw.line(self.screen, (50, 50, 50), (0, y), (self.WIDTH, y))
        # Draw game objects
        self.snake.draw(self.screen, self.GREEN, self.BLUE)
        self.food.draw(self.screen, self.RED)
        self.score.draw(self.screen, self.WHITE, self.WIDTH)
        # Game over message
        if self.game_over:
            font = pygame.font.Font(None, 74)
            game_over_text = font.render("游戏结束!", True, self.WHITE)
            restart_text = pygame.font.Font(None, 36).render("按 R 键重新开始", True, self.WHITE)
            self.screen.blit(game_over_text, (self.WIDTH//2 - 150, self.HEIGHT//2 - 50))
            self.screen.blit(restart_text, (self.WIDTH//2 - 100, self.HEIGHT//2 + 20))
        pygame.display.flip()
    def restart_game(self):
        """Restart the game"""
        self.snake = Snake(self.WIDTH, self.HEIGHT, self.GRID_SIZE)
        self.food = Food(self.WIDTH, self.HEIGHT, self.GRID_SIZE)
        self.score = Score()
        self.food.generate_food(self.snake.body)
        self.game_over = False
    def run(self):
        """Main game loop"""
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.FPS)