
def jogo():
    import pygame
    import sys
    import protagonista
    import coisas
    import camera
    import zumbi
    import random
    import boss
    import oferecimentos
    import gameover
    import vitoria

    pygame.init()
    janela = pygame.display.set_mode((640,640))
    pygame.display.set_caption('IN MEMORIAM')
    clock = pygame.time.Clock()
    background = pygame.Surface(janela.get_size())
    background.fill((0, 0, 0))
    mapa = pygame.image.load("./assets/mapa_santuario_apenas_caminho.png").convert()
    camada =  pygame.image.load("./assets/camada.png").convert_alpha()


    mapax = 0
    mapay = 0

    moeda = pygame.image.load("./assets/moeda.png").convert_alpha()
    coracao = pygame.image.load("./assets/coracao.png").convert_alpha()
    round = 1
    timer = 0
    tempoRound = 20
    pausa = False
    quantidade = 5
    grupo_zumbi = pygame.sprite.Group()
    grupo_colidiveis = pygame.sprite.Group()
    camadaColisao = coisas.Objeto(0, 0, camada)
    grupo_colidiveis.add(camadaColisao)
    grupo_tiros = pygame.sprite.Group()

    boossBattle = False
    mostrarJanelasBoss = True
    alternarJanelas = False

    escolha = 0
    spawnBoss = False
    grupo_boss = pygame.sprite.Group()

    screen_shake = 0

    grupo_camera = camera.CameraGroup(mapa, camada)
    personagem = protagonista.Protagonista(800, 700,grupo_tiros, grupo_colidiveis, grupo_camera, mapa, janela)

    def generateRandomValues():
        zumbiPrototipo = zumbi.Zumbi(random.randint(-300,600),random.randint(-300,600),grupo_colidiveis, grupo_camera, mapa, personagem, grupo_zumbi, janela)
        valor = zumbiPrototipo.checkColision() 
        if valor == True:
            grupo_camera.remove(zumbiPrototipo)
            return generateRandomValues()
        else:
            return zumbiPrototipo

    for i in range(quantidade):
        zumbi1 = generateRandomValues()
        grupo_zumbi.add(zumbi1)
    # boss = boss.Boss(random.randint(0,900),random.randint(0,900),grupo_colidiveis, grupo_camera, mapa, personagem, janela)

    fonte1 = pygame.font.Font('./assets/joystix.otf', 32)
    fonte2 = pygame.font.Font('./assets/joystix.otf', 20)

    velocidadeMaiorCard = oferecimentos.Ofertas(115, 140, "./assets/ofertas/velocidade.png", 0, 75, personagem)
    tiroRapidoCard = oferecimentos.Ofertas(115, 250, "./assets/ofertas/tiro_rapido.png", 1, 90, personagem)
    zumbiUmaVidaCard = oferecimentos.Ofertas(janela.get_width() - 115, 140, "./assets/ofertas/zumbiumavida.png", 4, 200, personagem)
    tiroInfinitoCard = oferecimentos.Ofertas(janela.get_width() - 115, 250, "./assets/ofertas/tiroinfinito.png", 2, 150, personagem)


    world_data = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0], #0
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #1
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #2
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #3
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0], #4
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #5 
            [0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #6
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #7
            [0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #8
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #9
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #10
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #11
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #12
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #13
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #14
            [0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #15
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #16
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #17
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #18
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #19
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #20
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #21
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #22
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #23
            [0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,8,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #24
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #25
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0], #26
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #27
            [0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #28
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #29
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #30
            [0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #31
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #32
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #33
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #34
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #35
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #36
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #37
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #38
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #39
    ]

    def get_x(x):
        return x*32 + mapax

    def get_y(y):
        return y*32 + mapay

    for y in range(0, len(world_data)):
        for x in range(0, len(world_data[y])):
            if world_data[y][x] == 99:
                imagem = pygame.Surface((32,32))
                imagem.fill((255,0,0))
                imagem.set_alpha(0)
                objeto = coisas.Objeto(get_x(x), get_y(y), imagem)
                grupo_colidiveis.add(objeto)
                grupo_camera.add(objeto)

            if world_data[y][x] != 0 and world_data[y][x] != 99:
                numero = world_data[y][x]
                imagem = pygame.image.load(f"./assets/objetos_sanct/{str(numero)}.png").convert_alpha()
                objeto = coisas.Objeto(get_x(x), get_y(y), imagem)
                if world_data[y][x] != 8 and world_data[y][x] != 7:
                    grupo_colidiveis.add(objeto)
                grupo_camera.add(objeto)

    mostrarVendas = [0,0,0,0,0]


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        janela.blit(background, (0,0))

        
        if screen_shake > 0:
            screen_shake -= 1

        grupo_camera.custom_draw(personagem, screen_shake)
        personagem.update()
        for tiro in grupo_tiros:
            tiro.update()
            for zombie in grupo_zumbi:
                if pygame.sprite.collide_rect(tiro, zombie):
                    grupo_tiros.remove(tiro)
                    grupo_camera.remove(tiro)
                    if zombie.vida_atual > 0:
                        zombie.vida_atual -= 1
                        if tiro.direcao == "cima":
                            zombie.rect.y -= random.randint(30,100)
                        elif tiro.direcao == "baixo":
                            zombie.rect.y -= random.randint(30,100)
                        elif tiro.direcao == "direita":
                            zombie.rect.x += random.randint(30,100)
                        else:
                            zombie.rect.x -= random.randint(30,100)
                        
        
        for zombie in grupo_zumbi:
            if zombie.vida_atual <= 0:
                screen_shake = 20
                grupo_zumbi.remove(zombie)
                grupo_camera.remove(zombie)
                personagem.dinheiro += 15
            if pygame.sprite.collide_mask(personagem, zombie):
                screen_shake = 20
            # print(zombie.rect.x, zombie.rect.y)

        if len(grupo_zumbi) == 0 and pausa == False:
            if personagem.vidas < 3:
                personagem.vidas += 1
            mostrarVendas = [0,0,0,0,0]
            timer = tempoRound
            pausa = True

        if len(grupo_zumbi) == 0 and pausa == True and timer <= 0 and not boossBattle:
            round += 1
            pausa = False
            quantidade *= 2
            if quantidade > 200:
                quantidade = 200
            for i in range(quantidade):
                zumbi2 = generateRandomValues()
                grupo_zumbi.add(zumbi2)
        
        if boossBattle:
            bencao1 = pygame.image.load("./assets/ofertas/bencao1.png").convert_alpha()
            bencao2 = pygame.image.load("./assets/ofertas/bencao2.png").convert_alpha()
            bencao1Rect = bencao1.get_rect()
            bencao2Rect = bencao2.get_rect()
            bencao1Rect.x = janela.get_width()/2 - bencao1.get_width()/2 + bencao2.get_width()/2
            bencao1Rect.y = janela.get_height()/2 - bencao1.get_height()/2
            bencao2Rect.x = janela.get_width()/2 - bencao2.get_width()/2 - bencao1.get_width()/2
            bencao2Rect.y = janela.get_height()/2 - bencao2.get_height()/2
            if escolha == 0:
                janela.blit(bencao2, bencao2Rect)
                janela.blit(bencao1, bencao1Rect)
            if escolha == 0:
                timer = 5
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if pygame.Rect.collidepoint(bencao1Rect, mouse):
                if click[0] == 1:
                    escolha = 1
                    personagem.poderFinal = 1
            if pygame.Rect.collidepoint(bencao2Rect, mouse):
                if click[0] == 1:
                    escolha = 2
                    personagem.poderFinal = 2
            if timer <= 0:
                # print("TImer zerou")
                if spawnBoss == False:
                    pausa = False
                    boss = boss.Boss(random.randint(0,900),random.randint(0,900),grupo_colidiveis, grupo_camera, mapa, personagem, janela)
                    grupo_boss.add(boss)
                    spawnBoss = True
                    print("BOSS")


        for zombie in grupo_zumbi:
            zombie.seguir_protagonista()

        if personagem.vidas <= 0:
            gameover.gameover()

        if pausa == True:
            personagem.updatePowers(round+1)
            
            if round%5 != 0:
                timer -= 1/60
                texto1 = fonte1.render(f"Próximo round em: {int(timer/60)}:{int(timer%60):02d}", True, (255, 255, 255))
                texto2 = fonte2.render(f"Aproveite para melhorar suas armas", True, (255, 255, 255))

                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if mostrarVendas[0] == 0:
                    velocidadeMaiorCard.draw(janela)
                    if velocidadeMaiorCard.rect.collidepoint(mouse):
                        if click[0] == 1:
                            mostrarVendas[0] = velocidadeMaiorCard.buy(round)

                if mostrarVendas[1] == 0:
                    tiroRapidoCard.draw(janela)
                    if tiroRapidoCard.rect.collidepoint(mouse):
                        if click[0] == 1:
                            mostrarVendas[1] = tiroRapidoCard.buy(round)

                if mostrarVendas[2] == 0:
                    tiroInfinitoCard.draw(janela)
                    if tiroInfinitoCard.rect.collidepoint(mouse):
                        if click[0] == 1:
                            mostrarVendas[2] = tiroInfinitoCard.buy(round)

                if mostrarVendas[4] == 0:
                    zumbiUmaVidaCard.draw(janela)
                    if zumbiUmaVidaCard.rect.collidepoint(mouse):
                        if click[0] == 1:
                            mostrarVendas[4] = zumbiUmaVidaCard.buy(round)
            else:
                timer -= 1/120
                texto1 = fonte1.render(f"Proposta BOSS: {int(timer/60)}:{int(timer%60):02d}", True, (255, 255, 255))
                texto2 = fonte2.render(f"Faça sua escolha", True, (255, 255, 255))
                imgBoss1 = pygame.image.load("assets/boss_1.png")
                imgBoss2 = pygame.image.load("assets/boss_2.png")

                if mostrarJanelasBoss and not alternarJanelas:
                    janela.blit(imgBoss1, (janela.get_width()/2 - imgBoss1.get_width()/2, janela.get_height()/2 - imgBoss1.get_height()/2))
                    mouse = pygame.mouse.get_pos()
                    click = pygame.mouse.get_pressed()
                    if imgBoss1.get_rect().collidepoint(mouse):
                        if click[0] == 1:
                            alternarJanelas = True
                if mostrarJanelasBoss and alternarJanelas:
                    janela.blit(imgBoss2, (janela.get_width()/2 - imgBoss2.get_width()/2, janela.get_height()/2 - imgBoss2.get_height()/2))

                    keyboard = pygame.key.get_pressed()
                    if keyboard[pygame.K_SPACE]:
                        mostrarJanelasBoss = False

                        if personagem.dinheiro >= 2000:
                            personagem.dinheiro -= 2000
                            boossBattle = True
                        else:
                            mostrarJanelasBoss = False
                            timer = 1

                    if keyboard[pygame.K_ESCAPE]:
                        mostrarJanelasBoss = False
                        boossBattle = False
                        timer = 1
        else: 
            texto1 = fonte1.render('Round: '+str(round), True, (255, 255, 255))
            texto2 = fonte2.render(f"{len(grupo_zumbi)} zumbis restantes", True, (255, 255, 255))
            
        texto3 = fonte2.render(str(personagem.dinheiro), True, (255, 255, 255))
        texto4 = fonte2.render(str(personagem.vidas), True, (255, 255, 255))

        if spawnBoss:
                texto1 = fonte1.render(f"BATALHA FINAL", True, (255, 255, 255))
                texto2 = fonte2.render(f"", True, (255, 255, 255))
                for boss in grupo_boss:
                    boss.seguir_protagonista()
                    if boss.vida_atual <= 0:
                        grupo_boss.remove(boss)
                        grupo_camera.remove(boss)
                        vitoria.vitoria()
                        print("BOSS MORREU")

                    for tiro in grupo_tiros:
                        if boss.rect.colliderect(tiro.rect):
                            grupo_tiros.remove(tiro)
                            grupo_camera.remove(tiro)
                            if escolha == 1:
                                boss.vida_atual -= 1
                            if escolha == 2:
                                boss.vida_atual -= 2
                            screen_shake = 20
                            print("BOSS TOMOU DANO")
                    
                    if pygame.sprite.collide_mask(boss, personagem):
                        personagem.vidas -= 1
                        print("PERSONAGEM TOMOU DANO")
                        screen_shake = 20
                    
                    

        janela.blit(texto1, (janela.get_width()/2 - texto1.get_width()/2,35))
        janela.blit(texto2, (janela.get_width()/2 - texto2.get_width()/2,70))
        janela.blit(moeda, (20,560))
        janela.blit(coracao, (20,600))
        janela.blit(texto4, (62, 603))
        janela.blit(texto3, (62, 560))
        pygame.display.update()
        clock.tick(60)