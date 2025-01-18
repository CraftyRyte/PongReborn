import pygame as pyg

class Entity:
    def __init__(self, position, entity_type):
        import main
        self.type = entity_type
        self.rect = pyg.Surface(position).get_rect(center=tuple(position))
        main.ALL_ENTITIES.append(self)
    
    def get_collisions(self):
        import main
        a = []
        for entity in main.ALL_ENTITIES:
            if self.rect.colliderect(entity.rect):
                a.append(entity)
        return a 
        
