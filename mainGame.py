import pygame

def startGame():
    print("Welcome to game.py!")

    pygame.init()

    screen_width = 800
    screen_height = 600

    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Space Shooter")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Game logic and drawing would go here
        playerShip = pygame.image.load('assets/Space_Shooter_Sprite.png').convert()
        r = playerShip.get_rect()
        r.center = screen.get_rect().center
        screen.blit(playerShip, r)

        pygame.display.flip()

        userGameInput = input("End Game? Type 'Y' to quit: ")

        if (userGameInput.lower() == 'y'):
                # Quit Pygame
               pygame.quit()
               running = False
        else:
            print("Invalid input. Try again")


        # # Update the display
        # pygame.display.flip()