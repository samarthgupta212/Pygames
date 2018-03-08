import pygame,time
from random import choice,randint,randrange
pygame.init()
display_width=640
display_height=640
clock=pygame.time.Clock()
gamedisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('reversi')
black=(0,0,0)
wincolor=(randrange(0,255),0,randrange(0,255))
dark_red=(127,0,0)
red=(255,0,0)
dark_green=(0,127,0)
green=(0,255,0)
dark_blue=(0,50,255)
blue=(0,0,255)
dark_yellow=(127,127,0)
yellow=(255,255,0)
white=(255,255,255)
c=[]
for i in range(8):
    c.append(0)
    
box_width=50
box_height=50
n=8
x_margin=int((display_width-(box_width*8))/2)
y_margin=int((display_width-(box_height*8))/2)
arr=[
    (3,3),
    (3,4),
    (4,3),
    (4,4)
    ]

whitearr=[(3,3),(4,4)]
blackarr=[(3,4),(4,3)]
unusedarr=[]
for i in range(8):
    for j in range(8):
        unusedarr.append((i,j))

unusedarr.remove((3,3))
unusedarr.remove((3,4))
unusedarr.remove((4,3))
unusedarr.remove((4,4))

def usedcoor(x,y):
    for i in range(len(arr)):
        if arr[i][0]==x and arr[i][1]==y:
            return '1'
    return None

def turn(color):
    pygame.draw.rect(gamedisplay,blue,(display_width/2,display_height-100,600,100))
    displaytext=pygame.font.Font(None,50)
    if color==white:
        text=displaytext.render('White Turn',True,white)
    else:
        text=displaytext.render('Black Turn',True,black)
        
    gamedisplay.blit(text,(display_width/2,display_height-50))
    pygame.display.update()


def win(color,game):
    displaytext=pygame.font.Font(None,25+10)
    displaytext1=pygame.font.Font(None,50)
    if game==1:
        if color==black:
            text=displaytext.render('Black Won',True,wincolor)
        else:
            text=displaytext.render('White Won',True,wincolor)
        surf=text.get_rect()
        surf.center=(int(display_width/2),int(display_height/2))
    if game==0:
        if color==black:
            text=displaytext.render('You lost',True,wincolor)
            surf=text.get_rect()
            surf.center=(int(display_width/2),int(display_height/2))
        elif color==white:
            text=displaytext.render('You Won',True,wincolor)
            surf=text.get_rect()
            surf.center=(int(display_width/2),int(display_height/2))

    gamedisplay.blit(text,surf)
    text=displaytext1.render('Play Again',True,wincolor)
    surf=text.get_rect()
    surf.center=(int(display_width/2),int(display_height/2+50))
    gamedisplay.blit(text,surf)
    pygame.display.update()
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
                
            pos=pygame.mouse.get_pos()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if 240 < pos[0]<405 and 260+100<pos[1]<282+100:                 
                    done=True
                    newgame(game)
                    
    clock.tick(40)
    
def score(game):
    pygame.draw.rect(gamedisplay,blue,(0,0,400,100))
    displaytext=pygame.font.Font(None,50)
    text1=displaytext.render('White Score:'+str(len(whitearr)),True,black)
    text2=displaytext.render('Black Score:'+str(len(blackarr)),True,black)
    gamedisplay.blit(text1,(0,0))
    gamedisplay.blit(text2,(0,40))
    if len(whitearr)+len(blackarr)==64:
        if len(blackarr)>len(whitearr):
            win(black,game)
        else:
            win(white,game)
    pygame.display.update()
    
def computer(color):
    max=0
    circles=0
    b=[]
    for i in range(len(blackarr)):
        x=blackarr[i][0]
        y=blackarr[i][1]
        for j in range(1,n):
            if x+j>=n:
                break
            
            for k in range(len(whitearr)):
                if whitearr[k][0]==x+j and whitearr[k][1]==y:
                    circles+=1

            if circles==j:
                if circles>max:
                    if x+j+1!=n:
                        x1=x+j+1
                        y1=y
                        if usedcoor(x1,y1)==None:
                            max=circles
                            b.append((x1,y1))
                           
            else:
                break
       
        circles=0
        for j in range(1,n):
            if x-j<0:
                break
            for k in range(len(whitearr)):
                if whitearr[k][0]==x-j and whitearr[k][1]==y:
                    circles+=1

            if circles==j:
                if circles>max:     
                    if x-j-1>=0:
                        x1=x-j-1
                        y1=y
                        if usedcoor(x1,y1)==None:
                            max=circles
                            b.append((x1,y1))
            
            else:
                break
      
        circles=0
        for j in range(1,n):
            if y+j>=n:
                break
            for k in range(len(whitearr)):
                if whitearr[k][0]==x and whitearr[k][1]==y+j:
                    circles+=1

            if circles==j:
                if circles>max:
                    
                  
                    if y+j+1<n:
                        x1=x
                        y1=y+j+1
                        if usedcoor(x1,y1)==None:
                            max=circles
                            b.append((x1,y1))
                
            else:
                break
     
        circles=0
        for j in range(1,n):
            if y-j<0:
                break
            for k in range(len(whitearr)):
                if whitearr[k][0]==x and whitearr[k][1]==y-j:
                    circles+=1

            if circles==j:
                if circles>max:
                   
                     
                    if y-j-1>=0:
                        x1=x
                        y1=y-j-1
                        if usedcoor(x1,y1)==None:
                            max=circles
                            b.append((x1,y1))
                     
            else:
                break
  
        circles=0
        for j in range(1,n):
            if y+j>=n or x+j>=n:
                break
            for k in range(len(whitearr)):
                if whitearr[k][0]==x+j and whitearr[k][1]==y+j:
                    circles+=1

            if circles==j:
                if circles>max:
                    
                    
                    if x+j+1<n and y+j+1<n:
                        x1=x+j+1
                        y1=y+j+1
                        if usedcoor(x1,y1)==None:
                            max=circles
                            b.append((x1,y1))
                   
                       
            else:
                break
            
 
        circles=0
        for j in range(1,n):
            if x+j>=n or y-j<0:
                break
            
            for k in range(len(whitearr)):
                if whitearr[k][0]==x+j and whitearr[k][1]==y-j:
                    circles+=1

            if circles==j:
                if circles>max:
                  
                    
                    if x+j+1<n and y-j-1>=0:
                        x1=x+j+1
                        y1=y-j-1
                        if usedcoor(x1,y1)==None:
                            max=circles
                            b.append((x1,y1))
        
                break
       
        circles=0
        for j in range(1,n):
            if x-j<0 or y-j<0:
                break
            for k in range(len(whitearr)):
                if whitearr[k][0]==x-j and whitearr[k][1]==y-j:
                    circles+=1

            if circles==j:
                if circles>max:
                    
                
                    if x-j-1>=0 and y-j-1>=0:
                        x1=x-j-1
                        y1=y-j-1
                        if usedcoor(x1,y1)==None:
                            max=circles
                            b.append((x1,y1))
                                       
            else:
                break
            
            
        circles=0
        for j in range(1,n):
            if x-j<0 or y+j>=n:
               break
            
            for k in range(len(whitearr)):
                if whitearr[k][0]==x-j and whitearr[k][1]==y+j:
                    circles+=1

            if circles==j:
                if circles>max:
                    
                                               
                    if x-j-1>=0 and y+j+1<n:
                        x1=x-j-1
                        y1=y+j+1
                        if usedcoor(x1,y1)==None:
                            max=circles
                            b.append((x1,y1))
                       
                         
            else:
                break

    try:
        blackturn(b[len(b)-1][0],b[len(b)-1][1])
        unusedarr.remove((b[len(b)-1][0],b[len(b)-1][1]))

    except IndexError:
        p=choice(unusedarr)
        unusedarr.remove(p)
        blackturn(p[0],p[1])
        
def changecolor(x,y,color,a):
    
    circles=0
    d=0         
    for i in range(1,x+1):
        for j in range(len(arr)):
            
            if arr[j][0]==x-i and arr[j][1]==y:
                circles+=1
                
        if circles!=i:
            break
      
    if circles!=0:
            
        for i in range(1,circles+1):
            for j in range(len(a)):
                
                if a[j][0]==x-i and a[j][1]==y:
                    d+=1
                    break
                
            if d==1:
                for j in range(1,i):
                    a.append((x-j,y))
                    pygame.draw.circle(gamedisplay,color,(x_margin+50*(x-j)+25,y_margin+50*y+25),20)
                    pygame.time.wait(100)
                    if color==white:
                        for k in range(len(blackarr)):
                            if blackarr[k][0]==x-j and blackarr[k][1]==y:
                                del blackarr[k]
                                break
                                
                    if color==black:
                        for k in range(len(whitearr)):
                            if whitearr[k][0]==x-j and whitearr[k][1]==y:
                                del whitearr[k]
                                break
                                
                break

    rightchange(x,y,color,a)

def rightchange(x,y,color,a):

    circles=0
    d=0
    for i in range(x+1,n):
        for j in range(len(arr)):
            
            if arr[j][0]==i and arr[j][1]==y:
                circles+=1
                
        if circles!=i-x:
            break
          
    if circles!=0:
            
        for i in range(1,circles+1):
            for j in range(len(a)):
                
                if a[j][0]==x+i and a[j][1]==y:
                    d+=1
                    break
                
            if d==1:
                
                for j in range(1,i):
                    a.append((x+j,y))
                    pygame.draw.circle(gamedisplay,color,(x_margin+50*(x+j)+25,y_margin+50*y+25),20)
                    pygame.time.wait(100)
                    if color==white:
                        for k in range(len(blackarr)):
                            if blackarr[k][0]==x+j and blackarr[k][1]==y:
                                del blackarr[k]
                                break
                            
                    if color==black:
                        for k in range(len(whitearr)):
                            if whitearr[k][0]==x+j and whitearr[k][1]==y:
                                del whitearr[k]
                                break
                                
                break
    topchange(x,y,color,a)

def topchange(x,y,color,a):
    circles=0
    d=0
    for i in range(1,y+1):
        for j in range(len(arr)):
            
            if arr[j][0]==x and arr[j][1]==y-i:
                circles+=1
                
        if circles!=i:
            break
          
    if circles!=0:
            
        for i in range(1,circles+1):
            for j in range(len(a)):
                
                if a[j][0]==x and a[j][1]==y-i:
                    d+=1
                    break
                
            if d==1:
                
                for j in range(1,i):
                    a.append((x,y-j))
                    pygame.draw.circle(gamedisplay,color,(x_margin+50*x+25,y_margin+50*(y-j)+25),20)
                    pygame.time.wait(100)
                    if color==white:
                        for k in range(len(blackarr)):
                            if blackarr[k][0]==x and blackarr[k][1]==y-j:
                                del blackarr[k]
                                break
                            
                    if color==black:
                        for k in range(len(whitearr)):
                            if whitearr[k][0]==x and whitearr[k][1]==y-j:
                                del whitearr[k]
                                break
                                
                break

    bottomchange(x,y,color,a)
    
def bottomchange(x,y,color,a):
    circles=0
    d=0
    for i in range(y+1,n):
        for j in range(len(arr)):
            
            if arr[j][0]==x and arr[j][1]==i:
                circles+=1
                
        if circles!=i-y:
            break
          
    if circles!=0:
            
        for i in range(1,circles+1):
            for j in range(len(a)):
                
                if a[j][0]==x and a[j][1]==y+i:
                    d+=1
                    break
                
            if d==1:
                
                for j in range(1,i):
                    a.append((x,y+j))
                    pygame.draw.circle(gamedisplay,color,(x_margin+50*x+25,y_margin+50*(y+j)+25),20)
                    pygame.time.wait(100)
                    if color==white:
                        for k in range(len(blackarr)):
                            if blackarr[k][0]==x and blackarr[k][1]==y+j:
                                del blackarr[k]
                                break
                            
                    if color==black:
                        for k in range(len(whitearr)):
                            if whitearr[k][0]==x and whitearr[k][1]==y+j:
                                del whitearr[k]
                                break
                                
                break
    diagonaldown(x,y,color,a)
        
def diagonaldown(x,y,color,a):
    
    circles=0
    d=0
    for i in range(1,n):
        for j in range(len(arr)):
            if i<n and i>=0:
                if arr[j][0]==x+i and arr[j][1]==y+i:
                    circles+=1
                
        if circles!=i:
            break
          
    if circles!=0:
            
        for i in range(1,circles+1):
            for j in range(len(a)):
                
                if a[j][0]==x+i and a[j][1]==y+i:
                    d+=1
                    break
                
            if d==1:
                
                for j in range(1,i):
                    a.append((x+j,y+j))
                    pygame.draw.circle(gamedisplay,color,(x_margin+50*(x+j)+25,y_margin+50*(y+j)+25),20)
                    pygame.time.wait(100)
                    if color==white:
                        for k in range(len(blackarr)):
                            if blackarr[k][0]==x+j and blackarr[k][1]==y+j:
                                del blackarr[k]
                                break
                            
                    if color==black:
                        for k in range(len(whitearr)):
                            if whitearr[k][0]==x+j and whitearr[k][1]==y+j:
                                del whitearr[k]
                                break
                                

                break
    diagonalup(x,y,color,a)
    
def diagonalup(x,y,color,a):
    
    circles=0
    d=0
    for i in range(1,n):
        for j in range(len(arr)):
            if i<n and i>=0:
                if arr[j][0]==x-i and arr[j][1]==y-i:
                    circles+=1
                
        if circles!=i:
            break
      
    if circles!=0:
            
        for i in range(1,circles+1):
            for j in range(len(a)):
                
                if a[j][0]==x-i and a[j][1]==y-i:
                    d+=1
                    break
                
            if d==1:
                
                for j in range(1,i):
                    a.append((x-j,y-j))
                    pygame.draw.circle(gamedisplay,color,(x_margin+50*(x-j)+25,y_margin+50*(y-j)+25),20)
                    pygame.time.wait(100)
                    if color==white:
                        for k in range(len(blackarr)):
                            if blackarr[k][0]==x-j and blackarr[k][1]==y-j:
                                del blackarr[k]
                                break
                            
                    if color==black:
                        for k in range(len(whitearr)):
                            if whitearr[k][0]==x-j and whitearr[k][1]==y-j:
                                del whitearr[k]
                                break
                                
                break
            
    circles=0
    d=0
    for i in range(1,n):
        
        for j in range(len(arr)):
            if i<n and i>=0:
                if arr[j][0]==x-i and arr[j][1]==y+i:
                    circles+=1
                
        if circles!=i:
            break
    
    if circles!=0:
            
        for i in range(1,circles+1):
            for j in range(len(a)):
                
                if a[j][0]==x-i and a[j][1]==y+i:
                    d+=1
                    break
                
            if d==1:
                
                for j in range(1,i):
                    a.append((x-j,y+j))
                    pygame.draw.circle(gamedisplay,color,(x_margin+50*(x-j)+25,y_margin+50*(y+j)+25),20)
                    pygame.time.wait(100)
                    if color==white:
                        for k in range(len(blackarr)):
                            if blackarr[k][0]==x-j and blackarr[k][1]==y+j:
                                del blackarr[k]
                                break
                            
                    if color==black:
                        for k in range(len(whitearr)):
                            if whitearr[k][0]==x-j and whitearr[k][1]==y+j:
                                del whitearr[k]
                                break
                                
                break
    
    circles=0
    d=0
    for i in range(1,n):
        
        for j in range(len(arr)):
            if i<n and i>=0:
                if arr[j][0]==x+i and arr[j][1]==y-i:
                    circles+=1
                
        if circles!=i:
            break
          
    if circles!=0:
            
        for i in range(1,circles+1):
            for j in range(len(a)):
                
                if a[j][0]==x+i and a[j][1]==y-i:
                    d+=1
                    break
                
            if d==1:
                
                for j in range(1,i):
                    a.append((x+j,y-j))
                    pygame.draw.circle(gamedisplay,color,(x_margin+50*(x+j)+25,y_margin+50*(y-j)+25),20)
                    pygame.time.wait(100)
                    if color==white:
                        for k in range(len(blackarr)):
                            if blackarr[k][0]==x+j and blackarr[k][1]==y-j:
                                del blackarr[k]
                                break
                            
                    if color==black:
                        for k in range(len(whitearr)):
                            if whitearr[k][0]==x+j and whitearr[k][1]==y-j:
                                del whitearr[k]
                                break
                                
                break   

def whiteturn(x,y):

    arr.append((x,y))
    whitearr.append((x,y))
    pygame.draw.circle(gamedisplay,white,(x_margin+50*x+25,y_margin+50*y+25),20)
    changecolor(x,y,white,whitearr)
                            
            
def blackturn(x,y):
    
    blackarr.append((x,y))
    arr.append((x,y))
    
    pygame.draw.circle(gamedisplay,black,(x_margin+50*x+25,y_margin+50*y+25),20)
    changecolor(x,y,black,blackarr)
        
def lefttopcoor(boxx,boxy):
    left=x_margin+50*boxx
    top=y_margin+50*boxy
    return left,top

def pixeltocoor(x,y):
    for boxx in range(n):
        for boxy in range(n):
            left,top=lefttopcoor(boxx,boxy)
            pixel=pygame.Rect(left,top,50,50)
            if pixel.collidepoint(x,y):
                return boxx,boxy
    return None,None


def start():
    pygame.draw.circle(gamedisplay,white,(x_margin+50*4-25,y_margin+50*4-25),20)
    pygame.draw.circle(gamedisplay,white,(x_margin+50*5-25,y_margin+50*5-25),20)
    pygame.draw.circle(gamedisplay,black,(x_margin+50*4-25,y_margin+50*5-25),20)
    pygame.draw.circle(gamedisplay,black,(x_margin+50*5-25,y_margin+50*4-25),20)
    pygame.display.flip()

def intro():
    gamedisplay.fill(black)
    displaytext=pygame.font.Font(None,50)
    text=displaytext.render('Samarth Games Presents',True,white)
    surf=text.get_rect()
    surf.center=(int(display_width/2),int(display_height/2))
    gamedisplay.blit(text,surf)
    text1=displaytext.render('Flippy',True,white)
    surf1=text1.get_rect()
    surf1.center=(int(display_width/2),int(display_height/2+50))
    gamedisplay.blit(text1,surf1)
    displaytext=pygame.font.Font(None,25)
    text=displaytext.render('Hit any key to continue',True,green)
    surf=text.get_rect()
    surf.center=(int(display_width/2),int(display_height/2+100))
    gamedisplay.blit(text,surf)
    pygame.display.update()
    key_pressed=False
    while not key_pressed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                key_pressed=True
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                key_pressed=True
                choose()
                
    clock.tick(60)
    
def choose():
    gamedisplay.fill(black)
    displaytext=pygame.font.Font(None,50)
    text=displaytext.render('Choose Mode',True,white)
    surf=text.get_rect()
    surf.center=(int(display_width/2),int(display_height/2))
    gamedisplay.blit(text,surf)
    displaytext=pygame.font.Font(None,40)
    text1=displaytext.render('Vs Player',True,white)
    surf1=text1.get_rect()
    surf1.center=(int(display_width/2),int(display_height/2+50))
    gamedisplay.blit(text1,surf1)
    text=displaytext.render('Vs Computer',True,white)
    surf=text.get_rect()
    surf.center=(int(display_width/2),int(display_height/2+100))
    gamedisplay.blit(text,surf)
    pygame.display.update()
    click=False
    while not click:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                click=True
                pygame.quit()
                quit()

            if event.type==pygame.MOUSEBUTTONDOWN:
                if 380>pos[0]>260 and 357<pos[1]<379:
                    click=True
                    onlyhumangame=1
                    game_loop(onlyhumangame)
                    
                if 235<pos[0]<405 and 410<pos[1]<430:
                    click=True
                    onlyhumangame=0
                    game_loop(onlyhumangame)

        clock.tick(60)
        

def game_loop(game):

    gamedisplay.fill(blue)
    pygame.draw.rect(gamedisplay,green,(x_margin,y_margin,box_width*n,box_height*n))
    for i in range(9):
         pygame.draw.line(gamedisplay,black,(x_margin+box_width*i,y_margin),(x_margin+box_width*i,display_height-y_margin))

    for i in range(9):
        pygame.draw.line(gamedisplay,black,(x_margin,y_margin+box_height*i),(display_width-x_margin,y_margin+box_height*i))

    start()
    pygame.display.update()
    memory=False
    c=0
    while not memory:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            
            x=pygame.mouse.get_pos()[0]
            y=pygame.mouse.get_pos()[1]
            click=pygame.mouse.get_pressed()
            if click[0]==1:
                pygame.event.wait()
                c+=1
                x1=pixeltocoor(x,y)[0]
                y1=pixeltocoor(x,y)[1]
                if 540<x<640 and 17<y<29+1:
                    newgame(game)
                    
                if game==1:
                    if x1!=None and y1!=None:
                        if c%2!=0:
                            if usedcoor(x1,y1)!=None:
                                c+=1
                                
                            else:
                                turn(black)
                                whiteturn(x1,y1)
                            
                        else:
                            if usedcoor(x1,y1)!=None:
                                c+=1
                                
                            else:
                                turn(white)
                                blackturn(x1,y1)
                    else:
                        c+=1
                else:
                    if x1!=None:
                        if usedcoor(x1,y1)==None:
                            unusedarr.remove((x1,y1))
                            whiteturn(x1,y1)
                            computer(black)

            
        score(game)
        displaytext=pygame.font.Font(None,28)
        text=displaytext.render('New Game',True,white)
        surf=text.get_rect()
        surf.center=(int(display_width-50),(25))
        gamedisplay.blit(text,surf)
        clock.tick(30)
        
        pygame.display.update()
        
def newgame(game):
    global arr
    arr=[
    (3,3),
    (3,4),
    (4,3),
    (4,4)
    ]
    global whitearr
    global blackarr
    global unusedarr
    for i in range(8):
        for j in range(8):
            unusedarr.append((i,j))

    unusedarr.remove((3,3))
    unusedarr.remove((3,4))
    unusedarr.remove((4,3))
    unusedarr.remove((4,4))
    whitearr=[(3,3),(4,4)]
    blackarr=[(3,4),(4,3)]

    game_loop(game)

intro()
