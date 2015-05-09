import sys, pygame, math


class Vector:
    def __init__(self, x = 0.0, y = 0.0):
        sqrt = (x*x+y*y)**0.5
        self.length = sqrt
        self.x = x
        self.y = y

    def __add__(self, v1):
        self.x += v1.x
        self.y += v1.y

    def __sub__(self, v1):
        self.x -= v1.x
        self.y -= v1.y

    def normcord(self):
        self.nx = self.x/self.length
        self.ny = self.y/self.length

    def __mul__(self, a):
        self.x = self.x * a
        self.y = self.y * a
  
    def dot(self, a):
        self.dot = self.x * a.x + self.y * a.yc

class Player:
    def __init__(self, pos, v, horspeed):
        self.pos = pos
        self.v = v
        self.horspeed = horspeed
        self.baseline = 480.0
        self.jumpheight = -700

    def update(self, screen, delta, (g, k)):
        if self.pos.y <= self.baseline:
            gt = g*delta
        else:
            gt = 0.0
            self.v.y = 0.0
        self.v.x -= delta * self.v.x * k
        self.v.y -= delta * self.v.y * k - gt
        self.pos.x += self.v.x * delta
        self.pos.y += self.v.y * delta
        
        if self.pos.x < 20:
            if self.v.x < 0:
                self.v.x = -self.v.x
            self.pos.x = 20.0
        if self.pos.y < 20:
            if self.v.y < 0:
                self.v.y = -self.v.y
            self.pos.y = 20.0
        if self.pos.x > 480:
            if self.v.x > 0:
                self.v.x = -self.v.x
            self.pos.x = 480
        if self.pos.y > 480:
            if self.v.y > 0:
                self.v.y = 0
            self.pos.y = 480


        self.draw(screen)

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 200, 200), (int(self.pos.x), int(self.pos.y)), 20)


class Box:
    def __init__(self, width = 500, height = 500, npoint = Vector(50.0, 50.0)):
        pygame.init        
        
        #physics const

        self.k = 2.0
        self.g = 1000.0
        
        #player initialization

        basev = Vector(2.0, 2.0)
        first = Player(npoint, basev, 1000.0)
        
        #screen

        size = width, height = 500, 500
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption('ok')
        ar = pygame.PixelArray(self.screen)
        self.update(first)

    def update(self, player):
        clock = pygame.time.Clock()
        tt = 0
        while True:
            self.dt = clock.tick(50) /1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            tt += self.dt
            print "%f %f %f" % (tt, player.v.x, player.pos.x)
            self.keyboard(player)
            self.screen.fill((0, 25, 75))

            #static graphics go here


            player.update(self.screen, self.dt, (self.g, self.k))
            pygame.display.flip()

    def keyboard(self, player):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            player.v.x -= self.dt * player.horspeed
        if pressed[pygame.K_RIGHT]:
            player.v.x += self.dt * player.horspeed
        if pressed[pygame.K_UP]:
            if player.pos.y == player.baseline:
                player.v.y = player.jumpheight
            else:
                x = 1
    

world = Box() 
