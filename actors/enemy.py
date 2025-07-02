from ..imports import *
from .base_actor import BaseActor

class Enemy(BaseActor):
    def __init__(self, x: float, y: float, enemy_type: str):
        # Additional attributes: speed, path, path_index, reward_value, armor
        super().__init__(x, y)
    
    def set_path(self, path: list):
        """Set movement path for enemy"""
        pass
    
    def move_along_path(self, dt: float):
        """Move enemy along its path"""
        pass
    
    def reached_goal(self) -> bool:
        """Check if enemy reached the end"""
        pass
    
    def apply_slow(self, duration: float, intensity: float):
        """Apply slowing effect"""
        pass
    
    def get_reward_value(self) -> int:
        """Return reward for defeating this enemy"""
        pass

class EnemyFactory:
    @staticmethod
    def create_enemy(enemy_type: str, spawn_pos: tuple) -> Enemy:
        """Create enemy of specified type"""
        pass
    
    @staticmethod
    def load_enemy_data(file_path: str):
        """Load enemy definitions from file"""
        pass