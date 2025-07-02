from ..imports import *
from ..engine.deck_system import Card

class UI:
    def __init__(self):
        # Attributes: font, energy_display, health_display, wave_info
        pass
    
    def update(self, player, wave_manager):
        """Update UI elements"""
        pass
    
    def draw(self, surface: pygame.Surface):
        """Render UI overlay"""
        pass
    
    def draw_card_preview(self, surface: pygame.Surface, card: Card, pos: tuple):
        """Show card tooltip"""
        pass

class LevelScreen:
    def __init__(self, state_manager, level_id: str):
        # Attributes: tile_map, player, tower_manager, wave_manager, entity_manager, ui, camera, state_manager
        pass
    
    def load_level(self, level_id: str):
        """Load level data and initialize systems"""
        pass
    
    def handle_events(self, events: list):
        """Process input events"""
        pass
    
    def update(self, dt: float):
        """Update all game systems"""
        pass
    
    def draw(self, surface: pygame.Surface):
        """Render complete game screen"""
        pass
    
    def handle_card_play(self, card: Card, target_pos: tuple):
        """Process card being played"""
        pass
    
    def handle_tower_placement(self, tower_type: str, pos: tuple):
        """Handle tower placement"""
        pass
    
    def check_win_condition(self) -> bool:
        """Check if level is completed"""
        pass
    
    def check_lose_condition(self) -> bool:
        """Check if level is failed"""
        pass
    
    def on_level_complete(self):
        """Handle level completion"""
        pass
    
    def on_level_failed(self):
        """Handle level failure"""
        pass
    
    def pause_game(self):
        """Pause/unpause game"""
        pass