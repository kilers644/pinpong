from pygame import*
from random import*
game = True
clock = time.Clock() 
okno = display.set_mode((1250,620)) 
display.set_caption("Зомби дети")
ara = transform.scale(image.load("hon.png"),(1280,520)) 
ara2 = transform.scale(image.load("hon.png"),(1280,520)) 
ara3 = transform.scale(image.load("hon.png"),(1280,520)) 

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

class pula(sprite.Sprite):
    def __init__(self, img, x,y):
        super().__init__()
        self.image = transform.scale(image.load(img), (50, 100))
        self.rect = self.image.get_rect()   
        self.rect.x = x 
        self.rect.y = y
    def letit(self):
        okno.blit((self.image), (self.rect.x, self.rect.y))
        self.rect.x += 10

class pulavrags(sprite.Sprite):
    def __init__(self, img, x,y):
        super().__init__()
        self.image = transform.scale(image.load(img), (50, 100)) 
        self.rect = self.image.get_rect()   
        self.rect.x = x 
        self.rect.y = y
    def letit(self):
        okno.blit((self.image), (self.rect.x, self.rect.y))
        self.rect.x -= 5

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

points = 25
class enemy(GameSprite):
    def taran(self):
        self.ris()
        self.rect.x -= 5
        if self.rect.x < 0:
            global points
            points -= 5
            self.rect.x = 1200
            self.rect.y = randint(0,360)

pv = [pulavrags('pulya.png', 1690,350)]

#mixer.init()
#fonov = mixer.Soand('Sinfonia 3.mp3')
#fonov.set_volume(0.5)
#fonov.play()

musicon = 1

a = 0
b = "Убито зомби-детей: 0"
c = 'Жизни: 5'
d = 'Очки: 25'
e = randint(0,3)
x1 = 0
finish = False

font.init()
lives = 5
UI = font.SysFont(None,40)

geroi = ship('kora.png', 690,350)
pulya = pula('pulya.png', 1690,350)
pulya1 = pula('pulya.png', 1690,250)
vragi = [
enemy('baby.png', 1200,1360),
enemy('baby.png', 1200,1360),
enemy('baby.png', 1200,1360)]

#v = mixer.Sound('srelba.ogg')

vragi2 = []
for i in range(5):
    en = enemy('baby.png', 1200,i*100)
    vragi2.append(en)

while game:
#    if musicon == 1:
#        mixer.music.unpause()
#    else:
#        mixer.music.pause()
    for i in event.get():  
        if i.type == QUIT: 
            game = False
        if i.type == KEYUP:
            if i.key == K_p:
                if musicon == 1:
                    musicon = 0
                else:
                    musicon = 1
        if i.type == KEYUP:
            if i.key == K_SPACE and pulya.rect.x > 1130:
#                v.play()
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
    b = 'Убито зомби-детей: '+ str(a)   
    c = 'Жизни: '+ str(lives)
    d = 'Очки:'+ str(points)
    zhizni = UI.render(c,True,(255,255,0))
    ochki = UI.render(d,True,(255,255,0))
    kills = UI.render(b,True,(255,255,0))
    okno.blit(zhizni,(1100,30))
    okno.blit(kills,(30,30))
    okno.blit(ochki,(500,30))
    for i in vragi:
        i.taran()
        if sprite.collide_rect(pulya,i):
            i.rect.x = 1200 
            i.rect.y = randint(0,360)
            a += 1
            points += 1
        if sprite.collide_rect(pulya1,i):
            i.rect.x = 1200 
            i.rect.y = randint(0,360)
            a += 1
            points += 1
        if sprite.collide_rect(geroi,i):
            i.rect.x = 1200
            i.rect.y = randint(0,450)
            lives -= 1
            points-=1
        if lives < 1 or points < 1:
            game = False
            finish = True
    x1 -= 1
    if x1> 1279:
        x1 =0
    if x1< -1279:
        x1 =0   
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
