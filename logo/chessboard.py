from tealight.logo import *

def w_square():
  for i in range(0,4):
    move(25)
    turn(90)
    color("black")
  
for i in range(0,8):
  w_square()
  move(-25)