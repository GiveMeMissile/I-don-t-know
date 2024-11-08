import pygame
pygame.init()
Width = 800
Height = 500
run = True
screen = pygame.display.set_mode((Width, Height))
shape = pygame.Rect(400, 250, 50, 50)
thing = pygame.Rect(600, 400, 50, 50)
while run == True:
    screen.fill((0, 0, 0))
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        shape.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        shape.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        shape.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        shape.move_ip(0, 1)
    elif key[pygame.K_i] == True:
        thing.move_ip(0, -1)
    elif key[pygame.K_k] == True:
        thing.move_ip(0, 1)
    elif key[pygame.K_l] == True:
        thing.move_ip(1, 0)
    elif key[pygame.K_j] == True:
        thing.move_ip(-1, 0)
    pygame.draw.rect(screen, (255, 0, 0), shape)
    pygame.draw.rect(screen, (0, 255, 0), thing)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit
