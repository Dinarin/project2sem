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

#class Sprite:
    #def __init__(self, )

class Player:
    def __init__(self, pos, v, horspeed, controls, color):
        self.pos = pos
        self.v = v
        self.horspeed = horspeed
        self.baseline = 480.0       
        self.jumpheight = -700 
        self.side = 1               #faced right
        self.controls = controls
        self.color = color
        self.movhor = 0

    def update(self, screen, delta, (g, k)):
      #  if self.side:
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
        pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), 20)


class Box:


    def __init__(self, width = 500, height = 500, npoint = Vector(50.0, 100.0)):
        pygame.init   

        controlsP1 = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP]
        controlsP2 = [pygame.K_a, pygame.K_d, pygame.K_w]
        red = (204, 0, 0)
        blue = (0, 128, 255)

        npoint2 = Vector(300, 100) 
        #physics const

        self.k = 2.0
        self.g = 1000.0
        
        #player initialization

        basev = Vector(0.0, 0.0)
        basev2 = Vector(0.0, 0.0)
        first = Player(npoint, basev, 500.0, controlsP1, blue)
        second = Player(npoint2, basev2, 700.0, controlsP2, red)
        
        #screen

        size = width, height = 500, 500
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption('ok')
        ar = pygame.PixelArray(self.screen)
        self.update(first, second)

    def update(self, player1, player2):
        clock = pygame.time.Clock()
        tt = 0
        while True:
            self.dt = clock.tick(50) /1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            tt += self.dt
            print "%f %f %f" % (tt, player1.v.x, player1.pos.x)
            print "     %f %f %f" % (tt, player2.v.x, player2.pos.x)
            self.keyboard(player1, player2)
            self.screen.fill((0, 25, 75))

            #static graphics go here


            player1.update(self.screen, self.dt, (self.g, self.k))
            player2.update(self.screen, self.dt, (self.g, self.k))
            pygame.display.flip()

    def keyboard(self, player1, player2):
        pressed = pygame.key.get_pressed()
        if pressed[player1.controls[0]]:
            player1.side = 0
            player1.v.x -= self.dt * player1.horspeed
        
        if pressed[player1.controls[1]]:
            player1.side = 1
            player1.v.x += self.dt * player1.horspeed

        if pressed[player1.controls[2]]:
            if player1.pos.y == player1.baseline:
                player1.v.y = player1.jumpheight
            else:
                x = 1

        if pressed[player2.controls[0]]:
            player2.side = 0
            player2.v.x -= self.dt * player2.horspeed

        if pressed[player2.controls[1]]:
            player2.side = 1
            player2.v.x += self.dt * player2.horspeed

        if pressed[player2.controls[2]]:
            if player2.pos.y == player2.baseline:
                player2.v.y = player2.jumpheight
            else:
                x = 1

    

world = Box() 
