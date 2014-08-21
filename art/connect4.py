from tealight.art import *

def rectangle(x, y, width, height):
  line(x, y, width, y)
  line(x, height, width, height)
  line(width, y, width, height)
  line(x, y, x, height)
  
rectangle(100,100,100,100)