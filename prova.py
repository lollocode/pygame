import pygame, sys

pygame.init()
screen_x = 680
screen_y = 480
screen = pygame.display.set_mode((screen_x, screen_y))

pygame.display.set_caption("First Pygame Application")


char = []

class Entity:
    def __init__ (self,x,y,color,lato):
        self.x = x
        self.y = y
        self.color = color
        self.lato = lato
 

    def draw(self):
        for i in char:
            pygame.draw.rect(screen,i.color,(i.x,i.y,i.lato,i.lato))



class Player(Entity):
    def __init__(self,x,y,color,lato):
        super().__init__(x,y,color,lato)
 

class Bullet(Entity):
    def __init__ (self,x,y,color,lato):
    	super().__init__(x,y,color,lato)
    
    def move (self):
        pygame.draw.rect(screen,[0,0,0],(self.x,self.y,self.lato,self.lato))
        self.y -= self.lato
        self.draw()
        if(self.y<0):
        	self.y = p.y-10




p = Player((screen_x/2)-20,400,[255,255,255],40)
b = Bullet(p.x+15,p.y-10,[0,255,0],10)
char.append(p)
char.append(b)

		
while True:
    screen.fill([0,0,0])
    p.draw()
    b.move()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    b.y -= p.lato
                    p.y -= p.lato
                    p.draw()
                if event.key == pygame.K_s and p.y < 480-p.lato:
                    b.y += p.lato
                    p.y += p.lato
                    p.draw()
                   
                if event.key == pygame.K_a and p.x > 0:
                    b.x -= p.lato
                    p.x -= p.lato
                    p.draw()

                if event.key == pygame.K_d and p.x+p.lato < screen_x:
                    b.x += p.lato
                    p.x += p.lato
                    p.draw()
    clock = pygame.time.Clock()
    clock.tick(60)
    pygame.display.update()