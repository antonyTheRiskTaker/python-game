class RocketGameSettings:
    """A class to store all settings for Rocket Game."""

    def __init__(self):
        """Initialise the game's settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)

        # Rocket settings
        self.rocket_speed = 1.5
