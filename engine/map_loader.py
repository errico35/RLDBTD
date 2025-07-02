from ..imports import *

class TileMap:
    def __init__(self, width: int, height: int):
        # Attributes: width, height, tiles (2D list), spawn_points, tower_positions, path_tiles
        pass
    
    def get_tile(self, x: int, y: int) -> str:
        """Get tile type at coordinates"""
        pass
    
    def set_tile(self, x: int, y: int, tile_type: str):
        """Set tile type at coordinates"""
        pass
    
    def is_valid_tower_position(self, x: int, y: int) -> bool:
        """Check if tower can be placed at position"""
        pass
    
    def get_spawn_points(self) -> list:
        """Return list of enemy spawn coordinates"""
        pass
    
    def get_path_to_goal(self, start_pos: tuple) -> list:
        """Calculate path from start to goal using pathfinding"""
        pass
    
    def draw(self, surface: pygame.Surface, camera_offset: tuple = (0, 0)):
        """Render the tile map to surface"""
        pass

class MapLoader:
    @staticmethod
    def load_map(file_path: str) -> TileMap:
        """
        Load map from JSON file
        Expected format:
        {
            "width": int,
            "height": int,
            "tiles": [[tile_type, ...], ...],
            "spawn_points": [[x, y], ...],
            "goal_points": [[x, y], ...],
            "tower_positions": [[x, y], ...]
        }
        """
        pass
    
    @staticmethod
    def save_map(tile_map: TileMap, file_path: str):
        """Save map to JSON file"""
        pass