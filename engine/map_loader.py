from ..imports import *

class TileMap:
    def __init__(self, width, height, tiles, spawn_points, tower_slots):
        self.width = width
        self.height = height
        self.tiles = tiles  # 2D list of tile values
        self.spawn_points = spawn_points  # list of (x, y)
        self.tower_slots = tower_slots    # list of (x, y)
        self.tile_size = 64  # pixels per tile (customizable)

    def draw(self, surface):
        colors = {
            0: (34, 139, 34),  # grass
            1: (139, 69, 19),  # path
            2: (200, 200, 50)  # tower slot
        }
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                rect = pygame.Rect(x * self.tile_size, y * self.tile_size,
                                   self.tile_size, self.tile_size)
                pygame.draw.rect(surface, colors.get(tile, (255, 0, 0)), rect)
                pygame.draw.rect(surface, (0, 0, 0), rect, 1)  # border

class MapLoader:
    @staticmethod
    def load_map(path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        tiles = data["tiles"]
        width = data["width"]
        height = data["height"]
        spawn_points = [(p["x"], p["y"]) for p in data["spawn_points"]]
        tower_slots  = [(p["x"], p["y"]) for p in data["tower_slots"]]

        return TileMap(width, height, tiles, spawn_points, tower_slots)
    
    @staticmethod
    def save_map(tile_map: TileMap, file_path: str):
        """Save map to JSON file"""
        pass