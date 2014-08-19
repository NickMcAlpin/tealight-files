from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

def movement():
  move()
  while touch == 'wall':
    turn(1)
    move()
    
while 1:
  movement()