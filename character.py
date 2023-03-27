import pygame

class Character:
    """A class to manage the character."""

    def __init__(self, ai_game):
        """Initialise the character and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the character image and get its rect.
        # TODO: resize the bitmap image