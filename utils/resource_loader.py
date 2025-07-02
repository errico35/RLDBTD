import pygame
import json
import os
from typing import Dict, Optional, Tuple, Any
from ..settings import COLORS

class ResourceLoader:
    """
    Resource loader with fallback to geometric shapes when assets are missing.
    Includes caching for better performance.
    """
    
    def __init__(self):
        self._image_cache: Dict[str, pygame.Surface] = {}
        self._sound_cache: Dict[str, pygame.mixer.Sound] = {}
        self._font_cache: Dict[str, pygame.font.Font] = {}
        self._json_cache: Dict[str, dict] = {}
        
        # Initialize pygame components if not already done
        if not pygame.get_init():
            pygame.init()
        if not pygame.font.get_init():
            pygame.font.init()
        if not pygame.mixer.get_init():
            pygame.mixer.init()
    
    def load_image(self, path: str, scale: Optional[Tuple[int, int]] = None, 
                   fallback_shape: str = "rect", fallback_size: Tuple[int, int] = (32, 32),
                   fallback_color: Tuple[int, int, int] = COLORS['WHITE']) -> pygame.Surface:
        """
        Load an image with fallback to geometric shape.
        
        Args:
            path: Path to image file
            scale: Optional (width, height) to scale image
            fallback_shape: Shape to draw if image not found ('rect', 'circle', 'triangle')
            fallback_size: Size of fallback shape
            fallback_color: Color of fallback shape
            
        Returns:
            pygame.Surface with image or geometric shape
        """
        # Create cache key including all parameters
        cache_key = f"{path}_{scale}_{fallback_shape}_{fallback_size}_{fallback_color}"
        
        if cache_key in self._image_cache:
            return self._image_cache[cache_key]
        
        surface = None
        
        # Try to load the actual image
        if os.path.exists(path):
            try:
                surface = pygame.image.load(path).convert_alpha()
                print(f"Loaded image: {path}")
            except pygame.error as e:
                print(f"Failed to load image {path}: {e}")
                surface = None
        else:
            print(f"Image not found: {path}, using fallback shape")
        
        # Create fallback shape if image loading failed
        if surface is None:
            surface = self._create_fallback_shape(fallback_shape, fallback_size, fallback_color)
        
        # Scale if requested
        if scale and surface:
            surface = pygame.transform.scale(surface, scale)
        
        # Cache and return
        self._image_cache[cache_key] = surface
        return surface
    
    def load_sound(self, path: str, fallback_duration: float = 0.1, 
                   fallback_frequency: int = 440) -> pygame.mixer.Sound:
        """
        Load a sound with fallback to generated tone.
        
        Args:
            path: Path to sound file
            fallback_duration: Duration of fallback tone in seconds
            fallback_frequency: Frequency of fallback tone in Hz
            
        Returns:
            pygame.mixer.Sound object
        """
        if path in self._sound_cache:
            return self._sound_cache[path]
        
        sound = None
        
        # Try to load the actual sound
        if os.path.exists(path):
            try:
                sound = pygame.mixer.Sound(path)
                print(f"Loaded sound: {path}")
            except pygame.error as e:
                print(f"Failed to load sound {path}: {e}")
                sound = None
        else:
            print(f"Sound not found: {path}, using fallback tone")
        
        # Create fallback tone if sound loading failed
        if sound is None:
            sound = self._create_fallback_tone(fallback_duration, fallback_frequency)
        
        # Cache and return
        self._sound_cache[path] = sound
        return sound
    
    def load_font(self, path: str, size: int, fallback_font: str = None) -> pygame.font.Font:
        """
        Load a font with fallback to system font.
        
        Args:
            path: Path to font file
            size: Font size
            fallback_font: Name of system font to use as fallback
            
        Returns:
            pygame.font.Font object
        """
        cache_key = f"{path}_{size}"
        
        if cache_key in self._font_cache:
            return self._font_cache[cache_key]
        
        font = None
        
        # Try to load the actual font
        if os.path.exists(path):
            try:
                font = pygame.font.Font(path, size)
                print(f"Loaded font: {path}")
            except pygame.error as e:
                print(f"Failed to load font {path}: {e}")
                font = None
        else:
            print(f"Font not found: {path}, using fallback")
        
        # Create fallback font if font loading failed
        if font is None:
            if fallback_font:
                try:
                    font = pygame.font.SysFont(fallback_font, size)
                except:
                    font = pygame.font.Font(None, size)  # Default font
            else:
                font = pygame.font.Font(None, size)  # Default font
        
        # Cache and return
        self._font_cache[cache_key] = font
        return font
    
    def load_json(self, path: str, fallback_data: Optional[dict] = None) -> dict:
        """
        Load JSON data with optional fallback.
        
        Args:
            path: Path to JSON file
            fallback_data: Dictionary to return if loading fails
            
        Returns:
            Dictionary with loaded data or fallback
        """
        if path in self._json_cache:
            return self._json_cache[path]
        
        data = None
        
        # Try to load the actual JSON
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    data = json.load(f)
                print(f"Loaded JSON: {path}")
            except (json.JSONDecodeError, IOError) as e:
                print(f"Failed to load JSON {path}: {e}")
                data = None
        else:
            print(f"JSON not found: {path}")
        
        # Use fallback data if loading failed
        if data is None:
            if fallback_data is not None:
                data = fallback_data.copy()
                print(f"Using fallback data for {path}")
            else:
                data = {}
        
        # Cache and return
        self._json_cache[path] = data
        return data
    
    def _create_fallback_shape(self, shape: str, size: Tuple[int, int], 
                              color: Tuple[int, int, int]) -> pygame.Surface:
        """
        Create a geometric shape as fallback for missing images.
        
        Args:
            shape: Type of shape ('rect', 'circle', 'triangle', 'diamond')
            size: (width, height) of the shape
            color: RGB color tuple
            
        Returns:
            pygame.Surface with drawn shape
        """
        width, height = size
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        surface.fill((0, 0, 0, 0))  # Transparent background
        
        if shape == "rect":
            pygame.draw.rect(surface, color, (0, 0, width, height))
            pygame.draw.rect(surface, COLORS['BLACK'], (0, 0, width, height), 2)
            
        elif shape == "circle":
            radius = min(width, height) // 2
            center = (width // 2, height // 2)
            pygame.draw.circle(surface, color, center, radius)
            pygame.draw.circle(surface, COLORS['BLACK'], center, radius, 2)
            
        elif shape == "triangle":
            points = [
                (width // 2, 0),           # Top
                (0, height),               # Bottom left
                (width, height)            # Bottom right
            ]
            pygame.draw.polygon(surface, color, points)
            pygame.draw.polygon(surface, COLORS['BLACK'], points, 2)
            
        elif shape == "diamond":
            points = [
                (width // 2, 0),           # Top
                (width, height // 2),      # Right
                (width // 2, height),      # Bottom
                (0, height // 2)           # Left
            ]
            pygame.draw.polygon(surface, color, points)
            pygame.draw.polygon(surface, COLORS['BLACK'], points, 2)
            
        elif shape == "hexagon":
            center_x, center_y = width // 2, height // 2
            radius = min(width, height) // 2
            points = []
            for i in range(6):
                angle = i * 60 * (3.14159 / 180)  # Convert to radians
                x = center_x + radius * pygame.math.Vector2(1, 0).rotate(angle * 180 / 3.14159).x
                y = center_y + radius * pygame.math.Vector2(1, 0).rotate(angle * 180 / 3.14159).y
                points.append((x, y))
            pygame.draw.polygon(surface, color, points)
            pygame.draw.polygon(surface, COLORS['BLACK'], points, 2)
            
        else:  # Default to rectangle
            pygame.draw.rect(surface, color, (0, 0, width, height))
            pygame.draw.rect(surface, COLORS['BLACK'], (0, 0, width, height), 2)
        
        return surface
    
    def _create_fallback_tone(self, duration: float, frequency: int) -> pygame.mixer.Sound:
        """
        Create a simple tone as fallback for missing sounds.
        
        Args:
            duration: Length of tone in seconds
            frequency: Frequency in Hz
            
        Returns:
            pygame.mixer.Sound with generated tone
        """
        sample_rate = 22050
        frames = int(duration * sample_rate)
        
        # Generate sine wave
        import numpy as np
        wave_array = np.zeros((frames, 2))  # Stereo
        
        for i in range(frames):
            time = float(i) / sample_rate
            wave = int(4096 * np.sin(frequency * 2 * np.pi * time))
            wave_array[i][0] = wave  # Left channel
            wave_array[i][1] = wave  # Right channel
        
        # Convert to pygame sound
        sound = pygame.sndarray.make_sound(wave_array.astype(np.int16))
        return sound
    
    def get_cached_resource(self, path: str, resource_type: str) -> Any:
        """
        Get a previously loaded resource from cache.
        
        Args:
            path: Path of the resource
            resource_type: Type of resource ('image', 'sound', 'font', 'json')
            
        Returns:
            Cached resource or None if not found
        """
        cache_map = {
            'image': self._image_cache,
            'sound': self._sound_cache,
            'font': self._font_cache,
            'json': self._json_cache
        }
        
        cache = cache_map.get(resource_type)
        if cache:
            return cache.get(path)
        return None
    
    def clear_cache(self, resource_type: Optional[str] = None):
        """
        Clear resource cache.
        
        Args:
            resource_type: Specific type to clear, or None for all
        """
        if resource_type == 'image' or resource_type is None:
            self._image_cache.clear()
        if resource_type == 'sound' or resource_type is None:
            self._sound_cache.clear()
        if resource_type == 'font' or resource_type is None:
            self._font_cache.clear()
        if resource_type == 'json' or resource_type is None:
            self._json_cache.clear()
        
        if resource_type:
            print(f"Cleared {resource_type} cache")
        else:
            print("Cleared all resource caches")

# Convenience functions for easy access
def load_image(path: str, scale: Optional[Tuple[int, int]] = None, 
               fallback_shape: str = "rect", fallback_size: Tuple[int, int] = (32, 32),
               fallback_color: Tuple[int, int, int] = COLORS['WHITE']) -> pygame.Surface:
    """Convenience function for loading images"""
    return _global_loader.load_image(path, scale, fallback_shape, fallback_size, fallback_color)

def load_sound(path: str, fallback_duration: float = 0.1, 
               fallback_frequency: int = 440) -> pygame.mixer.Sound:
    """Convenience function for loading sounds"""
    return _global_loader.load_sound(path, fallback_duration, fallback_frequency)

def load_font(path: str, size: int, fallback_font: str = None) -> pygame.font.Font:
    """Convenience function for loading fonts"""
    return _global_loader.load_font(path, size, fallback_font)

def load_json(path: str, fallback_data: Optional[dict] = None) -> dict:
    """Convenience function for loading JSON"""
    return _global_loader.load_json(path, fallback_data)

# Global loader instance
_global_loader = ResourceLoader()

# Predefined fallback shapes for common game objects
FALLBACK_SHAPES = {
    'player': ('circle', (24, 24), COLORS['BLUE']),
    'enemy': ('triangle', (20, 20), COLORS['RED']),
    'tower': ('rect', (32, 32), COLORS['GREEN']),
    'projectile': ('circle', (6, 6), COLORS['WHITE']),
    'card': ('rect', (60, 80), COLORS['GRAY']),
    'button': ('rect', (100, 30), COLORS['GRAY']),
    'tile_grass': ('rect', (32, 32), (34, 139, 34)),
    'tile_stone': ('rect', (32, 32), (128, 128, 128)),
    'tile_water': ('rect', (32, 32), (0, 100, 200)),
    'tile_path': ('rect', (32, 32), (139, 69, 19))
}

def load_game_image(path: str, object_type: str, scale: Optional[Tuple[int, int]] = None) -> pygame.Surface:
    """
    Load image with predefined fallbacks for common game objects.
    
    Args:
        path: Path to image file
        object_type: Type of game object (key in FALLBACK_SHAPES)
        scale: Optional scaling
        
    Returns:
        pygame.Surface with image or appropriate fallback
    """
    if object_type in FALLBACK_SHAPES:
        shape, size, color = FALLBACK_SHAPES[object_type]
        return load_image(path, scale, shape, size, color)
    else:
        return load_image(path, scale)