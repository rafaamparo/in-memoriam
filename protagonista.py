import pygame
import math
import tiros

class Protagonista(pygame.sprite.Sprite):
    def __init__(self, x, y, grupo_tiros, grupo_colisao, grupo_camera, mapa, screen):
        super().__init__(grupo_camera)
        
        self.initAnimations()

        self.grupo_tiros = grupo_tiros
        self.grupo_camera = grupo_camera
        self.grupo_colisao = grupo_colisao

        self.direcao = 'direita'
        self.direction = pygame.math.Vector2()
        self.screen = screen
        self.mapa = mapa
        self.velocidade = 3
        self.dinheiro = 30
        self.poderFinal = 0
        
        self.roundsID = [0,0,0,0,0]
        self.velocidadeMaior = False
        self.modoTeleguiado = False
        self.tiroInfinito = False
        self.tiroRapido = False
        self.zumbiUmaVida = False
        
        self.dano = 1
        self.vidas = 3

        self.delay_contador = 0
        self.delay = 0.5

        self.mask = pygame.mask.from_surface(pygame.image.load("./assets/sprites_mina/mask.png").convert_alpha())
        self.rect = self.image.get_rect(center = (x,y))
        self.position = pygame.math.Vector2(x, y)


    def updatePowers(self, round):
        self.velocidadeMaior = self.roundsID[0] > round
        self.tiroRapido = self.roundsID[1] > round
        self.tiroInfinito = self.roundsID[2] > round
        self.modoTeleguiado = self.roundsID[3] > round
        self.zumbiUmaVida = self.roundsID[4] > round

        if self.poderFinal == 1:
            self.vidas = 12
        elif self.poderFinal == 2:
            self.dano = 2
        else:
            self.dano = 1
            self.vidas = 3

        if self.velocidadeMaior:
            self.velocidade = 5
        else:
            self.velocidade = 3

        if self.tiroRapido:
            self.delay = 0.2
        else:
            self.delay = 0.5

        if self.tiroInfinito:
            self.delay = 0.1
        elif self.tiroRapido:
            self.delay = 0.2
        else:
            self.delay = 0.5
        

    def initAnimations(self):
        self.sprites = []
        self.animations = {'idle': [], 'walking': [], 'walkingUp': [], 'walkingDown': []}
        self.velocidade_animacao = 0.2
        self.status = 'idle'
        self.facing_right = True


        self.sprites.append(pygame.image.load("./assets/sprites_mina/minafrente1.png").convert_alpha())
        self.sprites.append(pygame.image.load("./assets/sprites_mina/minafrente2.png").convert_alpha())
        self.sprites.append(pygame.image.load("./assets/sprites_mina/minafrente3.png").convert_alpha())
        self.sprites.append(pygame.image.load("./assets/sprites_mina/minafrente4.png").convert_alpha())
        self.sprites.append(pygame.image.load("./assets/sprites_mina/minacostas1.png").convert_alpha())
        self.sprites.append(pygame.image.load("./assets/sprites_mina/minacostas2.png").convert_alpha())
        self.sprites.append(pygame.image.load("./assets/sprites_mina/minacostas3.png").convert_alpha())
        self.sprites.append(pygame.image.load("./assets/sprites_mina/minacostas4.png").convert_alpha())
        self.sprites.append(pygame.image.load("./assets/sprites_mina/mina1.png").convert_alpha())
        self.sprites.append(pygame.image.load("./assets/sprites_mina/mina2.png").convert_alpha())
        self.sprites.append(pygame.image.load("./assets/sprites_mina/mina3.png").convert_alpha())
        self.sprites.append(pygame.image.load("./assets/sprites_mina/mina4.png").convert_alpha())

        for i in range(0,3):
            self.animations['walkingDown'].append(self.sprites[i])
        for i in range(4,8):
            self.animations['walkingUp'].append(self.sprites[i])
        for i in range(9,12):
            self.animations['walking'].append(self.sprites[i])

        self.animations['idle'].append(self.sprites[0])

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

    def animate(self, animation):
        animation = self.animations[animation]

        self.current_sprite += self.velocidade_animacao
        if self.current_sprite >= len(animation):
            self.current_sprite = 0
        
        image = animation[int(self.current_sprite)]
        if self.facing_right:
            self.image = image
        else:
            self.image = pygame.transform.flip(image, True, False)

    def get_status(self):
        if self.direction.x == 1:
            self.status = 'walking'
            self.facing_right = True
            self.direcao = 'direita'
            self.animations['idle'][0] = (self.sprites[8])
        elif self.direction.x == -1:
            self.status = 'walking'
            self.direcao = 'esquerda'
            self.facing_right = False
            self.animations['idle'][0] = (self.sprites[8])
        elif self.direction.y == 1:
            self.status = 'walkingDown'
            self.direcao = 'baixo'
            self.facing_right = True
            self.animations['idle'][0] = (self.sprites[0])
        elif self.direction.y == -1:
            self.status = 'walkingUp'
            self.direcao = 'cima'
            self.facing_right = True
            self.animations['idle'][0] = (self.sprites[4])
        elif self.direction.x == 1/1.4142 and self.direction.y == 1/1.4142:
            self.status = 'walking'
            self.facing_right = True
            self.animations['idle'][0] = (self.sprites[0])
        elif self.direction.x == -1/1.4142 and self.direction.y == 1/1.4142:
            self.status = 'walking'
            self.facing_right = False
            self.animations['idle'][0] = (self.sprites[0])
        elif self.direction.x == 1/1.4142 and self.direction.y == -1/1.4142:
            self.status = 'walking'
            self.facing_right = True
            self.animations['idle'][0] = (self.sprites[0])
        elif self.direction.x == -1/1.4142 and self.direction.y == -1/1.4142:
            self.status = 'walking'
            self.facing_right = False
            self.animations['idle'][0] = (self.sprites[0])
        else:
            self.status = 'idle'

    def player_input(self):
        teclas = pygame.key.get_pressed()
        dx = teclas[pygame.K_d] - teclas[pygame.K_a]
        dy = teclas[pygame.K_s] - teclas[pygame.K_w]
        self.direction = pygame.math.Vector2(dx, dy)
        if dx != 0 and dy != 0:
            self.direction /= 1.4142

        
        self.position += self.direction * self.velocidade
        self.rect.x = round(self.position.x)
        self.rect.y = round(self.position.y) 

        for objeto in self.grupo_colisao:
            if pygame.sprite.collide_mask(objeto, self):
                self.position -= self.direction * (self.velocidade)
                self.rect.x = round(self.position.x)
                self.rect.y = round(self.position.y) 
                break
        
        if teclas[pygame.K_SPACE]:
            if self.delay_contador >= self.delay:
                self.delay_contador = 0
                self.atirar()

    def player_shoot(self):
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            if self.delay_contador >= self.delay:
                self.delay_contador = 0

                start = pygame.math.Vector2(self.rect.x, self.rect.y)
                mouse_position = pygame.mouse.get_pos()

                # ajustando a posição do mouse para a posição da camera
                mouse_position = mouse_position + self.grupo_camera.offset

                # calculando a direção do tiro
                distance = mouse_position - start
                if distance[0] == 0:
                    distance[0] = 1
                if distance[1] == 0:
                    distance[1] = 1
                mouseDirectionVec = distance.normalize()

                bulletRotation = math.degrees(math.atan2(mouseDirectionVec[1], mouseDirectionVec[0]))
                
                if bulletRotation > -106 and bulletRotation < -70:
                    bulletRotation = 0
                elif bulletRotation > 70 and bulletRotation < 106:
                    bulletRotation = 0
                elif bulletRotation > -16 and bulletRotation < 16:
                    bulletRotation = 90
                elif bulletRotation > 164 or bulletRotation < -164:
                    bulletRotation = 90
                elif bulletRotation > -164 and bulletRotation < -106:
                    bulletRotation = -135
                elif bulletRotation > 16 and bulletRotation < 70:
                    bulletRotation = -135
                else:
                    bulletRotation = 135

                tiros.Tiro(self.rect.centerx, self.rect.centery, "./assets/tiro.png", self.grupo_tiros, "mouse", self.grupo_colisao, self.grupo_camera, self.mapa, mouseDirectionVec, bulletRotation)

    def update(self):

        self.delay_contador += 1/60
        self.player_input()
        self.player_shoot()
        self.get_status()
        self.animate(self.status)

       
    def atirar(self):
        if self.direcao == "cima":
            tiros.Tiro(self.rect.centerx - 20 , self.rect.centery - 20, "./assets/tiro.png", self.grupo_tiros, self.direcao, self.grupo_colisao, self.grupo_camera, self.mapa)
        elif self.direcao == "baixo":
            tiros.Tiro(self.rect.centerx + 15, self.rect.centery - 17, "./assets/tiro.png", self.grupo_tiros, self.direcao, self.grupo_colisao, self.grupo_camera, self.mapa)
        elif self.direcao == "esquerda":
            tiros.Tiro(self.rect.centerx - 25, self.rect.centery - 14 , "./assets/tiro_horiz.png", self.grupo_tiros, self.direcao, self.grupo_colisao, self.grupo_camera, self.mapa)
        elif self.direcao == "direita":
            tiros.Tiro(self.rect.centerx + 20, self.rect.centery - 14, "./assets/tiro_horiz.png", self.grupo_tiros, self.direcao, self.grupo_colisao, self.grupo_camera, self.mapa)
