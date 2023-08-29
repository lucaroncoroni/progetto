'''questo primo pezzo non lo ho realizzato su git perchè
1 sapevo del progetto ma non che dovessi svolgerlo su git
2 non avevo svolto la registrazione a git'''
import pygame
import sys
import random

# Inizializzazione di pygame
pygame.init()

# Impostazioni della finestra
larghezza_finestra = 400
altezza_finestra = 600
finestra = pygame.display.set_mode((larghezza_finestra, altezza_finestra))
pygame.display.set_caption("Flappy Bird")

# Colori
nero = (0, 0, 0)
bianco = (255, 255, 255)

# Caricamento immagini
tubi=[]
t=0
posy=0
tubocreato=False
sfondo = pygame.image.load("background.png")
uccello = pygame.image.load("bird.png")
tubo_inferiore = pygame.image.load("pipe_top.png")
tubo_superiore = pygame.image.load("pipe_bottom.png")

sfondo=pygame.transform.scale(sfondo,(400,600))
uccello=pygame.transform.scale(uccello,(50,50))
tubo_superiore=pygame.transform.scale(tubo_superiore,(50,200))
tubo_inferiore=pygame.transform.scale(tubo_inferiore,(50,200))


uccello_rect = uccello.get_rect()
uccello_rect.center = (100, altezza_finestra // 2)
posy=uccello_rect.center[1]
tubi = []

# Velocità e gravità
gravita = 3.5
salto = -50
velocita = 7


clock = pygame.time.Clock()

def crea_tubo():
    global tubo_superiore,tubo_inferiore
    tubo_superiore=pygame.transform.scale(tubo_superiore,(50,random.randint(200,450)))
    tubo_inferiore=pygame.transform.scale(tubo_inferiore,(50,random.randint(200,450)))
    tubo_superiore_rect = tubo_superiore.get_rect(midbottom=(larghezza_finestra,600))
    tubo_inferiore_rect = tubo_inferiore.get_rect(midtop=(larghezza_finestra,0))
    return tubo_superiore_rect, tubo_inferiore_rect

def muovi_tubi(tubi):
    global t,tubocreato
    # tubo1=0
    # tubo2=0 

    # if tubocreato:
    #     tubo1.centerx -= velocita
    #     tubo2.centerx -= velocita
    #     tubi.append(tubo1)
    #     tubi.append(tubo2)
    #     print("ciao")

    if t==0:
        tubo1,tubo2=crea_tubo()
        t=60
        tubi.append(tubo1)
        tubi.append(tubo2)
        
    elif t>0:
        t-=1
    for tubo in tubi:
        tubo.centerx -= velocita
    
    # tubi = [tubo for tubo in tubi if tubo.right > 0]
    #return tubi

def disegna_tubi(tubi):
    for tubo in tubi:
        if tubo.bottom >= altezza_finestra:
            finestra.blit(tubo_superiore, tubo)
        else:
            finestra.blit(tubo_inferiore, tubo)

def controlla_collisione(tubi):
    #rect=pygame.rect.Rect(uccello_rect.left,)
    for tubo in tubi:
        if uccello_rect.colliderect(tubo):
            return True
    if uccello_rect.top <= 0 or uccello_rect.bottom >= altezza_finestra:
        return True
    return False

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            uccello_rect.y += salto
            posy+=salto

    
    finestra.blit(sfondo, (0, 0))  
    finestra.blit(uccello, uccello_rect)
    # finestra.blit(uccello,(100-(uccello.get_width()/2),posy))
    

    muovi_tubi(tubi)
    # if len(tubi) < 3:
    #     tubi.extend(crea_tubo())

    disegna_tubi(tubi)

    uccello_rect.y += gravita
    posy+=gravita
    collisione = controlla_collisione(tubi)
    if collisione:
        sys.exit()

    pygame.display.update()
    clock.tick(30) 