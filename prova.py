import pygame, sys

pygame.init()
screen_x = 680
screen_y = 480
screen = pygame.display.set_mode((screen_x, screen_y))
screen.fill([0,0,0])

pygame.display.set_caption("First Pygame Application")


class Player:
    def __init__ (self,x,y,color,lato):
        self.x = x
        self.y = y
        self.color = color
        self.lato = lato

    def draw(self):
        screen.fill([0,0,0])
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.lato,self.lato))

    def move (self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.y -= self.lato
                    self.draw()
                if event.key == pygame.K_s and self.y < 480-self.lato:
                    self.y += self.lato
                    self.draw()
                if event.key == pygame.K_a and self.x > 0:
                    self.x -= self.lato
                    self.draw()
                if event.key == pygame.K_d and self.x+self.lato < screen_x:
                    self.x += self.lato
                    self.draw()

		



p = Player((screen_x/2)-20,400,[255,255,255],40)
p.draw()
		
while True:
    clock = pygame.time.Clock()
    clock.tick(30)
    p.move()
    pygame.display.update()