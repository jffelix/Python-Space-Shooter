import pygame

def startGame():
    print("Loading Game...")

    pygame.init()

    screen_width = 1000
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Space Shooter")

    background = pygame.image.load('assets/Space_Shooter_Background.png').convert()

    playerX = 450
    playerY = 700

    angle = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Game logic and drawing would go here

        playerShip = pygame.image.load('assets/Space_Shooter_Sprite.png').convert()
        playerShip_rect = playerShip.get_rect(center=(playerX, playerY))

        # laserPoint = pygame.transform.rotate(playerShip,angle)

        key = pygame.key.get_pressed()

        if key[pygame.K_a] == True:
            playerX-=2
        if key[pygame.K_d] == True:
            playerX+=2
        if key[pygame.K_w] == True:
            playerY-=2
        if key[pygame.K_s] == True:
            playerY+=2

        if key[pygame.K_j] == True:
            angle -= 2
            # screen.blit(rotated_image, rotated_rec)

        rotated_image = pygame.transform.rotate(playerShip, angle)
        rotated_rec = rotated_image.get_rect(center=playerShip_rect.center)
    
        screen.blit(background, (0, 0))
        screen.blit(playerShip, (playerX, playerY))
        screen.blit(rotated_image, rotated_rec)
        # pygame.display.flip()

        # # Update the display
        pygame.display.update()

    pygame.quit()