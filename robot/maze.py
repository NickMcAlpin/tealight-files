from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

while 1:
  if left_side() != 'wall':
    turn(-1)
    move()
  elif right_side() != 'wall':
    turn(1)
    move()
  else:
    turn(2)
    move()
  