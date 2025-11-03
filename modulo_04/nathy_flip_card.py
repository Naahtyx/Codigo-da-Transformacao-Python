'''
Primicia - jogo de Cartas Viradas com Pygame
'''

import pygame
# Biblioteca padrão
import random
# Biblioteca do sistema 
import time
# Biblioteca do sistema - contador
import os
# Sistema de salvamento

def resolver_caminho_recurso(caminho_relativo):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, caminho_relativo)

pygame.init()
LARGURA, ALTURA = 800,600
COR_FUNDO = (20, 20, 20)
COR_TEXTO = (255, 255, 255)

caminho_imagens = "imagens"
NOMES_IMAGENS = [
    "imagem1.png", "imagem2.png", "imagem3.png", "imagem4.png", "imagem5.png", "imagem6.png",
]

VERSO_NOME = "verso.png"

TAMANHO_CARTA = (100, 100)
ALTURA_PLACAR = 50 
AREA_JOGO_Y = ALTURA_PLACAR 

caminho_verso = resolver_caminho_recurso(os.path.join(caminho_imagens, VERSO_NOME))
try:
    VERSO_CARTA_IMG = pygame.image.load(caminho_verso)
    VERSO_CARTA_IMG = pygame.transform.scale(VERSO_CARTA_IMG, TAMANHO_CARTA)
except pygame.error as e:
    print(f"ERRO: Não foi possível carregar o verso da carta: {e}")
    exit ()

dados_imagens = []
for nome_arquivo in NOMES_IMAGENS:

    img_path = resolver_caminho_recurso(os.path.join(caminho_imagens, nome_arquivo))
try:
    image_surface+pygame.image.load(img_path)
    image_surface=pygame.transform.scale(imagem_surface, TAMANHO_CARTA)
    dados_imagens.append((image_surface, nome_arquivo))