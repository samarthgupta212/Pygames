import pygame,random
pygame.init()
display_width=640
display_height=480
box_width=40
box_height=40
line_width=5
x_box=10
y_box=7
x_margin=((display_width-(x_box*(box_width+line_width)))/2)
y_margin=((display_height-(y_box*(box_height+line_width)))/2)
gamedisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('memory game')
black=(0,0,0)
white=(255,255,255)
gray=(0,127,127)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
orange=(255,128,0)
cyan=(0,255,255)

clock=pygame.time.Clock()

diamond='diamond'
line='line'
square='square'
oval='oval'
circle='circle'

shapes=(diamond,square,oval,circle,line)
colours=(black,white,gray,red,blue,orange,cyan)

half=int(box_width*0.5)
quarter=int(box_width*0.25)

def scored(score):
    font=pygame.font.Font('freesansbold.ttf',40)
    scoretext=font.render('Score:'+str(score),False,black)
    gamedisplay.blit(scoretext,(0,0))

def r():
    pygame.draw.rect(gamedisplay,red,(0,0,200,50))
    
def reveal(i,j,colour,shape):
    
    if shape=='diamond':
        pygame.draw.polygon(gamedisplay,colour,((i*(box_width+line_width)+x_margin+quarter,j*(box_width+line_width)+y_margin+half),(i*(box_width+line_width)+x_margin+half,j*(box_width+line_width)+y_margin+quarter),(i*(box_width+line_width)+x_margin+half+quarter,j*(box_width+line_width)+y_margin+half),(i*(box_width+line_width)+x_margin+half,j*(box_width+line_width)+quarter+half+y_margin)))
        
    if shape=='circle':
         pygame.draw.circle(gamedisplay,colour,(i*(box_width+line_width)+x_margin+half,j*(box_width+line_width)+y_margin+half),quarter)
 

    if shape=='square':
        pygame.draw.rect(gamedisplay,colour,(i*(box_width+line_width)+x_margin+quarter,j*(box_width+line_width)+y_margin+quarter,half,half))
        

    if shape=='oval':
        pygame.draw.ellipse(gamedisplay,colour,(i*(box_width+line_width)+x_margin+quarter,j*(box_width+line_width)+y_margin+quarter,half+quarter,half))

def usedcoordinates(arr,x,y):
    for i in range(len(arr)):
        if arr[i][0]==x and arr[i][1]==y:
            return '1'
            return None
            
        
def getboard():
    icons=[]
    for colour in colours:
        for shape in shapes:
            icons.append((colour,shape))

    n=int(x_box*y_box/2)
    icons=icons[:n]*2
    random.shuffle(icons)
    
    board=[]
    for i in range(x_box):
        column=[]
        for j in range(y_box):
            column.append(icons[0])
            del icons[0]
        board.append(column)

    a=[]
    for i in range(x_box):
        for j in range(y_box):
            a.append((i,j,board[i][j][0],board[i][j][1]))
            if board[i][j][1]=='diamond':
                pygame.draw.polygon(gamedisplay,board[i][j][0],((i*(box_width+line_width)+x_margin+quarter,j*(box_width+line_width)+y_margin+half),(i*(box_width+line_width)+x_margin+half,j*(box_width+line_width)+y_margin+quarter),(i*(box_width+line_width)+x_margin+half+quarter,j*(box_width+line_width)+y_margin+half),(i*(box_width+line_width)+x_margin+half,j*(box_width+line_width)+quarter+half+y_margin)))
                
                
            elif board[i][j][1]=='circle':
                pygame.draw.circle(gamedisplay,board[i][j][0],(i*(box_width+line_width)+x_margin+half,j*(box_width+line_width)+y_margin+half),quarter)
              
                
            elif board[i][j][1]=='square':
                pygame.draw.rect(gamedisplay,board[i][j][0],(i*(box_width+line_width)+x_margin+quarter,j*(box_width+line_width)+y_margin+quarter,half,half))
               
    
            elif board[i][j][1]=='oval':
                pygame.draw.ellipse(gamedisplay,board[i][j][0],(i*(box_width+line_width)+x_margin+quarter,j*(box_width+line_width)+y_margin+quarter,half+quarter,half))
                
    return a
    
def line():
    gamedisplay.fill(red)
    pygame.draw.rect(gamedisplay,green,(x_margin,y_margin,x_box*(box_width+line_width),y_box*(box_height+line_width)))
    
    for line1 in range(x_box+1):
        pygame.draw.line(gamedisplay,gray,(x_margin+(box_width+line_width)*line1,y_margin),(x_margin+(box_width+line_width)*line1,display_height-y_margin),line_width)

    for line in range(y_box+1):
        pygame.draw.line(gamedisplay,gray,(x_margin,y_margin+line*(box_height+line_width)),(display_width-x_margin,y_margin+line*(box_height+line_width)),line_width)

def lefttopcoor(boxx,boxy):
    
    left=x_margin+boxx*(box_width+line_width)
    top=y_margin+boxy*(box_height+line_width)
    return (left,top)

def pixelcoor(x,y):
    
    for boxx in range(x_box):
        for boxy in range(y_box):
            left,top=lefttopcoor(boxx,boxy)
            boxrect=pygame.Rect(left,top,box_width,box_height)
            if boxrect.collidepoint(x,y):
                return (boxx,boxy)
                return (None,None)

            
def game_loop():
    
    found=False
    c=0
    result=0
    score=0
    usedcoor=[]
    while not found:
        
        for event in pygame.event.get():
            
            if c==0:
                
                if event.type==pygame.QUIT:
                    found=True
                    quit()
                
                line()
                a=getboard()
                pygame.display.update()
                c=c+1
                pygame.time.wait(10000)
                
            elif c==1:
                
                line()
                c+=1
                pygame.display.update()
                
            else:
                r()
                scored(score)
                
                pygame.display.update()
                
                mousex=pygame.mouse.get_pos()[0]
                mousey=pygame.mouse.get_pos()[1]
         
                if pixelcoor(mousex,mousey)!=None:              
                        
                    click=pygame.mouse.get_pressed()
                    if event.type==pygame.QUIT:
                        python.quit()
                        quit()
                            
                    if click[0]==1:
                        result+=1
                        
                        x=pixelcoor(mousex,mousey)[0]
                        y=pixelcoor(mousex,mousey)[1]
                        if usedcoordinates(usedcoor,x,y)==None:
                            for i in range(x_box*y_box):
                                     
                                if result%2!=0:
                                         
                                    if x==a[i][0] and y==a[i][1]:
                                        colour=a[i][2]
                                        shape=a[i][2+1]
                                        reveal(x,y,colour,shape)
                                        usedcoor.append((x,y))
                                        if shape=='line':
                                            result+=1
                   
                                             
                                else:
                                         
                                    if x==a[i][0] and y==a[i][1]:
                                        if a[i][2+1]=='line':
                                            result+=1
                                        
                                            
                                        reveal(x,y,a[i][2],a[i][2+1])
                                        usedcoor.append((x,y))
                                        
                                        if a[i][2]==colour and a[i][2+1]==shape:
                                            if a[i][2+1]!='line':                                               
                                                score+=1                                               
                                                print 'woww'
                                                     
                                        else:
                                            if a[i][2+1]!=line:                                                
                                                print 'Not Same'                                   
            
                                                         
                
    clock.tick(60)
    
game_loop()
pygame.quit()
quit()

        
