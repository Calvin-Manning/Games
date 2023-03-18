import pygame 
import random
import Colours
import Player
pygame.init()

Screen = pygame.display.set_mode((900,470))
pygame.display.set_caption("Blocky")
pygame_icon = pygame.image.load('block-11.png')
pygame.display.set_icon(pygame_icon)
Clock = pygame.time.Clock()

EnemySpeed = 1.75

f = open("HighScore.txt", "r")
Score = 0 
HighScore = f.readline()
Base = 600
f.close()

Remove = 1000
Time = 0
Time2 = 0
Delay = 100

Enemys = []
Enemys.append(Player.Enemy(Screen))

Clouds = []

Play = Player.Player(Screen)

Font = pygame.font.Font('freesansbold.ttf', 20)
Font1 = pygame.font.Font('freesansbold.ttf', 15)
Font2 = pygame.font.Font('freesansbold.ttf', 30)

Run = True
Mode = 0
while Run == True:
    Screen.fill((Colours.BackGround))
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            Run = False
        if keys[pygame.K_SPACE] or keys[pygame.K_UP] or event.type == pygame.MOUSEBUTTONUP:
            if Mode == 1:
                Play.Jump()
            if Mode == 0 :
                Mode = 1
                Score = 0
                EnemySpeed = 1.75
            if Mode == 2:
                Mode = 1
                Score = 0
                EnemySpeed = 1.75
                while len(Enemys) > 0:
                    Enemys.pop(0)



    for i in range(len(Clouds)):
        Clouds[i].Draw()
        Clouds[i].Move()

    if int(Time2 % 1200) == 0:
        Clouds.append(Player.Cloud(Screen))

                
    if Mode == 0:
        text = Font.render('Press Space To Begin', True, Colours.Player)
        Screen.blit(text, (330,440))
    

    if Mode == 1:
        text = Font1.render(f'Score: {int(Score)}', True, Colours.Player)
        Screen.blit(text, (810,15))

        if Time > Base + Delay:
            Enemys.append(Player.Enemy(Screen))
            Time = 0
            Delay = random.randint(0,450)
            if Delay > 400:
                Delay = -450


        for i in range(len(Enemys)):
            Enemys[i].Draw()
            Enemys[i].Move(EnemySpeed)
            x, y = Enemys[i].LOCATION()
            if Play.Collide(x,y):
                Mode = 2
            if Enemys[i].retLoc() < -30:
                Remove = i

        if Remove != 1000:
            Enemys.pop(Remove)
            Remove = 1000        

        Play.Draw()   
        Play.Gravity() 
        Play.Check()

        pygame.draw.rect(Screen, Colours.Ground, (0,375, 900,150))
        
        Score += 0.25


    if Mode == 2:
        f = open("HighScore.txt", "r")
        HighScore = f.readline()
        f.close()

        text = Font2.render(f'High Score: {HighScore}', True, Colours.Player)
        Screen.blit(text, (200,100))
        text = Font2.render(f'Current Score: {int(Score)}', True, Colours.Player)
        Screen.blit(text, (200,200))


        if Score > float(HighScore):
            f = open("HighScore.txt", "w")
            f.write(str(int(Score)))
            f.close()

        Play.Draw() 
        for i in range(len(Enemys)):
            Enemys[i].Draw()
        pygame.draw.rect(Screen, Colours.Ground, (0,375, 900,150)) 

        

    if Score % 500 == 0:
        EnemySpeed += 0.12
        if Base > 25:
            Base -= 25

    pygame.display.flip()
    Clock.tick(90)
    Time += 1
    Time2 += 1
    
    
pygame.quit()
