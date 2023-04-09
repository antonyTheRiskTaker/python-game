import pygame


class Character:
    """A class to manage the character."""

    def __init__(self, ai_game):
        """Initialise the character and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the rocket image, resize it, and get its rect.
        self.image = pygame.image.load('images/random-character.bmp')
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.image = pygame.transform.scale(
            self.image, (self.width*0.2, self.height*0.2))
        self.rect = self.image.get_rect()

        # Start each new character at the centre of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)