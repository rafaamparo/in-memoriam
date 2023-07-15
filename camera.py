import pygame
import random


class CameraGroup(pygame.sprite.Group):
    def __init__(self, mapa, camada):
        super().__init__()

        self.mapa = mapa
        self.camada = camada
        self.display_surface = pygame.display.get_surface()

        self.offset = pygame.math.Vector2()
        self.map_rect = self.mapa.get_rect(topleft = (0,0))
    
        self.half_w = self.display_surface.get_size()[0] / 2
        self.half_h = self.display_surface.get_size()[1] / 2

        # Zoom
        self.zoom_scale = 2
        self.internal_surface_size = (self.display_surface.get_width(), self.display_surface.get_height())
        self.internal_surface = pygame.Surface(self.internal_surface_size, pygame.SRCALPHA)
        self.internal_surface_rect = self.internal_surface.get_rect(center = (self.half_w, self.half_h))
        self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surface_size)


    def center_target_camera(self, player):
        self.offset.x = player.rect.centerx - self.half_w
        self.offset.y = player.rect.centery - self.half_h

    def custom_draw(self, player, screen_shake = True):
        self.center_target_camera(player)
        self.internal_surface.fill((48, 44, 46))
        map_offset = self.map_rect.topleft - self.offset

        self.internal_surface.blit(self.mapa, map_offset)
        self.internal_surface.blit(self.camada, map_offset)
        for sprite in sorted(self.sprites(), key = lambda sprite: (sprite.rect.bottom)):
            offset_pos = sprite.rect.topleft - self.offset
            self.internal_surface.blit(sprite.image, offset_pos)

        scaled_surf = pygame.transform.scale(self.internal_surface, (int(self.internal_surface_size_vector.x * self.zoom_scale), int(self.internal_surface_size_vector.y * self.zoom_scale)))
        scaled_rect = scaled_surf.get_rect(center = (self.half_w, self.half_h))
        
        render_offset = [0,0]
        if screen_shake:
            render_offset[0] = random.randint(0, 16) - 4
            render_offset[1] = random.randint(0, 16) - 4
        else:
            render_offset[0] = 0
            render_offset[1] = 0
            
        scaled_rect.x += render_offset[0]
        scaled_rect.y += render_offset[1]

        self.display_surface.blit(scaled_surf, scaled_rect)