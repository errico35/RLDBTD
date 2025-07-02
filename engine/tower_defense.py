from ..imports import *
from .map_loader import TileMap

class Projectile:
    def __init__(self, start_pos: tuple, target_pos: tuple, damage: int, speed: float):
        # Attributes: pos, target_pos, damage, speed, active
        pass
    
    def update(self, dt: float):
        """Update projectile position"""
        pass
    
    def draw(self, surface: pygame.Surface):
        """Render projectile"""
        pass
    
    def has_hit_target(self) -> bool:
        """Check if projectile reached target"""
        pass

class ProjectileManager:
    def __init__(self, start_pos: tuple, target_pos: tuple, damage: int, speed: float):
        # Attributes: pos, target_pos, damage, speed, active
        pass
    
    def update(self, dt: float):
        """Update projectile position"""
        pass
    
    def draw(self, surface: pygame.Surface):
        """Render projectile"""
        pass
    
    def has_hit_target(self) -> bool:
        """Check if projectile reached target"""
        pass

class TowerManager:
    def __init__(self):
        # Attributes: towers, projectiles
        pass
    
    def add_tower(self, tower, position: tuple):
        """Place tower at position"""
        pass
    
    def remove_tower(self, position: tuple):
        """Remove tower from position"""
        pass
    
    def get_tower_at(self, position: tuple):
        """Get tower at specific position"""
        pass
    
    def update(self, dt: float, enemies: list):
        """Update all towers and projectiles"""
        pass
    
    def draw(self, surface: pygame.Surface):
        """Render all towers and projectiles"""
        pass

class WaveManager:
    def __init__(self, map_ref: TileMap):
        # Attributes: current_wave, wave_data, spawn_timer, enemies_spawned, map_ref
        pass
    
    def load_wave_data(self, file_path: str):
        """Load wave configuration from file"""
        pass
    
    def start_wave(self, wave_number: int):
        """Begin spawning wave"""
        pass
    
    def update(self, dt: float) -> list:
        """Update wave spawning, return list of new enemies"""
        pass
    
    def is_wave_complete(self) -> bool:
        """Check if current wave finished spawning"""
        pass
    
    def get_wave_info(self) -> dict:
        """Return current wave information"""
        pass