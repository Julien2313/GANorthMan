import sys, random
import pygame
from pygame.locals import *
from pymunk import Vec2d
import pymunk 
import pymunk.pygame_util
from array import array
from math import pow
from math import sqrt

class Stickman:
        
    def genStick(self):
        self.space.add(
        self.corpse.body,
        self.corpse.corpse_shape,
        self.corpse.head_shape,
        self.left_arm.body,
        self.left_arm.left_arm_shape,
        self.right_arm.body,
        self.right_arm.right_arm_shape,
        self.left_leg.body,
        self.left_leg.left_leg_shape,
        self.right_leg.body,
        self.right_leg.right_leg_shape,
        self.pin_la_c,
        self.pin_ll_c,
        self.pin_ra_c,
        self.pin_rl_c
    )
        
    def genJunctions(self):
        self.pin_ra_c = pymunk.PinJoint(self.right_arm.body, self.corpse.body, (0,0), (0, 30*self.size))
        self.pin_ra_c_r = pymunk.DampedRotarySpring(self.right_arm.body, self.right_arm.body_joint, -0.15, 20000000, 900000)
        self.pin_ra_c.error_bias = pow(0.7, 60.0)      
        
        self.pin_la_c = pymunk.PinJoint(self.left_arm.body, self.corpse.body, (0,0), (0, 30*self.size))  
        self.pin_la_c_r = pymunk.DampedRotarySpring(self.left_arm.body, self.left_arm.body_joint, -0.15, 20000000, 900000)
        self.pin_la_c.error_bias = pow(0.7, 60.0)      
        
        self.pin_rl_c = pymunk.PinJoint(self.right_leg.body, self.corpse.body, (0,0), (0, 0))
        self.pin_rl_c_r = pymunk.DampedRotarySpring(self.right_leg.body, self.right_leg.body_joint, -0.15, 20000000, 900000)
        self.pin_rl_c.error_bias = pow(0.7, 60.0)  
        
        self.pin_ll_c = pymunk.PinJoint(self.left_leg.body, self.corpse.body, (0,0), (0, 0))
        self.pin_ll_c_r = pymunk.DampedRotarySpring(self.left_leg.body, self.left_leg.body_joint, 10, 1, 1)
        self.pin_ll_c.error_bias = pow(0.7, 60.0)  
    
    def __init__(self, size, x, y, mass, moment, friction, space):
        self.mass = mass
        self.moment = moment
        self.size = size
        self.space = space
        self.right_leg = RightLeg(size, x, y, mass, moment, friction)
        self.right_arm = RightArm(size, x, y, mass, moment, friction)
        self.left_leg = LeftLeg(size, x, y, mass, moment, friction)
        self.left_arm = LeftArm(size, x, y, mass, moment, friction)
        self.corpse = Corpse(size, x, y, mass, moment, friction)
        
        self.genJunctions()
        self.genStick()

        
class Member:
    def __init__(self, mass, moment, friction):
        self.body = pymunk.Body(mass, moment)
        self.body_joint = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.friction = friction
        
class Corpse() : 
    
    def __init__(self, size, x, y, mass, moment, friction):  
        self.body = pymunk.Body(mass, moment)
        self.body.position = (x,y - 40*size)
        
        self.head_shape = pymunk.Circle(self.body, 10*size, (0,38*size))
        self.head_shape.friction = friction
        self.head_shape.filter = pymunk.ShapeFilter(categories=0x1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 0x1)  
   
        self.corpse_shape = pymunk.Segment(self.body, (0, 0), (0, 30*size), 2*size)
        self.corpse_shape.friction = friction
        self.corpse_shape.filter = pymunk.ShapeFilter(categories=0x1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 0x1)

      
class LeftLeg(Member) : 
    
    def __init__(self, size, x, y, mass, moment, friction):
        Member.__init__(self, mass, moment, friction)
        self.body.position =(x, y - 40*size)
        self.body_joint.position = self.body.position
        
        self.left_leg_shape = pymunk.Segment(self.body, (-10*size, -20*size), (0,0), 2*size)
        self.left_leg_shape.friction = friction
        self.left_leg_shape.filter = pymunk.ShapeFilter(categories=0x1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 0x1)  

    
class RightLeg(Member) : 
    
    def __init__(self, size, x, y, mass, moment, friction):
        Member.__init__(self, mass, moment, friction)
        self.body.position =(x, y - 40*size)
        self.body_joint.position = self.body.position
        
        self.right_leg_shape = pymunk.Segment(self.body, (10*size, -20*size), (0, 0), 2*size)
        self.right_leg_shape.friction = friction
        self.right_leg_shape.filter = pymunk.ShapeFilter(categories=0x1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 0x1)  

    
class LeftArm(Member) : 
    
    def __init__(self, size, x, y, mass, moment, friction):
        Member.__init__(self, mass, moment , friction)
        self.body.position =(x, y - 10*size)
        self.body_joint.position = self.body.position
        
        self.left_arm_shape = pymunk.Segment(self.body, (-10*size, -20*size), (0, 0), 2*size)
        self.left_arm_shape.friction = friction
        self.left_arm_shape.filter = pymunk.ShapeFilter(categories=0x1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 0x1)  


class RightArm(Member) : 
    
    def __init__(self, size, x, y, mass, moment, friction):
        Member.__init__(self, mass, moment , friction)
        self.body.position =(x, y - 10*size)
        self.body_joint.position = self.body.position
        
        self.right_arm_shape = pymunk.Segment(self.body, (10*size, -20*size), (0, 0), 2*size)
        self.right_arm_shape.friction = friction
        self.right_arm_shape.filter = pymunk.ShapeFilter(categories=0x1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 0x1)  


class Environment():
    
    def __init__(self, friction, color, space, length):
        self.length = length
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.environment = pymunk.Segment(self.body, (0,0), (length,0), 50.0)
        self.environment.friction = friction
        self.environment.color = color
        self.space = space
        space.add(self.environment, self.body)
        
class Level():
    def generateLevelGrid(self):
        self.w, self.h = int(self.x_resolution/20), int(self.y_resolution/20);
        return [[0 for x in range(self.h)] for y in range(self.w)] 
        

    def generateBounds(self):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (0,0)
        segLeft = pymunk.Segment(body, (0,0), (0,self.y_resolution), 2)
        segRight = pymunk.Segment(body, (self.x_resolution,0), (self.x_resolution,self.y_resolution), 2)
        segTop = pymunk.Segment(body, (0,self.y_resolution), (self.x_resolution,self.y_resolution), 2)
        segBot = pymunk.Segment(body, (0,0), (self.x_resolution,0), 2)
        self.space.add(body, segLeft, segBot, segRight, segTop)        
    
    def generateLevel(self):
        self.generateBounds()
        self.obstaclesGrid[5][2] = 1
        self.obstaclesGrid[6][2] = 1
        self.obstaclesGrid[9][3] = 1
        self.obstaclesGrid[10][3] = 1
        self.obstaclesGrid[14][1] = 1
        self.obstaclesGrid[15][2] = 1
        self.obstaclesGrid[16][2] = 1
        self.obstaclesGrid[17][3] = 1
        self.obstaclesGrid[18][3] = 1
        self.obstaclesGrid[19][3] = 1
        
        self.obstaclesGrid[19][4] = 2
        print("Level Generated")
        
    def renderLevel(self):
        for i in range(self.w):
            for j in range(self.h):
                if self.obstaclesGrid[i][j] == 1:
                    self.addObstacle(i,j)
                    
                elif self.obstaclesGrid[i][j] == 2:
                    self.addObjectivePoint(i,j)
    
    def addObstacle(self, i, j):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (i*int(self.x_resolution/20), j*int(self.y_resolution/20))
        
        segLeft = pymunk.Segment(body, (0,0), (0,self.y_resolution/20), 1)
        segRight = pymunk.Segment(body, (self.x_resolution/20,0), (self.x_resolution/20,self.y_resolution/20), 1)
        segTop = pymunk.Segment(body, (0,self.y_resolution/20), (self.x_resolution/20,self.y_resolution/20), 1)
        segBot = pymunk.Segment(body, (0,0), (self.x_resolution/20,0), 1)
        
        segLeft.color, segRight.color, segTop.color, segBot.color = ((0,0,0),(0,0,0),(0,0,0),(0,0,0))
        self.space.add(body, segLeft, segBot, segRight, segTop)
        
    def addObjectivePoint(self,i,j):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (i*int(self.x_resolution/20) + int(self.x_resolution/40), j*int(self.y_resolution/20) + int(self.y_resolution/20))
        objective = pymunk.Circle(body, 10, (0,0))
        objective.color = 0,200,0
        objective.filter = pymunk.ShapeFilter(categories=0x1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 0x1)
        self.objectivePointBody = body
        self.space.add(body, objective)
        
    def __init__(self, x_resolution, y_resolution, space):
        self.x_resolution = x_resolution
        self.y_resolution = y_resolution
        self.space = space
        self.obstaclesGrid = self.generateLevelGrid()
        self.generateLevel()
        self.renderLevel()
        
class Util():
    def distanceBetweenTwoBodies(firstBody, secondBody):
        (x_a,y_a) = firstBody.position
        (x_b,y_b) = secondBody.position
        return sqrt(pow(x_b - x_a, 2) + pow(y_b - y_a, 2))
    
    def __init(self):
        pass