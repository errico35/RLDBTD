from ..imports import *

class Button:
    def __init__(self, x: int, y: int, width: int, height: int, text: str, callback):
        # Attributes: rect, text, font, callback, hover_state
        pass
    
    def handle_event(self, event):
        """Process mouse events for button"""
        pass
    
    def update(self, mouse_pos: tuple):
        """Update button state"""
        pass
    
    def draw(self, surface: pygame.Surface):
        """Render button"""
        pass

class MenuScreen:
    def __init__(self, state_manager):
        # Attributes: buttons, background, title_font, state_manager
        pass
    
    def setup_buttons(self):
        """Initialize menu buttons"""
        pass
    
    def handle_events(self, events: list):
        """Process input events"""
        pass
    
    def update(self, dt: float):
        """Update menu state"""
        pass
    
    def draw(self, surface: pygame.Surface):
        """Render menu screen"""
        pass
    
    def on_start_game(self):
        """Handle start game button"""
        pass
    
    def on_options(self):
        """Handle options button"""
        pass
    
    def on_exit(self):
        """Handle exit button"""
        pass