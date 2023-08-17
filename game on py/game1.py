import pygame

pygame.init()
win = pygame.display.set_mode((500, 500)) # размеры X и Y
pygame.display.set_caption("Питон")

player = pygame.image.load("./GAME ON PY/green/men.png")
bg = pygame.image.load("./GAME ON PY/fon/eatrh.jpeg")
run = True
while(run):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False	

win.blit(bg, (0, 0))
win.blit(player (50, 50))


pygame.quit()


