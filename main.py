import pygame

pygame.init()

WIDTH, HEIGHT = 900, 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    screen.fill(pygame.Color("black"))
    pygame.display.flip()
    clock.tick(60)