import pygame
import noise
from PIL import Image
import Animator

pygame.init()
screen = pygame.display.set_mode((920, 720))
bg_color = (0, 0, 0)
pygame.display.set_caption('retro openworld')
clock = pygame.time.Clock()

def get_height(x, y, seed=0, scale=50.0):
    return noise.pnoise2(
        x / scale,
        y / scale,
        octaves=4,          # detailniveau (meer octaves = meer detail)
        persistence=0.5,    # hoe sterk elke octave meetelt
        lacunarity=2.0,     # frequentie-toename per octave
        base=seed           # dit is je "seed"
    )

def get_tile_type(x, y, seed):
    n = get_height(x, y, seed)
    if n < -0.3:
        return "water"
    elif n < -0.1:
        return "sand"
    elif n < 0.4:
        return "grass"
    else:
        return "forest"
print(get_height(920, 720))

def get_tile(tileset, x, y, size=16):
    tile = tileset.crop((
        x * size,
        y * size,
        (x + 1) * size,
        (y + 1) * size
    ))
    if tile.mode != "RGBA":
        tile = tile.convert("RGBA")
    alpha = tile.getchannel("A")
    if alpha.getbbox() is None:
        # volledig transparant -> lege tile
        return None
    return tile

tileset = Image.open("gfx/Overworld.png")

for i in range(100):
    for j in range(100):
        tile = get_tile(tileset, i, j)
        if tile is not None:
            tile.save(f"tile_{i}_{j}.png")

scale = (30,30)

grass = pygame.image.load("tile_0_0.png").convert()
grass_scaled = pygame.transform.scale(grass, scale)
water_1 = pygame.image.load("tile_0_2.png").convert()
water_2 = pygame.image.load("tile_1_2.png").convert()
water_3 = pygame.image.load("tile_2_2.png").convert()
water_4 = pygame.image.load("tile_3_2.png").convert()
water_5 = pygame.image.load("tile_0_2.png").convert()

water_1_scaled = pygame.transform.scale(water_1, scale)
water_2_scaled = pygame.transform.scale(water_2, scale)
water_3_scaled = pygame.transform.scale(water_3, scale)
water_4_scaled = pygame.transform.scale(water_4, scale)
water_5_scaled = pygame.transform.scale(water_5, scale)

water_animator = Animator.Animator([water_1_scaled, water_2_scaled, water_3_scaled, water_4_scaled, water_5_scaled], speed=0.01)

#def water_animation()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill(bg_color)

    tile_type = get_tile_type(920, 720, 0)
    screen.blit(grass_scaled, (100, 100, 130, 130))
    screen.blit(water_animator.update(), (100, 100, 130, 130))
    screen.blit(water_animator.update(), (130, 130,160, 160))

    pygame.display.flip()
    clock.tick(60)
