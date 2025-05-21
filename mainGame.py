import pygame

def startGame():
    print("Loading Game...")

    pygame.init()

    screen_width = 1000
    screen_height = 800
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

        # userGameInput = input("End Game? Type 'Y' to quit: ")

        # if (userGameInput.lower() == 'y'):
        #        running = False
        # else:
        #     print("Invalid input. Try again")

        # # Update the display
        pygame.display.update()
        
    pygame.quit()