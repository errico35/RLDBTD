from ..imports import *

class EntityManager:
    def __init__(self):
        # Attributes: entities, collision_groups
        pass
    
    def add_entity(self, entity, group: str = "default"):
        """Add entity to manager"""
        pass
    
    def remove_entity(self, entity):
        """Remove entity from manager"""
        pass
    
    def get_entities_by_group(self, group: str) -> list:
        """Get all entities in specific group"""
        pass
    
    def update_all(self, dt: float):
        """Update all managed entities"""
        pass
    
    def check_collisions(self, group1: str, group2: str) -> list:
        """Check collisions between two groups"""
        pass
    
    def draw_all(self, surface: pygame.Surface):
        """Render all entities"""
        pass
    
    def cleanup_dead_entities(self):
        """Remove entities marked for deletion"""
        pass