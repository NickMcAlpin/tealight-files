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
        while touch() == 'wall':
          if left_side() != 'wall':
            turn(-1)
            move()
            if left_side() != 'wall' and right_side() != 'wall':
              turn(-1)
              move()
          else:
            if right_side() != 'wall':
              turn(1)
              move()
            else:
              turn(2)
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