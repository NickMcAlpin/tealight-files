from tealight.logo import (move, turn, color)

def c_square():
  for i in range(0,4):
    move(25)
    turn(90)
    color("black")
  
  
for x in range (0,8):
  for i in range(0,8):
    c_square()
    move(25)
  turn(90)
  move(25)
  turn(90)
  move(200)
  turn(180)