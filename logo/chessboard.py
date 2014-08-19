from tealight.logo import *

def w_square():
  for i in range(0,4):
    move(25)
    turn(90)
    color("black")
  
for x in range (0,8):
  for i in range(0,8):
    w_square()
    move(25)
  turn(90)
  move(25)
  turn(90)
  move(200)
  turn(-90)
  move(25)
  turn(90)