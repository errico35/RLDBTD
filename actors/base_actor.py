from ..imports import *

class BaseActor:
    def __init__(self, x: float, y: float):
        # Attributes: pos, sprite, health, max_health, active, collision_rect
        pass
    
    def update(self, dt: float):
        """Update actor state"""
        pass
    
    def draw(self, surface: pygame.Surface):
        """Render actor"""
        pass
    
    def take_damage(self, amount: int):
        """Apply damage to actor"""
        pass
    
    def heal(self, amount: int):
        """Restore health to actor"""
        pass
    
    def is_alive(self) -> bool:
        """Check if actor is still alive"""
        pass
    
    def get_distance_to(self, other_pos: tuple) -> float:
        """Calculate distance to another position"""
        pass