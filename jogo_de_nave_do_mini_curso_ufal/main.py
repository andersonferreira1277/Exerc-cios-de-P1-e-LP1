import pygame, sys, os, random, math, time

pygame.init()
pygame.mixer.init()

RESOLUCAO = (800, 600) # tupla

tela = pygame.display.set_mode(RESOLUCAO) 	# RESOLUCAO EH UMA TUPLA
					# OUTRA FORMA SERIA pygame.display.set_mode((800, 600))
#Cor da tela#
branco = (255,255,255)
#VERMELHO = (255, 0, 0)
#tela.fill(VERMELHO) #fill tambem eh uma tupla

#Imagem
caminho = os.path.join("images", "sky.jpg")
ceu = pygame.image.load(caminho).convert()
caminho = os.path.join("images", "bomber.png")
bomba = pygame.image.load(caminho).convert_alpha()
#fonte
fonte = pygame.font.Font(os.path.join('fontes', 'gta.ttf'), 32)
fonte2 = pygame.font.Font(os.path.join('fontes', 'gta.ttf'), 120)
#musica
som = pygame.mixer.Sound(os.path.join('sons', 'trilha.ogg'))
som.set_volume(0.5) # volume do som
laser = pygame.mixer.Sound(os.path.join('sons', 'laser.wav'))
laser.set_volume(0.5)

#rosa = (255, 170, 255)
caminho = os.path.join("images", "nave.png")
sprite = pygame.image.load(caminho).convert()
sprite.set_colorkey((255, 170, 255))

x = 0
y = 0
criar = True
i_raio = 22.5
pontos = 0
def inimigo():
    global x, y, criar
    if criar:
        x = random.randint(20, 780)
        criar = False
        y = 0
    if y > 600:
        criar = True
    y +=2
    tela.blit(bomba, (x-i_raio, y-i_raio))
##################################
x3 = 0
y3 = 0
t_raio = 2.5
shot = pygame.Surface((5,5))
shot = shot.convert()
shot.fill(branco)
tiro_pronto = True

def tiro():
	global x3, y3, tiro_pronto, key
	if tiro_pronto:
		x3 = x2 - 3
		y3 = 480
	if key[pygame.K_SPACE] and tiro_pronto:
		tiro_pronto = False
		laser.play(0)
	if y3 < 0:
		tiro_pronto = True
	if not tiro_pronto:
		y3 -= 6
		tela.blit(shot, (x3-t_raio,y3-t_raio))
#################################
x2 = 450
y2 = 530
index = 0
frame = 0.0
n_raio = 50
vida = 3
def nave():
    global index, x2, y2, frame, key
    if x2 >= 750:
        if key[pygame.K_RIGHT]:
            pass
        if key[pygame.K_LEFT]:
            x2 -= 5
    if x2 <= 50:
        if key[pygame.K_LEFT]:
            pass
        if key[pygame.K_RIGHT]:
            x2 += 5
    if x2 >=50 and x2 <= 750:
        if key[pygame.K_LEFT]:
            x2 -= 5
        elif key[pygame.K_RIGHT]:
            x2 += 5
    if frame >= 1.0:
        index += 95
        frame = 0.0
    if index >= (95*3):
        index = 0
    frame += 0.1    

    tela.blit(sprite, (x2 - n_raio, y2 - n_raio), (index, 0, 93, 100))

def distancia(x, y, x2, y2):
	_distancia = math.sqrt((x-x2)**2+(y-y2)**2)
	return _distancia
def GUI():
	surface = fonte.render('Vidas: '+ str(vida), True, branco)
	tela.blit(surface, (10,10))
	surface = fonte.render('Pontos: '+ str(pontos), True, branco)
	tela.blit(surface, (10, 30))

clock = pygame.time.Clock()
running = True
audio = False
while running:
    clock.tick(60)
    if not audio:
        som.play(-1)
        audio = True
    key = pygame.key.get_pressed()
    pygame.display.set_caption("FPS %.2f" % clock.get_fps())
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # verificacao para fechar o programa
            running = False
    #############colisao nave e inimigo
    if distancia(x, y, x2, y2) < (i_raio + n_raio):  
        vida -= 1
        criar = True
	##################
    if distancia(x, y, x3, y3) < (i_raio + t_raio) and not tiro_pronto:
        criar = True
        tiro_pronto = True
        pontos += 1
    tela.blit(ceu, (0, 0))
    inimigo()
    nave()
    tiro()
    GUI()
    if vida <= 0:
        surface2 = fonte2.render('Gamer Over', True, branco)
        tela.blit(surface2, (200,200))
        running = False
    pygame.display.update()
if vida < 1:
    time.sleep(5)
pygame.display.quit()
sys.exit()
