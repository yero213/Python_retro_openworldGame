from PIL import Image


def get_tile(path, x, y, size=16):
    tileset=path
    return tileset.crop((
        x * size,
        y * size,
        (x + 1) * size,
        (y + 1) * size
    ))

tile = get_tile(3, 1)
tile.save("tile.png")