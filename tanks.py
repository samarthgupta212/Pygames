import pygame
from random import randrange
pygame.init()

display_width=800
display_height=600
clock=pygame.time.Clock()
gamedisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('tanks')
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
orange=(255,155,0)

displaycolor=(randrange(0,255),randrange(0,255),randrange(0,255))
color1=(randrange(0,255),randrange(0,255),0)
health_x=200
health_x_enemy=200
x=display_width-100
y=display_height-50
x_enemy=100
barrier_x=randrange(display_width/2,display_width*3/4)
barrier_y=randrange(display_height/4,display_height*3/4)
barrier_width=randrange(20,50)
barrier_height=display_height-barrier_y-25

def startagain():
    
    global x,x_enemy,health_x,health_x_enemy,displaycolor,color1
    displaycolor=(randrange(0,255),randrange(0,255),randrange(0,255))
    color1=(randrange(0,255),randrange(0,255),0)
    health_x=200
    health_x_enemy=200
    x=display_width-100
    y=display_height-50
    x_enemy=100
    barrier_x=randrange(display_width/2,display_width*3/4)
    barrier_y=randrange(display_height/4,display_height*3/4)
    barrier_width=randrange(20,50)
    barrier_height=display_height-barrier_y-25
    main(0,0,50,50,x,x_enemy,0)
    
def gameover(x):
    
    game=False
    gamedisplay.fill(black)
    while not game:
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                game=False

            pos=pygame.mouse.get_pos()
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                if 274<pos[0]<530 and 329<pos[1]<364:
                    startagain()
          
        if x==0:
            displaytext=pygame.font.Font(None,50)
            text=displaytext.render('Player 2 Won',True,displaycolor)
            surf=text.get_rect()
            surf.center=((display_width/2,display_height/2))
            gamedisplay.blit(text,surf)
            
        else:
            displaytext=pygame.font.Font(None,50)
            text=displaytext.render('Player 1 Won',True,displaycolor)
            surf=text.get_rect()
            surf.center=((display_width/2,display_height/2))
            gamedisplay.blit(text,surf)
            
        displaytext=pygame.font.Font(None,75)
        text=displaytext.render('Play Again',True,color1)
        surf=text.get_rect()
        surf.center=((display_width/2,display_height/2+50))
        gamedisplay.blit(text,surf)
        pygame.display.update()
        clock.tick(30)
    
    
def health(x):
    
    if x>100:
        pygame.draw.rect(gamedisplay,green,(display_width-250,20,x,40))
    if x<=100 and x>50:
        pygame.draw.rect(gamedisplay,orange,(display_width-250,20,x,40))
    if x<=50 and x>0:
        pygame.draw.rect(gamedisplay,red,(display_width-250,20,x,40))
    if x<0:
        gameover(0)
   

def enemy_health(x):
        
    if x<=100 and x>50:
        pygame.draw.rect(gamedisplay,orange,(50,20,x,40))
    if x<=50 and x>0:
        pygame.draw.rect(gamedisplay,red,(50,20,x,40))
    if x>100:
        pygame.draw.rect(gamedisplay,green,(50,20,x,40))
    if x<0:
        gameover(1)
    
    
def power(level):
    
    displaytext=pygame.font.Font(None,25)
    text=displaytext.render('POWER:'+str(level)+'%',True,black)
    gamedisplay.blit(text,(display_width/2-20,0))
    
def explosion(x,y):
    
    explode=True
    colors=[red,dark_red,yellow,dark_yellow]
    magnitude=1
    while explode:
        
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:           
                explode=False
         
        while magnitude<50:
            
            exploding_bit_x=x+randrange(-1*magnitude,magnitude)
            exploding_bit_y=y+randrange(-1*magnitude,magnitude)
            pygame.draw.circle(gamedisplay,colors[randrange(0,4)],(exploding_bit_x,exploding_bit_y),randrange(1,5))
            magnitude+=1
        
            pygame.display.update()
            clock.tick(50)
            explode=False
                                   
def fire(startpos,startpos_enemy,Turpos,Turpos_enemy,fire_power,fire_power_enemy,x,x_enemy,c):
    
    fire=True

    global health_x,health_x_enemy
    
    if c%2!=0:
        
        pos=list(startpos)
        
        while fire:
            
            for event in pygame.event.get():
                
                if event.type==pygame.QUIT:           
                    fire=False
                    main(Turpos_enemy,Turpos,fire_power,fire_power_enemy,x,x_enemy,c)

            pygame.draw.circle(gamedisplay,red,(pos[0],pos[1]),8)
            pos[0]-=Turpos*2
            pos[1]+=int((((pos[0]-startpos[0])*0.035*(100-fire_power)/100)**2)-(12-Turpos))
            if pos[1]>=display_height-25:
                explosion(pos[0],pos[1])
                main(Turpos_enemy,Turpos,fire_power,fire_power_enemy,x,x_enemy,c)

            if barrier_x<=pos[0]<=barrier_x+barrier_width and barrier_y<=pos[1]<=display_height:
                explosion(pos[0],pos[1])
                main(Turpos_enemy,Turpos,fire_power,fire_power_enemy,x,x_enemy,c)

            if barrier_x<=pos[0]<=barrier_x+barrier_width and pos[1]>=barrier_y:
                explosion(pos[0],pos[1])
                main(Turpos_enemy,Turpos,fire_power,fire_power_enemy,x,x_enemy,c)

            if x_enemy<=pos[0]<=x_enemy+50 and pos[1]>=display_height-50:
                health_x_enemy=health_x_enemy-4*min(abs(x_enemy-pos[0]),abs(x_enemy+50-pos[0]))
            
                explosion(pos[0],pos[1])
                main(Turpos_enemy,Turpos,fire_power,fire_power_enemy,x,x_enemy,c)
                
            pygame.display.update()
            clock.tick(30)
                
    else:
        
        pos=list(startpos_enemy)
        
        while fire:
            
            for event in pygame.event.get():
                
                if event.type==pygame.QUIT:           
                    fire=False
                    main(Turpos_enemy,Turpos,fire_power,fire_power_enemy,x,x_enemy,c)

            pygame.draw.circle(gamedisplay,red,(pos[0],pos[1]),8)
            pos[0]+=Turpos_enemy*2
            pos[1]+=int((((startpos_enemy[0]-pos[0])*0.035*(100-fire_power_enemy)/100)**2)-(12-Turpos_enemy))
            if pos[1]>=display_height-25:
                explosion(pos[0],pos[1])
                main(Turpos_enemy,Turpos,fire_power,fire_power_enemy,x,x_enemy,c)

            if barrier_x<=pos[0]<=barrier_x+barrier_width and barrier_y <=pos[1]<=display_height:
                explosion(pos[0],pos[1])
                main(Turpos_enemy,Turpos,fire_power,fire_power_enemy,x,x_enemy,c)

            if barrier_x<=pos[0]<=barrier_x+barrier_width and pos[1]>=barrier_y:
                explosion(pos[0],pos[1])
                main(Turpos_enemy,Turpos,fire_power,fire_power_enemy,x,x_enemy,c)
                
            if x<=pos[0]<=x+50 and pos[1]>=display_height-50:
                health_x=health_x-4*min(abs(x-pos[0]),abs(x+50-pos[0]))
                             
                explosion(pos[0],pos[1])
                main(Turpos_enemy,Turpos,fire_power,fire_power_enemy,x,x_enemy,c)
                
            pygame.display.update()
            clock.tick(30)

def tank(x_enemy,x,i,j,barrier):

    possible_turrets=[
        (x+25,y-50),
        (x+23,y-48),
        (x+20,y-45),
        (x+17,y-42),
        (x+14,y-40),
        (x+12,y-38),
        (x+10,y-36),
        (x+7,y-34),
        (x+4,y-32),
        (x+2,y-30),
        (x,y-28),
        (x-2,y-25),
        (x-5,y-20)
        ]
    possible_enemy_turrets=[
        (x_enemy+25,y-50),
        (x_enemy+27,y-48),
        (x_enemy+30,y-45),
        (x_enemy+33,y-42),
        (x_enemy+36,y-40),
        (x_enemy+38,y-38),
        (x_enemy+40,y-36),
        (x_enemy+43,y-34),
        (x_enemy+46,y-32),
        (x_enemy+48,y-30),
        (x_enemy+50,y-28),
        (x_enemy+52,y-25),
        (x_enemy+55,y-20)      
        ]
    
    gamedisplay.fill(white)
    pygame.draw.rect(gamedisplay,black,(x_enemy,y,50,25))
    pygame.draw.rect(gamedisplay,black,(x,y,50,25))
    pygame.draw.circle(gamedisplay,black,(x_enemy+25,y),20)
    pygame.draw.circle(gamedisplay,black,(x+25,y),20)
    pygame.draw.line(gamedisplay,black,possible_enemy_turrets[j],(x_enemy+25,y-20),5)
    pygame.draw.line(gamedisplay,black,possible_turrets[i],(x+25,y-20),5)
    pygame.draw.rect(gamedisplay,black,barrier)
    pygame.draw.rect(gamedisplay,green,(0,display_height-25,display_width,25))
    
    return possible_turrets[i],possible_enemy_turrets[j]
    
def main(currentTur_enemy,currentTur,fire_power,fire_power_enemy,x,x_enemy,c):
    
    
    done=False 
    change_x=0
    dx=0
    power_change=0
    
    barrier=(barrier_x,barrier_y,barrier_width,barrier_height)

    while not done:
    
        gun=tank(x_enemy,x,currentTur,currentTur_enemy,barrier)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    change_x=-5
                    
                if event.key==pygame.K_RIGHT:
                    change_x=5
                    
            
                if event.key==pygame.K_a:
                    dx=1
                    
                if event.key==pygame.K_d:
                    dx=-1
                    
                if event.key==pygame.K_SPACE:
                    pygame.event.wait()
                    c+=1
                    fire(gun[0],gun[1],currentTur,currentTur_enemy,fire_power,fire_power_enemy,x,x_enemy,c)
                             
                if event.key==pygame.K_UP:
                    power_change=1
                    
                if event.key==pygame.K_DOWN:
                    power_change=-1
                    

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    change_x=0

                if event.key==pygame.K_a or event.key==pygame.K_d:
                    dx=0

                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    power_change=0
                
        if c%2==0:

            x+=change_x
            currentTur+=dx
            fire_power+=power_change
            power(fire_power)
            
            if x>=display_width-50:
                x=display_width-50

            if x<=barrier_x+barrier_width:
                x=barrier_x+barrier_width
                
            if currentTur>=13:
                currentTur=12
                        
            if currentTur<0:
                currentTur=0            
                
        else:
        
            x_enemy+=change_x
            currentTur_enemy-=dx
            fire_power_enemy+=power_change
            power(fire_power_enemy)

            if x_enemy<=0:
                x_enemy=0

            if x_enemy>=barrier_x:
                x_enemy=barrier_x
                
            if currentTur_enemy>=13:
                currentTur_enemy=12
                        
            if currentTur_enemy<0:
                currentTur_enemy=0
            
        health(health_x)
        enemy_health(health_x_enemy)
        pygame.display.update()
        clock.tick(30)
    
main(0,0,50,50,x,x_enemy,0)
gameover(0)


