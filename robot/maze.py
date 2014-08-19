from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

def movement():
  move()
  while touch() == 'wall':
    if left_side() != 'wall':
      turn(-1)
      move()
    if left_side() != 'wall' and right_side() != 'wall':
      turn(-1)
      move()
    else:
      turn(2)
      move()
    
while 1:
  movement()