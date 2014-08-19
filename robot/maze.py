from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

if touch() == 'wall':
  if left_side() == 'wall':
    if right_side() == 'wall':
      turn(1)
      if touch == 'wall':
        turn(1)
        move()
    else:
      move()
  else:
    move()
else:
  move()    