from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import sin, cos, pi

def star(x, y, c, size):
  
  color(c)
  
  angle = 0
  
  for i in range(0,2):
    x0 = x + (size * cos(angle))
    y0 = y + (size * sin(angle))
    
    line(x, y, x0, y0)
    

star(300, 300, "blue", 100)
star(600, 400, "purple", 200)
star(450, 200, "orange", 125)