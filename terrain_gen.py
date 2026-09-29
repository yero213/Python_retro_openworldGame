import pygame
import random
import opensimplex

# --- instellingen ---
MAP_W, MAP_H = 128, 96      # aantal tiles
TILE = 8                    # pixels per tile
SCALE = 0.05                # lager = grotere landmassa's
OCTAVES = 5