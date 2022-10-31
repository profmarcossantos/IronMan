import os
from numpy import disp
import pygame
pygame.init()
os.system("cls")
print("Começando o Jogo de Futebol!")
largura = 453
altura = 612
tamanho = (largura,altura) #tupla - imutável -> não pode alterar os valores
display = pygame.display.set_mode( tamanho )
fps = pygame.time.Clock()
pygame.display.set_caption("Jogo de Futebol")
#         Red Green Blue
branco = (255,255,255)
preto = (0,0,0)
cor = (170,50,8) #lembrando que o RGB vai de 0 a 255
# looping para ficar rodando o jogo
jogando = True

fundo = pygame.image.load("assets/campo.jpg")
bola = pygame.image.load("assets/bola.png")
tamanhoXBola = 50
tamanhoYBola = 50
posicaoBolaX = 202
posicaoBolaY = 283
movimentoBolaX = 0
movimentoBolaY = 0
velocidade = 10

placarPlayer1 = 0
placarPlayer2 = 0

def escreverTexto (texto):
    fonte  = pygame.font.Font("freesansbold.ttf",15)
    textoDisplay = fonte.render(texto,True,branco)
    display.blit(textoDisplay, (5,5))


while jogando:
    # Mapendo os eventos do Game
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                movimentoBolaX = velocidade * -1
            elif evento.key == pygame.K_RIGHT:
                movimentoBolaX = velocidade
            elif evento.key == pygame.K_UP:
                movimentoBolaY = velocidade * -1
            elif evento.key == pygame.K_DOWN:
                movimentoBolaY = velocidade
        elif evento.type == pygame.KEYUP:
            movimentoBolaX = 0
            movimentoBolaY = 0
    
    # Controlando o objeto para não sair da tela
    if posicaoBolaX + movimentoBolaX + tamanhoXBola < largura and posicaoBolaX + movimentoBolaX > 0:
        posicaoBolaX = posicaoBolaX + movimentoBolaX

    if posicaoBolaY +movimentoBolaY + tamanhoYBola < altura and posicaoBolaY + movimentoBolaY > 0:
        posicaoBolaY = posicaoBolaY + movimentoBolaY

    display.fill(branco)
    display.blit(fundo , (0,0) )
    posicao = (posicaoBolaX,posicaoBolaY) # tupla 
    #pygame.draw.circle(display, cor ,posicao, 10)
    display.blit(bola , (posicaoBolaX,posicaoBolaY) )

    if posicaoBolaY < 8 and posicaoBolaX> 173 and posicaoBolaX < 279:
        placarPlayer1 += 1
        posicaoBolaX = 202
        posicaoBolaY = 283

    if posicaoBolaY > 552 and posicaoBolaX> 173 and posicaoBolaX < 279:
        placarPlayer2 += 1
        posicaoBolaX = 202
        posicaoBolaY = 283


    escreverTexto("Placar "+str(placarPlayer1)+" x "+str(placarPlayer2))
    pygame.display.update()
    fps.tick(60)


print("Volte Sempre!")
