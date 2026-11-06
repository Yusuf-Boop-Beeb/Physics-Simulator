import pygame

pygame.init()

WIDTH, HEIGHT = 900, 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

RADIUS = 200

def get_screen_pos(x, y):
    return CENTER_X * RADIUS + x, CENTER_Y * RADIUS - y


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    screen.fill(pygame.Color("white"))
    pygame.draw.line(screen, pygame.Color("grey"), (0, CENTER_Y), (WIDTH, CENTER_Y), 2)
    pygame.draw.line(screen, pygame.Color("grey"), (CENTER_X, 0), (CENTER_X, HEIGHT), 2)
    pygame.draw.circle(screen, pygame.Color("black"), (CENTER_X, CENTER_Y), RADIUS, 2)
    pygame.display.flip()
    clock.tick(60)