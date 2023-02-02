import pygame   #biblioteca que permite programar jogos em python
from pygame.locals import *     #importa as funcionalidades do pygame
import random

tamanhoJanela = (600, 600)          #podemos definir o tamanho da tela do game
tamanhoPixel = 10                   #tamanho dos pixeis que a cobrinha anda

def colisao(pos1, pos2):            #funçao de colisao da cobrinha
    return pos1 == pos2

def foraDaTela(pos):        #função de colisao da cobrinha com a janela, assim reiniciando o jogo qndo ocorre
    if 0 <= pos[0] < tamanhoJanela[0] and 0 <= pos[1] < tamanhoJanela[1]:
        return False
    else:
        return True

def random_on_grid():      #função que faz a maçã aparecer em lugares diferentes, conforme o tamanho da tela
    x = random.randint(0, tamanhoJanela[0])
    y = random.randint(0, tamanhoJanela[1])
    return (x // tamanhoPixel * tamanhoPixel, y // tamanhoPixel * tamanhoPixel)

def reiniciar():        #função de reiniciar o jogo
    global cobraPosicao
    global macaPosicao
    global cobraDirecao
    cobraPosicao = [(250, 50), (260, 50), (270, 50)]
    cobraDirecao = K_LEFT
    macaPosicao = random_on_grid()


cobraPosicao = [(250, 50), (260, 50), (270, 50)]        #posição da movimentação da cobra
cobraSuperficie = pygame.Surface((tamanhoPixel, tamanhoPixel))  #superficie em que a cobra se movimenta
cobraSuperficie.fill((255, 255, 255))           #cor da superficie em q a cobra se movimenta
cobraDirecao = K_LEFT           


macaSuperficie = pygame.Surface((tamanhoPixel, tamanhoPixel))   #superficie da maça
macaSuperficie.fill((255, 0, 0))        #cor da maçã(branca)
macaPosicao= random_on_grid()           #chama função que faz a maçã aparecer aleatoriamente na superficie

pygame.init()       #programa a inicialização da janela
screen = pygame.display.set_mode(tamanhoJanela)  #configura o tamanho da janela do jogo
pygame.display.set_caption('COBRINHA')      #Nome na janela do jogo

while True:
    pygame.time.Clock().tick(15)    #configura a taxa de quadros (velocidade do jogo)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit
        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                cobraDirecao = event.key

    screen.blit(macaSuperficie, macaPosicao)

    if colisao(macaPosicao, cobraPosicao[0]):
        cobraPosicao.append((-10, -10))
        macaPosicao = random_on_grid()


    for pos in cobraPosicao:
        screen.blit(cobraSuperficie, pos)

    for i in range(len(cobraPosicao)-1, 0, -1):
        if colisao(cobraPosicao[0], cobraPosicao[1]):
            reiniciar()
            
        cobraPosicao[i] = cobraPosicao[i-1]

    if foraDaTela(cobraPosicao[0]):
        reiniciar()

    if cobraDirecao == K_UP:
        cobraPosicao[0] = (cobraPosicao[0][0], cobraPosicao[0][1] - tamanhoPixel)
    elif cobraDirecao == K_DOWN:
        cobraPosicao[0] = (cobraPosicao[0][0], cobraPosicao[0][1] + tamanhoPixel)    
    elif cobraDirecao == K_LEFT:
        cobraPosicao[0] = (cobraPosicao[0][0] - tamanhoPixel, cobraPosicao[0][1])
    elif cobraDirecao == K_RIGHT:
        cobraPosicao[0] = (cobraPosicao[0][0] + tamanhoPixel, cobraPosicao[0][1])


    pygame.display.update()