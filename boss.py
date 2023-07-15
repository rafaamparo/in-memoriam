import pygame
import random
import math
import os

class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y, grupo_colisao, grupo_camera, mapa, player, janela):
        super().__init__()

        self.initAnimations()
        self.janela = janela
        self.vida_atual = 10
        self.vida_max = 10
        self.player = player
        self.image = self.sprites[int(self.current_sprite)]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.velocidade = 3
        self.grupo_colisao = grupo_colisao
        self.grupo_camera = grupo_camera
        self.mapa = mapa

        grupo_camera.add(self)
    
    def initAnimations(self):
        self.sprites = []
        self.animations = {'idle': [], 'walking': [], 'attacking': [], 'dying': []}
        self.velocidade_animacao = 0.2
        self.status = 'idle'
        self.facing_right = True

        self.sprites = [pygame.image.load('./assets/boss_sprites/' + img) for img in os.listdir('./assets/boss_sprites')]
        for i in range(0,9):
            self.animations['idle'].append(self.sprites[i])
        for i in range(9,16):
            self.animations['walking'].append(self.sprites[i])
        for i in range(16,27):
            self.animations['attacking'].append(self.sprites[i])
        for i in range(28,54):
            self.animations['dying'].append(self.sprites[i])

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
            


    def barradevida(self):
        pygame.draw.rect(self.image,(255,0,0), (10,-2,40,8))
        pygame.draw.rect(self.image,(0,255,0), (10,-2,40*(self.vida_atual/self.vida_max),8))
        

    def update(self):
        self.barradevida()




    def seguir_protagonista(self):
        
        self.update()
        dx = self.player.rect.x - self.rect.x
        dy = self.player.rect.y - self.rect.y
        if dx < 0 and self.facing_right:
            self.facing_right = False
        if dx > 0 and not self.facing_right:
            self.facing_right = True
        dist = math.hypot(dx, dy)
        if dist == 0:
            dist = 1
        if pygame.sprite.collide_mask(self, self.player):
            self.rect.x = random.randint(100,900)
            self.rect.y = random.randint(100,600)
        else:
            dx /= dist
            dy /= dist

        separation_force = self.separation()
        dx += separation_force[0]
        dy += separation_force[1]


        self.rect.x += dx * self.velocidade
        self.rect.y += dy * self.velocidade

        if dist < 90:
            self.animate('attacking')
        else:
            self.animate('walking')

    def separation(self):

        avg_dx = 0
        avg_dy = 0

        return avg_dx, avg_dy
        
