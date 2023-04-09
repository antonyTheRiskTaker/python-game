import sys
import pygame

from rocket_game_settings import RocketGameSettings
from rocket import Rocket


class RocketGame:
    """
    Try It Yourself Exercise 12-4. Overall class to manage game assets and
    behaviour.
    The game needs to fulfil three requirements:
    1. It position a rocket in the centre of the screen.
    2. The player can move the rocket up, down, left or right using the four 
       arrow keys.
    3. The rocket never moves beyond any edge of the screen.
    """

    # TODO: Create rocket class.

    def __init__(self):
        """Initialise the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = RocketGameSettings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        pygame.display.set_caption("Rocket Game")
        
        self.rocket = Rocket(self)
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            # self.rocket.update() #! Does not work
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_colour)
        self.rocket.blitme()
        
        # Uncomment it if pygame.display.update() doesn't work
        # pygame.display.flip()
        pygame.display.update()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    rg = RocketGame()
    rg.run_game()