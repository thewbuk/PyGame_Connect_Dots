import pygame
import random
import math
from pygame import mixer

pygame.init()

screen=pygame.display.set_mode((800,600))

#Icons
pygame.display.set_caption('My game')
icon=pygame.image.load('C:/Users/Dell/Desktop/Python/Dots/Dots/PyGame/images/teamwork1.png')
pygame.display.set_icon(icon)

#Player
playerimg = pygame.image.load('C:/Users/Dell/Desktop/Python/Dots/Dots/PyGame/images/girl.png')
playerX=370
playerY=500
playerXchange=0
playerYchange=0

#Enemy
enemyimg = pygame.image.load('C:/Users/Dell/Desktop/Python/Dots/Dots/PyGame/images/girl2.png')
enemyX=random.randint(50,736)
enemyY=random.randint(50, 536)
enemyXchange=0
enemyYchange=0

#Background
background=pygame.image.load('C:/Users/Dell/Desktop/Python/Dots/Dots/PyGame/images/pizza-3.jpg')

#Pizza Bullet
bulletimg=pygame.image.load('C:/Users/Dell/Desktop/Python/Dots/Dots/PyGame/images/pizzaslice.png')
bulletX=370
bulletY=500
bulletXchange=0
bulletychange=10
bulletstate='ready'

#Broccoli Bullet
broccoliimg=pygame.image.load('C:/Users/Dell/Desktop/Python/Dots/Dots/PyGame/images/broccoli.png')
broccoli_state='ready'

#Explosion
explosionimg=pygame.image.load('C:/Users/Dell/Desktop/Python/Dots/Dots/PyGame/images/explosion.png')

#Variables
run = True
i=0
temp_bullet=0
score_value=0
currentx=0
currenty=0
temp_rand=random.randint(1,8)
hit=0
enemyhit=False

#Text
font=pygame.font.Font('freesansbold.ttf',40)
textX=10
textY=10

#Health
health=3
healthx=10
healthy=42

#Game Over
over=pygame.font.Font('freesansbold.ttf', 70)
back_oryg=pygame.image.load('C:/Users/Dell/Desktop/Python/Dots/Dots/PyGame/images/pizza-2.jpg')

def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y):
    screen.blit(enemyimg,(x,y))

def bullet(x,y):
    global bulletstate
    bulletstate='fire'
    screen.blit(bulletimg,(x+16,y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 40:
        return True
    else:
        return False

def enemy_shoot(currentx, currenty):
    screen.blit(broccoliimg,(currentx+16,currenty+37))

def show_score_value(x,y):
    score_text=font.render('Score: '+str(score_value),True,(52,128,33))
    screen.blit(score_text,(x,y))

def show_health(x,y):
    health_text=font.render('Health: '+str(health), True, (52,128,33))
    screen.blit(health_text,(x,y))

def game_over():
    global back_oryg
    i=1
    while True:
        if i==1:
            screen.fill((0,255,0))
            screen.blit(back_oryg,(0,0))
            pygame.display.update()
            over_text1=font.render('GAME OVER :)',True, (52,128,33))
            over_text2=font.render('WOULD YOU LIKE TO PLAY AGAIN? ',True, (52,128,33))
            over_text3=font.render('PRESS SPACE TO RESTART', True,(52,128,33))
            over_text4=font.render('OR ENTER TO QUIT', True,(52,128,33))
            screen.blit(over_text1,(280,100))
            screen.blit(over_text2,(60,200))
            screen.blit(over_text3,(110,300))
            screen.blit(over_text4,(220,400))
            pygame.display.update()
            i+=1
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    return False
                elif event.key==pygame.K_RETURN:
                    return True
                else:
                    return game_over()
            if event.type==pygame.KEYUP:
                continue
def win():
    global back_oryg
    i=1
    while True:
        if i==1:
            screen.fill((0,255,0))
            screen.blit(back_oryg,(0,0))
            pygame.display.update()
            over_text1=font.render('YOU WON! :)',True, (52,128,33))
            over_text2=font.render('WOULD YOU LIKE TO PLAY AGAIN? ',True, (52,128,33))
            over_text3=font.render('PRESS SPACE TO RESTART', True,(52,128,33))
            over_text4=font.render('OR ENTER TO QUIT', True,(52,128,33))
            screen.blit(over_text1,(340,100))
            screen.blit(over_text2,(60,200))
            screen.blit(over_text3,(110,300))
            screen.blit(over_text4,(220,400))
            pygame.display.update()
            i+=1
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    return False
                elif event.key==pygame.K_RETURN:
                    return True
                else:
                    return win()
            if event.type==pygame.KEYUP:
                continue

while run:
    screen.fill((0,255,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type  ==  pygame.QUIT:
            run=False
        #Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerXchange=5
            if event.key == pygame.K_LEFT:
                playerXchange=-5
            if event.key == pygame.K_UP:
                playerYchange=-5
            if event.key == pygame.K_DOWN:
                playerYchange=5
            if event.key == pygame.K_RIGHT and event.key == pygame.K_LEFT:
                playerXchange=5
                playerYchange=5
            #Maybe if key is pressed constant fire of bullets - for later on
            if event.key==pygame.K_SPACE:
                if bulletstate=='ready':
                    bullet_sound=mixer.Sound('C:/Users/Dell/Desktop/Python/Dots/Dots/PyGame/sounds/bullet.wav')
                    bullet_sound.play()
                    bulletX=playerX
                    bulletY=playerY
                    bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key  ==  pygame.K_LEFT or event.key  ==  pygame.K_RIGHT:
                playerXchange=0
            if event.key   ==   pygame.K_UP or event.key == pygame.K_DOWN:
                playerYchange=0
    
    i+=1
    change=random.randint(50,150)
    if(i%change==0) or i==1:
        if random.randint(1,2)==1:
            enemyXchange=0.5
            if random.randint(1,2)==1:
                enemyYchange=0.5
            else:
                enemyYchange=-0.5
        else:
            enemyXchange=-0.5
            if random.randint(1,2)==1:
                enemyYchange=0.5
            else:
                enemyYchange=-0.5

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    if playerY <= 0:
        playerY=0
    elif playerY >=536:
        playerY=536
    

    if enemyX <= 0 :
        enemyX = 0
    elif enemyX >= 736:
        enemyX = 736
    if enemyY <= 0:
        enemyY=0
    elif enemyY >=536:
        enemyY=536

    enemyX+=enemyXchange
    enemyY+=enemyYchange

    playerX+=playerXchange
    playerY+=playerYchange

    if isCollision(enemyX, enemyY, bulletX, bulletY)==True:
        bulletY=500
        bulletstate='ready'
        temp_bullet=1
        score_value+=1
        enemyX=random.randint(50,736)
        enemyY=random.randint(50, 536)
        enemyhit=True

    if bulletY<=36:
        bulletstate='ready'
    
    if bulletstate=='fire':
        bulletY-=bulletychange
        bullet(bulletX,bulletY)

    enemyhit=False
    player(playerX, playerY)
    enemy(enemyX, enemyY)

    if 1<=temp_bullet<=40:
        screen.blit(explosionimg,(enemyX,enemyY-16))
        temp_bullet+=1
    else:
        temp_bullet=0


    if broccoli_state=='ready' or enemyhit==True:
        currentx=enemyX
        currenty=enemyY
        if enemyX<=150:
            if enemyY<=150:
                temp_list=[5,6,7]
                temp_rand=random.choice(temp_list)
            else:
                temp_list=[4,5,6]
                temp_rand=random.choice(temp_list)
        elif enemyX>=650:
            if enemyY<=150:
                temp_list=[1,7,8]
                temp_rand=random.choice(temp_list)
            else:
                temp_list=[1,2,8]
                temp_rand=random.choice(temp_list)
        elif enemyX>=650:
            if enemyY>=450:
                temp_list=[1,2,3]
                temp_rand=random.choice(temp_list)
            else:
                temp_list=[1,2,8]
                temp_rand=random.choice(temp_list)
        elif enemyX<=150:
            if enemyY>=450:
                temp_list=[3,4,5]
                temp_rand=random.choice(temp_list)
            else:
                temp_list=[4,5,6]
                temp_rand=random.choice(temp_list)
        elif enemyY<=150:
            temp_list=[6,7,8]
            temp_rand=random.choice(temp_list)
        elif enemyY>=450:
            temp_list=[2,3,4]
            temp_rand=random.choice(temp_list)
        else:
            temp_rand=random.randint(1,8)
        broccoli_state='fire'

    if currentx>=850 or currenty>=650 or currentx<=-50 or currenty<=-50:
        broccoli_state='ready'
    

    if temp_rand==1:
        currentx-=3
    elif temp_rand==2:
        currentx-=3
        currenty-=3
    elif temp_rand==3:
        currenty-=3
    elif temp_rand==4:
        currentx+=3
        currenty-=3
    elif temp_rand==5:
        currentx+=3
    elif temp_rand==6:
        currentx+=3
        currenty+=3
    elif temp_rand==7:
        currenty+=3
    elif temp_rand==8:
        currentx-=3
        currenty+=3

    iscollision2=isCollision(playerX, playerY, currentx, currenty)
    if iscollision2:
        broccoli_state='ready'
        health-=1
        hit+=1
    if 1<=hit<=30:
        screen.blit(explosionimg,(playerX, playerY))
        hit+=1
    else:
        hit=0

    enemy_shoot(currentx, currenty)
    show_score_value(textX, textY)
    show_health(healthx, healthy)

    if health==0:
        if game_over()==True:
            run=False
        else:
            playerX=370
            playerY=500
            playerXchange=0
            playerYchange=0
            enemyX=random.randint(50,736)
            enemyY=random.randint(50, 536)
            enemyXchange=0
            enemyYchange=0
            bulletX=370
            bulletY=500
            bulletXchange=0
            bulletychange=10
            bulletstate='ready'
            broccoli_state='ready'
            run = True
            i=0
            temp_bullet=0
            score_value=0
            currentx=0
            currenty=0
            temp_rand=random.randint(1,8)
            hit=0
            enemyhit=False
            health=3

    if score_value==10:
        if win()==True:
            run=False
        else:
            playerX=370
            playerY=500
            playerXchange=0
            playerYchange=0
            enemyX=random.randint(50,736)
            enemyY=random.randint(50, 536)
            enemyXchange=0
            enemyYchange=0
            bulletX=370
            bulletY=500
            bulletXchange=0
            bulletychange=10
            bulletstate='ready'
            broccoli_state='ready'
            run = True
            i=0
            temp_bullet=0
            score_value=0
            currentx=0
            currenty=0
            temp_rand=random.randint(1,8)
            hit=0
            enemyhit=False
            health=3
            
    pygame.display.update()