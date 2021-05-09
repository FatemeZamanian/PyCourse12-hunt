import pygame
import random
pygame.init()
class FlyingThings:
    def __init__(self):
        self.y=random.randint(0,(game.height/2)-20)
        self.speed=1
        self.direction=random.choice(['rtl','ltr'])
        if self.direction=='ltr':
            self.x=-50
        elif self.direction=='rtl':
            self.x=game.width+50

    def show(self):
        if self.direction=='ltr':
            game.disp.blit(self.img,(self.x,self.y))
        elif self.direction=='rtl':
            game.disp.blit(pygame.transform.flip(self.img,True,False),[self.x,self.y])
    
    def fly(self):
        if self.direction=='ltr':
            self.x+=self.speed
        elif self.direction=='rtl':
            self.x-=self.speed

class Duck(FlyingThings):
    def __init__(self):
        super().__init__()
        self.img='images/duck.png'
        self.img=pygame.image.load(self.img)
        self.rect=self.img.get_rect()
    
    def kill(self):
        if pygame.Rect.colliderect(gun.rect,self.rect):
            return True
        else:
            return False
        
class Stork(FlyingThings):
    def __init__(self):
        super().__init__()
        self.img='images/stork.png'
        self.img=pygame.image.load(self.img)
        self.rect=self.img.get_rect()

    def kill(self):
        if pygame.Rect.colliderect(gun.rect,self.rect):
            return True
        else:
            return False

    

class Donkey(FlyingThings):
    def __init__(self):
        super().__init__()
        self.img='images/donkey.png'
        self.img=pygame.image.load(self.img)
        self.rect=self.img.get_rect()

    def kill(self):
        if pygame.Rect.colliderect(gun.rect,self.rect):
            return True
        else:
            return False

class Cloud(FlyingThings):
    def __init__(self):
        super().__init__()
        self.img='images/clouds.png'
        self.img=pygame.image.load(self.img)
        

class Gun:
    def __init__(self):
        self.x=game.width/2
        self.y=game.height/2
        self.image=pygame.image.load('images/shooter.png')
        self.score=0
        self.sound=pygame.mixer.Sound('sounds/shotgun.wav')
        self.shot=5
        self.rect=self.image.get_rect()

    def show(self):
        game.disp.blit(self.image,(self.x,self.y))

    def fire(self):
        self.sound.play()
        self.shot-=1
    
    def lose(self):
        if self.shot<=0:
            return True
        else:
            return False
        
class Game:
    def __init__(self):
        self.width=852
        self.height=480
        self.disp=pygame.display.set_mode((self.width,self.height))
        self.clock=pygame.time.Clock()
        self.background=pygame.image.load('images/bg.jpg')
        self.fps=30

    def play(self):
        global spd
        spd=1
        pygame.mouse.set_visible=False
        font=pygame.font.SysFont('comicsansms',35)
        duks=[]
        storks=[]
        donkeies=[]
        clouds=[]
        while True:
            spd+=0.005
            gun.rect.update(gun.x,gun.y,40,40)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit()
                if event.type==pygame.MOUSEMOTION:
                    gun.x=pygame.mouse.get_pos()[0]
                    gun.y=pygame.mouse.get_pos()[1]
                if event.type==pygame.MOUSEBUTTONDOWN:
                    gun.fire()
                    for duck in duks:
                        if duck.kill()==True:
                            gun.score+=1
                            gun.shot+=2
                            duks.remove(duck)
                            break
                    for stork in storks:
                        if stork.kill()==True:
                            gun.score+=1
                            gun.shot+=2
                            storks.remove(stork)
                            break
                    for donkey in donkeies:
                        if donkey.kill()==True:
                            gun.score+=1
                            gun.shot+=10
                            donkeies.remove(donkey)
        
            if random.random()<0.005:
                duks.append(Duck())
            if random.random()<0.004:
                storks.append(Stork())
            if random.random()<0.0002:
                donkeies.append(Donkey())
            if random.random()<0.009:
                clouds.append(Cloud())

            for duck in duks:
                duck.fly()
                duck.speed=spd
                
            for stork in storks:
                stork.fly()
                stork.speed=spd
            for donkey in donkeies:
                donkey.fly()
                donkey.speed=spd
            for cloud in clouds:
                cloud.fly()
                cloud.speed=spd
            self.disp.blit(self.background,[0,0])
            pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
            for duck in duks:
                duck.show()
                duck.rect.update(duck.x,duck.y,30,30)
            for stork in storks:
                stork.show()
                stork.rect.update(stork.x,stork.y,30,30)
            for donkey in donkeies:
                donkey.show()
                donkey.rect.update(donkey.x,donkey.y,50,50)
            for cloud in clouds:
                cloud.show()
            gun.show()
            txt_score=font.render('Score: '+str(gun.score),True,(255,215,0))
            self.disp.blit(txt_score,(226,370))
            txt_shot=font.render('Shot: '+str(gun.shot),True,(255,215,0))
            self.disp.blit(txt_shot,(480,370))
            if gun.lose()==True:
                img_lose=pygame.image.load('images/GameOver.jpg')
                self.disp.blit(img_lose,[0,0])
            pygame.display.update()
            self.clock.tick(self.fps)

if __name__=='__main__':
    game=Game()
    gun=Gun()
    game.play()
    

