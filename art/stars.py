from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import sin, cos, pi

def star(x, y, c, rx, ry, spines):
  
  color(c)
  
  angle = 0
  
  for i in range(0, spines):
    x0 = x + (rx * cos(angle))
    y0 = y + (ry * sin(angle))
    
    line(x, y, x0, y0)
    
    angle = angle + (2 * pi / spines)

star(300, 300, "blue", 100, 150, 50)
star(600, 400, "purple", 200, 250, 100)
star(450, 200, "orange", 125, 175, 30)