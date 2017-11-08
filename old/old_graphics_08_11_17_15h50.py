        
def add_env(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    
    body.position = (0,50)
    env = pymunk.Segment(body, (0,0), (600.0,0), 50.0)
    env.color = 34,139,34
    env.friction = 0.2
    space.add(env, body)
    return env

def add_stickman(space, size, x, y):
    right_leg_body = pymunk.Body(10, 2000)
    right_leg_body.position = (x,y - 40*size)
    right_leg = pymunk.Segment(right_leg_body, (0, 0), (10*size, -20*size), 2*size)
    right_leg.friction = 0.2
    right_leg.filter = pymunk.ShapeFilter(categories=0x1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 0x1)
    space.add(right_leg_body, right_leg)
    
    left_leg_body = pymunk.Body(10, 2000)
    left_leg_body.position = (x, y - 40*size) 
    left_leg = pymunk.Segment(left_leg_body, (0, 0), (-10*size, -20*size), 2*size)
    left_leg.friction = 0.2
    left_leg.filter = pymunk.ShapeFilter(categories=0x1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 0x1)
    space.add(left_leg_body, left_leg)
    
    right_arm_body = pymunk.Body(10, 2000)
    right_arm_body.position = (x,y - 10*size)
    right_arm = pymunk.Segment(right_arm_body, (0, 0), (10*size, -20*size), 2*size)
    right_arm.friction = 0.2
    right_arm.filter = pymunk.ShapeFilter(categories=0x1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 0x1)
    space.add(right_arm_body, right_arm)
    
    left_arm_body = pymunk.Body(10, 2000)
    left_arm_body.position = (x,y - 10*size)
    left_arm = pymunk.Segment(left_arm_body, (0, 0), (-10*size, -20*size), 2*size)
    left_arm.friction = 0.2
    left_arm.filter = pymunk.ShapeFilter(categories=0x1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 0x1)
    space.add(left_arm_body, left_arm)
    
    corpse_body = pymunk.Body(10, 2000)
    corpse_body.position = (x,y - 40*size)
    
    corpse = pymunk.Segment(corpse_body , (0, 0), (0, 30*size), 2*size)
    corpse.friction = 0.2
    corpse.filter = pymunk.ShapeFilter(categories=0x1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 0x1)
    
    head = pymunk.Circle(corpse_body, 10*size, (0,38*size))
    head.friction = 0.2
    head.filter = pymunk.ShapeFilter(categories=0x1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 0x1)  
    
    space.add(corpse_body, corpse, head)
    
    pin_a = pymunk.PinJoint(right_arm_body, corpse_body, (0, 0), (0, 30*size))
    
    pin_b = pymunk.PinJoint(left_arm_body, corpse_body, (0, 0), (0, 30*size))
    
    pin_c = pymunk.PinJoint(right_leg_body, corpse_body, (0, 0), (0, 0))
    
    pin_d = pymunk.PinJoint(left_leg_body, corpse_body, (0, 0), (0, 0))
    
    
    
    space.add(pin_a, pin_b, pin_c, pin_d)
    
    return head
    
