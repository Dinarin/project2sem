import sys, pygame
import math

class Box:

  def __init__(self, width = 500, height = 500, a = 500.0, k = 2.0):
      pygame.init
      size = width, height = 500, 500
      speed = [2, 2]
      a = 500.0
      k = 2.0
      x, y = 100, 100
      g = 50.0
      clock = pygame.time.Clock()
      grav = -700.0
      first = Player(npoint, 0)
      first.update(dt)
      screen = pygame.display.set_mode(size)
      pygame.display.set_caption('ok')
      prev_t = pygame.time.get_ticks()
      tt = 0
      ar = pygame.PixelArray(screen)
      while True:
        delta = clock.tick(50) /1000.0
        for event in pygame.event.get():
          if event.type == pygame.QUIT: sys.exit()
          tt += delta
          print "%f %f %f" % (tt, vx, x)

class Vector:
  def __init__(self, x = 0.0, y = 0.0):
      self.length = sqrt(x*x+y*y)
      self.xc = x
      self.yc = y

  def __add__(self, v1):
    self.xc += v1.xc
    self.yc += v1.yc

  def __sub__(self, v1):
    self.xc -= v1.xc
    self.yc -= v1.yc

  def normcord(self):
    self.nx = self.xc/self.length
    self.ny = self.yc/self.length

  def __mul__(self, a):
    self.xc = self.xc * a
    self.yc = self.yc * a
  
  def dot(self, a):
    self.dot = self.xc * a.xc + self.yc * a.yc

class Player:
  def __init__(self, pos, v):
    self.pos = pos
    self.v = v

  def update(self, dt):
    self.v = self.v


world = Box()

first = Player(npoint, 0)
first.update(dt)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('ok')

prev_t = pygame.time.get_ticks()
tt = 0
ar = pygame.PixelArray(screen)
while True:
  delta = clock.tick(50) /1000.0
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
  tt += delta
  print "%f %f %f" % (tt, vx, x)

  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_LEFT]:
    vx -= delta * a
  if pressed[pygame.K_RIGHT]:
    vx += delta * a
  if pressed[pygame.K_UP]:
    if y == bottomline:
      vy = jumpheight
    if y <= bottomline:
      gt = 1000*delta
    else:
      gt = 0.0
      vy = 0.0




pos = Vector(startx, starty)
v = Vector(0.0, 0.0)
first = Player(pos, v) 
