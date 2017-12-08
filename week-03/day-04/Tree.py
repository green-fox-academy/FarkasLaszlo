import pygame, math

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()


def drawTree(x1, y1, angle, depth):
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 4.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 4.0)
        pygame.draw.line(screen, (254, 249, 53), (x1, y1), (x2, y2), 1)
        drawTree(x2, y2, angle - 15, depth - 1)
        drawTree(x2, y2, angle + 15, depth - 1)


def input(event):
    if event.type == pygame.QUIT:
        exit(0)


drawTree(300, 550, -90, 14)
pygame.display.flip()
while True:
    input(pygame.event.wait())