from ..imports import *

class LevelNode:
    def __init__(self, x: int, y: int, level_id: str, unlocked: bool = False):
        # Attributes: pos, level_id, unlocked, completed, rect
        pass
    
    def draw(self, surface: pygame.Surface):
        """Render level node"""
        pass
    
    def is_clicked(self, mouse_pos: tuple) -> bool:
        """Check if node was clicked"""
        pass

class WorldMapScreen:
    def __init__(self, state_manager):
        # Attributes: background_image, level_nodes, camera_pos, state_manager
        pass
    
    def load_world_data(self, file_path: str):
        """Load world map configuration"""
        pass
    
    def setup_level_nodes(self):
        """Initialize level selection nodes"""
        pass
    
    def handle_events(self, events: list):
        """Process input events"""
        pass
    
    def update(self, dt: float):
        """Update world map state"""
        pass
    
    def draw(self, surface: pygame.Surface):
        """Render world map screen"""
        pass
    
    def on_level_selected(self, level_id: str):
        """Handle level selection"""
        pass
    
    def on_back_to_menu(self):
        """Return to main menu"""
        pass