from tkinter import*
from math import sqrt
from random import randint, choice
from time import sleep
window=Tk()
c=Canvas(window, height=600, width=600, bg='orange')
c.pack()
class p:
    sscore = 0
    play=0
    g=0
    score=0
    upg = 0
    l=0
class player():
    def __init__(self, c, x, y):
        self.item=c.create_rectangle(x-10, y-10, x+10, y+10, fill='blue')
        self.x=x
        self.y=y
        self.health=15
        self.attack=3
        self.speed=5
        self.c=c
        self.range=125
        b=self
        def goo(e):
            e=e.keysym
            if e=="Up":
                b.walk(0, -b.speed)
            elif e=="Down":
                b.walk(0, b.speed)
            elif e=="Left":
                b.walk(-b.speed, 0)
            elif e=="Right":
                b.walk(b.speed, 0)
            elif e=="space":
                for i in p.g:
                    if not i.size==None:
                        if i.dis(b)<b.range:
                            i.health-=b.attack
                m=0
                for i in p.g:
                    if not i.size==None:
                        if i.health<1:
                            p.sscore+=1
                            p.upg+=1
                            p.l-=1
                            i.delete()
                    m=+1
            elif e=="z":
                b.upgrad(1)
            elif e=="x":
                b.upgrad(2)
            elif e=="c":
                b.upgrad(3)
            elif e=="v":
                b.upgrad(4)
        self.c.bind_all('<Key>', goo)
    def upgrad(self, i):
        if not p.upg == 0:
            if not( self.range>160 and i==4):
                p.upg-=1
                if i==1:
                    self.health+=1
                elif i==2:
                    self.speed+=1
                elif i==3:
                    self.attack+=1
                elif i==4:
                    self.range+=8
    def walk(self,x,y):
        self.c.move(self.item, x, y)
        self.x+=x
        self.y+=y
    def set(self, x, y):
        self.walk(x-self.x, y-self.y)
class ghost():
    def __init__(self, c, x, y):
        self.c=c
        self.item=self.c.create_rectangle(x-20, y-20, x+20, y+20, fill='white')
        self.text=self.c.create_text(x, y-25, fill='black')
        self.x=x
        self.y=y
        self.health=randint(how/2, how)/2
        self.attack=randint(how/2, how)/2
        self.speed=randint(how/2, how)
        self.range=150
        self.walk_chance=1000
        self.size=25
    def mell(self):
        self.c.delete(self.item)
        self.c.delete(self.text)
    def delete(self):
        self.mell()
        self.item=None
        self.x=None
        self.y=None
        self.health=None
        self.attack=None
        self.speed=None
        self.range=None
        self.walk_chance=None
        self.size=None
    def check(self):
        if self.health==None:
            self.mell()
    def hover(self, x, y):
        self.c.move(self.item, x, y)
        self.c.move(self.text, x, y)
        self.x+=x
        self.y+=y
    def dis(self, ano):
        x1, y1, x2, y2 = (int(self.x), int(self.y), int(ano.x), int(ano.y))
        return sqrt((x2-x1)**2+(y2-y1)**2)
    def Left(self, s):
        for i in range(self.speed*s):
            if not self.c.coords(self.item)[0]<1:
                self.hover(-1, 0)
    def Right(self,s):
        for i in range(self.speed*s):
            if not self.c.coords(self.item)[2]>599:
                self.hover(1, 0)
    def Up(self,s):
        for i in range(self.speed*s):
            if not self.c.coords(self.item)[1]<1:
                self.hover(0, -1)
    def Down(self,s):
        for i in range(self.speed*s):
            if not self.c.coords(self.item)[3]>599:
                self.hover(0, 1)
    def ran(self):
        i=randint(1,4)
        if i==1:
            self.Right(1)
        elif i==2:
            self.Left(1)
        elif i==3:
            self.Up(1)
        elif i==4:
            self.Down(1)
    def follow_x(self, ano):
        if ano.x>self.x:
            self.Right(2)
        else:
            self.Left(2)
    def follow_y(self, ano):
        if ano.y>self.y:
            self.Down(2)
        else:
            self.Up(2)
    def sets(self, x, y):
        self.hover(x-self.x, y-self.y)
    def upgrade(self):
        i = randint(1, 4)
        if i==1:
            self.health+=1
        elif i==2:
            self.speed+=1
        elif i==3:
            self.attack+=1
        elif i==4:
            self.range+=10
def update(i):
    for self in i:
        self.check()
        if not self.item==None:
            ig=self.health
            if len(str(ig).split('.'))==2:
                ig=int(ig)
            self.c.itemconfig(self.text, text=ig)
            if self.dis(p.play)<self.range:
                self.c.itemconfig(self.item, outline='red')
                if randint(1, int(self.walk_chance/4))==1:
                    self.follow_x(p.play)
                    self.follow_y(p.play)
            else:
                self.c.itemconfig(self.item, outline='black')
                if randint(1, self.walk_chance)==1:
                    self.ran()
            if self.dis(p.play)<self.size:
                p.play.health-=self.attack
                p.play.set(300, 300)
                self.upgrade()
def spawn():
    return ghost(c, choice([100, 500]), choice([100, 500]))


how=10
p.play=player(c, 300, 300)
p.score = c.create_text(0,0, text='0', font=('', 20), fill='white')
c.move(p.score, 300, 300)
def setup():
    p.g = []
    for i in range(50):
        p.g.append(spawn())
    p.l=50
setup()
v = False
while p.play.health>0:
    while p.l>0:
        update(p.g)
        c.update()
        if p.play.health<1:
            break
        c.itemconfig(p.score, text=str(p.sscore)+'                  '+str(p.play.health)+'                  '+str(p.upg)+'         '+str(how/10)+'''
























z=health, x=speed, c=attack, v=range''')
    for i in [0]:
        p.play.set(300, 300)
        how+=10
    setup()
print('GAME_OVER')
