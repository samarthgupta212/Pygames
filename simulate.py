import pygame
from random import choice,randint
pygame.init()
pygame.mixer.init()
display_width=640
display_height=480
clock=pygame.time.Clock()
gamedisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('memory game')
black=(0,0,0)
dark_red=(127,0,0)
red=(255,0,0)
dark_green=(0,127,0)
green=(0,255,0)
dark_blue=(0,0,127)
blue=(0,0,255)
dark_yellow=(127,127,0)
yellow=(255,255,0)
white=(255,255,255)

colours=(yellow,blue,red,green)

beep=pygame.mixer.Sound('C:\Users\Samarth Gupta\Downloads\Beep_Short.mp3')

def notplay(text):
    play=pygame.font.Font(None,25)
    play1=play.render(text,True,red)
    gamedisplay.blit(play1,(display_width/4+30,display_height/2+50))
    pygame.display.update()
    
def playagain(text):
    play=pygame.font.Font(None,50)
    play1=play.render(text,True,green)
    gamedisplay.blit(play1,(display_width/8,display_height/2))
    pygame.display.update()

def score(level):
    scoretext=pygame.font.Font(None,30)
    scored=scoretext.render('Level:'+str(level-1),True,white)
    gamedisplay.blit(scored,(0,0))
    

def r(bgcolor):
    pygame.draw.rect(gamedisplay,bgcolor,(0,0,100,50))
    return

def animation(color,x,y,speed,level):
    
    
    r,g,b=color
    flashsurf=pygame.Surface((235,180))
    flashsurf=flashsurf.convert_alpha()
    beep.play()
    
    for alpha in range(0,255,speed):
        
        flashsurf.fill((r,g,b,alpha))
        gamedisplay.blit(flashsurf,(x,y))
        pygame.display.update()
        clock.tick(30)

    if r==255:
        r=127
    if g==255:
        g=127
    if b==255:
        b=127
        
    for alpha in range(255,0,-speed):

        flashsurf.fill((r,g,b,alpha))
        gamedisplay.blit(flashsurf,(x,y))
        pygame.display.update()
        clock.tick(30)
        
    return

def lefttopcoor(boxx,boxy):
    left=75+255*boxx
    top=50+200*boxy
    return left,top

def pixeltocoor(x,y):
    for boxx in range(2):
        for boxy in range(2):
            left,top=lefttopcoor(boxx,boxy)
            pixel=pygame.Rect(left,top,235,180)
            if pixel.collidepoint(x,y):
                return boxx,boxy
    return None,None                      

def board(level,speed,bgcolor):
        
         
        arr=[]
        gamedisplay.fill(bgcolor)
        pygame.draw.rect(gamedisplay,dark_yellow,(75,50,235,180))
        pygame.draw.rect(gamedisplay,dark_blue,(display_width/2+10,50,235,180))
        pygame.draw.rect(gamedisplay,dark_red,(75,display_height/2+10,235,180))
        pygame.draw.rect(gamedisplay,dark_green,(display_width/2+10,display_height/2+10,235,180))
        pygame.display.update()
        poscolor=[]
        for color in colours:
            if color==yellow:
                x=75
                y=50
            if color==blue:
                x=330
                y=50
            if color==red:
                x=75
                y=250
            if color==green:
                x=330
                y=250

            poscolor.append((color,x,y))

        for i in range(level):
            p=choice(poscolor)
            arr.append(p[0])
            print arr
            animation(p[0],p[1],p[2],speed,level)

        return arr
                       
def game_loop(level,speed):
    
    bgcolor=(randint(0,255),randint(0,255),randint(0,255))
    memory=False
    arr=board(level,speed,bgcolor)
    c=0
    result=0      
    poscolor=[]
    for color in colours:
        if color==yellow:
            x=0
            y=0
        if color==blue:
            x=1
            y=0
        if color==red:
            x=0
            y=1
        if color==green:
            x=1
            y=1

        poscolor.append((color,x,y))
        
    while not memory:
        
        r(bgcolor)
        score(level)
        pygame.display.update()
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                memory=True
                pygame.quit()
                quit()
            
            mousex=pygame.mouse.get_pos()[0]
            mousey=pygame.mouse.get_pos()[1]
            x=pixeltocoor(mousex,mousey)[0]
            y=pixeltocoor(mousex,mousey)[1]
            click=pygame.mouse.get_pressed()
            if click[0]==1:
                
                pygame.event.wait()
                if x!=None and y!=None:
                    c+=1
                    if c<=len(arr):
                        
                    
                        left,top=lefttopcoor(x,y)
                        for i in range(4):
                            if x==poscolor[i][1] and y==poscolor[i][2]:
                                animation(poscolor[i][0],left,top,speed,level)
                                if arr[c-1]==poscolor[i][0]:
                                    result+=1
                                    print result
                                        
            if c==len(arr):
                if result==level:
                    print 'success'
                    game_loop(level+1,speed+5)
                else: 
                    playagain('Press Any Key To Continue')
                    notplay('Press Esc to Quit')
                    if event.type==pygame.KEYDOWN:

                        if event.key!=pygame.K_ESCAPE:
                            game_loop(2,50)                

                        else:
                            pygame.quit()
                            quit()
            else:
                if event.type==pygame.KEYDOWN:

                        if event.key!=pygame.K_ESCAPE:
                            game_loop(2,50)                

                        else:
                            pygame.quit()
                            quit()
            
                 
        clock.tick(30)              

game_loop(2,25)
python.quit()
quit()
