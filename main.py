import pygame
import random
import sys

# a game that can move the square

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("The best game ever!")

x_coordinate = 500
y_coordinate = 300


running = True
while running == True:
    for event in pygame.event.get():
        # draw the square
        pygame.draw.rect(screen, (random.randint(0, 255), (random.randint(0, 255), (random.randint(0, 255)), (x_coordinate, y_coordinate, 50, 50))))  # (0,0,0) is RGB black
    if event.type == pygame.QUIT:
        break



    button = pygame.key.get_pressed()   # store what button user pressed
    print(x_coordinate, y_coordinate)
    # logic for moving the square
    if button[pygame.K_LEFT]:
        x_coordinate -= 1
    if button[pygame.K_RIGHT]:
        x_coordinate += 1
    if button[pygame.K_UP]:
        y_coordinate -= 1
    if button[pygame.K_DOWN]:
        y_coordinate += 1
    pygame.time.Clock().tick(60)  # 60 fps

    # code to prevent square leaving the square

    if x_coordinate < 0:
        x_coordinate = 0
    if y_coordinate < 0:
        y_coordinate = 0

    pygame.display.flip()   # update changes