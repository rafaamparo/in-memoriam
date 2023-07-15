def creditos():

    import pygame
    import menu

    pygame.init()

    janela = pygame.display.set_mode((640,640))
    pygame.display.set_caption('IN MEMORIAM')
    clock = pygame.time.Clock()
    background = pygame.image.load("./assets/creditos.png").convert()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                     menu.creditos()

        janela.blit(background, (0, 0))


        pygame.display.update()
        clock.tick(60)