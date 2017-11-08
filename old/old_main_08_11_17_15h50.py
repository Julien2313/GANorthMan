import sys, random
import pygame
from pygame.locals import *
import pymunk 
import pymunk.pygame_util
from sqlalchemy.sql.expression import false
from graphics import graphics

def main():
    pygame.init()
    x_resolution = 1000
    y_resolution = 700
    screen = pygame.display.set_mode((x_resolution, y_resolution))
    pygame.display.set_caption("Test géométrie personnage")
    clock = pygame.time.Clock()
    friction = 0.2
    color_grass = 34,139,34
    space = pymunk.Space()
    space.gravity = (0.0, -900.0)
    env = graphics.Environment(friction, color_grass, space, x_resolution)
    original_stick = graphics.Stickman(5, x_resolution/2, y_resolution/1.5, 10, 2000, friction, space)
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    
    ticks_to_next_stick = 10
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit(0)
                
            elif event.type == MOUSEBUTTONUP:
                x,y = pygame.mouse.get_pos()
                graphics.Stickman(5, x, y_resolution - y, 10, 2000, friction, space)

        ticks_to_next_stick -= 1
        if ticks_to_next_stick <= 0:
            ticks_to_next_stick = 500
            original_stick.stickImpulse()

        screen.fill((255,255,240))

        space.debug_draw(draw_options)

        space.step(1/100)

        pygame.display.flip()
        clock.tick(100)

if __name__ == '__main__':
    main()