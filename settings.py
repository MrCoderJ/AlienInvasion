class Settings:
    """A class to store all the settings for Alien Invasion"""

    def __init__(self):

        """Initialize the Game's setting """
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 0.9
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

