import pygame
import random
import math

class Zumbi(pygame.sprite.Sprite):
    def __init__(self, x, y, grupo_colisao, grupo_camera, mapa, player, grupo_zumbi, janela):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load("./assets/zumbi_sprites/run_0.png").convert_alpha())
        self.sprites.append(pygame.image.load("./assets/zumbi_sprites/run_1.png").convert_alpha())
        self.sprites.append(pygame.image.load("./assets/zumbi_sprites/run_2.png").convert_alpha())
        self.sprites.append(pygame.image.load("./assets/zumbi_sprites/run_3.png").convert_alpha())
        self.sprites.append(pygame.image.load("./assets/zumbi_sprites/run_4.png").convert_alpha())
        self.sprites.append(pygame.image.load("./assets/zumbi_sprites/run_5.png").convert_alpha())
        self.sprites.append(pygame.image.load("./assets/zumbi_sprites/run_6.png").convert_alpha())
        self.sprites.append(pygame.image.load("./assets/zumbi_sprites/run_7.png").convert_alpha())
        self.mask = pygame.mask.from_surface(pygame.image.load("./assets/zumbi_sprites/mask.png").convert_alpha())
        self.current_frame = 0
        self.janela = janela
        self.vida_atual = 2
        self.vida_max = 2
        self.player = player
        self.grupo_zumbi = grupo_zumbi
        self.zumbiMinDistance = 100
        self.image = self.sprites[int(self.current_frame)]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.velocidade = random.uniform(1.0,2.0)
        self.grupo_colisao = grupo_colisao
        self.mapa = mapa
        self.grupo_colisao = grupo_colisao
        self.invert = False
        self.grupo_camera = grupo_camera
        grupo_camera.add(self)

        if self.player.zumbiUmaVida:
            self.vida_atual = 1
            self.vida_max = 1

    
    def barradevida(self):
        pygame.draw.rect(self.image,(255,0,0), (10,-2,20,5))
        pygame.draw.rect(self.image,(0,255,0), (10,-2,20*(self.vida_atual/self.vida_max),5))
        
    def checkColision(self):
        for obj in self.grupo_colisao:
            return pygame.sprite.collide_mask(self, obj)


    def update(self):
        
        self.current_frame += 0.1
        if self.current_frame >= len(self.sprites):
            self.current_frame = 0
        if self.invert:
            self.image = pygame.transform.flip(self.sprites[int(self.current_frame)], True, False)
        else:
            self.image = self.sprites[int(self.current_frame)]
        self.barradevida()

    def seguir_protagonista(self):
        self.update()
        dx = self.player.rect.x - self.rect.x
        dy = self.player.rect.y - self.rect.y
        if dx < 0 and not self.invert:
            self.invert = True
        if dx > 0 and self.invert:
            self.invert = False
        dist = math.hypot(dx, dy)
        if pygame.sprite.collide_mask(self, self.player):
            dx = random.randint(100,300)
            dy = random.randint(100,300)
            self.player.vidas -= 1
        else:
            dx /= dist
            dy /= dist

        # evitar colisão entre zumbis
        separation_force = self.separation()
        dx += separation_force[0]
        dy += separation_force[1]

        self.rect.x += dx * self.velocidade
        self.rect.y += dy * self.velocidade

    def separation(self):
        sum_dx = 0
        sum_dy = 0
        count = 0
        avg_dx = 0
        avg_dy = 0

        for zombie in self.grupo_zumbi:
            if zombie != self:
                dist_x = self.rect.x - zombie.rect.x
                dist_y = self.rect.y - zombie.rect.y
                distance = math.hypot(dist_x, dist_y)

                if distance < self.zumbiMinDistance:
                    if distance < 1:
                        distance = 1

                    sum_dx += dist_x / distance
                    sum_dy += dist_y / distance
                    count += 1

        if count > 0:
            avg_dx = sum_dx / count
            avg_dy = sum_dy / count
            avg_dist = math.hypot(avg_dx, avg_dy)
            if avg_dist > 0:
                avg_dx /= avg_dist
                avg_dy /= avg_dist

        return avg_dx, avg_dy
        
    