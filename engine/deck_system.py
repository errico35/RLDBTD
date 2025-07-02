from ..imports import *

class Card:
    def __init__(self, card_id: str, name: str, cost: int, card_type: str, description: str):
        # Attributes: id, name, cost, type, description, effect_data
        pass
    
    def can_play(self, game_state) -> bool:
        """Check if card can be played in current game state"""
        pass
    
    def play(self, game_state, target_pos: tuple = None):
        """Execute card effect"""
        pass
    
    def get_tooltip_text(self) -> str:
        """Return formatted tooltip text"""
        pass

class Deck:
    def __init__(self, cards: list = None):
        # Attributes: cards, discard_pile
        pass
    
    def shuffle(self):
        """Shuffle the deck"""
        pass
    
    def draw_card(self) -> Card:
        """Draw top card from deck"""
        pass
    
    def add_card(self, card: Card):
        """Add card to deck"""
        pass
    
    def remove_card(self, card: Card):
        """Remove card from deck"""
        pass
    
    def reshuffle_from_discard(self):
        """Move discard pile back to deck and shuffle"""
        pass

class Hand:
    def __init__(self, max_size: int = 7):
        # Attributes: cards, max_size
        pass
    
    def add_card(self, card: Card) -> bool:
        """Add card to hand if space available"""
        pass
    
    def remove_card(self, card: Card):
        """Remove card from hand"""
        pass
    
    def play_card(self, card: Card, game_state, target_pos: tuple = None):
        """Play card from hand"""
        pass
    
    def is_full(self) -> bool:
        """Check if hand is at max capacity"""
        pass
    
    def draw(self, surface: pygame.Surface, x: int, y: int):
        """Render hand cards"""
        pass

class DeckManager:
    @staticmethod
    def load_deck_from_file(file_path: str) -> Deck:
        """Load deck configuration from JSON"""
        pass
    
    @staticmethod
    def create_starter_deck() -> Deck:
        """Create default starting deck"""
        pass