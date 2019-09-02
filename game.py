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
back1 = pygame.image.load("./images/space1.png")

play = pygame.image.load("./images/starship1.png")
bull = pygame.image.load("./images/bullet.png")
enem = pygame.image.load("./images/enemy.png")
points = 0
level = 1
speed = 1


opt = ["e0"]
enemy = []


pygame.font.init()
myfont = pygame.font.SysFont('arcade classic', 23)

start_time = 0
elapsed_time = 0
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

class Entity:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Bullet(Entity):
    def __init__(self,x,y,start):
        self.start = start
        super().__init__(x,y)

    def move(self):
        self.y -= 15*level
        if self.y < 0:
            self.y = py-20
            self.start = self.x



class Enemy(Entity):
    def __init__(self,x,y):
        super().__init__(x,y)

def write(bol):
    global running
    scritta = 0
    screen.fill([0,0,0])
    pres = pygame.mouse.get_pressed()
    if bol == False:
        scritta = pygame.image.load("./images/gameover.png")    
    else: 
        scritta = pygame.image.load("./images/win.png") 
    screen.blit(scritta,(0,0 ))
    if pres[2] == 1:
        running = False
    




def lose():    
    write(False)
    

def win():
    write(True)


def init():
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
    
    clock = pygame.time.Clock()
    clock.tick(60)
    pygame.display.update()

def generator(n):
    opt.clear()
    for i in range(0,n):
        opt.append("e"+str(i))

def seeder(n):
    generator(n)
    enemy.clear()
    n = len(opt)+1
    for i in opt:
        i = Enemy((screen_x-elato)/n+int(i[1])*120,ey)
        enemy.append(i)
def draw():
    for i in enemy:
        screen.blit(enem,(i.x,i.y))

def move():
    global ey,ex,points,speed,game,running
    for i in enemy:
        i.y += (speed*level/3)/2
        if points >= speed*5:
            speed += 1
        if i.y > screen_y:
            game = False
            i.y = 20

def change(n):
    global back1,play
    play = pygame.image.load("./images/starship"+str(n)+".png")
    back1 = pygame.image.load("./images/space"+str(n)+".png")


def choose():
    global running, start_time,game 
    titolo = pygame.image.load("./images/titolo.png")
    screen.blit(titolo,(0,0))
    pres = pygame.mouse.get_pressed()
    if pres[0] == 1:
        start_time = datetime.datetime.now()
        running = True
        game = True


def end(suca):
    global level, points
    level = 1
    points = 0
    change(level)
    if suca == True:
        win()
    else:
        lose()


b = Bullet(bx,by,bx)
e = Enemy((screen_x-elato)/2,40)
enemy.append(e)
game = True
running = False
x = False
while True:
    init()
    choose()
    while running:
        init()
        end(x)
        while game:
            if level == 3 and points == 1:
                level = 1
                points = 0
                game = False
                x = True
            if points == 15:
                level += 1
                points = 0
                seeder(level)
                change(level)

            scritte()
            
            screen.blit(play,(px,py))
            screen.blit(bull,(b.start,b.y))
            b.move()
            draw()
            move()
            for i in enemy:
                if (b.start +blato >= i.x and b.start <= i.x+elato) and (b.y >= i.y and b.y  <= i.y+elato):
                    i.y = 20.
                    i.x = randint(0,9)*elato
                    points += 1
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            b.y -= plato
                            py -= plato
                        if event.key == pygame.K_s and py < screen_y-plato:
                            b.y += plato
                            py += plato
                           
                        if event.key == pygame.K_a and px > 0:
                            b.x -= plato
                            px -= plato

                        if event.key == pygame.K_d and px+plato < screen_x:
                            b.x += plato
                            px += plato
            clock = pygame.time.Clock()
            clock.tick(60)
            pygame.display.update()
