import pygame
import random
import Colours

class Enemy:
    def __init__(self, Screen):
        self.loc = [900,325]
        self.size = [20,50]
        self.Screen = Screen
    def Draw(self):
        pygame.draw.rect(self.Screen, Colours.Enemy, (self.loc[0], self.loc[1], self.size[0],self.size[1]))
    def Move(self, Speed):
        self.loc[0] -= Speed
    def retLoc(self):
        return self.loc[0]
    def LOCATION(self):
        return self.loc[0], self.loc[1]

class Player:
    def __init__(self, Screen):
        self.loc = [100,315]
        self.size = [40,60]
        self.Screen = Screen

        self.count = 0

        self.Acc = 2.5
        self.Speed = 0
        self.Time = 0.21111111
        
    def Draw(self):
        pygame.draw.rect(self.Screen, Colours.Player, (self.loc[0], self.loc[1], self.size[0],self.size[1]))

    def Gravity(self):
        self.Speed += self.Acc*self.Time
        self.loc[1] += self.Speed*self.Time
    def Jump(self):
        if self.loc[1] > 310 and self.loc[1] < 320:
            self.Speed -= 25
            self.loc[1] -= 25
            
    def Check(self):
        if self.loc[1] > 315:
           self.loc[1] = 315 
           self.Speed = 0

    def Collide(self, RightWall, TopWall):
        if RightWall < self.loc[0]+ self.size[0] and RightWall > self.loc[0]:
            if TopWall < self.loc[1]+ self.size[1]:
                self.ret = True
            else:
                self.ret = False
        else:
            self.ret = False
        return self.ret


class Cloud:
    def __init__(self, Screen):
        self.loc = [900,75]
        self.size = [70,40]
        self.loc[1] += random.randint(-30,30)
        self.Screen = Screen
        self.speed = random.randint(1,6)
        self.speed = self.speed/16
        
    def Move(self):
        self.loc[0] -= self.speed

    def Draw(self):
        pygame.draw.rect(self.Screen, Colours.White, (self.loc[0], self.loc[1], self.size[0],self.size[1]))
        pygame.draw.rect(self.Screen, Colours.White, (self.loc[0] + 40, self.loc[1] + 15, self.size[0],self.size[1]))