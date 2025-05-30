import pygame

def rot_center(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect

def startGame():
    print("Loading Game...")

    pygame.init()

    screen_width = 1000
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Space Shooter")

    playerX = 450
    playerY = 700

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Game logic and drawing would go here
        background = pygame.image.load('assets/Space_Shooter_Background.png').convert()
        playerShip = pygame.image.load('assets/Space_Shooter_Sprite.png').convert()

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
            rot_center(playerShip, 1, playerX, playerY)

        screen.blit(background, (0, 0))
        screen.blit(playerShip, (playerX, playerY))
        # pygame.display.flip()

        # # Update the display
        pygame.display.update()

    pygame.quit()