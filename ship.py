import pygame
class Ship:
    """A class to manag the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and get it starting location"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Starting each ship at the bottom 

        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        # Draw's the ship at it's current location

        self.screen.blit(self.image, self.rect)

    def update(self):
        """ Updating the ship's position based on movement flag. """
        if self.moving_right == True:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1