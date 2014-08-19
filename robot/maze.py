from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

def move():
  if touch() == 'wall':
    if left_side() == 'wall':
      if right_side() == 'wall':
        turn(1)
        move()
        if touch == 'wall':
          turn(1)
          move()
      else:
        turn(1)
        move()
    else:
      turn(-1)
      move()
  else:
    move()
    
while 1:
  move()