import sys
import pygame
from pygame.locals import *
import pymunk 
import pymunk.pygame_util

from GA.GeneticAlgorithm import GeneticAlgorithm
from graphics import graphics

def main():
    pygame.init()
    x_resolution = 1200
    y_resolution = 700
    screen = pygame.display.set_mode((x_resolution, y_resolution))
    pygame.display.set_caption("Test geometrie personnage")
    clock = pygame.time.Clock()
    size = 1.5
    friction = 0.2
    mass = 2
    moment = 50000
    color_grass = 34,139,34
    space = pymunk.Space()
    space.gravity = (0.0, -900.0)
    original_stick = graphics.Stickman(size, x_resolution/7, y_resolution/3, mass, moment, friction, space)
    level = graphics.Level(x_resolution, y_resolution, space)
    env = graphics.Environment(friction, color_grass, space, x_resolution)
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit(0)
              
            #test angle case  
            elif event.type == KEYDOWN and event.key == K_UP:
                print("Deplacement jambe droite")
                original_stick.right_leg.body.angle += 1.57
                space.reindex_shape(original_stick.right_leg.right_leg_shape)

            elif event.type == KEYDOWN and event.key == K_DOWN:
                print("Deplacement jambe gauche")
                original_stick.left_leg.body.angle += 1.57
                space.reindex_shape(original_stick.left_leg.left_leg_shape)
                
            elif event.type == KEYDOWN and event.key == K_LEFT:
                print("Deplacement bras gauche")
                original_stick.left_arm.body.angle += 1.57
                space.reindex_shape(original_stick.left_arm.left_arm_shape)
                
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                print("Deplacement bras droit")
                original_stick.right_arm.body.angle += 1.57
                space.reindex_shape(original_stick.right_arm.right_arm_shape)
                
            #elif event.type == MOUSEBUTTONUP:
                #print("New stickman")
                #x,y = pygame.mouse.get_pos()
                #graphics.Stickman(size, x, y_resolution - y, mass, moment, friction, space)
        
        print("Distance : " + str(graphics.Util.distanceBetweenTwoBodies(original_stick.corpse.body,level.objectivePointBody)))
        screen.fill((240, 255, 255))

        space.debug_draw(draw_options)

        space.step(1/100)

        pygame.display.flip()
        clock.tick(100)

if __name__ == '__main__':
    GA = GeneticAlgorithm()

    GA.initializePop()
    GA.pop[0].setInputs([True] * GA.pop[0].nbrInputs)
    GA.pop[0].calculateOutputs()
    GA.pop[0].printNN()
    GA.pop[0].mutate(1)
    GA.pop[0].printNN()
    GA.pop[0].drawNN()

    #main()
