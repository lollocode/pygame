import pygame, sys, time, datetime
from random import randint

pygame.init()
screen_x = 600
screen_y = 480
px = (screen_x/2)-20
py = 400
bx = px+3
by = py-20
blato = 10
ex = 100
ey = 40
elato = 60
plato = 40
screen = pygame.display.set_mode((screen_x, screen_y))

pygame.display.set_caption("First Pygame Application")
back = pygame.image.load("./space.png")
play = pygame.image.load("./player.png")
bull = pygame.image.load("./bullet.png")
enem = pygame.image.load("./enemy.png")
points = 0
level = 1
speed = 1
char = []
pygame.font.init()
myfont = pygame.font.SysFont('arial', 20)

start_time = datetime.datetime.now()

def scritte():
    screen.fill([0,0,0])
    elapsed_time = datetime.datetime.now() - start_time
    textsurface = myfont.render("Tempo trascorso  "+str(elapsed_time), True, (255, 0, 0))
    punti = myfont.render("Il tuo punteggio "+ str(points), True,(255,0,0))
    livello = myfont.render("Livello "+ str(level), True,(255,0,0))
    screen.blit(back,(0,0))
    screen.blit(textsurface,(0,0))
    screen.blit(punti,(300,0))
    screen.blit(livello,(500,0))

def move():
    global by
    global ey,ex,points,speed
    by -= 10
    if by < 0:
        by = py-20
    ey += speed
    if points >= speed*5:
        speed += 1
    if ey > screen_y:
        print("hai perso")
        sys.exit()

class Entity:
    def __init__ (self,x,y,color,lato):
        self.x = x
        self.y = y
        self.color = color
        self.lato = lato
 

class Player(Entity):
    def __init__(self,x,y,color,lato):
        super().__init__(x,y,color,lato)
 

class Bullet(Entity):
    def __init__ (self,x,y,color,lato):
    	super().__init__(x,y,color,lato)
    
    def move (self):
        self.y -= self.lato/3
        self.draw()
        if(self.y<0):
        	self.y = p.y-self.lato


class Enemy(Entity):
    def __init__(self,x,y,color,lato):
        super().__init__(x,y,color,lato)

    def move(self):
        self.y += 1
        



p = Player((screen_x/2)-20,400,[255,255,255],40)
b = Bullet(p.x+15,p.y-10,[0,255,0],10)
e = Enemy(randint(0,screen_x-p.lato),20,[255,0,0],40)
char.append(p)
char.append(b)
char.append(e)

		
while True:
    scritte()
    screen.blit(play,(px,py))
    screen.blit(bull,(bx,by))
    screen.blit(enem,(ex,ey))
    move()
    if (bx +blato >= ex and bx <= ex+elato) and (by >= ey and by  <= ey+elato):
        ey = 20
        ex = randint(0,9)*elato
        points += 1
    if(e.x + e.lato >= p.x and e.x <= p.x+p.lato) and (e.y >= p.y and e.y < p.y+p.lato) or (e.y >= screen_y):
        print("hai perso")
        print("il tuo tempo:",elapsed_time)
        sys.exit()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    by -= plato
                    py -= plato
                if event.key == pygame.K_s and py < screen_y-plato:
                    by += plato
                    py += plato
                   
                if event.key == pygame.K_a and px > 0:
                    bx -= plato
                    px -= plato

                if event.key == pygame.K_d and px+plato < screen_x:
                    bx += plato
                    px += plato
    clock = pygame.time.Clock()
    clock.tick(60)
    pygame.display.update()