import pygame
pygame.mixer.init()
musica = pygame.mixer.Sound("./assets/musicajogo.mp3").play(-1).set_volume(0.1)
def menu():
    import controle
    pygame.init()
    janela = pygame.display.set_mode((640,640))
    pygame.display.set_caption('IN MEMORIAM')
    clock = pygame.time.Clock()
    background = pygame.image.load("./assets/menu_1.png").convert()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                controle.controle()
            


        janela.blit(background, (0, 0))


        pygame.display.update()
        clock.tick(60)
