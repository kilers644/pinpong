from pygame import*
game = True
clock = time.Clock() 
okno = display.set_mode((1200,500)) 
display.set_caption("Пин понг")

class igrok1(sprite.Sprite): 
    def __init__(self,x,y):
        super().__init__()
        self.image = Surface(( 10,100))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()  
        self.rect.x = x 
        self.rect.y = y
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))
    def control(self):
        knopka = key.get_pressed()
        if knopka[K_w] and self.rect.y >0:
            self.rect.y -= 1
        if knopka[K_s] and self.rect.y < 410:
            self.rect.y += 1
class igrok2(sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = Surface(( 10, 100))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect() 
        self.rect.x = x 
        self.rect.y = y 
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))
    def control(self):
        knopka = key.get_pressed()
        if knopka[K_UP] and self.rect.y >0:
            self.rect.y -= 1
        if knopka[K_DOWN] and self.rect.y < 410:
            self.rect.y += 1
class ball(sprite.Sprite): 
    def __init__(self, img, x, y):
        super().__init__()
        self.image = transform.scale(image.load(img), (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y)) 
dx = 1
dy = 1
c = 'Забил игрок 1: 0'
d = 'Забил игрок 2: 0'
finish = False
font.init()
pisatel = font.SysFont(None, 70)
font.init()
points1 = 0
points2 = 0
UI = font.SysFont(None,40)

myach = ball('ball.png', 580,220)
igrok1 = igrok1(10,0)
igrok2 = igrok2(1180,0)

while game:
    okno.fill((0,0,0))
    myach.rect.x += dx
    myach.rect.y -= dy
    if myach.rect.x > 1160:
        dx *= -1
        points1 += 1
    if myach.rect.y > 460:
        dy *= -1
    if myach.rect.x < 0:
        dx *= -1
        points2 += 1
    if myach.rect.y < 0:
        dy *= -1
    for i in event.get():  
        if i.type == QUIT: 
            game = False
    igrok1.control()
    igrok2.control()
    igrok1.ris()
    igrok2.ris()  
    myach.ris()
    if sprite.collide_rect(myach,igrok1):
        dx *= -1
        dy *= -1
    if sprite.collide_rect(myach,igrok2):
        dx *= -1
        dy *= -1
    if points1 >= 5:
        game = False
        finish = True
        text = pisatel.render('Игрок 1 победил',True,(0,0,0))
    if points2 >= 5:
        game = False
        finish = True
        text = pisatel.render('Игрок 2 победил',True,(0,0,0))
    c = str(points2)+':'+ str(points1)
    ochki1 = UI.render(c,True,(255,255,0))
    okno.blit(ochki1,(550,30))
    clock.tick(300)
    display.update()



while finish:
    for i in event.get():  
        if i.type == QUIT: 
            finish = False
    okno.fill((255,0,0))
    okno.blit(text,(480,250))
    display.update()
#pyinstaller --onefile gg.py = имя файла
