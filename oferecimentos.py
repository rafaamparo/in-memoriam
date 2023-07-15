import pygame

class Ofertas(pygame.sprite.Sprite):
    def __init__(self, x, y, img, id, valor, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.id = id
        self.valor = valor
        self.player = player	

    def buy(self, round):
        if self.player.dinheiro >= self.valor:
            self.player.dinheiro -= self.valor
            if self.id == 0:
                self.player.velocidadeMaior = True
                self.player.roundsID[0] = round+2
            if self.id == 1:
                self.player.tiroRapido = True
                self.player.roundsID[1] = round+3
            if self.id == 2:
                self.player.tiroInfinito = True
                self.player.roundsID[2] = round+2
            if self.id == 3:
                self.player.modoTeleguiado = True
                self.player.roundsID[3] = round+3
            if self.id == 4:
                self.player.zumbiUmaVida = True
                self.player.roundsID[4] = round+2

            return True
        else:
            return False


    def draw(self, screen):
        screen.blit(self.image, self.rect)
