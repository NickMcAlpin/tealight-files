from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

def movement():
  if touch() == 'wall':
    if left_side() == 'wall':
      if right_side() == 'wall':
        turn(1)
        for touch() == 'wall':
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
  movement()