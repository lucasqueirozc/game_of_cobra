import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480
x_cobra = int(largura / 2)
y_cobra = int(altura / 2)

velocidade = 10
x_controle = velocidade
y_controle = 0

x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('cabriola', 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('game of cobrinha')
relogio = pygame.time.Clock()
listacr = []
comprimento_inicial = 5
morreu = False

def aumentacr(listacr):
    for XeY in listacr:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20,20))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, listacr, lista_c, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura / 2)
    y_cobra = int(altura / 2)
    listacr = []
    lista_c = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False



while True:
    relogio.tick(30)
    tela.fill((255,255,255))
    msg = f'Pontos: {pontos}'
    txt_format = fonte.render(msg, True, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
            if event.key == K_l:
                y_cobra = y_cobra == x_cobra

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
    '''
    if pygame.key.get_pressed()[K_a]:
        x_cobra = x_cobra - 20
    if pygame.key.get_pressed()[K_d]:
        x_cobra = x_cobra + 20
    if pygame.key.get_pressed()[K_w]:
        y_cobra = y_cobra - 20
    if pygame.key.get_pressed()[K_s]:
        y_cobra = y_cobra + 20
    if pygame.key.get_pressed()[K_l]:
        y_cobra = y_cobra == x_cobra'''


    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca, y_maca, 20, 20))

    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos = pontos + 1
        comprimento_inicial = comprimento_inicial + 1

    lista_c = []
    lista_c.append(x_cobra)
    lista_c.append(y_cobra)

    listacr.append(lista_c)

    if listacr.count(lista_c) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        msg = 'Game over ! Presione a tecla R para jogar novamente'
        txt_format = fonte2.render(msg, True, (0,0,0))
        ret_txt = txt_format.get_rect()

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_txt.center = (largura//2, altura//2)
            tela.blit(txt_format, ret_txt)
            pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0

    if len(listacr) > comprimento_inicial:
        del listacr[0]

    aumentacr(listacr)

    tela.blit(txt_format, (480,40))


    pygame.display.update()