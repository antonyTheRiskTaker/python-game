import pygame


class Rocket:
    """A class to manage the rocket."""

    def __init__(self, rg_game):
        """Initialise the rocket and set its initial position."""
        self.screen = rg_game.screen
        self.settings = rg_game.settings
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

        # Store a float for the rocket's exact horizontal and vertical location.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag; start with a rocket that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False

    def update(self):
        "Update the rocket's location based on the movement flag."
        # Update the rocket's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed

        # Update rect object from self.x and self.y.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)
