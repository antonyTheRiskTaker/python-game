class Settings:
    """A class to store all settings for Alien Invasion."""
    GREY_COLOR = (230, 230, 230)
    BLUE_COLOR = (0, 100, 255)

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = "blue"