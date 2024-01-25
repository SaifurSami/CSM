import numpy as np
import math
import pygame
def distance_btwn_ftr_and_bmbr_crdt(fighter,bomber):
    x = pow((fighter[0]-bomber[0]),2)
    y = pow((fighter[1]-bomber[1]),2)
    return math.sqrt(x+y)
def scaling_pixel(pixel):
    return (3*(pixel[0]+50), 6*(pixel[1]+50))
    
def main():
    vf = 20
    fighter_coordinates = [[0,0]]
    bomber_coordinates = []
    T = 0
    with open("./bomberInp.txt") as f:
        for line in f:
            x,y = line.strip().split(',')
            x = int(x)
            y= int(y)
            bomber_coordinates.append([x ,y])
            T+=1
    pygame.init()
    pygame.display.set_caption("Pure Pursuit Game")
    scrn_height = 800
    scrn_width = 1200
    scrn_surface = pygame.display.set_mode((scrn_width,scrn_height))
    font_name = pygame.font.get_fonts()[0]
    font = pygame.font.SysFont(font_name,64)
    bomber_surface = font.render("B",True,"white","black")
    fighter_surface = font.render("F",True,"white","black")
    escaped_surface = font.render("ESCAPED",True,"white","orange")
    caught_surface = font.render("CAUGHT",True,"white","orange")
    running  = True
    t = 0
    
    scrn_surface.fill("black")
    while t<T and running:
        pygame.time.Clock().tick(1.5)
        time_surface = font.render("Time : "+str(t),True,"white",'black')
        scrn_surface.blit(time_surface,(100,scrn_height-150))
        if t==T:
            scrn_surface.blit(escaped_surface,(scrn_width/2,scrn_height/2))
            print("Escaped")
            running = False
        if t>0:
            pygame.draw.line(scrn_surface,"white",scaling_pixel(fighter_coordinates[t-1]),scaling_pixel(fighter_coordinates[t]))
            pygame.draw.line(scrn_surface,"orange",scaling_pixel(bomber_coordinates[t-1]),scaling_pixel(bomber_coordinates[t]))
            pygame.draw.circle(scrn_surface,"white",scaling_pixel(fighter_coordinates[t]),4)
            pygame.draw.circle(scrn_surface,"orange",scaling_pixel(bomber_coordinates[t]),4)
        else:
            scrn_surface.blit(fighter_surface,scaling_pixel(fighter_coordinates[0]))
            scrn_surface.blit(bomber_surface,scaling_pixel(bomber_coordinates[0]))
        dist = distance_btwn_ftr_and_bmbr_crdt(fighter_coordinates[t],bomber_coordinates[t])
        if dist<=10:
            scrn_surface.blit(caught_surface,(scrn_width/2,scrn_height/2))
            print(f"Bomber caught at {t} seconds")
            running = False
        else:
            cos_Theta = (bomber_coordinates[t][0] - fighter_coordinates[t][0]) / dist
            sin_Theta = (bomber_coordinates[t][1] - fighter_coordinates[t][1]) / dist
            xf = fighter_coordinates[t][0] + vf * cos_Theta
            yf = fighter_coordinates[t][1] + vf * sin_Theta
            fighter_coordinates.append([xf,yf])
        t+=1
        pygame.display.flip()
        
    if not running:
        pygame.time.delay(5000)
        pygame.quit()
        


main()