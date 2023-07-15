import pygame

class Tiro(pygame.sprite.Sprite):
    def __init__(self, x, y, imagem, group, direcao, grupo_colisao, grupo_camera, mapa, mouseDirectionVec = 0, bulletRotation = 0):
        super().__init__(grupo_camera)
        self.image = pygame.image.load(imagem).convert_alpha()
        self.image = pygame.transform.rotate(self.image, bulletRotation)
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        self.velocidade = 10
        self.grupo_camera = grupo_camera
        self.direcao = direcao
        self.group = group
        self.mapa = mapa
        self.mouseDirectionVec = mouseDirectionVec
        self.mapa_rect = self.mapa.get_rect()
        self.grupo_colisao = grupo_colisao
        
        self.display_surface = pygame.display.get_surface()
        group.add(self)


    def update(self):

        for objeto in self.grupo_colisao:
            for tiro in self.group:
                if (pygame.sprite.collide_mask(objeto, self)):
                    self.group.remove(tiro)
                    self.grupo_camera.remove(tiro)

        for tiro in self.group:
            if (tiro.rect.x >= self.mapa.get_width()) or (tiro.rect.x <= 0):
                self.group.remove(tiro)
                self.grupo_camera.remove(tiro)
            elif (tiro.rect.y >= self.mapa.get_height()) or (tiro.rect.y <= 0):
                self.group.remove(tiro)
                self.grupo_camera.remove(tiro)
        
        if self.direcao == "cima":
            self.rect.y -= self.velocidade

        elif self.direcao == "baixo":
            self.rect.y += self.velocidade


        elif self.direcao == "esquerda":
            self.rect.x -= self.velocidade

        elif self.direcao == "direita":
            self.rect.x += self.velocidade
        
        elif self.direcao == "mouse":
            
            self.rect.x += self.mouseDirectionVec[0]*self.velocidade
            self.rect.y += self.mouseDirectionVec[1]*self.velocidade
            
