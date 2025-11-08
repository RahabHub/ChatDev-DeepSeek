'''
Main entry point for the Snake Game
Initializes the game and starts the main loop
'''
import pygame
from game import Game
def main():
    """Initialize and run the Snake game"""
    game = Game()
    game.run()
if __name__ == "__main__":
    main()