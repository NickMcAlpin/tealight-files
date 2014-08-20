from tealight.logo import *
# Creates chessboard

def c_wsquare():
  for i in range(0,4):
    move(25)
    turn(90)
    color("black")
    
def c_bsquare():
  for i in range(0,4):
    move(25)
    turn(90)
    color("black")
  
  
for x in range (0,8):
  for i in range(0,8):
    c_wsquare()
    move(25)
  turn(90)
  move(25)
  turn(90)
  move(200)
  turn(180)