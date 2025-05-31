import pygame

pygame.init()

font = pygame.font.Font(None, 36)

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
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Game logic and drawing here
        playerImg = pygame.image.load('assets/Space_Shooter_Sprite.png').convert()
        # playerShip_rect = playerShip.get_rect(center=(playerX, playerY))
        playerShip = pygame.transform.scale(playerImg, (75, 75))
        
        key = pygame.key.get_pressed()

        if key[pygame.K_a] == True:
            playerX -= 2
        if key[pygame.K_d] == True:
            playerX += 2
        if key[pygame.K_w] == True:
            playerY -= 2
        if key[pygame.K_s] == True:
            playerY += 2

        if key[pygame.K_j] == True:
            angle += 2
        if key[pygame.K_k] == True:
            angle -= 2

        rotated_image = pygame.transform.rotate(playerShip, angle)
        rotated_rec = rotated_image.get_rect(center=(playerX, playerY))

        angle_text = str(angle)
        angle_surface = font.render(angle_text, True, (255, 255, 255))
    
        screen.blit(background, (0, 0))
        screen.blit(rotated_image, rotated_rec)
        screen.blit(angle_surface, (100, 50))
        # pygame.display.flip()

        # # Update the display
        pygame.display.update()

    pygame.quit()