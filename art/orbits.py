from tealight.art import (color, line, spot, circle, box, image, text, background, screen_width, screen_height)

# Almost working

x = 600
y = 400
vx = 0
vy = 0
ax = 0
ay = 0
grav = 1

power = 0.3

def handle_keydown(key):
  global ax, ay
  

  if key == "left":
    ax = -power
  elif key == "right":
    ax = power
  elif key == "up":
    ay = -power
  elif key == "down":
    ay = power

def handle_keyup(key):
  global ax, ay

  if key == "left" or key == "right":
    ax = 0
  elif key == "up" or key == "down":
    ay = 0
    
def handle_frame():
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)
  vx = vx + ax
  vy = vy + ay - grav
  
  if x <= 0 or x >= 900:
    vx = -vx
    ax = -0.8*ax
  else:
    x = x + vx
    
  if y <= 0 or y >= 900:
    vy = -vx
    ax = -0.8*ax
  else:
    y = y + vy
  
  color("blue")
  
  spot(x,y,8)