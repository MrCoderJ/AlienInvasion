import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # For FUll screen activate
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()




        # set the background

    def run_game(self):
        """Starting the main loop for the game"""

        while True:
            # Watch for keyboard and mouse events
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            # Redraw the screen during pass through the loop
            
    def _check_events(self):
        """Respond to keypress and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
                

            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _fire_bullet(self):
        """Create a new bullet and add it to bullets group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
                
    def _check_keydown_event(self, event):
        """Respond to Keydown Press"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()    
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_event(self, event):
        """Responf to keyup press """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _update_screen(self):
        """Open Images  on the screen and flip to another screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the fame
    ai = AlienInvasion()
    ai.run_game()