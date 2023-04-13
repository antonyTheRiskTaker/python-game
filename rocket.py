import pygame


class Rocket:
    """A class to manage the rocket."""

    def __init__(self, rg_game):
        """Initialise the rocket and set its initial position."""
        self.screen = rg_game.screen
        self.screen_rect = rg_game.screen.get_rect()

        # Load the rocket image, resize it, and get its rect.
        self.image = pygame.image.load('images/cohete_off.png')
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.image = pygame.transform.scale(
            self.image, (self.width*1, self.height*1))
        self.rect = self.image.get_rect()

        # Start the rocket at the centre of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)
