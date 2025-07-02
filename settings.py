"""
Global settings and constants for the Roguelike Tower Defense game.
"""

import os
from enum import Enum

# ==============================================================================
# DISPLAY SETTINGS
# ==============================================================================
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
FPS = 60
TITLE = "Roguelike Tower Defense"

# Fullscreen settings
FULLSCREEN = False
VSYNC = True

# UI scaling (for different screen sizes)
UI_SCALE = 1.0

# ==============================================================================
# COLORS (RGB tuples)
# ==============================================================================
COLORS = {
    # Basic colors
    'BLACK': (0, 0, 0),
    'WHITE': (255, 255, 255),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'YELLOW': (255, 255, 0),
    'CYAN': (0, 255, 255),
    'MAGENTA': (255, 0, 255),
    'GRAY': (128, 128, 128),
    'DARK_GRAY': (64, 64, 64),
    'LIGHT_GRAY': (192, 192, 192),
    
    # Game-specific colors
    'BACKGROUND': (32, 32, 48),
    'UI_BACKGROUND': (48, 48, 64),
    'UI_BORDER': (96, 96, 128),
    'TEXT_PRIMARY': (255, 255, 255),
    'TEXT_SECONDARY': (192, 192, 192),
    'TEXT_DISABLED': (128, 128, 128),
    
    # Game element colors
    'PLAYER': (64, 128, 255),
    'ENEMY': (255, 64, 64),
    'TOWER': (64, 255, 64),
    'PROJECTILE': (255, 255, 128),
    'HEALTH_BAR': (255, 64, 64),
    'ENERGY_BAR': (64, 64, 255),
    
    # Tile colors
    'TILE_GRASS': (34, 139, 34),
    'TILE_STONE': (128, 128, 128),
    'TILE_WATER': (0, 100, 200),
    'TILE_PATH': (139, 69, 19),
    'TILE_SPAWN': (255, 128, 128),
    'TILE_GOAL': (128, 255, 128),
    
    # Card rarity colors
    'CARD_COMMON': (255, 255, 255),
    'CARD_UNCOMMON': (64, 255, 64),
    'CARD_RARE': (64, 64, 255),
    'CARD_EPIC': (255, 64, 255),
    'CARD_LEGENDARY': (255, 215, 0),
    
    # Button states
    'BUTTON_NORMAL': (96, 96, 128),
    'BUTTON_HOVER': (128, 128, 160),
    'BUTTON_PRESSED': (64, 64, 96),
    'BUTTON_DISABLED': (64, 64, 64),
}

# ==============================================================================
# PATHS
# ==============================================================================
# Base directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Asset paths
ASSET_PATHS = {
    'images': os.path.join(ASSETS_DIR, 'images'),
    'sounds': os.path.join(ASSETS_DIR, 'sounds'),
    'fonts': os.path.join(ASSETS_DIR, 'fonts'),
    'music': os.path.join(ASSETS_DIR, 'music'),
}

# Data paths
DATA_PATHS = {
    'maps': os.path.join(DATA_DIR, 'maps'),
    'cards': os.path.join(DATA_DIR, 'cards'),
    'enemies': os.path.join(DATA_DIR, 'enemies'),
    'towers': os.path.join(DATA_DIR, 'towers'),
    'levels': os.path.join(DATA_DIR, 'levels'),
    'saves': os.path.join(DATA_DIR, 'saves'),
}

# ==============================================================================
# GAME BALANCE
# ==============================================================================
# Player settings
PLAYER_SETTINGS = {
    'starting_health': 20,
    'starting_energy': 3,
    'max_energy': 10,
    'energy_per_turn': 1,
    'cards_per_turn': 2,
    'max_hand_size': 7,
    'starting_deck_size': 15,
}

# Tower settings
TOWER_SETTINGS = {
    'base_cost': 2,
    'upgrade_cost_multiplier': 1.5,
    'max_upgrade_level': 3,
    'base_damage': 10,
    'base_range': 100,
    'base_fire_rate': 1.0,  # shots per second
}

# Enemy settings
ENEMY_SETTINGS = {
    'base_health': 50,
    'base_speed': 30,  # pixels per second
    'base_reward': 10,
    'health_scaling': 1.2,  # per wave
    'speed_scaling': 1.05,  # per wave
}

# Wave settings
WAVE_SETTINGS = {
    'enemies_per_wave': 10,
    'wave_scaling': 1.3,
    'time_between_enemies': 1.0,  # seconds
    'time_between_waves': 10.0,  # seconds
    'max_waves': 20,
}

# Card settings
CARD_SETTINGS = {
    'deck_shuffle_cost': 1,
    'card_draw_cost': 1,
    'discard_pile_size_limit': 50,
}

# ==============================================================================
# TILE SETTINGS
# ==============================================================================
TILE_SIZE = 32
TILES_PER_SCREEN_WIDTH = SCREEN_WIDTH // TILE_SIZE
TILES_PER_SCREEN_HEIGHT = SCREEN_HEIGHT // TILE_SIZE

# Tile types
class TileType(Enum):
    GRASS = "grass"
    STONE = "stone"
    WATER = "water"
    PATH = "path"
    SPAWN = "spawn"
    GOAL = "goal"
    TOWER_SLOT = "tower_slot"

# ==============================================================================
# GAME STATES
# ==============================================================================
class GameState(Enum):
    MENU = "menu"
    WORLD_MAP = "world_map"
    LEVEL = "level"
    PAUSE = "pause"
    GAME_OVER = "game_over"
    VICTORY = "victory"
    OPTIONS = "options"

# ==============================================================================
# INPUT SETTINGS
# ==============================================================================
# Key bindings
KEYS = {
    'PAUSE': 'p',
    'MENU': 'escape',
    'NEXT_TURN': 'space',
    'SHUFFLE_DECK': 's',
    'DRAW_CARD': 'd',
    'SPEED_UP': 'f',
    'SLOW_DOWN': 'q',
}

# Mouse settings
MOUSE_SETTINGS = {
    'double_click_time': 300,  # milliseconds
    'drag_threshold': 5,  # pixels
}

# ==============================================================================
# AUDIO SETTINGS
# ==============================================================================
AUDIO_SETTINGS = {
    'master_volume': 0.7,
    'music_volume': 0.5,
    'sfx_volume': 0.8,
    'channels': 8,  # number of sound channels
    'buffer_size': 512,
}

# ==============================================================================
# DEBUG SETTINGS
# ==============================================================================
DEBUG = {
    'show_fps': True,
    'show_collision_boxes': False,
    'show_pathfinding': False,
    'show_tower_ranges': False,
    'god_mode': False,
    'infinite_energy': False,
    'skip_waves': False,
}

# ==============================================================================
# UI SETTINGS
# ==============================================================================
UI_SETTINGS = {
    'font_size_small': 12,
    'font_size_medium': 16,
    'font_size_large': 24,
    'font_size_huge': 36,
    'button_padding': 10,
    'panel_padding': 15,
    'card_width': 80,
    'card_height': 120,
    'health_bar_width': 50,
    'health_bar_height': 6,
}

# Animation settings
ANIMATION_SETTINGS = {
    'card_hover_scale': 1.1,
    'button_hover_scale': 1.05,
    'tower_fire_duration': 0.2,
    'projectile_speed': 200,  # pixels per second
    'damage_text_duration': 1.0,
    'fade_duration': 0.5,
}

# ==============================================================================
# PERFORMANCE SETTINGS
# ==============================================================================
PERFORMANCE = {
    'max_projectiles': 100,
    'max_enemies_on_screen': 50,
    'particle_limit': 200,
    'culling_margin': 100,  # pixels outside screen to still render
}

# ==============================================================================
# GAME CONSTANTS
# ==============================================================================
DIRECTIONS = {
    'UP': (0, -1),
    'DOWN': (0, 1),
    'LEFT': (-1, 0),
    'RIGHT': (1, 0),
    'UP_LEFT': (-1, -1),
    'UP_RIGHT': (1, -1),
    'DOWN_LEFT': (-1, 1),
    'DOWN_RIGHT': (1, 1),
}

# Difficulty settings
DIFFICULTY_SETTINGS = {
    'EASY': {
        'enemy_health_multiplier': 0.7,
        'enemy_speed_multiplier': 0.8,
        'wave_size_multiplier': 0.8,
        'starting_resources_multiplier': 1.5,
    },
    'NORMAL': {
        'enemy_health_multiplier': 1.0,
        'enemy_speed_multiplier': 1.0,
        'wave_size_multiplier': 1.0,
        'starting_resources_multiplier': 1.0,
    },
    'HARD': {
        'enemy_health_multiplier': 1.3,
        'enemy_speed_multiplier': 1.2,
        'wave_size_multiplier': 1.2,
        'starting_resources_multiplier': 0.8,
    },
    'NIGHTMARE': {
        'enemy_health_multiplier': 1.6,
        'enemy_speed_multiplier': 1.4,
        'wave_size_multiplier': 1.5,
        'starting_resources_multiplier': 0.6,
    }
}

# ==============================================================================
# UTILITY FUNCTIONS
# ==============================================================================
def get_asset_path(asset_type: str, filename: str) -> str:
    """Get full path to an asset file."""
    return os.path.join(ASSET_PATHS[asset_type], filename)

def get_data_path(data_type: str, filename: str) -> str:
    """Get full path to a data file."""
    return os.path.join(DATA_PATHS[data_type], filename)

def scale_ui_value(value: float) -> float:
    """Scale a UI value based on UI_SCALE setting."""
    return value * UI_SCALE

def get_difficulty_multiplier(difficulty: str, setting: str) -> float:
    """Get difficulty multiplier for a specific setting."""
    return DIFFICULTY_SETTINGS.get(difficulty, DIFFICULTY_SETTINGS['NORMAL']).get(setting, 1.0)

# ==============================================================================
# VALIDATION
# ==============================================================================
def validate_settings():
    """Validate that all settings are reasonable."""
    errors = []
    
    if SCREEN_WIDTH <= 0 or SCREEN_HEIGHT <= 0:
        errors.append("Screen dimensions must be positive")
    
    if FPS <= 0:
        errors.append("FPS must be positive")
    
    if TILE_SIZE <= 0:
        errors.append("Tile size must be positive")
    
    if PLAYER_SETTINGS['starting_health'] <= 0:
        errors.append("Starting health must be positive")
    
    # Add more validation as needed
    
    if errors:
        raise ValueError("Settings validation failed: " + "; ".join(errors))

# Validate settings on import
validate_settings()
