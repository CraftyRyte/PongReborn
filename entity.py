import pygame as pyg

class Entity:
    def __init__(self, position, entity_type):
        import main
        self.type = entity_type
        self.rect = pyg.Surface(position).get_rect(center=tuple(position))
        main.ALL_ENTITIES.append(self)

# test if entity gets updated once appended in the list  
        
