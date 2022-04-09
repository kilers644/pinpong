from pygame import
game = True
clock = time.Clock() 
okno = display.set_mode((1250,620)) 
display.set_caption("Зомби дети")
ara = transform.scale(image.load("hon.png"),(1280,520)) 

class GameSprite(sprite.Sprite):
    def __init__(self, img, x,y):
        super().__init__()
        self.image = transform.scale(image.load(img), (100, 100)) 
        self.image = transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()   
        self.rect.x = x 
        self.rect.y = y
    def ris(self):
        okno.blit((self.image), (self.rect.x, self.rect.y))

class ship(GameSprite): 
    def control(self):
        knopka = key.get_pressed()
        if knopka[K_UP] and self.rect.y >0:
            self.rect.y -= 5
        if knopka[K_DOWN] and self.rect.y < 400:
            self.rect.y += 5
        if knopka[K_LEFT] and self.rect.x >0:
            self.rect.x -= 5
        if knopka[K_RIGHT] and self.rect.x < 1200:
            self.rect.x += 5

c = 'Забил игрок 1: 0'
d = 'Забил игрок 2: 0'
finish = False

font.init()

import pygame
import sys
 
WIN_WIDTH = 800
WIN_HEIGHT = 600
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
 
 
class Rocket:
   
    width_rocket = 20
    height_rocket = 50
 
    def __init__(self, surface, color):
        
        self.surf = surface
        self.color = color
        
        self.x = surface.get_width()//2 \
                 - Rocket.width_rocket//2
        self.y = surface.get_height()
 
    def fly(self):
        
        pygame.draw.rect(
            self.surf, self.color,
            (self.x, self.y,
             Rocket.width_rocket,
             Rocket.height_rocket))
        self.y -= 3
        
        if self.y < -Rocket.height_rocket:
            
            self.y = WIN_HEIGHT
 
 
sc = pygame.display.set_mode(
    (WIN_WIDTH, WIN_HEIGHT))
 

surf_left = pygame.Surface(
    (WIN_WIDTH//2, WIN_HEIGHT))
surf_left.fill(YELLOW)
 

surf_right = pygame.Surface(
    (WIN_WIDTH//2, WIN_HEIGHT))
surf_right.fill(WHITE)
 

sc.blit(surf_left, (0, 0))
sc.blit(surf_right, (WIN_WIDTH//2, 0))
 

rocket_left = Rocket(surf_left, YELLOW)
rocket_right = Rocket(surf_right, WHITE)
 

active_left = False
active_right = False
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.MOUSEBUTTONUP:
            
            if i.pos[0] < WIN_WIDTH//2:
                
                active_left = True
                active_right = False
            elif i.pos[0] > WIN_WIDTH//2:
                
                active_right = True
                active_left = False
 
    if active_left:
        
        surf_left.fill(YELLOW)
       
        rocket_left.fly()
      
        sc.blit(surf_left, (0, 0))
    elif active_right:
        surf_right.fill(WHITE)
        rocket_right.fly()
        sc.blit(surf_right, (WIN_WIDTH//2, 0))
 
    pygame.display.update()
    pygame.time.delay(20)
points1 = 0
points2 = 0
UI = font.SysFont(None,40)

geroi = ship('kora.png', 690,350)
pulya = pula('pulya.png', 1690,350)
pulya1 = pula('pulya.png', 1690,250)


while game:
    for i in event.get():  
        if i.type == QUIT: 
            game = False
        if i.type == KEYUP:
            if i.key == K_SPACE and pulya.rect.x > 1130:
                pulya.rect.x = geroi.rect.x 
                pulya.rect.y = geroi.rect.y + 40
            if i.key == K_SPACE and pulya1.rect.x > 1130:
                pulya1.rect.x = geroi.rect.x 
                pulya1.rect.y = geroi.rect.y - 40
    okno.blit(ara,(-1280+x1,0))
    okno.blit(ara2,(0+x1,0))
    okno.blit(ara3,(1280+x1,0)) 
    geroi.ris()
    geroi.control()
    pulya.letit()
    pulya1.letit()
    for i in pv:
        i.letit()
        if sprite.collide_rect(geroi,i):
            points -= 1
            lives -= 1
            i.rect.x = 0
            i.rect.y = 1500
    for i in vragi2:
        i.ris()
        if sprite.collide_rect(pulya,i):
            a += 1
            points += 1
            vragi2.remove(i)
        if sprite.collide_rect(pulya1,i):
            a += 1
            points += 1
        if pv[0].rect.x < 0:
            shuffle(vragi2)
            pv[0].rect.x = vragi2[0].rect.x
            pv[0].rect.y = vragi2[0].rect.y
    if points < 20 and len(vragi2)<5:
        for i in range(5):
            en = enemy('baby.png', 1200,i*100)
            vragi2.append(en)     
    c = 'Забил игрок 1:'+ str(points1)
    d = 'Забил игрок 2:'+ str(points2)
    ochki1 = UI.render(c,True,(255,255,0))
    ochki2 = UI.render(d,True,(255,255,0))
    okno.blit(ochki1,(30,30))
    okno.blit(ochki2,(1100,30))
    display.update()

font.init()
pisatel = font.SysFont(None, 70)
text = pisatel.render('Ты помер',True,(0,0,0))

while finish:
    for i in event.get():  
        if i.type == QUIT: 
            finish = False
    okno.fill((255,0,0))
    okno.blit(text,(500,250))
    display.update()
#pyinstaller --onefile gg.py = имя файла
