import pygame
import time
import random
pygame.init()

back=(255,250,205)
mw=pygame.display.set_mode((500,500))
mw.fill(back)
clock=pygame.time.Clock()
rocket_x=200
rocket_y=330
dx=3
dy=3
move_right=False
move_left=False
game = True
true = True


class Area():
    def __init__(self,x=0,y=0,widht=10,height=10,color=None):
        self.rect=pygame.Rect(x,y,widht,height)
        self.fill_color=back
        if color:
            self.fill_color=color

    def color(self,new_color):
        self.fill_color=new_color

    def fill(self):
        pygame.draw.rect(mw,self.fill_color,self.rect)


    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
    
    def colliderect(self,rect):
        return self.rect.colliderect(rect)


class Picture(Area):
    def __init__(self,filename,x=0,y=0,widht=10,height=10):
        Area.__init__(self,x=x,y=y,widht=widht,height=height,color=None)
        self.imege=pygame.transform.scale(pygame.image.load(filename),(widht,height))
    
    def draw(self):
        mw.blit(self.imege,(self.rect.x,self.rect.y))


def restart():
    global win,lose,ball,platform,quit1,restart1,start_x,start_y,monsters,count,lose1,game
    game = True
    win = Picture("winner.png",145,-150,200,150)
    lose = Picture("loser.png",145 ,-100,200,100)
    ball = Picture("ball.png",175,300,30,30)
    platform = Picture("plartforma.png",175,350,100,25)
    quit1= Picture("quit.png",125,200,100,100)
    restart1 = Picture("restart.png",275,200,100,100)
    lose1 = Picture("loser.png",150 ,-100,200,100)
    start_x=5
    start_y=5
    monsters =[]
    count=9
    for j in range(3):
        y=start_y+(55*j)
        x=start_x+(27.7*j)
        for i in range(count):
            monster = Picture("monster.png",x,y,40,40)
            monsters.append(monster)
            x+=55
        count-=1

restart()

while true:
    mw.fill(back)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            true = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                move_right=True
            if event.key==pygame.K_LEFT:
                move_left=True
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                move_right=False
            if event.key==pygame.K_LEFT:
                move_left=False
    
    if game:
        if move_right:
            if platform.rect.x + 3 + 100 < 505:
                platform.rect.x+=3
        if move_left:
            if platform.rect.x - 3 > -5:
                platform.rect.x-=3
        if ball.rect.y<0:
            dy*=-1
        if ball.rect.x>450 or ball.rect.x<0:
            dx*=-1
        ball.rect.x+=dx
        ball.rect.y+=dy
        if ball.rect.colliderect(platform.rect):
            dy*=-1

        for m in monsters:
            m.draw()
            if m.rect.colliderect(ball.rect):
                monsters.remove(m)
                m.fill()
                dy*=-1

        ball.draw()
        platform.draw()

    if len(monsters)==0:
        game = False
        if win.rect.y==150:
            back=(178,255,102)
            mw.fill(back)
            pygame.time.wait(3000)
            true=False
        
        else:
            back=(178,255,102)
            mw.fill(back)
            win.rect.y+=1
            win.draw()

    if ball.rect.y>600:
        game = False
        if lose.rect.y > 150:
            restart1.draw()
            quit1.draw()
            event_x, event_y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and quit1.collidepoint(event_x, event_y):
                true = False
            if event.type == pygame.MOUSEBUTTONDOWN and restart1.collidepoint(event_x, event_y):
                back=(255,250,205)
                mw.fill(back)
                restart()

        else:
            back=(255,102,102)
            mw.fill(back)
            lose.rect.y+=1
            lose.draw()

    pygame.display.update()
    clock.tick(80)