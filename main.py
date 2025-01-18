import pygame as pyg
import sys
import entity
import data

pyg.init()

# Window Opt
WIDTH,HEIGHT = 800, 800
ALL_ENTITIES = []
screen = pyg.display.set_mode((WIDTH, HEIGHT))
pyg.display.set_caption("Pong Reborn")

def draw():
    pass

# Game loop
is_running = True
while is_running:
    # event loop and quit logic
    for e in pyg.event.get():
        # Quit Logic
        if e.type == pyg.QUIT:
            print("hi")
            is_running = False
    # LOGIC
    # -------------------------------------------------------
    
    # -------------------------------------------------------
    
    # DRAWING
    # -------------------------------------------------------
    
    
    # -------------------------------------------------------

    # update logic
    pyg.display.update()
    

pyg.quit()
sys.exit(69)
