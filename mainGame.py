import pygame

def startGame():
    print("Welcome to game.py!")
    
    pygame.init()

    screen_width = 800
    screen_height = 600

    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Space Shooter")

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Game logic and drawing would go here

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()