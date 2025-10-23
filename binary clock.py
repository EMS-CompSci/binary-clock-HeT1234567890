# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 09:36:41 2025

@author: henrytodd1
"""

#ignore this as i was just making sure i could make a function to convert to binary
"""def denaryToBinary(num):
    bnNum = []
    length = 0 # how many binary characters we need
    done = False
    i = 0
    while not done:
        if num < 2**i:
            length = i
            done = True
        else:
            i+=1
    temp = num
    for i in range(length):
        exp = length-i-1
        print(exp)
        if temp >= 2**exp:
            temp-=(2**exp)
            bnNum.append(1)
        else:
            bnNum.append(0)
    return tuple(bnNum)
            
print(denaryToBinary(453))"""

import datetime
import time
import pygame

pygame.init()
screen = pygame.display.set_mode((200,350))
pygame.display.set_caption("Binary clock")

while True:
    screen.fill((100,100,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    now = datetime.datetime.now().time()
    
    hr = bin(now.hour)[2:]
    mn = bin(now.minute)[2:]
    sec = bin(now.second)[2:]
    
    if len(hr) < 5:
        hr = (5-len(hr))*"0"+hr
    if len(mn) < 6:
        mn = (6-len(mn))*"0"+mn
    if len(sec) < 6:
        sec = (6-len(sec))*"0"+sec
        
    hr = tuple(hr)
    mn = tuple(mn)
    sec = tuple(sec)
    
    #print(str(hr)+":"+str(mn)+":"+str(sec))
    for i,v in enumerate(hr):
        clr = (0,0,0)
        if v == "1":
            clr = (255,255,255)
        pygame.draw.circle(screen,clr,(50,50*(i+1)),20)
    for i,v in enumerate(mn):
        clr = (0,0,0)
        if v == "1":
            clr = (255,255,255)
        pygame.draw.circle(screen,clr,(100,50*(i+1)),20)
    for i,v in enumerate(sec):
        clr = (0,0,0)
        if v == "1":
            clr = (255,255,255)
        pygame.draw.circle(screen,clr,(150,50*(i+1)),20)
    pygame.display.update()
    time.sleep(1)
