import pygame               
import random
import math
from pygame import mixer
x=pygame.init()

gamewindow=pygame.display.set_mode((1300,650))
pygame.display.set_caption("HORSE GAME")

background2=pygame.image.load("background2.jpg")

#BACKGROUN SOUND
mixer.music.load("music.mp3")
mixer.music.play(-1)

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)

clock=pygame.time.Clock()

font=pygame.font.SysFont(None,55) 
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])


# TO ADD HOMESCREEN ON WINDOW
def Welcome():
    exit_game=False
    while not exit_game:
        #gamewindow.fill(white)
        gamewindow.fill((0,0,254))
        text_screen("WELCOME TO HORSE  GAME",black,400,250)    
        text_screen("PRESS SPACE BAR TO PLAY",red,400,290)     #another message on screen
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:      #this is used to open game  when we press buttom
                if event.key==pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(60)


#GAME LOOP
def gameloop():
    exit_game=False
    game_over=False
    
    playerimg=pygame.image.load("horseback.png")
    playerX=10
    playerY=650
    playerX_change=0
    playerY_change=0
    
    tower1img=pygame.image.load("tower.png")
    tower1X=-10
    tower1Y=400
    tower1X_change=5
    
    #ENEMY
    enemyimg=[]
    enemyX=[]
    enemyY=[]
    enemyX_change=[]
    enemyY_change=[]
    num_of_enemies=3
    
    for i in range(num_of_enemies):
        enemyimg.append(pygame.image.load("tower3.png"))
        enemyX.append(random.randint(0,1150))
        enemyY.append(random.randint(50,300))
        enemyX_change.append(4)
        enemyY_change.append(10)
    
     
    #ENEMY
    appleimg=pygame.image.load("fruit.png")
    appleX=random.randint(0,1150)
    appleY=random.randint(0,300)
    
    
    #score
    score_value=0
    font=pygame.font.Font("freesansbold.ttf",32)
    textX=10
    textY=10
    
    def show_score(x,y):
        score=font.render("Score:"+str(score_value),True,(255,255,255))
        gamewindow.blit(score,(x,y))
    
    
    def player(x,y):
        gamewindow.blit(playerimg,(x,y))
    
    
    def tower(x,y):
        gamewindow.blit(tower1img,(x,y))
    
    def enemy(x,y,i):
        gamewindow.blit(enemyimg[i],(x,y))
    
    
    def apple(x,y):
        gamewindow.blit(appleimg,(x,y))
    
    
    def iscollision(appleX,appleY,playerX,playerY):
        distance=math.sqrt((math.pow(appleX-playerX,2))+(math.pow(appleY-playerY,2)))
        if distance<40:
            return True
        else:
            return False 
    
    def encollision(enemyX,enemyY,playerX,playerY):
        distance=math.sqrt((math.pow(enemyX-playerX,2))+(math.pow(enemyY-playerY,2)))
        if distance<27:
            return True
        else:
            return False
    
    fps=60
    while not exit_game:
        if game_over:
            gamewindow.fill(white)
            text_screen("GAME OVER PRESS ENTER TO CONTINUE",black,200,250)
            text_screen("--------Develop by Meraj",red,600,300)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        Welcome()

        else:
            gamewindow.fill(black)
            gamewindow.blit(background2,(0,550))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        playerX_change=10
                        playerY_change=0
                    if event.key==pygame.K_UP:
                        playerY_change=-10
                        playerX_change=0
                    if event.key==pygame.K_DOWN:
                        playerY_change=10     
                        playerX_change=0       
           
            
            playerX+=playerX_change
            playerY+=playerY_change
        
            if playerX <=0:    #lower limit of x-coordinate
                playerX=0
            elif playerX >=1150:  #upper limit of x-coordinate--image size
                playerX=0
                playerY=360
        
            if playerY <=0:   
                playerY=0
            elif playerY>=360:  
                playerY=360 
        
            tower1X+=tower1X_change
            if tower1X <=-10:    
                tower1X=-10
            elif tower1X >=1150: 
                tower1X=-10     
        
             #ENEMY MOVEMENT
            for i in range(num_of_enemies):
                enemyX[i]+=enemyX_change[i]
                if enemyX[i] <=0:    
                    enemyX_change[i]=5
                    enemyY[i]+=enemyY_change[i]
                elif enemyX[i] >= 1150: 
                    enemyX_change[i]=-5
                    enemyY[i]+=enemyY_change[i] 
        
                #COLLISION
                collisions=encollision(enemyX[i],enemyY[i],playerX,playerY)
                if collisions:
                    playerX_change=0
                    playerY_change=0
                    #SOUND
                    mixer.music.load("music2.mp3")
                    mixer.music.play()
                    game_over=True
                enemy(enemyX[i],enemyY[i],i)                
        
            #COLLISION
            collision=iscollision(appleX,appleY,playerX,playerY)
            if collision:
                playerY=600
                score_value+=1
                #SOUND
                mixer.music.load("music3.mp3")
                mixer.music.play()
                appleX=random.randint(0,1150)
                appleY=random.randint(0,300)
        
             
            #gamewindow.fill(red)
            player(playerX,playerY)
            tower(tower1X,tower1Y)
            apple(appleX,appleY)
            show_score(textX,textY)
        pygame.display.update()
        clock.tick(fps)
        
    pygame.quit()
    quit() 

Welcome()


    
    
    
    
