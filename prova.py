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
ex = 0
ey = 40
elato = 60
plato = 40
screen = pygame.display.set_mode((screen_x, screen_y))

pygame.display.set_caption("First Pygame Application")
back1 = pygame.image.load("./space1.png")

play = pygame.image.load("./starship.png")
bull = pygame.image.load("./bullet.png")
enem = pygame.image.load("./enemy.png")
points = 0
level = 1
speed = 1


opt = ["e0"]
enemy = []


pygame.font.init()
myfont = pygame.font.SysFont('arial', 20)

start_time = datetime.datetime.now()

def scritte():
    screen.fill([0,0,0])
    elapsed_time = datetime.datetime.now() - start_time
    textsurface = myfont.render("Tempo trascorso  "+str(elapsed_time), True, (255, 0, 0))
    punti = myfont.render("Il tuo punteggio "+ str(points), True,(255,0,0))
    livello = myfont.render("Livello "+ str(level), True,(255,0,0))
    screen.blit(back1,(0,0))
    screen.blit(textsurface,(0,0))
    screen.blit(punti,(300,0))
    screen.blit(livello,(500,0))

class Enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def generator(n):
    opt.clear()
    for i in range(0,n):
        opt.append("e"+str(i))

def seeder(n):
    generator(n)
    enemy.clear()
    for i in opt:
        i = Enemy(int(i[1])*100,ey)
        enemy.append(i)
def draw():
    for i in enemy:
        screen.blit(enem,(i.x,i.y))

def move():
    global by
    global ey,ex,points,speed
    by -= 10*level
    if by < 0:
        by = py-20
    for i in enemy:
        i.y += speed/2
        if points >= speed*5:
            speed += 1
        if i.y > screen_y:
            print("hai perso")
            sys.exit()

def change(n):
    global back1,play
    play = pygame.image.load("./starship"+str(n)+".png")
    back1 = pygame.image.load("./space"+str(n)+".png")
    



e = Enemy(0,40)
enemy.append(e)

while True:
    if points == 15:
        level += 1
        points = 0
        seeder(level)
        change(level)
    scritte()
    
    screen.blit(play,(px,py))
    screen.blit(bull,(bx,by))
    draw()
    move()
    for i in enemy:
        if (bx +blato >= i.x and bx <= i.x+elato) and (by >= i.y and by  <= i.y+elato):
            i.y = 20
            i.x = randint(0,9)*elato
            points += 1
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