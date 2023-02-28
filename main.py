import pygame, sys

class Game:
    def __init__(self):
        pass

    def run(self):
        pass
        # update all sprite groups
        # draw all sprite groups

if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    # Set up the window
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()
    game = Game()
 
    while True:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the background with black
        screen.fill((30,30,30))
        game.run()


        # Flip the display
        pygame.display.flip()
        clock.tick(60)

