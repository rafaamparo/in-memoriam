def vitoria():

    import pygame
    import menu
    import creditos

    pygame.init()

    janela = pygame.display.set_mode((640,640))
    pygame.display.set_caption('IN MEMORIAM')
    clock = pygame.time.Clock()
    background = pygame.image.load("./assets/vitoria.png").convert()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                menu.menu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                     creditos.creditos()


        janela.blit(background, (0, 0))


        pygame.display.update()
        clock.tick(60)