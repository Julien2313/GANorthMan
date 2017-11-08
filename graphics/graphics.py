import sys, random
import pygame
from pygame.locals import *
import pymunk 
import pymunk.pygame_util
from sqlalchemy.sql.expression import false

class Stickman:
    
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
        self.pin_ra_c = pymunk.PinJoint(self.right_arm.body, self.corpse.body, (-10*self.size, 20*self.size), (0, 30*self.size))
        self.pin_ra_c.error_bias = pow(0.7, 60.0)      
        
        self.pin_la_c = pymunk.PinJoint(self.left_arm.body, self.corpse.body, (10*self.size, 20*self.size), (0, 30*self.size))  
        self.pin_la_c.error_bias = pow(0.7, 60.0)      
        
        self.pin_rl_c = pymunk.PinJoint(self.right_leg.body, self.corpse.body, (-10*self.size, 20*self.size), (0, 0))
        self.pin_rl_c.error_bias = pow(0.7, 60.0)  
        
        self.pin_ll_c = pymunk.PinJoint(self.left_leg.body, self.corpse.body, (10*self.size, 20*self.size), (0, 0))
        self.pin_ll_c.error_bias = pow(0.7, 60.0)  
        
        
    def stickImpulse(self):
        self.left_leg.body.apply_impulse_at_local_point((0,50), (self.left_leg.body.position))
        self.right_leg.body.apply_impulse_at_local_point((0,50), (self.right_leg.body.position))
        
class Member:
    
    def __init__(self, mass, moment, x, y, friction):
        self.x = x 
        self.y = y
        self.body = pymunk.Body(mass, moment)
        self.friction = friction


class Corpse(Member) : 
    
    def __init__(self, size, x, y, mass, moment, friction):
        Member.__init__(self, mass, moment, x, y , friction)
        self.body.position = (x,y - 40*size)
        
        self.head_shape = pymunk.Circle(self.body, 10*size, (0,38*size))
        self.head_shape.friction = friction
        self.head_shape.filter = pymunk.ShapeFilter(categories=0x1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 0x1)  
   
        self.corpse_shape = pymunk.Segment(self.body, (0, 0), (0, 30*size), 2*size)
        self.corpse_shape.friction = 0.2
        self.corpse_shape.filter = pymunk.ShapeFilter(categories=0x1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 0x1)

      
class LeftLeg(Member) : 
    
    def __init__(self, size, x, y, mass, moment, friction):
        Member.__init__(self, mass, moment, x, y , friction)
        self.body.position =(x - 10*size, y - 60*size)
        
        self.left_leg_shape = pymunk.Segment(self.body, (10*size, 20*size), (0,0), 2*size)
        self.left_leg_shape.friction = friction
        self.left_leg_shape.filter = pymunk.ShapeFilter(categories=0x1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 0x1)  

    
class RightLeg(Member) : 
    
    def __init__(self, size, x, y, mass, moment, friction):
        Member.__init__(self, mass, moment, x, y , friction)
        self.body.position =(x + 10*size, y - 60*size)
        
        self.right_leg_shape = pymunk.Segment(self.body, (-10*size, 20*size), (0, 0), 2*size)
        self.right_leg_shape.friction = friction
        self.right_leg_shape.filter = pymunk.ShapeFilter(categories=0x1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 0x1)  

    
class LeftArm(Member) : 
    
    def __init__(self, size, x, y, mass, moment, friction):
        Member.__init__(self, mass, moment, x, y , friction)
        self.body.position =(x - 10*size, y - 30*size)
        
        self.left_arm_shape = pymunk.Segment(self.body, (10*size, 20*size), (0, 0), 2*size)
        self.left_arm_shape.friction = friction
        self.left_arm_shape.filter = pymunk.ShapeFilter(categories=0x1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 0x1)  


class RightArm(Member) : 
    
    def __init__(self, size, x, y, mass, moment, friction):
        Member.__init__(self, mass, moment, x, y , friction)
        self.body.position =(x + 10*size, y - 30*size)
        
        self.right_arm_shape = pymunk.Segment(self.body, (-10*size, 20*size), (0, 0), 2*size)
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