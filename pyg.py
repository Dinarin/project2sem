import sys, pygame
import math
pygame.init()

size = width, height = 500, 500
speed = [2, 2]
a = 500.0
k = 2.0
x, y = 100, 100
vx, vy = 0, 0
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
pygame.display.set_caption('YAHOOOO')

prev_t = pygame.time.get_ticks()
tt = 0
ar = pygame.PixelArray(screen)
while True:
  delta = clock.tick(50) / 1000.0
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
  
  #t = pygame.time.get_ticks()
  #delta = (t - prev_t) / 1000.0
  #prev_t = t
  tt += delta
  print "%f %f %f" % (tt, vx, x)

  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_LEFT]:
    vx -= delta * a
  if pressed[pygame.K_RIGHT]:
    vx += delta * a
  if pressed[pygame.K_UP]:
    vy -= delta * a
  if pressed[pygame.K_DOWN]:
    vy += delta * a

  vx -= delta * vx * k
  vy -= delta * vy * k
  x += vx * delta
  y += vy * delta

  if x < 20:
    if vx < 0:
      vx = -vx
    x = 20
  if y < 20:
    if vy < 0:
      vy = -vy
    y = 20
  if x > 480:
    if vx > 0:
      vx = -vx
    x = 480
  if y > 480:
    if vy > 0:
      vy = -vy

  screen.fill((0, 25, 75))
  col = min(255, int(math.sqrt(vx ** 2 + vy ** 2)) + 100)
  pygame.draw.circle(screen, (col-100, col-25, col), (int(x), int(y)), 20)
  ar[int(x/10.0),int(y/10.0)] = (200,200,200)
  pygame.display.flip()

