import pygame

def startGame():
    print("Loading Game...")

    pygame.init()

    screen_width = 1000
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Space Shooter")

    playerX = 500
    playerY = 700

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Game logic and drawing would go here
        playerShip = pygame.image.load('assets/Space_Shooter_Sprite.png').convert()

        key = pygame.key.get_pressed()

        if key[pygame.K_a] == True:
            playerX-=1
        if key[pygame.K_d] == True:
            playerX+=1
        if key[pygame.K_w] == True:
            playerY-=1
        if key[pygame.K_s] == True:
            playerY+=1

        screen.blit(playerShip, (playerX, playerY))
        # pygame.display.flip()

        # # Update the display
        pygame.display.update()

    pygame.quit()