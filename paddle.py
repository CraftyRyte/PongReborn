import pygame as pyg
import entity as ent

class Paddle(ent.Entity):
    def __init__(self, position, width, height, entity_type):
        super().__init__(position, entity_type)
        
        self.rect = pyg.Surface(position).get_rect(center=tuple(position), width=width, height=height)

        self.velocity = 0
    
        